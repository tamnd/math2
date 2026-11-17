---
tag: THE3TBABMK
kind: example
name: A knockout tournament without byes needs a power of 2 players
msc: ["00A35", "05A99"]
topics: [EEH2F76CYQ]
audience: ug1
not_instance_of:
  - target: QC9FKGZH1V
    note: the forward step P(n) ⇒ P(2n) holds, but the backward step P(n) ⇒ P(n − 1) fails at n = 4
uses: [QC9FKGZH1V, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Bye_(sports)
    locator: Elimination tournaments
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Forward-backward induction
---

## Example

A knockout tournament for $n$ players runs in rounds.
In each round, the remaining players form pairs, each pair plays one game, and the loser of each game leaves.
The tournament ends when one player remains.
The tournament is without byes if every remaining player plays in every round, so that no player goes to the next round without a game.
Let $P(n)$ be the statement "a knockout tournament without byes for $n$ players exists".
We show that $P(n)$ has the forward part of a [[forward-backward induction|QC9FKGZH1V]] but not the backward part, and that $P(n)$ is false for many $n$.

1. $P(1)$ holds: the single player wins after zero rounds.
2. Forward step: assume $P(n)$, and take $2n$ players. In the first round they form $n$ pairs, and the $n$ winners remain. By $P(n)$, the $n$ winners can finish without byes. So $P(2n)$ holds.
3. By [[induction|0ASJVEFA9J]] on $k$, steps 1 and 2 give $P(2^k)$ for every $k \ge 0$. In particular $P(4)$ holds.
4. $P(3)$ fails: in the first round, $3$ players cannot all be in pairs, because $3$ is odd. So the backward step $P(4) \Rightarrow P(3)$ is false.
5. In general, a round without byes needs an even number of players, at least $2$, and it halves this number.
6. Let $n = 2^a b$ with $b$ odd. After $a$ rounds, $b$ players remain, because each of these rounds halves an even number.
7. If $b \ge 3$, the $b$ players cannot form pairs, and $b > 1$, so the tournament cannot end. If $b = 1$, one player remains and the tournament ends.
8. So $P(n)$ holds exactly when $n$ is a power of $2$.

The first values are as follows.

| $n$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ |
|---|---|---|---|---|---|---|---|---|
| $P(n)$ | true | true | false | true | false | false | false | true |

## Remarks

1. The forward part alone proves $P(n)$ only for $n$ in the set $\{1, 2, 4, 8, \ldots\}$. Without a backward step, nothing follows for the other $n$.
2. The backward step fails at every $n = 2^k$ with $k \ge 2$: $P(2^k)$ holds and $P(2^k - 1)$ fails, because $2^k - 1$ is odd and at least $3$.
3. In the proof of the AM-GM inequality, the backward step adds the mean as an extra number, and the mean does not change. Here no extra player can be added and later removed with no effect on the pairings.
4. Real tournaments with $n$ players allow byes. Then a tournament exists for every $n \ge 1$, and it has exactly $n - 1$ games, because each game removes one player.

## Explanations

### L1 human

In a knockout tournament, players meet in pairs, and the loser of each game goes home.
If nobody may sit out a round, the number of players must be even in every round until one player is left.
With $8$ players, this works: $8$, then $4$, then $2$, then $1$.
With $6$ players, it fails: after one round $3$ players remain, and $3$ players cannot form pairs.
So doubling works, but going down by one player does not.

### L2 human

We test the rule of step 6 for $n = 12 = 2^2 \cdot 3$.

1. Round 1: $12$ players form $6$ pairs, and $6$ players remain.
2. Round 2: $6$ players form $3$ pairs, and $3$ players remain.
3. Round 3: $3$ players cannot form pairs, so the tournament stops with $3$ players.

The typical use of this example is a check on a forward-backward proof: the backward step needs its own argument, and it can fail even when the forward step holds.
A trap is to read "$P(2^k)$ for all $k$" as "$P(n)$ for all large $n$".
