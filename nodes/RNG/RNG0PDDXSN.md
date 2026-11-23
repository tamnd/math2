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

A pile has $21$ counters.
Two players take turns, and each turn removes $1$, $2$ or $3$ counters.
The player who takes the last counter wins.
Can the first player force a win, and how?
Following the [[inventor's paradox|FVRKDXBJF6]], we solve the game for every number $n$ of counters, not only for $21$.

1. We name the positions.
   A pile of $n$ counters is a winning position if the player to move can force a win, and a losing position otherwise.
2. We do the smallest cases.
   $n = 0$ is losing, since the player to move has nothing to take and the opponent has just won.
   $n = 1, 2, 3$ are winning, since the player to move takes everything.
3. $n = 4$ is losing, because every move leaves $1$, $2$ or $3$, a winning position for the opponent.
4. $n = 5, 6, 7$ are winning, because the player to move can take $1$, $2$ or $3$ to leave $4$.
5. We conjecture that $n$ is losing exactly when $4$ divides $n$.
6. We prove this by strong [[induction|0ASJVEFA9J]] on $n$.
   If $4 \mid n$ and $n > 0$, every move leaves $n - 1$, $n - 2$ or $n - 3$, none divisible by $4$, so by the hypothesis every move leaves a winning position for the opponent.
   If $4 \nmid n$, let $r \in \{1, 2, 3\}$ be the remainder of $n$ on division by $4$, and taking $r$ counters leaves a losing position for the opponent.
7. We specialize to $n = 21$.
   Since $21 = 4 \cdot 5 + 1$, the first player wins by taking $1$ counter and then answering each move of $k$ counters by taking $4 - k$.

## Remarks

The general problem was easier because induction can solve it, and the question for $21$ alone gives no induction hypothesis to use.
The general answer also gives the strategy, which the question needs and does not ask for.
The same method solves the game with moves of $1$ to $m$ counters, where the losing positions are the multiples of $m + 1$.
The game is one of the simplest examples of [[combinatorial game theory|SHQ800E0J4]], and [[Nim|HYQPVQF509]] is solved by the same idea of winning and losing positions.

## Explanations

### L1 human

Start with $21$ counters, and take turns removing $1$, $2$ or $3$; whoever takes the last one wins.
With $4$ counters the player to move loses, because whatever they take, the other player takes the rest.
So your aim is to leave a multiple of $4$ for the other player.
From $21$, take $1$ and leave $20$.
Then whenever the other player takes $k$, you take $4 - k$, and the pile goes $20$, $16$, $12$, $8$, $4$, $0$.

### L2 human

We use the same method on the game with moves of $1$ or $2$ counters, starting from $10$.
The small cases give: $0$ losing, $1$ and $2$ winning, $3$ losing, $4$ and $5$ winning, $6$ losing.
The same induction as in step 6 shows that the losing positions are the multiples of $3$.
Since $10 = 3 \cdot 3 + 1$, the first player wins by taking $1$ and then answering each move of $k$ by taking $3 - k$.

This is the typical use: a question about one position is answered by classifying all positions, and the classification is proved by induction.
Watch out: the pattern from small cases must be proved, and it need not be "multiples of one number".
With moves of $1$, $3$ or $4$ counters, the losing positions are $0, 2, 7, 9, 14, 16, \ldots$, which repeat with period $7$.
