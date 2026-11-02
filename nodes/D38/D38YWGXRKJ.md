---
tag: D38YWGXRKJ
kind: definition
name: Space of bounded continuous functions
msc: ["46E15", 54C35, 46B25]
defines: MG3X8Y1VT4
uses: [0CQHFPGJ45, 0X3WGX95FE, 03J5RAKB30, 0BTMQ04556]
sources:
  - url: https://en.wikipedia.org/wiki/Space_of_continuous_functions_on_a_compact_space
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]] and let $\mathbb{K}$ be $\R$ or $\C$.
The *space of bounded continuous functions* $C_b(X)$ is the set of [[continuous functions|0X3WGX95FE]] $f \colon X \to \mathbb{K}$ such that $\sup_{x \in X} \abs{f(x)} < \infty$.
It is a vector space under pointwise addition and scalar multiplication.
It is a [[normed space|03J5RAKB30]] with the norm
$$\norm{f}_\infty = \sup_{x \in X} \abs{f(x)},$$
with $\norm{f}_\infty = 0$ when $X$ is empty.

## Remarks

Example: $f(x) = \sin x$ on $X = \R$ is continuous, and $\abs{\sin x} \le 1$ with equality at $x = \pi/2$, so $f \in C_b(\R)$ with $\norm{f}_\infty = 1$.

Non-example: $g(x) = x$ on $\R$ is continuous, but $\sup_x \abs{g(x)} = \infty$, so $g \notin C_b(\R)$.

The [[supremum|0BTMQ04556]] is finite by the definition, and the norm axioms follow from those of $\abs{\cdot}$.
The space $C_b(X)$ is complete, so it is a Banach space.
If $X$ is compact, $C_b(X)$ is the space $C(X)$ of all continuous functions on $X$.
If $X$ is a set with the discrete topology, $C_b(X)$ is the space $\ell^\infty(X)$ of bounded functions.
