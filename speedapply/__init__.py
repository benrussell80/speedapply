def start(bots, settings):
    from speedapply.bots import ApplyBot

    for name, bot in bots.__dict__.items():
        if isinstance(bot, ApplyBot): 
            bot(settings).auto_apply()