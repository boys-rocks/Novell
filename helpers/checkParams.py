def checkCommandParams(bot, args):
    values = []
    for each in bot.get_command(args).params.keys():
        if each != 'ctx' and each != 'self':
            values.append(each)
    if values:
        return values
    else:
        return None