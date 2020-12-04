
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


async def EpvGem(message, ListElementInMessage):
    if len(ListElementInMessage) == 3 and ListElementInMessage[1].isnumeric() and ListElementInMessage[2].isnumeric():
        a = int(ListElementInMessage[1])
        b = int(ListElementInMessage[2])
        c = round((a * 2.36) / (1 - ((b * 1.68) / ((b * 1.68) + 1200))))
        d = round((a * 1.68) / (1 - ((b * 2.36) / ((b * 2.36) + 1200))))
        embed = discord.Embed(
            title="Choisir entre : \n- 2 gemmes pv + 1 gemme def\n- 2 gemmes def + 1 gemme pv", color=0xffffff)
        embed.set_thumbnail(
            url="https://vignette.wikia.nocookie.net/mslgame/images/a/aa/Gem.png/revision/latest/top-crop/width/150/height/150?cb=20160922163030")
        embed.add_field(name="Calculs effectués avec:", value="\nPV de base: " + str(a) + "\nDéfense de base: " +
                        str(b) + "\n\nEpv avec 2Pv + 1Def: " + str(c) + "\nEpv avec 1Pv + 2Def: " + str(d), inline=False)
        await message.channel.send(embed=embed)
    else:
        await message.channel.send("Erreur, Ecrivez EpvGem suivi des PV de base et de la Def de base")


async def D(message, ListElementInMessage):
    if len(ListElementInMessage) == 4 and ListElementInMessage[1].isnumeric() and ListElementInMessage[2].isnumeric and ListElementInMessage[3].isnumeric:
        a = int(ListElementInMessage[1])
        b = int(ListElementInMessage[2])
        c = int(ListElementInMessage[3])
        d = round(a*5.5)
        e = round(a*5.5*(1+(b/100)*(c/100)))
        f = round(a*5.5*(1+(c/100)))
        embed = discord.Embed(
            title="les Dmg de l'Astromon :", color=0xffffff)
        embed.set_thumbnail(url="")
        embed.add_field(name="Calculs effectués avec : ", value="atk : " + str(a) + "\nTc : " + str(b) + "\nDc : " + str(
            c) + "\n\nDégats sans crit : " + str(d) + "\nDégats moyens : "+str(e)+"\nDégats crit : "+str(f), inline=False)
        await message.channel.send(embed=embed)
    else:
        await message.channel.send("Erreur, Ecrivez D suivi de l'attaque, du taux critique et des dégats critique")
