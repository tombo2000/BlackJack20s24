import random
import tkinter as tk
from tkinter import messagebox

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(hand):
  if sum(hand) == 21 and len(hand) == 2:
    return 0
  if 11 in hand and sum(hand) > 21:
    hand.remove(11)
    hand.append(1)
  return sum(hand)

def play_game():
  global player_hand
  global computer_hand
  player_hand = []
  computer_hand = []

  for _ in range(2):
    player_hand.append(deal_card())
    computer_hand.append(deal_card())

  player_score_label.config(text=f"Your score: {calculate_score(player_hand)}")
  computer_score_label.config(text=f"Computer score: {calculate_score(computer_hand)}")
  player_cards_label.config(text=f"Your cards: {player_hand}")
  computer_cards_label.config(text=f"Computer's first card: {computer_hand[0]}")

def hit():
  global player_hand
  player_hand.append(deal_card())
  player_score_label.config(text=f"Your score: {calculate_score(player_hand)}")
  player_cards_label.config(text=f"Your cards: {player_hand}")
  if calculate_score(player_hand) > 21:
    messagebox.showinfo("Blackjack", "You went over. You lose!")
    player_hand = []
    computer_hand = []

def stand():
  global player_hand
  global computer_hand
  while calculate_score(computer_hand) < 17:
    computer_hand.append(deal_card())
  player_score_label.config(text=f"Your final score: {calculate_score(player_hand)}")
  computer_score_label.config(text=f"Computer final score: {calculate_score(computer_hand)}")
  player_cards_label.config(text=f"Your cards: {player_hand}")
  computer_cards_label.config(text=f"Computer's cards: {computer_hand}")
  if calculate_score(player_hand) > 21:
    messagebox.showinfo("Blackjack", "You went over. You lose!")
  elif calculate_score(computer_hand) > 21:
    messagebox.showinfo("Blackjack", "Computer went over. You win!")
  elif calculate_score(player_hand) == calculate_score(computer_hand):
    messagebox.showinfo("Blackjack", "It's a draw!")
  elif calculate_score(player_hand) == 0:
    messagebox.showinfo("Blackjack", "Blackjack! You win!")
  elif calculate_score(computer_hand) == 0:
    messagebox.showinfo("Blackjack", "Computer got a Blackjack. You lose!")
  elif calculate_score(player_hand) > calculate_score(computer_hand):
    messagebox.showinfo("Blackjack", "You win!")
  else:
    messagebox.showinfo("Blackjack", "You lose!")
  player_hand = []
  computer_hand = []

root = (tk.Tk)()
root.title("Blackjack")

player_score_label = tk.Label(root, text="Your score: 0")
player_score_label.pack()

computer_score_label = tk.Label(root, text="Computer score: 0")
computer_score_label.pack()

player_cards_label = tk.Label(root, text="Your cards: []")
player_cards_label.pack()

computer_cards_label = tk.Label(root, text="Computer's cards: []")
computer_cards_label.pack()

deal_button = tk.Button(root, text="Deal", command=play_game)
deal_button.pack()

hit_button = tk.Button(root, text="Hit", command=hit)
hit_button.pack()

stand_button = tk.Button(root, text="Stand", command=stand)
stand_button.pack()

root.mainloop()