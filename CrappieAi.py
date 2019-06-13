import random

class Small_talk:
    def get_message(self,message):
        my_dict = [["hi", "hello", "hey", "hey there", "greeting"],["bye", "good bye", "nice having you bye","thank you bye","see you later","cya"],["thank you","appriciated","thank alot","that would help","thanks","thank"]]
        greet= ["Hi! Great Day What can I do for you?","Greeting my Friend! How can I help you?","Good Day! What I help you friend"]
        bye = "Bye-bye come again anytime"
        thank = ["Honor to help","My pleasure","No problem","You welcome"]
        message = message.lower()
        if message in my_dict[0]:
            return [random.choice(greet),1]
        elif message in my_dict[1]:
            return [bye,0]
        elif message in my_dict[2]:
            return [random.choice(thank),0]
        else:
            return [f"My knowledge is limit Sorry for the inconvience",1]

# a = Small_talk()
# print(a.get_message("Hello"))