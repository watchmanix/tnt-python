# tnt-python

tnt - Telegram notification tool

## Features

* Sending text messages to chat
* Sending text documents to chat


## Installation

```
poetry add tnt-python
```

or

```
pip install tnt-python
```

## Example

This code sends a message on your behalf to the chat

```python
import os
from tnt_python.types import MessageData
from tnt_python.services import NotifyerService

# Your API Token
token = os.getenv("TG_TOKEN")

data = MessageData(
    chat_id=os.getenv("CHAT_ID"),
    text="Hello world"
)
NotifyerService.send_message(data, token)
```