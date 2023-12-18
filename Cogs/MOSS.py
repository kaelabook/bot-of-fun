# imports Discord 
from discord import app_commands
from discord.ext import commands
from utils.utils import *

# adds my cog to the bot
async def setup(bot:commands.Bot):
    await bot.add_cog(MOSS(bot))

# constructor method that passes in Cog commands???
class MOSS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @app_commands.command(description="This will check if students are cheaters")
    @app_commands.default_permissions(administrator=True)
    async def test(self, interaction:discord.Interaction):
        """ Run MOSS command
        Idk

        Args:
            upload_file (file): similar to course management upload file

        Outputs:
            MOSS URL
        """
        await interaction.response.send_message("MOSS has been run ;)")
