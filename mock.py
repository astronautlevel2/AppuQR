from discord.ext import commands
from random import random

"""CoG uSeD fOr TyPiNg LiKe ThIs"""

class Mock:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def mock(self, ctx, *, message):
        """`mock` text you want to mock"""

        msgbuf = ""
        uppercount = 0
        lowercount = 0
        for c in message:
            if c.isalpha():
                if uppercount == 2:
                    uppercount = 0
                    upper = False
                    lowercount += 1
                elif lowercount == 2:
                    lowercount = 0
                    upper = True
                    uppercount += 1
                else:
                    upper = random() > 0.5
                    uppercount = uppercount + 1 if upper else 0
                    lowercount = lowercount + 1 if not upper else 0

                msgbuf += c.upper() if upper else c.lower()
            else:
                msgbuf += c
        await ctx.message.edit(content=msgbuf)

def setup(bot):
    bot.add_cog(Mock(bot))
