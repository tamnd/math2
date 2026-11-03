---
tag: GBVM7ERC1E
kind: definition
name: Cooperative game theory
msc: [91A12]
defines: 39HGM44CFZ
uses: []
sources:
  - url: https://en.wikipedia.org/wiki/Cooperative_game_theory
    locator: Mathematical definition
---

## Definition

A *cooperative game with transferable utility* is a pair $(N, v)$ where:

1. $N$ is a finite nonempty set, whose elements are called players, and whose subsets are called coalitions;
2. $v$ is a function from the set of all subsets of $N$ to $\R$, called the characteristic function;
3. $v(\emptyset) = 0$.

The number $v(S)$ is the worth of the coalition $S$.
It is the total payoff that the members of $S$ can secure together and share in any way.
A *payoff vector* is a vector $x = (x_i)_{i \in N}$ in $\R^N$, and for a coalition $S$ one writes $x(S) = \sum_{i \in S} x_i$.

## Remarks

Example: the glove game with $N = \set{1, 2, 3}$, where player $1$ owns a left glove and players $2$ and $3$ each own a right glove.
Put $v(S) = 1$ if $S$ contains player $1$ and at least one of players $2$ and $3$, and $v(S) = 0$ otherwise.
Then $v(\emptyset) = 0$, so $(N, v)$ is a cooperative game.
Non-example: a function with $v(\emptyset) = 1$ fails clause 3, since the empty coalition has no members and can secure nothing.
A game is *superadditive* if $v(S \cup T) \ge v(S) + v(T)$ for disjoint $S$ and $T$, which many applications assume.
A *simple game* is a game in which $v$ takes only the values $0$ and $1$, $v(N) = 1$ and $v$ is monotone; it models voting.

## Explanations

### L1 human

The model lists, for every group of players, how much that group can earn on its own.
"Transferable utility" means the earnings are like money: the group can split them in any way it likes.
Everything else about the game, such as who does what, is left out.
