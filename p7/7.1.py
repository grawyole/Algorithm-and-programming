text = "програма"

size = len(text)
head = text[0] if size > 0 else ""
tail = text[-1] if size > 0 else ""
backward = text[::-1]

print(f"{size}, '{head}', '{tail}', \"{backward}\"")