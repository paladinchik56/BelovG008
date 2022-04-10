saved_var = {}
echo = lambda sentences: sentences
my_split = lambda sentences: sentences[1:].split(sentences[0])
get_saved = lambda val: saved_var[val.strip("\n")]

def funcSaveVal(message):
    global saved_var
    message = message.split("=")
    name = message[0].replace("$", "")
    val = message[1]
    saved_var[name] = val
    return f"{name}={saved_var[name]}"
saveVal = funcSaveVal