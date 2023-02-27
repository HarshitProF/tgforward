from telethon import events
import asyncio
channels=[1133911744,1784987632,1324553349,1221643554,1767508327,1225233975,1487384219,1332718766,1816608121,1722675118,1822253001]
@events.register(events.NewMessage(incoming=True))
async def send(event):
    client=event.client
    try:
        if event.original_update.message.peer_id.channel_id in channels:
            print("event_recieved")
            try:
                result=await client.forward_messages("@LinkConvertTerabot",event.original_update.message)
            except Exception as e:
                print(e)
                await client.send_message("@LinkConvertTerabot",event.original_update.message)
            entity=await client.get_entity("@LinkConvertTerabot")
            print(entity)
            await asyncio.sleep(10)
            message_recieved= await client.get_messages(entity,limit=1)
            print(message_recieved[0].message)
            try:
                channel_entity=await client.get_entity(1674861391)
            except Exception as e:
                print(e)
            try:
                await client.forward_messages(channel_entity,message_recieved[0])
            except Exception as e:
                print(e)
    except:
        pass
