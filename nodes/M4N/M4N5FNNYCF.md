---
tag: M4N5FNNYCF
kind: definition
name: Cokernel
msc: [18A30, "18E05"]
defines: H8W38933NC
uses: [YF9F9EG6M3, DVSTWGVCSZ, RVXDSY04KG, S417YNEJ6M, 082GHNPJ53, 0NZ8JA25WK]
sources:
  - url: https://en.wikipedia.org/wiki/Cokernel
---

## Definition

Let $\mathcal{C}$ be a category with [[zero morphisms|YF9F9EG6M3]], and let $f \colon X \to Y$ be a morphism of $\mathcal{C}$.
A *cokernel* of $f$ is an object $Q$ with a morphism $q \colon Y \to Q$ such that:

1. $q \circ f = 0$;
2. for every morphism $u \colon Y \to T$ with $u \circ f = 0$ there is a unique morphism $v \colon Q \to T$ with $u = v \circ q$.

## Remarks

Equivalently, $q$ is a [[coequalizer|DVSTWGVCSZ]] of $f$ and $0 \colon X \to Y$; it is the [[kernel|S417YNEJ6M]] of $f$ in the opposite category.
A cokernel is unique up to a unique isomorphism, is written $Y \to \operatorname{coker} f$, and is an [[epimorphism|RVXDSY04KG]].

Example: in the category of [[modules|0NZ8JA25WK]] over a ring, the quotient map $q \colon Y \to Y / f(X)$ is a cokernel of $f$.
If $u \circ f = 0$, then $u$ vanishes on $f(X)$ and so induces a unique $v \colon Y / f(X) \to T$ with $u = v \circ q$.
For multiplication by $n \ge 1$ on the [[abelian group|082GHNPJ53]] $\Z$, the cokernel is the reduction $\Z \to \Z / n\Z$.

Non-example: for multiplication by $2$ on $\Z$, the map $\Z \to 0$ satisfies clause 1 but not clause 2.
The reduction $u \colon \Z \to \Z/2$ satisfies $u \circ 2 = 0$ but does not factor through the zero group, since $u \ne 0$.
