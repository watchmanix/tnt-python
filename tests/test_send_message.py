import os

from dotenv import load_dotenv

from tnt_python.data import MessageData
from tnt_python.services import NotifyerService
from tnt_python.types import ResponseSuccessType, ResponseType


def test_send_message():
    load_dotenv()
    token: str = os.getenv("TG_TOKEN")
    data: MessageData = MessageData(
        chat_id=os.getenv("CHAT_ID"),
        text="Hello world"
    )
    response: ResponseType = NotifyerService().send_message(data, token)
    assert response.status_code == 200 and isinstance(response.result, ResponseSuccessType)
