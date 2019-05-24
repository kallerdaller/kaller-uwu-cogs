from .hboobs import Hboobs

def setup(bot):
    n = Hboobs(bot)
    bot.add_cog(n)
    bot.loop.create_task(n.boob_knowlegde())