from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit
import wikipedia

bot = ChatBot(
    'Riyona',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)
#bot.set_trainer(ListTrainer)
trainer = ListTrainer(bot)

for files in os.listdir('english/'):
    data = open('english/' + files ,'r').readlines()
    trainer.train(data)

weather = YahooWeather(APP_ID="bZfbp95i",
                     api_key="dj0yJmk9WlFYSnR2ZG5aTUcxJmQ9WVdrOVlscG1ZbkE1TldrbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWJh",
                     api_secret="46d7dd26679a3d6bdfc8e59ccb392469c1027d5d")

print('---------------------------------------------')
print('|HAI, I AM RIYONA.\n|1.You can Check Weather TYPE: Weather.\n|2.Search Wiki TYPE: Wiki.')
print('---------------------------------------------')
while True:
    message = input('You:')
    if message.strip() == 'Wiki':
        wiki = input('Search:')
        print('Riyona:',wikipedia.summary(wiki,sentences=3))
        print('For More Visit:',wikipedia.page(wiki).url)

    if message.strip() == 'Weather':
        wloc = input('Location/City:')
        weather.get_yahoo_weather_by_city(wloc, Unit.celsius)
        print('Riyona: Its',weather.condition.text,',',weather.condition.temperature,' Degree')
    
    if message.strip() != 'Bye':
        replay = bot.get_response(message)
        print('Riyona:',replay)
    if message.strip()=='Bye':
        print('Riyona: Bye')
        break
