from telethon import events
import asyncio
channels=[1133911744,1784987632,1324553349,1221643554,1767508327,1225233975,1487384219,1332718766]
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
                await client.send_message("@LinkConverTerabot",event.original_update.message)
            time.sleep(2)
            message_recieved=await client.get_messages("@LinkConverTerabot",limit=1)
            await client.forward_messages(1674861391,message_recieved)
    except:
        pass
