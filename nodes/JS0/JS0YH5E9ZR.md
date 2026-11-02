---
tag: JS0YH5E9ZR
kind: definition
name: Kernel pair
msc: [18A30, 18A20]
defines: E70DQGM8X5
uses: [A2DE66937D, 859F0TFVA3, Q05K04QJ71]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_category
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]] and let $f \colon X \to Y$ be a [[morphism|859F0TFVA3]] of $\mathcal{C}$.
A *kernel pair* of $f$ is an object $K$ with morphisms $p_1, p_2 \colon K \to X$ such that $(K, p_1, p_2)$ is a [[pullback|Q05K04QJ71]] of $f$ and $f$.
That is:

1. $f \circ p_1 = f \circ p_2$.
2. For every object $W$ and morphisms $q_1, q_2 \colon W \to X$ with $f \circ q_1 = f \circ q_2$, there is a unique $u \colon W \to K$ with $p_1 \circ u = q_1$ and $p_2 \circ u = q_2$.

## Remarks

Example: in the category of sets, $K = \set{(x, x') \in X \times X : f(x) = f(x')}$ with the two projections is a kernel pair.
Clause 1 holds by the definition of $K$, and for clause 2 the map $u$ is $w \mapsto (q_1(w), q_2(w))$.
For a group homomorphism $f$ with kernel $N$, this $K$ is the subgroup of pairs $(x, x')$ with $x^{-1} x' \in N$.

Non-example: in the category of sets, if $f$ is not injective, then $(X, \id_X, \id_X)$ satisfies clause 1 but not clause 2.
Take $W$ a point and $q_1, q_2$ picking $x \neq x'$ with $f(x) = f(x')$; no $u$ has $u = q_1$ and $u = q_2$.

A morphism $f$ is a monomorphism if and only if $(X, \id_X, \id_X)$ is a kernel pair of $f$.
