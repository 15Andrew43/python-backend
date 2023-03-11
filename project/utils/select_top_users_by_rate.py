from functools import cmp_to_key
from typing import List
from models.user import User

def select_top_users_by_rate(users: List[User], top_size: int) -> List[User]:
    return sorted(users, key=cmp_to_key(lambda x, y: y.rate - x.rate))[:top_size]
