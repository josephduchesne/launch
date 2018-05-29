# Copyright 2018 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module for the RegisterEventHandler action."""

from ..action import Action
from ..event_handler import EventHandler
from ..launch_context import LaunchContext


class RegisterEventHandler(Action):
    """Action that registers an event handler."""

    def __init__(self, event_handler: EventHandler):
        """Constructor."""
        super().__init__()
        self.__event_handler = event_handler

    @property
    def event_handler(self) -> EventHandler:
        """Getter for self.__event_handler."""
        return self.__event_handler

    def execute(self, context: LaunchContext):
        """Execute the action."""
        context.register_event_handler(self.__event_handler)
