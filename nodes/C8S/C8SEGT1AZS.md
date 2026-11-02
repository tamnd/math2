---
tag: C8SEGT1AZS
kind: example
name: Weak order of permutations
msc: [06A07, 05A05]
instance_of: [WH4SFAACAS, 1C7TKGTB2F]
uses: [05RWFKVTJ7, 0515A6D2Y1]
sources:
  - url: https://en.wikipedia.org/wiki/Inversion_(discrete_mathematics)
---

## Example

Let $n \ge 1$ and let $S_n$ be the [[symmetric group|0515A6D2Y1]] of [[permutations|05RWFKVTJ7]] of $\set{1, \ldots, n}$, written in one-line notation $w = w(1) w(2) \cdots w(n)$.
The inversion set $\mathrm{Inv}(w)$ is the set of pairs of values $(a, b)$ with $a < b$ such that $b$ stands left of $a$ in $w$.
The *weak order* on $S_n$ is defined by $u \le w$ when $\mathrm{Inv}(u) \subseteq \mathrm{Inv}(w)$.
It is a partial order, and it is a [[lattice|WH4SFAACAS]].
The covering relations are the moves that swap two adjacent entries $a < b$ standing as $\ldots a b \ldots$.
Such a move adds the single pair $(a, b)$ to the inversion set.
The least element is the identity $12 \cdots n$, and the greatest element is the reversal $n \cdots 21$.

Check for $n = 3$.
The inversion sets are $\mathrm{Inv}(123) = \emptyset$, $\mathrm{Inv}(213) = \set{(1,2)}$, $\mathrm{Inv}(132) = \set{(2,3)}$, $\mathrm{Inv}(231) = \set{(1,2), (1,3)}$, $\mathrm{Inv}(312) = \set{(1,3), (2,3)}$, and $\mathrm{Inv}(321)$ has all three pairs.
So the weak order is the two chains $123 < 213 < 231 < 321$ and $123 < 132 < 312 < 321$.
The elements $213$ and $312$ are incomparable, since $(1,2) \notin \mathrm{Inv}(312)$.

## Remarks

The weak order is graded by the number of inversions.
Its Hasse diagram for $S_3$ is a hexagon.
The Bruhat order has more relations: there $213 < 312$.

## Explanations

### L1 human

Start with the numbers in order, $1 2 \cdots n$, and swap neighbours that are in the right order, one swap at a time.
Each swap creates one new out-of-order pair.
A permutation is below another when the pairs it has out of order are among those of the other.
For three numbers you get a hexagon, from $123$ at the bottom to $321$ at the top.
