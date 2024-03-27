#Dictionary Exercise - Emoji Converter
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "🙁",
    ":|": "😐",
    "<3": "❤️",
}

print(words)

output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
