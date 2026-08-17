from InternetSpeedTwitterBot import InternetSpeedTwitterBot
DOWN_SPEED = 150
UP_SPEED = 10
tweetbot = InternetSpeedTwitterBot()
Net_data = tweetbot.get_internet_speed()
message = f"hey internet provider,  why is my iinternet speed is {Net_data[0].text}Down/{Net_data[1].text}Up When i pay for {DOWN_SPEED}Down/{UP_SPEED}Up"
print(Net_data[0].text)
print(Net_data[1].text)
tweetbot.tweet_at_provider(message)
# if float(Net_data[0].text)<DOWN_SPEED or float(Net_data[1].text)<UP_SPEED:
#     tweetbot.tweet_at_provider(Message=message)