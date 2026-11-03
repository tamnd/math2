---
tag: MHQ5T0EGXP
kind: definition
name: Baric algebra
msc: [17D92, 92D10]
defines: A6HRHW6CBY
uses: [60W3THKGA7, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Genetic_algebra
---

## Definition

Let $K$ be a [[field|04C5ZBG1WT]] and let $A$ be a [[nonassociative algebra|60W3THKGA7]] over $K$, that is, a vector space over $K$ with a bilinear product.
A *weight* on $A$ is a nonzero $K$-linear map $w \colon A \to K$ such that $w(xy) = w(x)\, w(y)$ for all $x, y \in A$.
A *baric algebra* over $K$ is a pair $(A, w)$ of such an algebra and a weight on it.

## Remarks

Example: let $A$ have basis $A_1, A_2$ over $\Q$ with $A_1^2 = A_1$, $A_2^2 = A_2$ and $A_1 A_2 = A_2 A_1 = \tfrac12 (A_1 + A_2)$, the gametic algebra of one gene with two alleles.
Let $w(A_1) = w(A_2) = 1$.
Each product of two basis vectors has weight $1$, so $w(xy) = w(x) w(y)$ on the basis, and by bilinearity on all of $A$.

Non-example: a nonzero vector space $A$ with the zero product.
A weight would satisfy $w(x)^2 = w(x^2) = w(0) = 0$, so $w(x) = 0$ for all $x$, and $A$ has no weight.
The same argument shows that an algebra with $x^2 = 0$ for all $x$, such as a Lie algebra, is never baric.

A baric algebra is also called a weighted algebra.
The kernel of $w$ is an ideal of codimension $1$.
