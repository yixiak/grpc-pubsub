from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class themeList(_message.Message):
    __slots__ = ["theme_index"]
    THEME_INDEX_FIELD_NUMBER: _ClassVar[int]
    theme_index: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, theme_index: _Optional[_Iterable[int]] = ...) -> None: ...

class theme(_message.Message):
    __slots__ = ["theme_index"]
    THEME_INDEX_FIELD_NUMBER: _ClassVar[int]
    theme_index: int
    def __init__(self, theme_index: _Optional[int] = ...) -> None: ...

class pub(_message.Message):
    __slots__ = ["theme_index", "text"]
    THEME_INDEX_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    theme_index: theme
    text: str
    def __init__(self, theme_index: _Optional[_Union[theme, _Mapping]] = ..., text: _Optional[str] = ...) -> None: ...

class sub(_message.Message):
    __slots__ = ["theme_index", "text"]
    THEME_INDEX_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    theme_index: theme
    text: str
    def __init__(self, theme_index: _Optional[_Union[theme, _Mapping]] = ..., text: _Optional[str] = ...) -> None: ...
