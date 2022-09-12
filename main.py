import discord
import os
from stay_active import stay_active
from responses import on_message
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot:
      return
    if client.user.mentioned_in(message):
        await message.channel.send('Who Pinged')
    
    if message.content.startswith('Ankle'):
        await message.channel.send('Ok')

    if message.content.startswith('ankle'):
        await message.channel.send('Ok')

    if message.content.startswith('Me'):
        await message.channel.send('You')

    if message.content.startswith('me'):
        await message.channel.send('u')
    
    if message.content.startswith('dess'):
        await message.channel.send('Shut the fuck up! NOW!')

    if message.content.startswith('Dess'):
        await message.channel.send('Shut the fuck up! NOW!')
    
    if message.content.startswith('Bulg'):
        await message.channel.send('<:bulgariansquidward:913409675855265864>')

    if message.content.startswith('bulg'):
        await message.channel.send('<:bulgariansquidward:913409675855265864>')

    if message.content.startswith('stfu'):
        await message.channel.send('rude <:bulgariansquidward:913409675855265864>')
    if message.content.startswith('Stfu'):
        await message.channel.send('rude <:bulgariansquidward:913409675855265864>')

    if message.content.startswith('sremb'):
        await message.channel.send('what')

    if message.content.startswith('Sremb'):
        await message.channel.send('what')

    if message.content.startswith('srem'):
        await message.channel.send('Ok')

    if message.content.startswith('Srem'):
        await message.channel.send('Ok')

    if message.content.startswith('darcy'):
        await message.channel.send('fuck you')

    if message.content.startswith('Darcy'):
        await message.channel.send('fuck you')

    if message.content.startswith('albania'):
        await message.channel.send('🇦🇱')
    if message.content.startswith('Albania'):
        await message.channel.send('🇦🇱')
    if message.content.startswith('🇦🇱'):
        await message.channel.send('🇦🇱')

    if message.content.startswith('^'):
        await message.channel.send('^')

    if message.content.startswith('dumb bot'):
        await message.channel.send('no you dumb')

    if message.content.startswith('ugly'):
        await message.channel.send('no you')

    if message.content.startswith('hm'):
        await message.channel.send('hmmmmmmmmmmmmmmm')

    if message.content.startswith('Hm'):
        await message.channel.send('hmmmmmmmmmmmmmmm')

    if message.content.startswith('<:bulgariansquidward:913409675855265864>'):
        await message.channel.send('<:bulgariansquidward:913409675855265864>')

    if message.content.startswith('pepe'):
        await message.channel.send('<:PepeBosnianMujahideen:860450044234170388>')

    if message.content.startswith('Pepe'):
        await message.channel.send('<:PepeBosnianMujahideen:860450044234170388>')
    
    if message.content.startswith('thank'):
        await message.channel.send("you're welcome")
    
    if message.content.startswith('Thank'):
        await message.channel.send("you're welcome")

    if message.content.startswith('thank you'):
        await message.channel.send("you're welcome")

    if message.content.startswith('not'):
        await message.channel.send('why not')

    if message.content.startswith('Not'):
        await message.channel.send('why not')
    
    if message.content.startswith('yes'):
        await message.channel.send('nah')

    if message.content.startswith('Yes'):
        await message.channel.send('nah')
    
    if message.content.startswith('Taz'):
        await message.channel.send('cringe')

    if message.content.startswith('taz'):
        await message.channel.send('cringe')

    if message.content.startswith('🇳🇴'):
        await message.channel.send('🇳🇴')

    if message.content.startswith('Norway'):
        await message.channel.send('🇳🇴')

    if message.content.startswith('norway'):
        await message.channel.send('🇳🇴')

    if message.content.startswith('Malcolm'):
        await message.channel.send('ugly, i hate that gay boy')
    if message.content.startswith('malcolm'):
        await message.channel.send('ugly, i hate that gay boy')

    if message.content.startswith('ew'):
        await message.channel.send('eeeeewwwwwwww')

    if message.content.startswith('Ew'):
        await message.channel.send('eeeeewwwwwwww')
    if message.content.startswith('Shut'):
        await message.channel.send(':(')
    if message.content.startswith('shut'):
        await message.channel.send(':(')
    
    if message.content.startswith('Guendo'):
        await message.channel.send('<:Lipbite:916774004805758996>')
    if message.content.startswith('guendo'):
        await message.channel.send('<:Lipbite:916774004805758996>')
    if message.content.startswith('gwen'):
        await message.channel.send('<:Lipbite:916774004805758996>')
    if message.content.startswith('Gwen'):
        await message.channel.send('<:Lipbite:916774004805758996>')

    if message.content.startswith('Ash'):
        await message.channel.send('🤡')
    if message.content.startswith('ash'):
        await message.channel.send('🤡')

    if message.content.startswith('what'):
        await message.channel.send('idk')
    if message.content.startswith('What'):
        await message.channel.send('idk')
    
    if message.content.startswith('Ballony'):
        await message.channel.send('<:17:856061339806335006>')
    if message.content.startswith('ballony'):
        await message.channel.send('<:17:856061339806335006>')
    
    if message.content.startswith('zero'):
        await message.channel.send('microwave gaming')
    if message.content.startswith('Zero'):
        await message.channel.send('microwave gaming')
    
    if message.content.startswith('steak'):
        await message.channel.send('🥩')
    if message.content.startswith('Steak'):
        await message.channel.send('🥩')

    if message.content.startswith('Abel'):
        await message.channel.send('😍')
    if message.content.startswith('abel'):
        await message.channel.send('❤️')
    if message.content.startswith('Weeknd'):
        await message.channel.send('👍')
    if message.content.startswith('weeknd'):
        await message.channel.send('🎵')
    if message.content.startswith('4 8 15 16 23 42'):
        await message.channel.send('108')
    if message.content.startswith('4815162342'):
        await message.channel.send('108')
    
    if message.content.startswith('Syeda'):
        await message.channel.send('table tennis ball')
    if message.content.startswith('syeda'):
        await message.channel.send('banana how')
    if message.content.startswith('SYEDA'):
        await message.channel.send('table tennis ball')
    if message.content.startswith('ask'):
        await message.channel.send('Ask syeda')
    if message.content.startswith('Ask'):
        await message.channel.send('Ask syeda')
    if message.content.startswith('ASK'):
        await message.channel.send('ask syeda')

stay_active()
client.run(os.getenv('TOKEN'))

