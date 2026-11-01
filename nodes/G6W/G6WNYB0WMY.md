---
tag: G6WNYB0WMY
kind: statement
role: theorem
name: Kruskal–Katona theorem
msc: [05D05]
uses: [0C21Q694AG, 0GBZM0MT0F]
about: [0C21Q694AG]
sources:
  - url: https://en.wikipedia.org/wiki/Kruskal–Katona_theorem
same_as:
  wikidata: Q3527102
  wikipedia: Kruskal–Katona theorem
---

## Statement

Let $k \ge 1$ be an integer.
For a [[family|0C21Q694AG]] $\mathcal{F}$ of $k$-element sets, the *shadow* $\partial \mathcal{F}$ is the family of all $(k-1)$-element sets that are contained in some member of $\mathcal{F}$.
Every positive integer $m$ can be written in exactly one way as
$$m = \binom{a_k}{k} + \binom{a_{k-1}}{k-1} + \cdots + \binom{a_t}{t}$$
with integers $a_k > a_{k-1} > \cdots > a_t \ge t \ge 1$.
If $\mathcal{F}$ is a family of $m$ sets of size $k$, then
$$|\partial \mathcal{F}| \ge \binom{a_k}{k-1} + \binom{a_{k-1}}{k-2} + \cdots + \binom{a_t}{t-1}.$$

## Remarks

The bound is attained by the first $m$ sets of size $k$ of positive integers in the colexicographic order.
In this order, $A$ comes before $B$ when the largest element of $A \mathbin{\triangle} B$ lies in $B$.
The proof shows, with compression operators, that one may assume $\mathcal{F}$ is an initial segment of this order, and then counts.

Example: let $k = 2$ and $m = 3$, so $m = \binom{3}{2}$ and the bound is $\binom{3}{1} = 3$.
A graph with $3$ edges, seen as a family of $2$-sets, covers at least $3$ vertices, and the triangle covers exactly $3$.

A simpler form due to Lovász: if $|\mathcal{F}| = \binom{x}{k}$ for a real number $x \ge k$, then $|\partial \mathcal{F}| \ge \binom{x}{k-1}$, where $\binom{x}{j} = x(x-1)\cdots(x-j+1)/j!$.

## Explanations

### L1 human

Given many sets of the same size, look at all the smaller sets you get by removing one element.
The theorem says exactly how few such smaller sets there can be.
The answer is always attained by packing the sets as tightly as possible, using as few elements as possible.

### L2 human

The theorem characterises the possible $f$-vectors of simplicial complexes, since the faces of a complex form a family closed under taking shadows.
It implies the [[Erdős–Ko–Rado theorem|FJ92Q6VTJH]].
Its numerical form, through the $k$-binomial representation of $m$, reappears in Macaulay's theorem on Hilbert functions and in the [[g-theorem|4CZMWQVC30]] for polytopes.
