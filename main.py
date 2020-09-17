from random import choice


def get_weather_bot_response(user_input):
    bot_response_sunny = ['Wear some sunglasses. ',
                          'Going to the pool would be nice today. ']
    bot_response_rainy = ['Better get an umbrella. ',
                          'You should stay inside. ', 'Dont get cold you might get sick. ']
    bot_response_smokey = ['California is on FIRE!! ', 'The air qulaity is horrible wear a mask. ',
                           'We need to fund ideas to stop climate change and stop big oil companies. ']
    bot_response_foggy = ['Kinda of chilly, better wear a light jacket. ',
                          'Be careful when driving. ', 'It might rain. ']
    bot_response_snowy = ['It would be nice to snowboard or ski. ',
                          'Snowball fights are always fun. ', 'Hot coco on snowy days is nice. ']

    if user_input == 'sunny':
        return choice(bot_response_sunny)
    elif user_input == 'rainy':
        return choice(bot_response_rainy)
    elif user_input == 'smokey':
        return choice(bot_response_smokey)
    elif user_input == 'foggy':
        return choice(bot_response_foggy)
    elif user_input == 'snowy':
        return choice(bot_response_snowy)
    else:
        return('I dont have this weather in my database')
