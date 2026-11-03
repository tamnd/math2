---
tag: S6N7A60HPX
kind: definition
name: Shapley–Shubik power index
msc: [91B12, 91A12]
defines: WZTAFH7W2C
uses: [39HGM44CFZ, QVK36CXP03, YET20Q6WW6, 05RWFKVTJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Shapley%E2%80%93Shubik_power_index
---

## Definition

Let $N$ be a finite set of $n$ voters, and let $v$ be a simple game on $N$.
That is, $v$ is a [[cooperative game|39HGM44CFZ]] with $v(S) \in \set{0, 1}$ for every $S \subseteq N$, $v(\emptyset) = 0$ and $v(N) = 1$.
It is also monotone: $v(S) \le v(T)$ whenever $S \subseteq T$.
For an ordering $\pi$ of $N$, that is a [[permutation|05RWFKVTJ7]], let $P_\pi(i)$ be the set of voters before $i$ in $\pi$.
Voter $i$ is *pivotal* for $\pi$ if $v(P_\pi(i)) = 0$ and $v(P_\pi(i) \cup \set{i}) = 1$.
The *Shapley–Shubik power index* of $i$ is
$$\phi_i = \frac{\text{number of orderings } \pi \text{ for which } i \text{ is pivotal}}{n!}.$$

## Remarks

Each ordering has exactly one pivotal voter, so $\sum_i \phi_i = 1$.
The index $\phi$ is the [[Shapley value|QVK36CXP03]] of the simple game $v$.
Example: in the weighted voting game $[3; 2, 1, 1]$, voter $1$ is pivotal in the orderings $(2, 1, 3)$, $(3, 1, 2)$, $(2, 3, 1)$ and $(3, 2, 1)$, voter $2$ in $(1, 2, 3)$, and voter $3$ in $(1, 3, 2)$.
So $\phi = (2/3, 1/6, 1/6)$, which differs from the [[Banzhaf power index|YET20Q6WW6]] $(3/5, 1/5, 1/5)$ of the same game.
Non-example: in the ordering $(1, 2, 3)$ voter $3$ is not pivotal, since the voters before her, $\set{1, 2}$, already win.

## Explanations

### L1 human

The index is the probability that a voter casts the deciding vote when the voters line up in a random order.
It weighs coalitions differently from the Banzhaf index, so the two indices can disagree.
