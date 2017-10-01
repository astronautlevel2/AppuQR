from discord.ext import commands

"""CoG uSeD fOr TyPiNg LiKe ThIs"""

class Mock:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def mock(self, ctx, *, message):
        """`mock` text you want to mock"""

        msgbuf = ""
        upper = False
        for c in message:
            if c.isalpha():
                msgbuf += c.upper() if upper else c.lower()
                upper = not upper
            else:
                msgbuf += c
        await ctx.message.edit(content=msgbuf)

def setup(bot):
    bot.add_cog(Mock(bot))
