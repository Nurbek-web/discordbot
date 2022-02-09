import os, sys, discord, platform, random, aiohttp, json
from discord.ext import commands

if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class general(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="info", aliases=["botinfo"])
    async def info(self, context):
        """
        Get some useful (or not) information about the bot.
        """
        embed = discord.Embed(
            description="Использовал Nurbek's шаблон",
            color=config.success
        )
        embed.set_author(
            name="Bot Information"
        )
        embed.add_field(
            name="Владелец:",
            value="actuallyastarfish#3921",
            inline=True
        )
        embed.add_field(
            name="Префикс:",
            value=f"{config.BOT_PREFIX}",
            inline=False
        )
        embed.set_footer(
            text=f"Requested by {context.message.author}"
        )
        await context.send(embed=embed)

    @commands.command(name="serverinfo")
    async def serverinfo(self, context):
        """
        Get some useful (or not) information about the server.
        """
        server = context.message.guild
        roles = [x.name for x in server.roles]
        role_length = len(roles)
        if role_length > 50:
            roles = roles[:50]
            roles.append(f">>>> Displaying[50/{len(roles)}] Roles")
        roles = ", ".join(roles)
        channels = len(server.channels)
        time = str(server.created_at)
        time = time.split(" ")
        time = time[0]

        embed = discord.Embed(
            title="**Server Name:**",
            description=f"{server}",
            color=config.success
        )
        embed.set_thumbnail(
            url=server.icon_url
        )
        embed.add_field(
            name="Владелец",
            value=f"{server.owner}\n{server.owner.id}"
        )
        embed.add_field(
            name="Server ID",
            value=server.id
        )
        embed.add_field(
            name="Количество учатников",
            value=server.member_count
        )
        await context.send(embed=embed)

    @commands.command(name="ping")
    async def ping(self, context):
        """
        Check if the bot is alive.
        """
        embed = discord.Embed(
            color=config.success
        )
        embed.add_field(
            name="Понг!",
            value=":ping_pong:",
            inline=True
        )
        embed.set_footer(
            text=f"Pong request by {context.message.author}"
        )
        await context.send(embed=embed)

    @commands.command(name="invite")
    async def invite(self, context):
        """
        Get the invite link of the bot to be able to invite it.
        """
        await context.send("I sent you a private message!")
        await context.author.send(f"Invite me by clicking here: https://discordapp.com/oauth2/authorize?&client_id={config.APPLICATION_ID}&scope=bot&permissions=8")

    @commands.command(name="server")
    async def server(self, context):
        """
        Get the invite link of the discord server of the bot for some support.
        """
        await context.send("Я отправил сообщение в личку!")
        await context.author.send("Даун что ли?")

    @commands.command(name="poll")
    async def poll(self, context, *args):
        """
        Create a poll where members can vote.
        """
        poll_title = " ".join(args)
        embed = discord.Embed(
            title="Новое голосование создано!",
            description=f"{poll_title}",
            color=config.success
        )
        embed.set_footer(
            text=f"Голосование было создано: {context.message.author} • реагируй чтобы голосовать!"
        )
        embed_message = await context.send(embed=embed)
        await embed_message.add_reaction("👍")
        await embed_message.add_reaction("👎")
        await embed_message.add_reaction("🤷")

    @commands.command(name="ask")
    async def eight_ball(self, context, *args):
        """
        Ask any question to the bot.
        """
        answers = ['Конечно!', 'Безусловно', 'НЕТ ДАУН ЧТО ЛИ', 'КОНЕЧНО ДА', 'Нурбек лучший']
        embed = discord.Embed(
            title=f"{answers[random.randint(0, len(answers))]}",
            color=config.success
        )
        await context.send(embed=embed)

    @commands.command(name="bitcoin")
    async def bitcoin(self, context):
        """
        Get the current price of bitcoin.
        """
        url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
        # Async HTTP request
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed = discord.Embed(
                title=response,
                color=config.success
            )
            await context.send(embed=embed)




def setup(bot):
    bot.add_cog(general(bot))