from dataclasses import dataclass
from tempfile import NamedTemporaryFile
from typing import Union


@dataclass
class DocumentType:
    document: NamedTemporaryFile

    def as_dict(self):
        return {
            "document": self.document
        }


@dataclass
class BaseResponseType:
    ok: bool


@dataclass
class ResponseFailType(BaseResponseType):
    error_code: int
    description: str


@dataclass
class ResponseSuccessType(BaseResponseType):
    result: dict


@dataclass
class ResponseType:
    status_code: int
    result: Union[ResponseFailType, ResponseSuccessType]
