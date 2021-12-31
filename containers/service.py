"""
Implementation of a container service handler
"""

import os

import docker
import yaml

from .exceptions import ToolNotFound, ArgumentNotFound


class Service:
    """
    Implementation of task computation service with docker api
    """

    def __init__(self, tools_dir: str):
        try:
            self.client = docker.from_env()
        except docker.errors.DockerException:
            print("Err: Couldn't connect to docker!")
        self._read_tools(tools_dir)

    def _run(self, image: str, cmd: str):
        return self.client.containers.run(image, command=cmd, detach=True)

    def _read_tools(self, tools_dir: str):
        self.tools = {}
        for filename in os.scandir(tools_dir):
            with open(filename.path, "r", encoding="utf-8") as yaml_file:
                tool = yaml.safe_load(yaml_file)
                self.tools[tool["id"]] = tool

    def start_task(self, tool_id: str, args: {str: str} = None):
        """
        Start a task given a tool id
        """
        try:
            tool = self.tools[tool_id]
        except KeyError as ex:
            raise ToolNotFound() from ex

        if len(tool["args"]) != 0:
            try:
                required_args = {arg["key"]: args[arg["key"]] for arg in tool["args"]}
                container = self._run(
                    tool["image"], tool["cmd"].format(**required_args)
                )
                return container.id
            except TypeError as ex:
                raise ArgumentNotFound() from ex

    def stream_task_log(self, task_id: str):
        """
        get a blocking stream of task log
        """
        return self.client.containers.get(task_id).logs(stdout=True, stream=True)
