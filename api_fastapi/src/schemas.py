from pydantic import BaseModel
from datetime import datetime

# schema for input requests and responses
# base schema
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

# schema for input requests (post and update)
class PostCreate(PostBase):
    pass

# schema for output responses
class Post(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime

    # this will convert the sqlalchemy object to a dictionary since the response is a dictionary
    class Config:
        orm_mode = True