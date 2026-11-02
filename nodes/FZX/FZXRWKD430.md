---
tag: FZXRWKD430
kind: definition
name: Fredholm map
msc: [58B15, 47A53, 58C25]
defines: GFXQ6HEM65
uses: [VB95VVVDM8, Q5B5YGY7D6, ADJZ99KY2Q, 06EH97V2A7]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_operator
---

## Definition

Let $M$ and $N$ be [[Banach manifolds|VB95VVVDM8]] of class $C^k$ with $k \ge 1$, and let $f \colon M \to N$ be a map of class $C^1$.
The map $f$ is a *Fredholm map* if for every $x \in M$ the [[derivative|06EH97V2A7]] $d f_x \colon T_x M \to T_{f(x)} N$ is a [[Fredholm operator|Q5B5YGY7D6]].
This means that the kernel of $d f_x$ is finite-dimensional and its image is closed and of finite codimension.
The *index* of $f$ at $x$ is the [[Fredholm index|ADJZ99KY2Q]]
$$\operatorname{ind}_x f = \dim \ker d f_x - \dim \operatorname{coker} d f_x.$$

## Remarks

The Fredholm operators form an open set on which the index is locally constant, and $x \mapsto d f_x$ is continuous in local charts.
So the index is locally constant in $x$, and on a connected $M$ it is a single integer.


Example: every $C^1$ map $f \colon \R^m \to \R^n$ is Fredholm of index $m - n$, since $\dim \ker A - \dim \operatorname{coker} A = m - n$ for every linear map $A \colon \R^m \to \R^n$ by rank-nullity.

Non-example: the inclusion $\iota \colon \ell^2 \to \ell^2 \times \ell^2$, $x \mapsto (x, 0)$, is smooth and its derivative is injective with closed image, but the cokernel is isomorphic to $\ell^2$, which is infinite-dimensional, so $\iota$ is not Fredholm.

A map of the form $f = L + K$ with $L$ a linear Fredholm operator and $K$ a $C^1$ map whose derivatives are compact operators is Fredholm with the index of $L$.
