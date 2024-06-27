import typing

import orjson
import pydantic
from pydantic import ConfigDict


def orjson_dumps(
    v: typing.Any,
    *,
    default: typing.Callable[[typing.Any], typing.Any] | None,
) -> str:
    return orjson.dumps(v, default=default).decode()


class BaseModel(pydantic.BaseModel):
    model_config = ConfigDict()
