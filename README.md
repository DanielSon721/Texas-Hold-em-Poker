# Texas Hold'em Poker (Python)

This is a simple terminal-based Texas Hold'em Poker game written in Python. Play against AI opponents with basic betting logic and hand evaluation.

## 🎮 Features

- Simulates Texas Hold'em Poker (Flop, Turn, River)
- Play against up to 10 AI opponents
- AI uses basic probability to decide whether to bet or fold
- Hand ranking from High Card to Royal Flush
- Money system with betting and folding logic
- Clear card display using Unicode symbols

## 🃏 How to Play

1. Choose the number of AI opponents (1 to 7 recommended)

2. During each round:
   - Cards are dealt to all players.
   - You’ll be asked if you'd like to bet 25 cents during each stage: Flop, Turn, and River.
   - AI opponents will automatically decide to bet or fold.
   - At the end, hand rankings are displayed and the winner is determined.

3. The game continues until you run out of money.

## 📦 Project Structure

- `game.py` – Main game loop and logic
- `card.py` – Card class with display formatting
- `ai.py` – AI player class with hand evaluation logic

## 💡 Hand Rankings

1. High Card  
2. Pair  
3. Two Pair  
4. Three of a Kind  
5. Straight  
6. Flush  
7. Full House  
8. Four of a Kind  
9. Straight Flush  
10. Royal Flush

## 🔧 Requirements

- Python 3.x
- No external libraries needed

## 📸 Example Output

```plaintext
Opponent 1: 🂠 🂠     Money: 975
You:        Q♦ J♠   Money: 975

Flop: 4♥ 10♣ K♠
Would you like to bet 25 cents? (Y/N):
```

---

*DISCLAIMER: THIS PROJECT IS STILL A WORK IN PROGRESS*
