---
tag: W786JVQDCP
kind: example
name: Centipede game
msc: [91A18]
instance_of: [4Y8AF9H9HA]
uses: [JEMK4V2PCW, HE8K9M4EXN]
sources:
  - url: https://en.wikipedia.org/wiki/Centipede_game
same_as:
  wikidata: Q1463264
  wikipedia: Centipede game
---

## Example

The *centipede game* is an [[extensive-form game|4Y8AF9H9HA]] of perfect information in which two players alternate.
At each node the mover either takes, which ends the game, or passes, which makes the pot larger.
Here is a version with four nodes; player 1 moves at nodes 1 and 3, player 2 at nodes 2 and 4.

- Take at node 1: payoffs $(1, 0)$.
- Take at node 2: payoffs $(0, 2)$.
- Take at node 3: payoffs $(3, 1)$.
- Take at node 4: payoffs $(2, 4)$.
- Pass at node 4: payoffs $(5, 3)$.

Apply [[backward induction|JEMK4V2PCW]].
At node 4, player 2 takes, since $4 > 3$.
At node 3, player 1 then takes, since $3 > 2$.
At node 2, player 2 takes, since $2 > 1$.
At node 1, player 1 takes, since $1 > 0$.
So the unique [[subgame perfect equilibrium|HE8K9M4EXN]] has each player take at every node, and the game ends at once with payoffs $(1, 0)$.
Both players would be better off with $(5, 3)$ by always passing.

## Explanations

### L1 human

The longer the players cooperate, the more there is to share, but whoever stops first takes the larger piece at that moment.
Reasoning back from the end, each player wants to stop just before the other does, and this unravels to stopping at the very start.
The game was introduced by Robert Rosenthal in 1981, and in experiments people usually pass for a while.
