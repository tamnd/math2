---
tag: 7VS7JZ3Y5B
kind: definition
name: Normed algebra
msc: [46H05]
defines: 4DJ4V5VBSH
uses: [03J5RAKB30, 0V2WP9B1MF]
sources:
  - url: https://en.wikipedia.org/wiki/Normed_algebra
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$.
A *normed algebra* over $\mathbb{K}$ is an associative algebra $A$ over $\mathbb{K}$ with a [[norm|0V2WP9B1MF]] $\norm{\cdot}$ on the vector space $A$ such that
$$\norm{x y} \le \norm{x} \norm{y} \quad \text{for all } x, y \in A.$$
If $A$ has a unit $1$, many authors also ask $\norm{1} = 1$.

## Remarks

The inequality makes the product $A \times A \to A$ continuous.
A normed algebra that is complete as a [[normed vector space|03J5RAKB30]] is a Banach algebra.

Example: the algebra $C([0,1])$ of continuous real functions with $\norm{f}_\infty = \sup_t \abs{f(t)}$.
For each $t$, $\abs{f(t) g(t)} \le \norm{f}_\infty \norm{g}_\infty$, so $\norm{fg}_\infty \le \norm{f}_\infty \norm{g}_\infty$.
The polynomial functions form a subalgebra, which is a normed algebra that is not complete.

Non-example: $M_2(\R)$ with the norm $\norm{a} = \max_{i,j} \abs{a_{ij}}$.
For the matrix $a$ with all entries $1$, $a^2$ has all entries $2$, so $\norm{a^2} = 2 > 1 = \norm{a}^2$.
The operator norm on $M_2(\R)$, in contrast, does make it a normed algebra.
