from dis import dis
import discord
import responses





async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
        
    except Exception as e:
        print(e)
        
        
def run_discord_bot():
    TOKEN = "MTAzNTUxOTM4MzcwNDk2NTE2MA.GzNteM.IyvW18FnwkhgQv0AOHG3H9ExQ4BOk8ypQSTek0"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
    
    #envio de mensajes    
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        #leyendo el chat
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f'{username} said:"{user_message}"({channel})')
        
        #prefijo para mensajes hacía el bot
        
        if message.content.startswith('a!'):
            user_message = user_message[2:]
            await send_message(message, user_message, is_private=False)
        
        #prefijo para obtener mensaje privado del bot
        
        elif user_message[0] == '!':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
    
        
            
    client.run(TOKEN)
            
        
        
    
            
             
    
            
    