---
tag: FAGMBTRN7Z
kind: definition
name: Bidual and canonical embedding
msc: [46B10]
defines: QKR3D65TTH
uses: [03J5RAKB30, 4A82S5FVRT, 07SJXTWVQW]
sources:
  - url: https://en.wikipedia.org/wiki/Reflexive_space
---

## Definition

Let $X$ be a [[normed vector space|03J5RAKB30]] over $\mathbb{K} = \R$ or $\C$, and let $X^*$ be its [[continuous dual space|4A82S5FVRT]] with the operator norm.
The *bidual* of $X$ is the Banach space $X^{**} = (X^*)^*$.
The *canonical embedding* is the map $J \colon X \to X^{**}$ given by
$$(Jx)(f) = f(x) \quad \text{for } x \in X \text{ and } f \in X^*.$$

## Remarks

For each $x$, the map $Jx$ is linear on $X^*$ and $\abs{(Jx)(f)} \le \norm{f}\,\norm{x}$, so $Jx \in X^{**}$ with $\norm{Jx} \le \norm{x}$.
The [[Hahn–Banach theorem|QB5AE3VYZZ]] gives $f$ with $\norm{f} = 1$ and $f(x) = \norm{x}$, so in fact $J$ is a [[linear isometry|07SJXTWVQW]].
Example: for $X = \mathbb{K}^n$ with any norm, $J$ is an isometric isomorphism onto $X^{**}$, because $\dim X^{**} = \dim X$; compare [[the double dual in linear algebra|0ZJM9D7NPS]].
Example: for $X = c_0$ one has $X^* = \ell^1$ and $X^{**} = \ell^\infty$, and $J$ is the inclusion of $c_0$ in $\ell^\infty$, which is not onto.
Non-example: the algebraic double dual, the space of all linear forms on $X^*$, is in general larger than $X^{**}$, because it does not require continuity.
The image $J(X)$ is closed in $X^{**}$ exactly when $X$ is complete; in general the closure of $J(X)$ is a [[completion|2W7R5JHF0C]] of $X$.
