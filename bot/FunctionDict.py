import discord


async def Epv(message, ListElementInMessage):
    if len(ListElementInMessage) == 3 and ListElementInMessage[1].isnumeric() and ListElementInMessage[2].isnumeric():
        a = int(ListElementInMessage[1])
        b = int(ListElementInMessage[2])
        c = round(a/(1-(b/(b+1200))))
        embed = discord.Embed(title="Epv", color=0xffffff)
        embed.set_thumbnail(url="")
        embed.add_field(name="Calculs effectués avec:", value="\nPV : " +
                        str(a) + "\nDéfense : " + str(b) + "\n\nEpv : " + str(c), inline=False)
        await message.channel.send(embed=embed)
    else:
        await message.channel.send("Erreur, Ecrivez Epv suivi des PV et de la Def. (ex : Epv 20000 2000)")

Functions = {
    "Epv2": Epv
}
