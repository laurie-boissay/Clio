#!/usr/bin/python3.8
#coding:u8


import discord

from commandes.all_cmd import *


class MyClient(discord.Client):
    """
    Confirme dans la console que Clio est connectée.

    Clio affiche : "Regarde !help" sous son nom.

    Prend tous les message en entrée pour vérifier s'il s'agit d'une commande.

    Appelle is_it_cmd, affiche le text dans le canal définit ou ne fait rien.
    """
    async def on_ready(self):

        print(f'{self.user} est connectée à Discord !')
        await client.change_presence(activity=discord.Activity(type=3, name="!aide"))

    async def on_message(self, message):
        canal, text = all_users_cmd(message, client)
        if text != "not a cmd":
            await canal.send(text)
        
                

client = MyClient()
client.run('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

# cd /home/jaenne/Python/clio
# ./clio.py