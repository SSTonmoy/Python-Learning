# Repeat program 4 for a list of such words to be censored
# Code of program 4 :


bad_words = [
    "fuck",
    "shit",
    "bitch",
    "asshole",
    "bastard",
    "damn",
    "hell",
    "crap",
    "dick",
    "piss"
]
censored_words = {
    "fuck": "f***",
    "shit": "s***",
    "bitch": "b****",
    "asshole": "a******",
    "bastard": "b******",
    "damn": "d***",
    "hell": "h***",
    "crap": "c***",
    "dick": "d***",
    "piss": "p***"
}
with open('Chapter09/Censored.txt', 'r') as f:
    content = f.read()
for word in bad_words:
    content = content.replace(word, censored_words[word])

with open('Chapter09/Censored.txt', 'w') as f:
    f.write(content)
