---
tag: KJ2NZCB7TH
kind: definition
name: Free object
msc: [18A40, 08B20]
defines: QBDT694BAP
uses: [FYBRP16KAN, EN4DD2FAJH, WP0YB7VC59]
sources:
  - url: https://en.wikipedia.org/wiki/Free_object
---

## Definition

Let $\mathcal{C}$ be a [[concrete category|FYBRP16KAN]] with forgetful functor $U \colon \mathcal{C} \to \mathbf{Set}$, and let $X$ be a set.
A *free object* on $X$ is an object $A$ of $\mathcal{C}$ with a map of sets $i \colon X \to U A$ with this [[universal property|EN4DD2FAJH]].
For every object $B$ of $\mathcal{C}$ and every map $f \colon X \to U B$, there is a unique morphism $g \colon A \to B$ with $U(g) \circ i = f$.

## Remarks

A free object on $X$ is unique up to a unique isomorphism compatible with $i$.
If every set has a free object $F(X)$, then $F$ is a functor and is left adjoint to $U$.

Example: in the category of groups, the free group $F(X)$ of reduced words in $X \cup X^{-1}$, with $i$ sending $x$ to the one-letter word, is a free object.
Given $f \colon X \to U B$, the morphism $g$ sends a reduced word $x_1^{\epsilon_1} \cdots x_n^{\epsilon_n}$ to $f(x_1)^{\epsilon_1} \cdots f(x_n)^{\epsilon_n}$, and it is the only homomorphism extending $f$.

Non-example: the group $\Z/2\Z$ with $i$ sending the point of $X = \set{x}$ to $1$ is not free on $X$.
For $B = \Z$ and $f(x) = 1$, there is no homomorphism $g \colon \Z/2\Z \to \Z$ with $g(1) = 1$, since $2 g(1) = g(0) = 0$.
