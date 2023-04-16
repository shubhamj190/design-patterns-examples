import random
import string
from iot.message import Message, MessageType
from typing import Protocol
import asyncio


def generate_id(length: int = 8):
    return "".join(random.choices(string.ascii_uppercase, k=length))


class Device(Protocol):
    async def connect(self) -> None:
        ...

    async def disconnect(self) -> None:
        ...

    async def send_message(self, message_type: MessageType, data: str) -> None:
        ...


class IOTService:
    def __init__(self):
        self.devices: dict[str, Device] = {}

    async def register_devices(self, device: Device):
        await device.connect()
        device_id = generate_id()
        self.devices[device_id] = device
        return device_id

    async def unregister(self, device_id: str):
        await self.devices[device_id].disconnect()
        del self.devices[device_id]

    def get_device(self, device_id: str):
        return self.devices[device_id]

    async def run_program(self, programs: list[Message]):
        print("====== Program Running ======")
        for msg in programs:
            await self.send_msg(msg)
        print("====== End of program ======")

    async def send_msg(self, msg: Message):
        await self.devices[msg.device_id].send_message(msg.msg_type, msg.data)
