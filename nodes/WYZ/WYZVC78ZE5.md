---
tag: WYZVC78ZE5
kind: definition
name: Kernel
msc: [18A30, "18E05"]
defines: S417YNEJ6M
uses: [YF9F9EG6M3, CTJ5AD8ST5, Y2NP1JFR86, 0NZ8JA25WK, 0W88CEGQP1]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(category_theory)
---

## Definition

Let $\mathcal{C}$ be a category with [[zero morphisms|YF9F9EG6M3]], and let $f \colon X \to Y$ be a morphism of $\mathcal{C}$.
A *kernel* of $f$ is an object $K$ with a morphism $k \colon K \to X$ such that:

1. $f \circ k = 0$;
2. for every morphism $u \colon T \to X$ with $f \circ u = 0$ there is a unique morphism $v \colon T \to K$ with $u = k \circ v$.

## Remarks

Equivalently, $k$ is an [[equalizer|CTJ5AD8ST5]] of $f$ and $0 \colon X \to Y$.
A kernel is unique up to a unique isomorphism, and is written $\ker f \to X$.
Every kernel is a [[monomorphism|Y2NP1JFR86]], by the uniqueness in clause 2.

Example: in the category of [[modules|0NZ8JA25WK]] over a ring, the inclusion $k \colon \set{x \in X : f(x) = 0} \to X$ of the [[kernel of the homomorphism|0W88CEGQP1]] is a kernel.
If $f \circ u = 0$, then $u$ takes values in this submodule, so $u$ factors through $k$, and uniquely since $k$ is injective.

Non-example: for the reduction $f \colon \Z \to \Z/2$ of abelian groups, the inclusion $k \colon 4\Z \to \Z$ satisfies clause 1 but not clause 2.
The inclusion $u \colon 2\Z \to \Z$ satisfies $f \circ u = 0$ but does not factor through $4\Z$, since $2 \notin 4\Z$.
