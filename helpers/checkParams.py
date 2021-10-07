def checkCommandParams(bot, args):
    values = []
    for each in bot.get_command(args).params.keys():
        if each not in ("ctx", "self"):
            values.append(each)
    if values:
        return values
    return None
