import os

from dotenv import load_dotenv

from tnt_python.types import DocumentType, ResponseSuccessType
from tnt_python.data import FileData
from tnt_python.file_creator import FileCreator
from tnt_python.services import NotifyerService


def test_send_document():
    load_dotenv()
    token = os.getenv("TG_TOKEN")

    data = FileData(
        chat_id=os.getenv("CHAT_ID"),
        caption="Hello world"
    )

    file_creator = FileCreator()
    file_creator.write("Hello world".encode())

    document = DocumentType(document=file_creator.file)
    response = NotifyerService().send_document(data, document, token)
    file_creator.close()
    assert response.status_code == 200 and isinstance(response.result, ResponseSuccessType)
