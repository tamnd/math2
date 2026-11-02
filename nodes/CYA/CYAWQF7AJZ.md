---
tag: CYAWQF7AJZ
kind: definition
name: Stein space
msc: ["32E10", 32C15]
defines: Z4AMJS5KA6
uses: [HXSZA44J5J, CD6SMMZSW8, 0R6EWFKRCF, 03PPNCM9GG, 0S1FJ8VEX9]
sources:
  - url: https://en.wikipedia.org/wiki/Stein_manifold
---

## Definition

Let $(X, \mathcal{O}_X)$ be a [[complex analytic space|HXSZA44J5J]] whose underlying topological space is [[Hausdorff|0S1FJ8VEX9]] and [[second countable|03PPNCM9GG]].
Let $\mathcal{O}(X)$ be the algebra of global holomorphic functions on $X$, and let $f(x) \in \C$ denote the value of $f \in \mathcal{O}(X)$ at $x \in X$.
For a [[compact set|0R6EWFKRCF]] $K \subseteq X$, its [[holomorphically convex hull|CD6SMMZSW8]] is $\widehat{K} = \set{x \in X : \abs{f(x)} \le \sup_K \abs{f} \text{ for all } f \in \mathcal{O}(X)}$.
The space $X$ is a *Stein space* if:

1. $X$ is holomorphically convex: $\widehat{K}$ is compact for every compact $K \subseteq X$.
2. $X$ is holomorphically separable: for all $x \ne y$ in $X$ there is $f \in \mathcal{O}(X)$ with $f(x) \ne f(y)$.

## Remarks

A Stein space whose underlying space is a complex manifold is a Stein manifold.
Example: every closed complex subspace $X$ of $\C^N$ is Stein.
The coordinate functions restricted to $X$ separate points, and $\widehat{K}$ is a closed subset of $X$ contained in a closed ball of $\C^N$, hence compact.
Non-example: the complex projective line $\mathbb{P}^1$ is a complex space whose global holomorphic functions are constant, so clause 2 fails.
An equivalent form: $X$ is Stein if and only if $H^q(X, \mathcal{F}) = 0$ for every coherent analytic sheaf $\mathcal{F}$ on $X$ and every $q \ge 1$.
The direction from Stein to vanishing is Cartan's theorem B.
