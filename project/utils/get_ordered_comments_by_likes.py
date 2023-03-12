from functools import cmp_to_key
from typing import List
from models.comment import Comment

def get_ordered_comments_by_likes(comments: List[Comment]) -> List[Comment]:
    return sorted(comments, key=cmp_to_key(lambda x, y: y.like_count - x.like_count))
