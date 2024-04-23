import re
import random
import datetime
import wikipedia
import wolframalpha

wolf = wolframalpha.Client("85UUPW-6XGJ3AUEVR")

class Bot:
    negative_r = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_c = ("quit", "pause", "exit", "goodbye", "bye", "later")
    small_talk = ("why are you here?",
                  "Are there many humans like you?",
                  "what do you consume for sustenance?",
                  "Is there Intelligent life on this planet?",
                  "does Earth have a leader ?")

    def __init__(self):
        self.babble = {
            'describe_planet_intent': r'.*\s*your planet.*',
            'answer_why_intent': r'why\sare.*'
        }

    def greet_and_handle(self,match=None):
        self.name = input("What is your name?\n")
        current_time = datetime.datetime.now()
        hour = current_time.hour
        if 5 <= hour < 12:
            greeting = "Good morning!"
        elif 12 <= hour < 18:
            greeting = "Good afternoon!"
        elif 18 <= hour < 22:
            greeting = "Good evening!"
        else:
            greeting = "Hello!"
        
        will_help = input(f"{greeting} {self.name}, I am Erebus. Will you help me learn about your planet?\n")
        if will_help.lower() in self.negative_r:
            print("Have a nice Earth day!")
            return False  # Return False to indicate the user declined to help
        return True # Return True to indicate the user agreed to help

    def exit(self, reply):
        for command in self.exit_c:
            if reply == command:
                print("Have a nice day!")
                return True

    def chat(self):
        reply = input(random.choice(self.small_talk)).lower()
        while not self.exit(reply):
            reply = input(self.match(reply))

    def match(self, reply):
        for intent, regex_pattern in self.babble.items():
            found_match = re.match(regex_pattern, reply)
            if found_match:
                if intent == 'describe_planet_intent':
                    return self.planet()
                elif intent == 'answer_why_intent':
                    return self.why()
        return self.no_match()

    def planet(self):
        responses = ("My planet is a utopia of diverse organisms\n",
                     "I heard the coffee is good\n")
        return random.choice(responses)

    def why(self):
        responses = ("I come in peace\n", "I am here to collect data on your planet and its inhabitants\n",
                     "I heard the coffee is good\n")
        return random.choice(responses)

    def no_match(self):
        responses = ("Please tell me more.\n", "Tell me more!\n", "I see. Can you elaborate?\n",
                      "Interesting. Can you tell me more?\n", "I see. How do you think?\n", "Why?\n",
                      "How do you think I feel when I say that? Why?\n")
        return random.choice(responses)


def handle_bye(match=None):
    return "Goodbye! Have a great day!"



def handle_time(match=None):
    current_time = datetime.datetime.now()
    return f"The current time is {current_time.strftime('%H:%M')}."


def handle_calculation(query):
    try:
        result = wolf.query(query)
        answer = next(result.results).text
        return answer
    except StopIteration:
        return "Sorry, I couldn't understand that calculation."
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"



def handle_wikipedia(topic):
    try:
        answer = wikipedia.summary(topic, sentences=2)
        return answer
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:5]  # Limiting options to the first 5
        return f"Multiple options found. Did you mean: {', '.join(options)}?"
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find information on that topic."

def chatbot(input_text):
    bot = Bot()
    if re.match(r"hi|hello|hey", input_text, re.IGNORECASE):
        if bot.greet_and_handle():  # If the user agreed to help, start the conversation
            bot.chat()
        return  # Exit the chatbot function if the user declined to help
    patterns = {
        r"hi|hello|hey": Bot().greet_and_handle,
        r"bye|goodbye": lambda match: handle_bye(),
        r"time|current time": handle_time,
        r"calculate (.*)": lambda match: handle_calculation(match.group(1)if match else None),
        r"tell me about (.*)": lambda match: handle_wikipedia(match.group(1)if match else None),
    }

    for pattern, response in patterns.items():
        match = re.match(pattern, input_text, re.IGNORECASE)
        if match:
            if callable(response):
                return response(match)
            else:
                return response

    return bot.match(input_text)


print("Welcome to the Erebus Chatbot!")
print("You can type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye! Thanks for chatting with me.")
        break
    response = chatbot(user_input)
    if response:
        print("Erebus:", response)
