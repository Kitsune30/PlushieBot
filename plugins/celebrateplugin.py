from .plugin import *

import random


class CelebratePlugin(PlushiePlugin):
    name = "Celebration Plugin"
    description = "Give Plushie some awesome celebration lines"
    authors = ["Garth"]

    @plushieCmd("celebrate")
    @commandDoc(doc="Has Plushie celebrate.")
    def celebrate(self, ctx, msg):
        rand = random.randint(0, 3)

        if rand == 0:
            ctx.msg("WooOOooOOooOOooOOoo! Party! \\ :O /", msg.replyTo)
        elif rand == 1:
            ctx.msg("It's time to celebrate everyone! ~(^.^~)", msg.replyTo)
        elif rand == 2:
            ctx.msg("\\(^.^)/ Get happy: celebrate!", msg.replyTo)
        else:
            ctx.msg("(~^.^)~ Party time! ~(^.^~)", msg.replyTo)
