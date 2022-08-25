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
from tnt_python.data import MessageData
from tnt_python.services import NotifyerService

# Your API Token
token = os.getenv("TG_TOKEN")

data = MessageData(
    chat_id=os.getenv("CHAT_ID"),
    text="Hello world"
)
NotifyerService().send_message(data, token)
```

## Debug
 Methods `send_message`, `send_coument` returns `ResponseType` type dataclass.
 You can output `status_code` or the entire response via `result`
 
 ```python

import os
from tnt_python.data import MessageData
from tnt_python.services import NotifyerService
from tnt_python.types import ResponseType

token = os.getenv("TG_TOKEN")

data = MessageData(
    chat_id=os.getenv("CHAT_ID"),
    text="Hello world"
)
response: ResponseType = NotifyerService().send_message(data, token)

# So you can display the entire response and the response code
print(response.status_code, response.result)
```