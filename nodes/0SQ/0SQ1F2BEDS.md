---
tag: 0SQ1F2BEDS
kind: definition
name: Branch of the logarithm
aliases: [branch-of-log, logarithm-branch]
msc: [33B10]
defines: 02YSJPQYQH
uses: [0X2FY491PF, 054VXHMCA3]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_logarithm
    locator: Branches of the complex logarithm
---

## Definition

Let $U$ be an open subset of $\mathbb{C} \setminus \{0\}$.
A branch of the logarithm on $U$ is a continuous function $L : U \to \mathbb{C}$ such that $e^{L(z)} = z$ for each $z \in U$.
Thus $L(z)$ is a [[complex logarithm|0X2FY491PF]] of $z$ for each $z \in U$.

## Remarks

Each branch $L$ of the logarithm on $U$ is holomorphic on $U$, with $L'(z) = 1/z$.
If $U$ is a [[domain|097KNJFJ7V]] and $L_1, L_2$ are two branches on $U$, then $L_1 - L_2$ is the constant $2 \pi i k$ for one $k \in \mathbb{Z}$.
There is no branch of the logarithm on $\mathbb{C} \setminus \{0\}$, or on any open set that contains a circle with center $0$.
The [[principal branch|0YKY4M3KRQ]] $\operatorname{Log}$ is a branch on $\mathbb{C} \setminus (-\infty, 0]$. The functions $\operatorname{Log} z + 2 \pi i k$ with $k \in \mathbb{Z}$ are the other branches on this set.

## Explanations

### L1 human

The logarithm has many values at each point, so to get a function we must choose one value at each point, and the choice must change continuously.
Such a choice is a branch.
If you go once around $0$, the argument grows by $2\pi$, so no continuous choice is possible on a full circle around $0$.
