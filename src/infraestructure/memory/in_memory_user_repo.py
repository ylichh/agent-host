from typing import Optional

from ...domain.repositories.i_repositories import IUserRepository
from ...domain.entities import Usuario


class InMemoryUserRepository(IUserRepository):
    def __init__(self):
        self.users = {}

    def get_user_by_id(self, user_id: str) -> Optional[Usuario]:
        return self.users.get(user_id)

    def create_user(self, user: Usuario) -> Usuario:
        self.users[user.user_id] = user
        return user
