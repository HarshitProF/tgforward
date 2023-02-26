from telethon import events
import asyncio
channels=[1133911744,1784987632,1324553349,1221643554,1767508327,1225233975,1487384219,1332718766,1816608121]
@events.register(events.NewMessage(incoming=True))
async def send(event):
    client=event.client
    try:
        if event.original_update.message.peer_id.channel_id in channels:
            print(event.original_update.message)
            print("event_recieved")
            try:
                result=await client.forward_messages("@LinkConvertTerabot",event.original_update.message)
            except Exception as e:
                print(e)
                await client.send_message("@LinkConvertTerabot",event.original_update.message)
            message_recieved=await client.get_messages("@LinkConvertTerabot",limit=1)
            print("done")
            print(massage_recieved)
            await client.forward_messages(1674861391,message_recieved)
    except:
        pass
