import discord
from discord.ext import commands
from openai import OpenAI

api_key = 'get ur own one 2'

def generate_response(prompt, system_msg=None):
    client = OpenAI(
        
    
        api_key=api_key,
    )

    messages = [
        {
            "role": "user",
            "content": prompt,
        }
    ]
    if system_msg:
        messages.append({
            "role": "system",
            "content": system_msg
        })

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )

    response = chat_completion.choices[0].message.content
    return response

bot = commands.Bot(command_prefix="-", intents=discord.Intents.all())

@bot.event
async def on_ready():
    # set bot status
    await bot.change_presence(activity=discord.Game(name="Made by Glitch Network | discord.gg/dmD752HN | https://github.com/infdevv/personality-bot"))

@bot.command()
async def msg(ctx, *, message):
    async with ctx.typing():
        generated_response = generate_response(message, f"User mentioned in message by {ctx.author}")
        await ctx.send(generated_response)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message) or (message.reference and message.reference.resolved.author == bot.user):
        referenced_message = message.reference.resolved.content if message.reference else None
        ctx = await bot.get_context(message)
        await bot.process_commands(message)  
    else:
        await bot.process_commands(message)



bot.run('get ur own one')
