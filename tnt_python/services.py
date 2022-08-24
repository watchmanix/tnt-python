import httpx
from tempfile import NamedTemporaryFile

from .types import *


class NotifyerService:
    @staticmethod
    def send_message(data: MessageData, token: str) -> int:
        url: str = f"https://api.telegram.org/bot{token}/sendMessage"
        data: dict = data.as_dict()
        response: httpx.Response = httpx.post(url, data=data)
        return response.status_code

    @staticmethod
    def send_document(data: FileData, document: DocumentType, token: str) -> int:
        url: str = f"https://api.telegram.org/bot{token}/sendDocument"
        data: dict = data.as_dict()
        document = document.as_dict()
        response: httpx.Response = httpx.post(url, data=data, files=document)
        return response.status_code

