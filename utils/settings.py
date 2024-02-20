import os

import pydantic
from dotenv import load_dotenv


class Config(pydantic.BaseModel):
    load_dotenv()
    login: str = os.environ.get('USER_NAME')
    access_key: str = os.environ.get('ACCESS_KEY')


config = Config()
