import os, sys, discord
from discord.ext import commands

if not os.path.isfile("config.py"):
	sys.exit("'config.py' not found! Please add it and try again.")
else:
	import config

class moderation(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', pass_context=True)
    async def kick(self, context, member: discord.Member, *args):
        """
        Kick a user out of the server.
        """
        if context.message.author.guild_permissions.kick_members:
            if member.guild_permissions.administrator:
                embed = discord.Embed(
                    title="Ошибочка!",
                    description="Админа никто не может кикнуть",
                    color=config.error
                )
                await context.send(embed=embed)
            else:
                try:
                    reason = " ".join(args)
                    await member.kick(reason=reason)
                    embed = discord.Embed(
                        title="Пользователь был кикнун",
                        description=f"**{member}** хахаахахахахахахах!",
                        color=config.success
                    )
                except:
                    embed = discord.Embed(
                        title="Ошибка!",
                        description="Ошибка произашла при ....(надоело писать код)",
                        color=config.success
                    )
                    await context.message.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Ошибка!",
                description="Ты не имеешб достаточно прав чтобы использовать эти команды (аххаах от Нурбека)",
                color=config.error
            )
            await context.send(embed=embed)

    @commands.command(name="nick")
    async def nick(self, context, member: discord.Member, *, name: str):
        """
        Change the nickname of a user on a server.
        """
        if context.message.author.guild_permissions.administrator:
            try:
                if name.lower() == "!reset":
                    name = None
                await member.change_nickname(name)
                embed = discord.Embed(
                    title="Изменил ник!",
                    description=f"**{member}'s** новый никнейм **{name}**!",
                    color=config.success
                )
                await context.send(embed=embed)
            except:
                embed = discord.Embed(
                    title="Ошибка!",
                    description="Ошибка произашла при изменений ника",
                    color=config.success
                )
                await context.message.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="ОШибка!",
                description="Ты не имеешь достаточно прав чтобы использовать эту команду",
                color=config.error
            )
            await context.send(embed=embed)

    @commands.command(name="ban")
    async def ban(self, context, member: discord.Member, *args):
        """
        Bans a user from the server.
        """
        if context.message.author.guild_permissions.administrator:
            try:
                if member.guild_permissions.administrator:
                    embed = discord.Embed(
                        title="Ошибка!",
                        description="Пользователь имеет админские права",
                        color=config.success
                    )
                    await context.send(embed=embed)
                else:
                    reason = " ".join(args)
                    await member.ban(reason=reason)
                    embed = discord.Embed(
                        title="Пользователь забанен",
                        description=f"**{member}** забанен от **{context.message.author}**!",
                        color=config.success
                    )
                    embed.add_field(
                        name="Reason:",
                        value=reason
                    )
                    await context.send(embed=embed)
                    await member.send(f"Ты был банен от **{context.message.author}**!\nReason: {reason}")
            except:
                embed = discord.Embed(
                    title="Ошибка!",
                    description="Ошибка произашла при бане пользователя(ахах от Нурбека)",
                    color=config.success
                )
                await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Ошибка!",
                description="Ты не имеешь достаточно прав чтобы использовать эту команду",
                color=config.error
            )
            await context.send(embed=embed)


def setup(bot):
    bot.add_cog(moderation(bot))