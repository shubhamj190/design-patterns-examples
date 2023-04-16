import asyncio


class HueLightDevice:
    async def connect(self):
        print("Connecting hue light")
        await asyncio.sleep(0.5)
        print("huelight connected")

    async def disconnect(self):
        print("disonnecting hue light")
        await asyncio.sleep(0.5)
        print("huelight disconnected")

    async def send_message(self, message_type, data):
        print(f"hue ligh handling message of type {message_type} with {data}")
        await asyncio.sleep(0.5)
        print("hue light message sent successfully")


class SmartSpeakerDevice:
    async def connect(self):
        print("Connecting smart speaker")
        await asyncio.sleep(0.5)
        print("smart speaker connected")

    async def disconnect(self):
        print("disonnecting smart speaker")
        await asyncio.sleep(0.5)
        print("smart speaker disconnected")

    async def send_message(self, message_type, data):
        print(f"smart speaker handling message of type {message_type} with {data}")
        await asyncio.sleep(0.5)
        print("smart speaker message sent successfully")


class SmartToiletDevice:
    async def connect(self):
        print("Connecting  toilet")
        await asyncio.sleep(0.5)
        print("toilet speaker connected")

    async def disconnect(self):
        print("disonnecting smart toilet")
        await asyncio.sleep(0.5)
        print("smart toilet disconnected")

    async def send_message(self, message_type, data):
        print(f"smart toilet handling message of type {message_type} with {data}")
        await asyncio.sleep(0.5)
        print("smart toilet message sent successfully")
