from typing import List, Optional

from ...api.cache import Cache
from .Request import Request

class HTTPThread:

    _req: Request
    cache: Cache

    def __init__(self, _req, cache) -> None: ...
    async def join_thread(self, thread_id: int) -> None: ...
    async def leave_thread(self, thread_id: int) -> None: ...
    async def add_member_to_thread(self, thread_id: int, user_id: int) -> None: ...
    async def remove_member_from_thread(self, thread_id: int, user_id: int) -> None: ...
    async def get_member_from_thread(self, thread_id: int, user_id: int) -> dict: ...
    async def list_thread_members(self, thread_id: int) -> List[dict]: ...
    async def list_public_archived_threads(
        self, channel_id: int, limit: int = None, before: Optional[int] = None
    ) -> List[dict]: ...
    async def list_private_archived_threads(
        self, channel_id: int, limit: int = None, before: Optional[int] = None
    ) -> List[dict]: ...
    async def list_joined_private_archived_threads(
        self, channel_id: int, limit: int = None, before: Optional[int] = None
    ) -> List[dict]: ...
    async def list_active_threads(self, guild_id: int) -> List[dict]: ...
    async def create_thread(
        self,
        channel_id: int,
        name: str,
        thread_type: int = None,
        auto_archive_duration: Optional[int] = None,
        invitable: Optional[bool] = None,
        message_id: Optional[int] = None,
        reason: Optional[str] = None,
    ) -> dict: ...
