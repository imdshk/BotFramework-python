from botbuilder.core import TurnContext
from botbuilder.schema import ActivityTypes

class ActivityBot():
    async def onTurn(self, turnContext: TurnContext):
        if turnContext.activity.type == ActivityTypes.conversation_update:
            await turnContext.send_activity("Hello! Welcome to the Echo Bot!")
        if turnContext.activity.type == ActivityTypes.message:
            await turnContext.send_activity(turnContext.activity.text)