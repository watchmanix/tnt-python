import os

from dotenv import load_dotenv

from tnt_python.types import ResponseFailType
from tnt_python.data import MessageData
from tnt_python.services import NotifyerService


def test_error_response():
    load_dotenv()
    token = ''
    data = MessageData(
        chat_id=os.getenv("CHAT_ID"),
        text="Hello world"
    )
    response = NotifyerService().send_message(data, token)
    assert response.status_code == 404 and isinstance(response.result, ResponseFailType)
