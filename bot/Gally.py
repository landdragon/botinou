import discord
from discord.ext import commands
import os
import asyncio
import FunctionDict

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
HEROKU_RELEASE_VERSION = os.getenv("HEROKU_RELEASE_VERSION")
HEROKU_RELEASE_CREATED_AT = os.getenv("HEROKU_RELEASE_CREATED_AT")
HEROKU_SLUG_DESCRIPTION = os.getenv("HEROKU_SLUG_DESCRIPTION")
IsInNotProd = os.getenv("IsInNotProd")

client = discord.Client()
Functions = FunctionDict.Functions


@client.event
async def on_message(message: discord.Message):
    # don't respond to ourselves
    if message.author == client.user:
        return
    ListElementInMessage: list[str] = message.content.split()

    if ListElementInMessage[0] in Functions:
        await Functions[ListElementInMessage[0]](message, ListElementInMessage)
        return

    if ListElementInMessage[0] == "Hello":
        await message.channel.send("salut ami humain")

    if ListElementInMessage[0].lower() == "version":
        await message.channel.send("ma version est "+HEROKU_RELEASE_VERSION+".\nj'ai été créer à " + HEROKU_RELEASE_CREATED_AT)

    if ListElementInMessage[0].lower() == "git":
        await message.channel.send("Ma version git est "+HEROKU_SLUG_DESCRIPTION)

    if ListElementInMessage[0] == "Liste":
        embed = discord.Embed(title="Liste des commandes :", color=0xffffff)
        embed.set_thumbnail(url="")
        embed.add_field(
            name="Menu :", value="Menu \nSommaire \nInfo \nHelp \npas fini", inline=False)
        embed.add_field(name="Lexique :", value="Lexique", inline=False)
        embed.add_field(
            name="Trinket :", value="Trink \nTrinkPv \nTrinkAtk \n TrinkDc", inline=False)
        embed.add_field(name="Gemmes :",
                        value="On met quoi dans Gemmes ?", inline=False)
        embed.add_field(name="Améliorations :",
                        value="Hp+ Hp% Def+ Atk+ Atk% Dc", inline=True)
        embed.add_field(name="Astromons :", value="DarkVadehors", inline=False)
        embed.add_field(
            name="Calculs :", value="Epv \nEpvGem \nDégats \nDmg Aggr PV \nDmg Aggr Def \nDmg Aggr Rec \nHeal", inline=False)
        embed.add_field(
            name="Titi :", value="Titi# (# étant un chiffre ou un nombre)", inline=False)
        embed.add_field(
            name="Lead :", value="Lead \nLdTcDown \nLdTcUp \nLdDefUp \nLdDefDown", inline=False)
        embed.add_field(name="Attaques :",
                        value="Competences \nAdrenaline", inline=False)
        embed.add_field(
            name="Top Liste :", value="En image ce serai pas mal \nHeal \npvp \nTiti \nbois \nEtc", inline=False)
        embed.add_field(
            name="Boss :", value="Colosses \nTitans \nGolems \nDragon \n WB", inline=False)
        embed.add_field(name="Liste de Commandes :",
                        value="Liste", inline=False)
        await message.channel.send(embed=embed)


@client.event
async def on_ready():
    print(client.user.name)
    print("[ON]")
    print('- - - - - - - -')
    if IsInNotProd == "true":
        print('send message to say Hello')
        for Channel in client.get_all_channels():
            if Channel.type == discord.ChannelType.text:
                await Channel.send("salut je viens d'être livré avec pour version : " + HEROKU_RELEASE_VERSION)

client.run(TOKEN)
