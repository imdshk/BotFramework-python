from botbuilder.core import TurnContext, ActivityHandler
from botbuilder.schema import ActivityTypes, ChannelAccount

class ActivityBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        await turn_context.send_activity(turn_context.activity.text)
    async def on_members_added_activity(self, member_added: ChannelAccount, turnContext: TurnContext):
        await turnContext.send_activity("Welcome! This is Activity Bot")
        for member in member_added:
            await turnContext.send_activity(member.name)