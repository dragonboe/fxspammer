import asyncio
import aiohttp
import colorama
from colorama import Fore, init
from pystyle import Center, Write, Colors, Colorate 

async def send_message(session, webhook_url, message_content, username, successful_messages, num_messages):
    payload = {'content': f'{message_content}', 'tts': False, 'username': username}

    async with session.post(webhook_url, json=payload) as response:
        if response.status == 204:
            successful_messages += 1
            print(Colorate.Horizontal(Colors.blue_to_red, f"Message sent successfully. ({successful_messages}/{num_messages})"))
            return True
        elif response.status == 429:
            print(Colorate.Horizontal(Colors.blue_to_red, ("Rate limited, retrying after 2 seconds...")))
            await asyncio.sleep(2)
            return False
        else:
            print(Colorate.Horizontal(Colors.blue_to_red, "Failed to send message. Retrying..."))
            return False

async def webhook_spammer():
    webhook_url = input(Colorate.Horizontal(Colors.blue_to_red, "Webhook URL: "))
    message_content = input(Colorate.Horizontal(Colors.blue_to_red, "Message: "))
    username = input(Colorate.Horizontal(Colors.blue_to_red, "Webhook username: "))
    num_messages = int(input(Colorate.Horizontal(Colors.blue_to_red, "Number of messages to send: ")))

    successful_messages = 0

    async with aiohttp.ClientSession() as session:
        while successful_messages < num_messages:
            try:
                success = await send_message(session, webhook_url, message_content, username, successful_messages, num_messages)
                if success:
                    successful_messages += 1
            except:
                print(Colorate.Horizontal(Colors.blue_to_red, "An error occurred while sending the message. Retrying..."))

asyncio.run(webhook_spammer())