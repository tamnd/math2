---
tag: CPA1C45GQR
kind: definition
name: Torsor
msc: [14L15, 14L30, 20G10]
defines: 5CYEQY4SWR
uses: [0WCY42EV9V, RW85C34GQW, GH81SYAPPN]
sources:
  - url: https://en.wikipedia.org/wiki/Principal_homogeneous_space
---

## Definition

Let $G$ be a group.
A *$G$-torsor* is a nonempty set $X$ with a [[group action|0WCY42EV9V]] of $G$ such that for all $x, y \in X$ there is exactly one $g \in G$ with $g \cdot x = y$.

Let $k$ be a field and let $G$ be an [[algebraic group|GH81SYAPPN]] over $k$.
A *$G$-torsor* over $k$ is a nonempty variety $X$ over $k$ with an [[action|RW85C34GQW]] $\sigma$ of $G$ such that the morphism
$$G \times_k X \to X \times_k X, \quad (g, x) \mapsto (\sigma(g, x), x)$$
is an isomorphism.

## Remarks

In the set case, the condition says that the action is free and transitive.
In the variety case, $X$ becomes isomorphic to $G$, with $G$ acting by left translation, after a finite extension of $k$.
The torsor is *trivial* if $X \cong G$ over $k$, and this holds if and only if $X$ has a $k$-point.

Example: let $V$ be a vector space and let $A$ be an affine space with translation space $V$.
For any two points $a, b \in A$ there is exactly one vector $v$ with $a + v = b$, so $A$ is a $V$-torsor.

Example over a field: let $G = \mu_2 = \set{\pm 1}$ over $\R$ act on $X = \set{x^2 = -1}$ by $x \mapsto \pm x$.
Over $\C$, $X$ has the two points $\pm i$, and $G$ swaps them freely.
So $X$ is a $\mu_2$-torsor, and it is not trivial, since $X(\R)$ is empty.

Non-example: $\mathbb{G}_m$ acting on $\mathbb{A}^1$ by multiplication is not a torsor.
The point $0$ is fixed by every $t$, so the action is neither free nor transitive.
