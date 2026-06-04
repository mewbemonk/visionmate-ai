def save_context(text):

    with open("context.txt", "w", encoding="utf-8") as f:
        f.write(text)


def get_context():

    try:

        with open("context.txt", "r", encoding="utf-8") as f:
            return f.read()

    except FileNotFoundError:

        return ""