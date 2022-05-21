from flask import Flask, request, Response
from botbuilder.schema import Activity
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, ConversationState, UserState, MemoryStorage
import asyncio

from bot.state_bot import StateBot

app = Flask(__name__)
loop = asyncio.get_event_loop()

botAdapterSettings = BotFrameworkAdapterSettings("","")
botAdapter = BotFrameworkAdapter(botAdapterSettings)

memstore = MemoryStorage()
constate = ConversationState(memstore)
userstate = UserState(memstore)

eBot = StateBot(constate, userstate)

@app.route("/api/messages", methods=["POST"])
def messages():
    if "application/json" in request.headers["content-type"]:
        jsonMessage = request.json
    else:
        return Response(status=415)
    
    activity = Activity().deserialize(jsonMessage)

    async def turn_call(turn_context):
        await eBot.on_turn(turn_context)

    task = loop.create_task(botAdapter.process_activity(activity, "", turn_call))
    loop.run_until_complete(task)

if __name__ == "__main__":
    app.run("localhost", 3978) 