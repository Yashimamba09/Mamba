import random
def get_choice():
    player_choice = input("Enter a choice( rock,paper,scissors:")
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_wiin(player,computer): 
    return [player, computer]