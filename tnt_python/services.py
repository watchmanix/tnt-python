from typing import Union
from string import Template

import httpx

from .data import *
from .types import *


class NotifyerService:
    __url_template = Template("https://api.telegram.org/bot${token}/${method}")

    def __get_response(self, status_code: int, response: dict) -> ResponseType:
        result = ResponseSuccessType(**response) if status_code == 200 else ResponseFailType(**response)
        return ResponseType(status_code=status_code, result=result)

    def send_message(self, data: MessageData, token: str) -> ResponseType:
        url = self.__url_template.substitute(token=token, method="sendMessage")
        data: dict = data.as_dict()
        response: httpx.Response = httpx.post(url, data=data)
        return self.__get_response(response.status_code, response.json())

    def send_document(self, data: FileData, document: DocumentType, token: str) -> ResponseType:
        url = self.__url_template.substitute(token=token, method="sendDocument")
        data: dict = data.as_dict()
        document = document.as_dict()
        response: httpx.Response = httpx.post(url, data=data, files=document)
        return self.__get_response(response.status_code, response.json())
