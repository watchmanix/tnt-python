import os

from dotenv import load_dotenv

from tnt_python.types import MessageData
from tnt_python.services import NotifyerService


def test_send_message():
    load_dotenv()
    token = os.getenv("TG_TOKEN")
    data = MessageData(
        chat_id=os.getenv("CHAT_ID"),
        text="Hello world"
    )
    assert NotifyerService.send_message(data, token) == 200
