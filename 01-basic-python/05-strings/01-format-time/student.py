def format_time(hours, minutes, seconds):
    def format(x):
        return str(x).rjust(2, '0')
        # rjust --> minsten 2 karakters lang anders word het opgevuld met nullen
    hours = format(hours)
    minutes = format(minutes)
    seconds = format(seconds)

    return f"{hours}:{minutes}:{seconds}"

print(format_time(14,5,48))