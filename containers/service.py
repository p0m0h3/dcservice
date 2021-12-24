"""
Implementation of a container service handler
"""

import os
import docker
import yaml
from .exceptions.tool_not_found import ToolNotFound


class Service:
    """
    Implementation of task computation service with docker api
    """

    def __init__(self, tools_dir: str):
        self.client = docker.from_env()
        self._read_tools(tools_dir)

    def _run(self, image: str):
        return self.client.containers.run(image, detach=True)

    def _read_tools(self, tools_dir: str):
        self.tools = {}
        for filename in os.scandir(tools_dir):
            with open(filename, "r", encoding="utf-8") as yaml_file:
                tool = yaml.safe_load(yaml_file)
                self.tools[tool["id"]] = tool

    def start_task(self, tool_id: str):
        """
        Start a task given a tool id
        """
        try:
            container = self._run(self.tools[tool_id]["image"])
        except KeyError as ex:
            raise ToolNotFound() from ex
        return container.id

    def stream_task_log(self, task_id: str):
        """
        get a blocking stream of task log
        """
        return self.client.containers.get(task_id).logs(stdout=True, stream=True)
