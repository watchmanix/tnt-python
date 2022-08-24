from dataclasses import dataclass
from tempfile import NamedTemporaryFile

from .enums import *


@dataclass
class BaseData:
    chat_id: str

    def as_dict(self):
        return {
            "chat_id": self.chat_id
        }


@dataclass
class MessageData(BaseData):
    text: str
    parse_mode: ParseModeEnum = ParseModeEnum.markdown

    def as_dict(self):
        base_dict = super(MessageData, self).as_dict()
        base_dict["text"] = self.text
        base_dict["parse_mode"] = self.parse_mode.value
        return base_dict


@dataclass
class FileData(BaseData):
    caption: str = None

    def as_dict(self):
        base_dict = super(FileData, self).as_dict()
        base_dict["caption"] = self.caption
        return base_dict


@dataclass
class DocumentType:
    document: NamedTemporaryFile

    def as_dict(self):
        return {
            "document": self.document
        }
