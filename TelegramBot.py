from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
import time
from config import api_hash, api_id, phone

class TelegramBot:
    def __init__(self) -> None:
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone = phone
        self.client = TelegramClient(self.phone, self.api_id, self.api_hash)
        self.connect()

    def connect(self):
        self.client.connect()
        if not self.client.is_user_authorized():
            self.client.send_code_request(self.phone)
            self.client.sign_in(self.phone, input('Digite o código:'))
        return