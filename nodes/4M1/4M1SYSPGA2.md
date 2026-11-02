---
tag: 4M1SYSPGA2
kind: definition
name: Rational map
msc: ["14E05"]
defines: 4D073CCYGV
uses: [HV6YBS0YDH, CDS1VWB7A3, 02BH3MCBQB, 0G8VEZ3WTK, 0BSJSX7ME2, ZT9A6JK8QF]
sources:
  - url: https://en.wikipedia.org/wiki/Rational_mapping
---

## Definition

Let $X$ and $Y$ be [[algebraic varieties|HV6YBS0YDH]] over an algebraically closed field $k$.
Consider pairs $(U, \varphi_U)$ where $U \subseteq X$ is a nonempty [[open subset|02BH3MCBQB]] and $\varphi_U \colon U \to Y$ is a [[morphism|CDS1VWB7A3]].
Two pairs $(U, \varphi_U)$ and $(V, \varphi_V)$ are equivalent if $\varphi_U = \varphi_V$ on $U \cap V$.
A *rational map* $\varphi \colon X \dashrightarrow Y$ is an equivalence class of such pairs.
It is *dominant* if for some, hence every, pair $(U, \varphi_U)$ in the class, the image $\varphi_U(U)$ is [[dense|0BSJSX7ME2]] in $Y$.

## Remarks

This relation is an [[equivalence relation|0G8VEZ3WTK]].
The key fact is that two morphisms $U \to Y$ that agree on a nonempty open subset of $U$ are equal.
The reason is that the set where they agree is closed, while a nonempty open subset of the irreducible space $U$ is dense.
The union of the domains of all pairs in the class is the largest open set on which $\varphi$ is defined, its domain of definition.

Example: $\varphi \colon \mathbb{P}^2 \dashrightarrow \mathbb{P}^1$, $[x : y : z] \mapsto [x : y]$, is a rational map.
It is a morphism on $U = \mathbb{P}^2 \setminus \set{[0 : 0 : 1]}$, and it cannot be extended to a morphism on all of $\mathbb{P}^2$.
It is dominant, since it is surjective onto $\mathbb{P}^1$.

Non-example: on $X = k$, the assignment $x \mapsto 1/x$ for $x \ne 0$ and $0 \mapsto 0$ is a function $X \to k$ but not a morphism, so it is not a pair in the definition.
Its restriction to $k \setminus \set{0}$ is a morphism and defines a rational map $k \dashrightarrow k$, whose domain of definition is $k \setminus \set{0}$.

Rational maps can only be composed when the first one is dominant; otherwise the image may lie outside the domain of the second.
A rational map $X \dashrightarrow \mathbb{A}^1$ is the same as a rational function on $X$.
