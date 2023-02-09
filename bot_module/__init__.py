from telethon import TelegramClient 
api_id=18068266
api_hash='f7b6ef1e9bcfde7cbb4aca38c944d0ac'
def connect():
    client=TelegramClient('Harshit',api_id,api_hash)
    return client
user=connect()