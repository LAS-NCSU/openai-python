# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

from .conversation_item_content_param import ConversationItemContentParam

__all__ = ["ConversationItemWithReferenceParam"]


class ConversationItemWithReferenceParam(TypedDict, total=False):
    id: str
    """
    For an item of type (`message` | `function_call` | `function_call_output`) this
    field allows the client to assign the unique ID of the item. It is not required
    because the server will generate one if not provided.

    For an item of type `item_reference`, this field is required and is a reference
    to any item that has previously existed in the conversation.
    """

    arguments: str
    """The arguments of the function call (for `function_call` items)."""

    call_id: str
    """
    The ID of the function call (for `function_call` and `function_call_output`
    items). If passed on a `function_call_output` item, the server will check that a
    `function_call` item with the same ID exists in the conversation history.
    """

    content: Iterable[ConversationItemContentParam]
    """The content of the message, applicable for `message` items.

    - Message items of role `system` support only `input_text` content
    - Message items of role `user` support `input_text` and `input_audio` content
    - Message items of role `assistant` support `text` content.
    """

    name: str
    """The name of the function being called (for `function_call` items)."""

    object: Literal["realtime.item"]
    """Identifier for the API object being returned - always `realtime.item`."""

    output: str
    """The output of the function call (for `function_call_output` items)."""

    role: Literal["user", "assistant", "system"]
    """
    The role of the message sender (`user`, `assistant`, `system`), only applicable
    for `message` items.
    """

    status: Literal["completed", "incomplete"]
    """The status of the item (`completed`, `incomplete`).

    These have no effect on the conversation, but are accepted for consistency with
    the `conversation.item.created` event.
    """

    type: Literal["message", "function_call", "function_call_output", "item_reference"]
    """
    The type of the item (`message`, `function_call`, `function_call_output`,
    `item_reference`).
    """
