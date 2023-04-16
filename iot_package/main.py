from iot.message import Message, MessageType
from iot.device import HueLightDevice, SmartSpeakerDevice, SmartToiletDevice
from iot.service import IOTService
import asyncio
from typing import Awaitable, Any


async def run_sequestial(*functions: Awaitable[Any]) -> None:
    for fucntion in functions:
        await fucntion


async def run_parallel(*fucntions: Awaitable[Any]):
    await asyncio.gather(*fucntions)


async def main():
    service = IOTService()

    hue_light = HueLightDevice()
    smart_speaker = SmartSpeakerDevice()
    smart_toilet = SmartToiletDevice()

    # registering the devices
    # hue_light_id=await service.register_devices(hue_light)
    # smart_speaker_id=await service.register_devices(smart_speaker)
    # smart_toilet_id=await service.register_devices(smart_toilet)

    # TODO conncting devices asyncio gather fucntion

    hue_light_id, smart_speaker_id, smart_toilet_id = await asyncio.gather(
        service.register_devices(hue_light),
        service.register_devices(smart_speaker),
        service.register_devices(smart_toilet),
    )

    # few programs

    wakeup_program = [
        Message(hue_light_id, MessageType.SWITCH_ON),
        Message(smart_speaker_id, MessageType.SWITCH_ON),
        Message(smart_toilet_id, MessageType.SWITCH_ON),
    ]

    # sleep_prgram = [
    #     Message(hue_light_id, MessageType.SWITCH_OFF),
    #     Message(smart_speaker_id, MessageType.SWITCH_OFF),
    #     Message(smart_toilet_id, MessageType.FLUSH),
    #     Message(smart_toilet_id, MessageType.CLEAN),
    # ]

    await service.run_program(wakeup_program)
    # await service.run_program(sleep_prgram)

    # TODO mixture of sequestial and parallesim goes here

    await run_parallel(
        service.send_msg(Message(hue_light_id, MessageType.SWITCH_OFF)),
        service.send_msg(Message(smart_speaker_id, MessageType.SWITCH_OFF)),
        run_sequestial(
            service.send_msg(Message(smart_toilet_id, MessageType.FLUSH)),
            service.send_msg(Message(smart_toilet_id, MessageType.CLEAN)),
        ),
    )


if __name__ == "__main__":
    asyncio.run(main())
