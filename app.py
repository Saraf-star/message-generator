from flask import Flask, render_template
import random

app = Flask(__name__)

messages = [

   """  
	You say you bring people nothing but trouble. But all you have brought in my life is just solutions and relief. Idc what you’ve brought for other people but it’s definitely not trouble for me specifically. You’re an absolute gem and I won’t let you tell me otherwise.

   """,
   """
   Where other people just end it with surface level “I’m there for you” and “It’ll be fineeee”, you go an extra mile to respond sincerely no matter whether it’s a solution or just a response to a vent. I know I can always rely on you as someone who will balance me out and help me see things from a logical perspective when I get immature or lose my ability to be objective.

   """,
   """
   You’re never a burden and don’t let anyone treat you that way. If anyone thinks you’re a burden, it’s their personal problem. Not a reflection of the person you are. No one can make you inferior without your consent. So…do not give the consent to anyone because you are NOT what happened to you; rather, you are what you choose to become. And you’ve never been a burden to me specially silly because I’m more of a headache than you are. You can’t outcompete me. 

   """
]

@app.route('/')
def home():
    message = random.choice(messages)

    return render_template(
        "index.html",
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)
