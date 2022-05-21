from flask import Flask, request, Response
from botbuilder.schema import Activity
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
import asyncio
from echoBot import EchoBot

app = Flask(__name__)
loop = asyncio.get_event_loop()

botAdapterSettings = BotFrameworkAdapterSettings("","")
botAdapter = BotFrameworkAdapter(botAdapterSettings)

echoBot = EchoBot()

@app.route("/api/messages", methods=["POST"])
def messages():
    if "application/json" in request.headers["content-type"]:
        jsonMessage = request.json
    else:
        return Response(status=415)
    
    activity = Activity().deserialize(jsonMessage)

    async def turnCall(turnContext):
        await echoBot.OnTurn(turnContext)

    task = loop.create_task(botAdapter.process_activity(activity, "", turnCall))
    loop.run_until_complete(task)

if __name__ == "__main__":
    app.run("localhost", 3978) 