---
tag: FCA0J1X07K
kind: statement
role: lemma
name: Vitali covering lemma
msc: [28A75, 28A15]
uses: [0VKD1TP7F3, 05DSV40EB9, 0Z2P41SVDP]
about: [05DSV40EB9]
sources:
  - url: https://en.wikipedia.org/wiki/Vitali_covering_lemma
same_as:
  wikidata: Q3229352
  wikipedia: Vitali covering lemma
---

## Statement

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]].
For a [[closed ball|05DSV40EB9]] $B = \bar B(x, r)$ with $r > 0$ and $c > 0$, let $cB = \bar B(x, cr)$.

1. Finite version: for closed balls $B_1, \dots, B_k$ of positive radius in $X$, there is a subfamily $B_{j_1}, \dots, B_{j_m}$ of pairwise disjoint balls with $B_1 \cup \dots \cup B_k \subseteq 3B_{j_1} \cup \dots \cup 3B_{j_m}$.
2. Infinite version: let $\mathcal{F}$ be a family of closed balls of positive radius in $X$ with bounded radii. There is a subfamily $\mathcal{G} \subseteq \mathcal{F}$ of pairwise disjoint balls with this property: each $B \in \mathcal{F}$ meets some $B' \in \mathcal{G}$ of radius at least half that of $B$. In particular $\bigcup_{B \in \mathcal{F}} B \subseteq \bigcup_{B' \in \mathcal{G}} 5B'$.

If $X$ is [[separable|0Z2P41SVDP]], for example $X = \R^n$, the subfamily $\mathcal{G}$ in part 2 is countable.

## Remarks

The finite version is greedy: pick the largest ball, discard every ball that meets it, and repeat.
A discarded ball meets a chosen ball of at least its radius, so it lies in the triple of that ball.
The infinite version sorts the balls by radius into dyadic classes $R/2^{k+1} < r \le R/2^k$ and chooses a maximal disjoint subfamily in each class in turn, using Zorn's lemma.
If $B$ meets $B'$ and the radius of $B$ is at most twice that of $B'$, then $B \subseteq 5B'$.

Example: in $\R^n$ the lemma gives $\lambda\big(\bigcup_i B_i\big) \le 3^n \sum_m \lambda(B_{j_m})$, which is the key step in the weak type estimate for the Hardy–Littlewood maximal function.

The bound on the radii is needed in part 2.
The balls $\bar B(0, k)$ for $k = 1, 2, \dots$ in $\R$ pairwise meet, so a disjoint subfamily has one ball, and no fixed enlargement of it covers $\R$.

## Explanations

### L1 human

Given a bunch of overlapping balls, one can keep a few of them that do not overlap at all.
After blowing the kept balls up by a fixed factor, they cover everything the original balls covered.
So the total size of a union of balls is controlled by the size of a disjoint subfamily.

### L2 human

The lemma turns overlapping covers into disjoint ones at the price of a constant factor.
It gives the weak $(1,1)$ bound for the maximal function and so the Lebesgue differentiation theorem.
The Vitali covering theorem built on it says that a fine cover of a set by balls contains a disjoint subfamily that covers almost all of the set.
