from flask import Flask, request, Response
from botbuilder.schema import Activity
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
import asyncio

from bot import ActivityBot
from middleware import Middleware1

app = Flask(__name__)
loop = asyncio.get_event_loop()

eBot = ActivityBot()

botAdapterSettings = BotFrameworkAdapterSettings("","")
botAdapter = BotFrameworkAdapter(botAdapterSettings)
botAdapter.use(Middleware1())

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