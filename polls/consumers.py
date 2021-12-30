import asyncio
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.core import serializers
from polls.models import Answer, Poll
from django.db.models.signals import post_save
from django.dispatch import receiver



class PollConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("connected", event)
        await self.send({
            "type": "websocket.accept"
        })
        # get selected poll
        self.poll = int(self.scope['path'].split('/')[3])

        self.poll_num = f"{self.poll}"

        # add channel to group
        await self.channel_layer.group_add(self.poll_num, self.channel_name)


    async def websocket_receive(self, event):
        print("received", event)


    async def websocket_disconnect(self, event):
        await self.channel_layer.group_discard(
            self.poll_num,
            self.channel_name,
        ) 
        print("disconnect", event)


    @receiver(post_save,sender=Answer)
    def answers_update(sender, instance, **kwargs):
        poll = str(instance.question_id.id)
        channel_layer = get_channel_layer()
        msg = serializers.serialize('json', [instance, ])

        async_to_sync(channel_layer.group_send)(
            poll,
            {
                "type": "send_update",
                "text": msg,
            }
        )

    async def send_update(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event['text'],
        })
        

        
        
        