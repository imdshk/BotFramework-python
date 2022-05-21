from botbuilder.core import TurnContext

class EchoBot:
    async def OnTurn(self, turn_context: TurnContext):
        await turn_context.send_activity(turn_context.activity.text)