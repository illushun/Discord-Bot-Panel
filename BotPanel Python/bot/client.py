from discord.ext import commands

import bot.commands as client_commands

import asyncio, time

class Client():
    def __init__(self, prefix: str="!", loop: object=None):
        self.prefix=prefix
        self.loop=loop
        self.client=commands.Bot(command_prefix=self.prefix, loop=self.loop, help_command=None)
    
    def get_client(self):
        return self.client
    
    def run(self, loop: object, client: object, token: str):
        while True:
            try:
                client_commands.Commands(client).start()
                loop.run_until_complete(client.start(token))
                loop.close()
            except Exception as ex:
                print("ERROR ->", ex)
                return
    
    def stop(self, client: object):
        client.logout()

class EventLoop():
    def __init__(self):
        pass

    def get_loop(self):
        return asyncio.get_event_loop()

    def create(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        return asyncio.get_event_loop()

    async def destroy(self, loop: object):
        await loop.stop()
        await loop.close()