# bibliotecas de importação
import discord
from discord.ext import commands

# prefixo do bot e intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

# eventos do bot e comndos de verificação de funcionamento
@bot.event
async def on_ready():
    print(f'bhee Esta! pronto como {bot.user.name}')

@bot.command()
async def pat(ctx: commands.Context):
    await ctx.reply("bhee~")

# comando de rolagem de dados ( deve conter comando sem prefixo utilizando XdY e tambem poder conter modificadores como XdYlZ entre outros tambem deve conter comando com prefixo para fazer calculos dos dados com + - / * ^ % )

# comandos para puxar ficha de personagem ( contendo comandos para anexar pdf editar campo fazer anotações calcular nivel e criar macro de rolagem de dados)

# comando para tocar musica do rpg ( deve conter comando que cria um painel para controlar a musica deve receber playlists deve ter opção de looping deve ter opção de trocar para uma musica especifica da playlist deve ter opção de pular musica deve ter opção de pausar musica deve ter opção de voltar para a musica anterior deve ter opção de aumentar e diminuir volume deve ter opção de mostrar a musica atual que esta tocando)

bot.run("Token")
