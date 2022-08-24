import os

from dotenv import load_dotenv

from tnt_python.types import FileData, DocumentType
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
    status = NotifyerService.send_document(data, document, token)
    file_creator.close()
    assert status == 200
