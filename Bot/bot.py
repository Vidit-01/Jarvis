
from chatterbot import ChatBot,logic
import pyjokes
from chatterbot.trainers import ListTrainer

bot = ChatBot('Bot')

print(dir(logic))
#trainer = ChatterBotCorpusTrainer(bot,)
trainer = ListTrainer(bot)

trainer.train([
	"hi",
    "hello"
])

trainer.train([
    "what is your name",
    "My name is jarvis"])
trainer.train([
    "what can you do",
    "I can open websites,search google and many more you can read them at release notes"
])

trainer.train([
    "whats'app"
    "I am fine Sir, how are you doing?"
    "I am also fine"
])

trainer.train([
    "I am bored",
    "Sir shall I tell you a joke",
    "yes",
    pyjokes.get_joke(language="en")
])


if __name__ == "__main__":
    while True:
        request=input('you :')
        if request == 'OK' or request == 'ok':
            print('Bot: bye')
            break
        else:
            response=bot.get_response(request)
            print('Bot:', response)
