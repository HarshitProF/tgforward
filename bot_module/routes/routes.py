from telethon import events
import asyncio
channels=[1496705628,13572755556,1433606813,1514109014,1687952246,1450755585,1348625748]
@events.register(events.NewMessage(incoming=True))
async def send(event):
    client=event.client
    try:
        if event.original_update.message.peer_id.channel_id in channels:
            print(event.original_update.message)
            print("event_recieved")
            try:
                result=await client.forward_messages("Deals_01_bot",event.original_update.message)
            except Exception as e:
                print(e)
                await client.send_message("Deals_01_bot",event.original_update.message)
    except:
        pass