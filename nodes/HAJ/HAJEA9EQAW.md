---
tag: HAJEA9EQAW
kind: definition
name: Shapley value
msc: [91A12]
defines: QVK36CXP03
uses: [39HGM44CFZ, 05RWFKVTJ7, CBP13S0ETD]
sources:
  - url: https://en.wikipedia.org/wiki/Shapley_value
    locator: Formal definition
---

## Definition

Let $(N, v)$ be a [[cooperative game with transferable utility|39HGM44CFZ]] with $n = \abs{N}$ players.
The *Shapley value* of $(N, v)$ is the vector $\varphi(v) \in \R^N$ with components
$$\varphi_i(v) = \sum_{S \subseteq N \setminus \set{i}} \frac{\abs{S}! \, (n - \abs{S} - 1)!}{n!} \bigl( v(S \cup \set{i}) - v(S) \bigr), \qquad i \in N.$$
Equivalently, $\varphi_i(v)$ is the average of $v(P \cup \set{i}) - v(P)$ over all $n!$ orderings of $N$, that is over all [[permutations|05RWFKVTJ7]].
Here $P$ is the set of players that come before $i$ in the ordering.

## Remarks

Example: take the glove game with $N = \set{1, 2, 3}$, where $v(S) = 1$ if $S$ contains $1$ and at least one of $2, 3$, and $v(S) = 0$ otherwise.
Player $1$ adds $1$ exactly when she is not first, which happens in $4$ of the $6$ orderings.
So $\varphi_1 = 2/3$.
Player $2$ adds $1$ only in the ordering $1, 2, 3$, so $\varphi_2 = 1/6$, and likewise $\varphi_3 = 1/6$; the sum is $1 = v(N)$.
The Shapley value is the unique map $v \mapsto \varphi(v)$ on games with player set $N$ with four properties.
Efficiency: $\sum_i \varphi_i(v) = v(N)$.
Symmetry: two players with the same marginal contributions to every coalition get the same amount.
Null player: a player who adds nothing to any coalition gets $0$.
Additivity: $\varphi(v + w) = \varphi(v) + \varphi(w)$.
Non-example: the equal split $x_i = v(N)/n$ is efficient, symmetric and additive, but it fails the null player property.
So it is not the Shapley value; in the glove game it gives $1/3$ to each player.
The Shapley value need not lie in the [[core|CBP13S0ETD]]: in the glove game the core is $\set{(1, 0, 0)}$.

## Explanations

### L1 human

The formula averages what a player adds to the group, over all orders in which the group could have been formed.
The weights count how many orders put exactly the coalition $S$ in front of player $i$.
