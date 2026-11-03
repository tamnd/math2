---
tag: N88XYTB03D
kind: definition
name: Combinatorial game theory
msc: [91A46]
defines: SHQ800E0J4
uses: [0BBTH3YSZA, 0DQPNJNPYK]
sources:
  - url: https://en.wikipedia.org/wiki/Combinatorial_game_theory
---

## Definition

Combinatorial game theory studies *short combinatorial games*, which are defined recursively as follows.

1. If $\mathcal{L}$ and $\mathcal{R}$ are [[finite sets|0BBTH3YSZA]] of short games, then $G = \set{\mathcal{L} \mid \mathcal{R}}$ is a short game.
2. Every short game arises by finitely many applications of clause 1, starting from $0 = \set{\ \mid \ }$, the game with $\mathcal{L} = \mathcal{R} = \emptyset$.

The elements of $\mathcal{L}$ are the *left options* of $G$ and the elements of $\mathcal{R}$ are its *right options*.
The game $G$ is played by two players, Left and Right, starting at $G$.
On her turn, Left moves to a left option and Right moves to a right option.
The other player then moves next from the new game.
Under *normal play*, a player who has no option when it is her turn loses.
A game is *impartial* if, at it and at every position reachable from it, the left options equal the right options.

## Remarks

The *sum* $G + H$ is the game in which a player moves in exactly one of $G$ and $H$.
Recursively, its left options are $G^L + H$ and $G + H^L$, and similarly for right options.
Every short game belongs to exactly one of four outcome classes: Left wins, Right wins, the first player wins, or the second player wins.
Since the recursion in clause 2 is finite, every play ends after finitely many moves, so this classification follows by induction; the induction is along a [[well-founded relation|0DQPNJNPYK]].

Example: $1 = \set{0 \mid \ }$ is a short game.
Only Left can move, to $0$, where Right cannot move, so Left wins whoever starts.
The game $* = \set{0 \mid 0}$ is impartial, and the first player wins by moving to $0$.

Non-example: a game with a chance move, such as backgammon, is not a combinatorial game, since the definition leaves no room for dice.
A game that can end in a draw, such as chess, also falls outside the normal play convention described here.
