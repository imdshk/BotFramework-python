from botbuilder.core import TurnContext

class Bot():
    def onTurn(self, turnContext: TurnContext):
        turnContext.send_activity(turnContext.activity.text)