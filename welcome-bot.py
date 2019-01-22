# welcome-bot
## this bot will send a welcome message and assign a role

# import all necessary commands and libraries
import discord
import asyncio
import datetime


client=discord.Client()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Created by: MrFox'))
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

newUserMessage = """**WELCOME    TO    FOX ROBOT'S    SERVER**

:warning: `Server Rules:`

`➀` **No harassment or personal attacks. Ever.**

`➁` **No NSFW content. If its even suggestive (images OR text), it's not allowed.**

`➂` **No spamming. This goes for text/voice/reactions/everything. The exception is**

`➃` **No advertising. This applies to advertisements of any kind, and includes direct messages. Advertising is an immediate ban.**

`➄` **Do not ask for roles. You can use the commands listed at the bottom of this channel for updates roles. You will only be given the Bot Developers role if I like your bot enough to add it here. You may ask (only once), and it must already be approved on the Discord Bots server.**

`Source By Mr.Fox#6950`
"""
newUserMessage2 = """https://discord.gg/yk5B3bM"""
@client.event
async def on_member_join(member):
    date = datetime.datetime.now()
    em2 = discord.Embed(description = newUserMessage,colour=0x3955a3)
    await client.send_message(member,embed=em2)
    em = discord.Embed(description= f":small_orange_diamond:`Username:` <@{member.id}>\n:small_blue_diamond:`UserId:` {member.id}\n:small_orange_diamond:`time:` {date.hour} : {date.minute} : {date.second}\n:small_blue_diamond:`date:` {date.year} / {date.month} / {date.day}\n\n:white_check_mark:**Has been joined To Server**",colour=0x1bbc20)
    print("Recognised that a member called " + member.name + " joined")
    await client.send_message(member, newUserMessage2)
    await client.send_message(client.get_channel('521692602207174656'),embed=em)
    await client.send_message(client.get_channel('521690991770468362'),embed=em)
    print("Sent message to " + member.name)
    
    # give member the steam role here
    ## to do this the bot must have 'Manage Roles' permission on server, and role to add must be lower than bot's top role
    role = discord.utils.get(member.server.roles, name="Member")
    await client.add_roles(member, role)
    print("Added role '" + role.name + "' to " + member.name)
    
@client.event
async def on_member_remove(member):
    date = datetime.datetime.now()
    em = discord.Embed(description= f":small_orange_diamond:`Username:` <@{member.id}>\n:small_blue_diamond:`UserId:` {member.id}\n:small_orange_diamond:`time:` {date.hour} : {date.minute} : {date.second}\n:small_blue_diamond:`date:` {date.year} / {date.month} / {date.day}\n\n:warning:**Has been Left To Server**",colour=0xe50f00)
    print("Recognised that a member called " + member.name + " left")
    await client.send_message(client.get_channel('521692602207174656'),embed=em)
    
client.run('NTI5OTkzMTY2MDgyODAxNjc1.Dw-kaw.uRv4PRMJW-th_27cLOqrrr1SJMk') 
#await client.send_message(client.get_channel('521690991770468362'),embed=em)




