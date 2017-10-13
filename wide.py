from discord.ext import commands

"""Cog used to make text ＷＩＤＥ"""

class Wide:
    def __init__(self, bot):
        self.bot = bot
        self.substitution_dict = {
            "a": "Ａ",
            "b": "Ｂ",
            "c": "Ｃ",
            "d": "Ｄ",
            "e": "Ｅ",
            "f": "Ｆ",
            "g": "Ｇ",
            "h": "Ｈ",
            "i": "Ｉ",
            "j": "Ｊ",
            "k": "Ｋ",
            "l": "Ｌ",
            "m": "Ｍ",
            "n": "Ｎ",
            "o": "Ｏ",
            "p": "Ｐ",
            "q": "Ｑ",
            "r": "Ｒ",
            "s": "Ｓ",
            "t": "Ｔ",
            "u": "Ｕ",
            "v": "Ｖ",
            "w": "Ｗ",
            "x": "Ｘ",
            "y": "Ｙ",
            "z": "Ｚ",
            "1": "１",
            "2": "２",
            "3": "３",
            "4": "４",
            "5": "５",
            "6": "６",
            "7": "７",
            "8": "８",
            "9": "９",
            "0": "０",
            "!": "！",
            "?": "？",
            " ": "　"
            }

    @commands.command()
    async def wide(self, ctx, *, message):
        """[p]wide <text to make wide>"""

        result = message.lower().translate(str.maketrans(self.substitution_dict))

        await ctx.message.delete()
        await ctx.send(result)

def setup(bot):
    bot.add_cog(Wide(bot))
