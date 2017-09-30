import qrcode
from discord.ext import commands

"""Module for generating QR codes from attachments and URLs"""

class QRGen:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def qr(self, ctx, url=""):
        """Generate QR Code"""

        if url == "":
            async for m in ctx.channel.history():
                if len(m.attachments) == 1: # Currently this only supports 1 attachment at most
                    img = qrcode.make(m.attachments[0].url)
                    await ctx.send(file=discord.File(img, "qr_code.png")
