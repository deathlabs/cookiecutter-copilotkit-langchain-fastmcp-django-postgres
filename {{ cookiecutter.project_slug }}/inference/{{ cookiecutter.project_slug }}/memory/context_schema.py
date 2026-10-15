# Standard library imports.
from dataclasses import dataclass, field
from typing import Any


@dataclass
class ContextSchema:
    subject: str = "{{ cookiecutter.project_slug }}"  # TODO: replace with a value set within a JWT.

    # The following properties are sent by CopilotKit.
    thread_id: str = ""
    copilotkit: dict[str, Any] = field(default_factory=dict)
