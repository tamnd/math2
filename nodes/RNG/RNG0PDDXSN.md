---
tag: RNG0PDDXSN
kind: example
name: A take-away game solved for every number of counters
msc: ["00A35", "91A46"]
topics: [X1NSTVGDNQ]
audience: school
instance_of: [FVRKDXBJF6]
uses: [FVRKDXBJF6, SHQ800E0J4, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Subtraction_game
    locator: lead section
---

## Example

Problem: a pile has $21$ counters.
Two players take turns, and each turn removes $1$, $2$ or $3$ counters.
The player who takes the last counter wins.
Decide whether the first player can force a win, and how.
We use the [[inventor's paradox|FVRKDXBJF6]]: we solve the game for every number $n$ of counters, not only for $21$.

1. Call a number $n$ of counters a winning position if the player to move can force a win, and a losing position otherwise.
2. Small cases. $n = 0$ is losing, since the player to move has no counter to take and the opponent has just won. $n = 1, 2, 3$ are winning: take all.
3. $n = 4$ is losing: every move leaves $1$, $2$ or $3$, a winning position for the opponent.
4. $n = 5, 6, 7$ are winning: take $1$, $2$ or $3$ to leave $4$.
5. Conjecture: $n$ is losing exactly when $4$ divides $n$.
6. Proof by strong [[induction|0ASJVEFA9J]] on $n$. If $4 \mid n$ and $n > 0$, every move leaves $n - 1$, $n - 2$ or $n - 3$, none divisible by $4$, so by the hypothesis every move leaves a winning position for the opponent. If $4 \nmid n$, let $r \in \{1, 2, 3\}$ be the remainder of $n$ on division by $4$; taking $r$ counters leaves a multiple of $4$, a losing position for the opponent.
7. Specialize to $n = 21$. Since $21 = 4 \cdot 5 + 1$, the first player wins by taking $1$ counter, and after that answers each move of $k$ counters by taking $4 - k$.

## Remarks

The general problem was easier because it can be solved by induction, and the question for $21$ alone gives no induction hypothesis.
The general answer also gives the strategy, which the question for $21$ did not ask for but needs.
The same method solves the game with moves of $1$ to $m$ counters: the losing positions are the multiples of $m + 1$.
This game is one of the simplest examples of [[combinatorial game theory|SHQ800E0J4]], and [[Nim|HYQPVQF509]] is solved by the same idea of winning and losing positions.

## Explanations

### L1 human

Take $21$ counters, and take turns removing $1$, $2$ or $3$; whoever takes the last one wins.
With $4$ counters, the player to move loses: whatever they take, the other takes the rest.
So the aim is to leave a multiple of $4$ for the other player.
From $21$, take $1$ and leave $20$; then, whenever the other takes $k$, take $4 - k$, and the pile goes $20$, $16$, $12$, $8$, $4$, $0$.

### L2 human

We use the same general method on the game with moves of $1$ or $2$ counters, starting from $10$ counters.

1. Small cases: $0$ is losing, $1$ and $2$ are winning, $3$ is losing, $4$ and $5$ are winning, $6$ is losing.
2. Conjecture and proof, as in steps 5 and 6: the losing positions are the multiples of $3$.
3. Specialize: $10 = 3 \cdot 3 + 1$, so the first player wins by taking $1$ and then answering $k$ with $3 - k$.

The typical use: a question about one position is answered by classifying all positions, and the classification is proved by induction.

A trap: the pattern of step 1 must be proved; in games with other move sets, such as moves of $1$, $3$ or $4$ counters, the losing positions are $0, 2, 7, 9, 14, 16, \ldots$, not the multiples of a single number.
