---
tag: N6TH42TD7F
kind: statement
role: lemma
name: Sunflower lemma
msc: [05D05]
uses: [0C21Q694AG, 0HBRW4E6G1]
about: [0C21Q694AG]
sources:
  - url: https://en.wikipedia.org/wiki/Sunflower_(mathematics)
---

## Statement

A *sunflower* with $p$ petals is a [[family|0C21Q694AG]] of $p$ distinct sets $S_1, \ldots, S_p$ whose pairwise [[intersections|0HBRW4E6G1]] are all equal.
That is, there is a set $Y$, the core, with $S_i \cap S_j = Y$ for all $i \ne j$.
Let $k \ge 1$ and $p \ge 1$ be integers.
Let $\mathcal{F}$ be a family of sets, each with exactly $k$ elements, such that $|\mathcal{F}| > k! \, (p - 1)^k$.
Then $\mathcal{F}$ contains a sunflower with $p$ petals.

## Remarks

The proof is by induction on $k$.
Take a maximal subfamily of pairwise disjoint sets.
If it has at least $p$ members, they form a sunflower with empty core.
Otherwise their union $U$ has at most $(p - 1) k$ elements and meets every set of $\mathcal{F}$, so some $x \in U$ lies in more than $(k-1)! \, (p-1)^{k-1}$ sets.
Remove $x$ from these sets and apply the induction hypothesis to get a sunflower, then add $x$ back to its core.

Example: for $k = 1$ and $p = 3$, a family of $3$ distinct one-element sets is a sunflower with empty core, and $3 > 1! \cdot 2^1$.
The result is due to Erdős and Rado, who conjectured that $k! \, (p-1)^k$ can be replaced by $C_p^k$ for a constant $C_p$ that depends only on $p$; this is open.
In 2019 Alweiss, Lovett, Wu and Zhang improved the bound to $(C p \log k \log \log k)^k$ for an absolute constant $C$, and later work lowered it to $(C p \log k)^k$.

## Explanations

### L1 human

A sunflower is a group of sets that all overlap in exactly the same core, like petals around the centre of a flower.
The lemma says that any large enough collection of sets of the same size must contain a sunflower with as many petals as you like.
So size alone forces this very regular pattern.

### L2 human

The sunflower lemma is a basic tool in extremal set theory and in theoretical computer science, for example in lower bounds for monotone circuits.
Its proof is a typical Ramsey-type argument: either many sets are disjoint, or many share an element, and then one recurses.
It belongs to the circle of results of [[Ramsey theory|G5TWXV565S]], where a large structure always contains an orderly part.
