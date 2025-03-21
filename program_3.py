# Title: Program 3 Week 8
# Author: Michael Beaudet
# Date: 3/21/25

import random

# Dictionary of U.S. states and capitals
states_and_capitals = {
    "Alabama": "Montgomery", "Alaska": "Juneau", "Arizona": "Phoenix", "Arkansas": "Little Rock", 
    "California": "Sacramento", "Colorado": "Denver", "Connecticut": "Hartford", "Delaware": "Dover", 
    "Florida": "Tallahassee", "Georgia": "Atlanta", "Hawaii": "Honolulu", "Idaho": "Boise", 
    "Illinois": "Springfield", "Indiana": "Indianapolis", "Iowa": "Des Moines", "Kansas": "Topeka", 
    "Kentucky": "Frankfort", "Louisiana": "Baton Rouge", "Maine": "Augusta", "Maryland": "Annapolis", 
    "Massachusetts": "Boston", "Michigan": "Lansing", "Minnesota": "St. Paul", "Mississippi": "Jackson", 
    "Missouri": "Jefferson City", "Montana": "Helena", "Nebraska": "Lincoln", "Nevada": "Carson City", 
    "New Hampshire": "Concord", "New Jersey": "Trenton", "New Mexico": "Santa Fe", "New York": "Albany", 
    "North Carolina": "Raleigh", "North Dakota": "Bismarck", "Ohio": "Columbus", "Oklahoma": "Oklahoma City", 
    "Oregon": "Salem", "Pennsylvania": "Harrisburg", "Rhode Island": "Providence", "South Carolina": "Columbia", 
    "South Dakota": "Pierre", "Tennessee": "Nashville", "Texas": "Austin", "Utah": "Salt Lake City", 
    "Vermont": "Montpelier", "Virginia": "Richmond", "Washington": "Olympia", "West Virginia": "Charleston", 
    "Wisconsin": "Madison", "Wyoming": "Cheyenne"
}

def quiz():
# Initialize the correct answers variable
    correct_answers = 0
# Ask the user 10 random questions
# Start the for loop and give it a range of 10
    for _ in range(10):
# Randomly get a state and its capital
        state, correct_capital = random.choice(list(states_and_capitals.items()))
# Ask the user to give the correct capital of the state given
        user_answer = input(f"What is the capital of {state}? ").strip()
# Check if the answer is correct
        if user_answer.lower() == correct_capital.lower():
            print("Correct!")
# Add 1 to correct_answers if it is correct
            correct_answers += 1
        else:
# If it is wrong give the correct answer
            print(f"Incorrect! The correct answer is {correct_capital}.")
    
# Display the results
    print(f"\nQuiz Complete! You got {correct_answers} correct.")

quiz()