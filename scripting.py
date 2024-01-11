from lupa import LuaRuntime
import json
import time

lua = LuaRuntime(unpack_returned_tuples=False)


class LuaReturnException(Exception):
    def __init__(self, value):
        self.value = value


def meta_return(value):
    raise LuaReturnException(value)


lua.globals().meta_return = meta_return
lua.globals().sleep = lambda value: time.sleep(value)


def register_functions(functions: dict):
    for key, value in functions.items():
        lua.globals()[key] = value


def eval(script):
    try:
        if lua:
            return lua.eval(script)
        else:
            raise RuntimeError("No runtime set")
    except LuaReturnException as e:
        return e.value


class script:
    class meta:
        def __init__(self) -> None:
            pass

    def __init__(self, file: str) -> None:
        with open(file, "r") as f:
            self.script = f.read()
        header, content = self.script.split("\n")[0], "\n".join(
            self.script.split("\n")[1:]
        )
        self.header = json.loads(header)
        self.script = content
        for key, value in self.header.items():
            self.meta.__setattr__(self, key, value)

    def eval(self):
        global lua
        lua.globals().meta_get = lambda value: self.meta_get(value)
        return lua.eval(self.script)

    def meta_get(self, key):
        return self.meta.__getattribute__(key)
