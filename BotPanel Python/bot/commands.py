from discord.ext import commands

import render.screens.start as screen_start
import bot.client as client

commandList={
    "help": "Used to view available commands."
}

class Commands():
    def __init__(self, client: object=None):
        self.client=client
    
    def start(self):
        @self.client.event
        async def on_ready():
            screen_start.update_textbox(screen_start.getTag["botStartupMessages"], "Login from -> {0.user}".format(self.client))

        @self.client.event
        async def on_message(message):
            userName=message.author
            channel=message.channel.name
            sentMessage=str(message.content)
            
            screen_start.update_textbox(screen_start.getTag["eventMessages"], "{}, {}: '{}'".format(userName, channel, sentMessage))

            await self.client.process_commands(message)

        @self.client.event
        async def on_member_join(member):
            userName=member.name
            server=member.guild
            screen_start.update_textbox(screen_start.getTag["memberJoinMessages"], "{} has joined {}".format(userName, server))

        @self.client.command(name="help")
        async def help_command(ctx):
            for command in commandList:
                commandDescription=commandList[command]
                await ctx.send("{}: {}".format(command, commandDescription))

        @self.client.command(name="quit")
        async def quit_command(ctx):
            await ctx.send("Closing event loop...")
            await client.EventLoop().destroy(client.EventLoop().get_loop())