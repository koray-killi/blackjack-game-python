# Blackjack Game for Python

Project Language: **English**  
Programming Language: **Python 3**  
Aim: **A comprehensive project to review programming concepts and Python fundamentals.**

---

## Overview
This project is a fully functional Blackjack (21) game designed for educational purposes. It helps reinforce programming skills by incorporating Python's core features and concepts. The project saves the player’s balance persistently and uses interactive elements like colored text for better engagement.

---

## Features

### 1. Core Gameplay Mechanics
- Implements the rules of Blackjack, including dealing cards, scoring, and decision-making (hit/stand).
- Ensures that the player competes against a dealer (computer).
- Built with user-friendly input prompts and detailed game flow.

### 2. Programming Concepts with Features

#### File I/O
- The program saves and retrieves the player’s balance using a file named `balan.ce`. This ensures persistent data storage between game sessions.

#### Modular Code Structure
- Organized into reusable functions for better readability and maintainability.
- Example functions include:
  - `c_print(text, color)`: Displays text in various colors for improved readability.
  - Game logic functions for decision-making and scoring.

#### Randomization
- Utilizes Python’s `random` module to shuffle and deal cards, ensuring unpredictability in gameplay.

#### Interactive Console Design
- Incorporates color-coded outputs for different game events (e.g., winning, losing, or errors) using ANSI escape codes.

---

## How to Play
1. Run the script using Python 3: `python 21.py`.
2. Follow the on-screen instructions to:
   - Place your bet.
   - Choose to "Hit" or "Stand" during your turn.
3. Aim to get a hand value closer to 21 than the dealer without exceeding it.

---

## Installation
1. Ensure you have Python 3 installed on your system.
2. Download the script `21.py` and place it in your desired directory.
3. Install any required dependencies (if applicable, none specified in this version).

---

## File Descriptions
- `21.py`: Main script containing the Blackjack game logic.
- `balan.ce`: A text file that stores the player’s current balance. This file is auto-generated during gameplay.

---

## Educational Objectives
- Reinforce Python basics such as loops, conditionals, and functions.
- Demonstrate practical applications of file handling and data persistence.
- Enhance understanding of randomization and interactive programming.

---
