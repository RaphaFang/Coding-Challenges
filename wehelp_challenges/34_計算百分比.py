def toPercentage(completed, total):
    if total == 0:
        return "0%"
    else:
        percentage = (completed / total) * 100
        return f"{int(percentage)}%"

toPercentage(3,10)