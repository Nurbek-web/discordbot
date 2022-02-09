import os, sys, discord
from discord.ext import commands

if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class Help(commands.Cog, name="help"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, context):
        """
        List all commands from every Cog the bot has loaded.
        """

        text = 'cock - размер\n' \
               'info - информация о боте\n' \
               'ping - пинг\n' \
               'server - сервер\n' \
               'poll - начать голосование\n' \
               'ask - спросить у бота\n' \
               'bitcoin - цена на биткойн\n' \
               'kick - кикнуть участника\n' \
               'nick - изменить никнейм учатника\n' \
               'ban - дать бан участнику\n' \
               'shutdown - закрыть рот боту\n' \
               'say - скажет бот\n'
        embed = discord.Embed(
            title="КОМАНДЫ:",
            description=text,
            color=config.success
        )
        await context.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))