# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResponseFileSearchToolCallParam", "Result"]


class Result(TypedDict, total=False):
    attributes: Optional[Dict[str, Union[str, float, bool]]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard. Keys are
    strings with a maximum length of 64 characters. Values are strings with a
    maximum length of 512 characters, booleans, or numbers.
    """

    file_id: str
    """The unique ID of the file."""

    filename: str
    """The name of the file."""

    score: float
    """The relevance score of the file - a value between 0 and 1."""

    text: str
    """The text that was retrieved from the file."""


class ResponseFileSearchToolCallParam(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the file search tool call."""

    queries: Required[List[str]]
    """The queries used to search for files."""

    status: Required[Literal["in_progress", "searching", "completed", "incomplete", "failed"]]
    """The status of the file search tool call.

    One of `in_progress`, `searching`, `incomplete` or `failed`,
    """

    type: Required[Literal["file_search_call"]]
    """The type of the file search tool call. Always `file_search_call`."""

    results: Optional[Iterable[Result]]
    """The results of the file search tool call."""
