"""
Implementation of a container service handler
"""

import os
from typing import Dict, List

import docker
import yaml

from .exceptions import (
    ToolNotFound,
    ArgumentNotFound,
    ContainerNotExited,
    ContainerNotFound,
)


class Service:
    """
    Implementation of task computation service with docker api
    """

    client: docker.DockerClient
    tools: Dict[str, Dict]
    containers: List[str]

    def __init__(self, tools_dir: str):
        self.tools = {}
        self.containers = []
        try:
            self.client = docker.from_env()
        except docker.errors.DockerException:
            print("Err: Couldn't connect to docker!")
        self._read_tools(tools_dir)

    def _run(self, image: str, cmd: str, stdin: str = "") -> str:
        if stdin:
            cmd = f'echo "{stdin}" | {cmd}'
        container_id = self.client.containers.run(image, command=cmd, detach=True).id
        self.containers.append(container_id)
        return container_id

    def _read_tools(self, tools_dir: str):
        for filename in os.scandir(tools_dir):
            with open(filename.path, "r", encoding="utf-8") as yaml_file:
                tool = yaml.safe_load(yaml_file)
                self.tools[tool["id"]] = tool

    def start_task(self, tool_id: str, args: {str: str} = None, stdin: str = "") -> str:
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
                container_id = self._run(
                    tool["image"], tool["cmd"].format(**required_args), stdin
                )
                return container_id
            except TypeError as ex:
                raise ArgumentNotFound() from ex

    def fetch_output(self, task_id: str) -> str:
        """
        get a blocking stream of task log
        """
        try:
            container = self.client.containers.get(task_id)
            if container.status != "exited":
                raise ContainerNotExited()

            logs = container.logs(stdout=True)

            container.remove()
            self.containers.remove(task_id)
            return logs.decode("utf-8")
        except docker.errors.NotFound as ex:
            raise ContainerNotFound() from ex
