# This file was auto-generated by Fern from our API Definition.

import enum


class FernApiEnvironment(enum.Enum):
    LOCAL = "http://localhost:8080"
    """
    Local testing
    """

    PRODUCTION = "http://TODO"
    """
    Prod env
    """
