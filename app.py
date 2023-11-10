#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random
from enum import Enum
from flask import Flask, request, render_template
app = Flask(__name__, template_folder="static")

class Action(Enum):
    ROCK = 'rock'
    PAPER = "paper"
    SCISSORS = "scissors"
    def win_against(self) -> 'Action':
        return {
            Action.ROCK: Action.SCISSORS,
            Action.PAPER: Action.ROCK,
            Action.SCISSORS: Action.PAPER
        }.get(self)

@app.route("/")
def hello():
    played_value = request.args.get('shifumi')
    context = {}
    if played_value:
        played_action = Action(played_value)
        generated_action = __select_action()
        context['played_action'] = played_value
        context['generated_action'] = generated_action.value
        context['has_won'] = __compare_action(played_action, generated_action)

    return render_template("index.html", **context)
    #return app.send_static_file("index.html")

def __select_action() -> Action:
    return random.choice(list(map(Action, Action)))

def __compare_action(player1_value: Action, player2_value: Action) -> bool:
    return player1_value.win_against() == player2_value