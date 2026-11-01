---
tag: 0PBWWQD9KY
kind: problem
name: Monty Hall problem
msc: [60C05]
uses: [0FJB06AD2P, 0NM6E9VW04]
sources:
  - url: https://en.wikipedia.org/wiki/Monty_Hall_problem
    locator: Standard assumptions
same_as:
  wikidata: Q198835
  wikipedia: Monty Hall problem
history:
  posed_by: "Steve Selvin"
  first_stated: "1975"
---

## Problem

A game show has three closed doors. A car is behind one door, chosen uniformly at random, and a goat is behind each of the two other doors.
The player chooses one door. Then the host, who knows where the car is, opens one of the two other doors and shows a goat.
If both other doors hide goats, the host chooses one of them with probability $1/2$ each. The host always opens a door and always offers a switch.
The player can keep the first door or switch to the other closed door. Which choice gives the larger probability of the car?

## Remarks

Under these assumptions, switching wins with probability $2/3$ and staying wins with probability $1/3$. The player's first door hides the car with probability $1/3$, and the host's action does not change this.
The conditional probability that switching wins, given the door that the host opens, is also $2/3$. [[Bayes' theorem|0NM6E9VW04]] gives this.
The answer depends on the rules of the host. If the host opens a random other door and it shows a goat by chance, both choices win with probability $1/2$.

## History

Steve Selvin posed the problem in a letter to The American Statistician in 1975. It became famous through the column of Marilyn vos Savant in Parade magazine.

## Explanations

### L1 human

Staying wins only when your first choice was right, which happens one time in three.
Switching wins every time your first choice was wrong, which happens two times in three.
