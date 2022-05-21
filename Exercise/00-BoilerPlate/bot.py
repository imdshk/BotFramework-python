from botbuilder.core import TurnContext

class Bot():
    def onTurn(self, turn_context: TurnContext):
        turn_context.send_activity(turn_context.activity.text)