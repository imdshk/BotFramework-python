from botbuilder.core import TurnContext

class EchoBot:
    async def OnTurn(self, turnContext: TurnContext):
        await turnContext.send_activity(turnContext.activity.text)