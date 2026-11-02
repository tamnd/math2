---
tag: EQHPSKC5SY
kind: statement
role: theorem
name: Cartan's uniqueness theorem
msc: [32H02, 32M18]
uses: [507C34W0ZT, 3MQTWKBBBT, 047NDTEPCV, 09QSZVVM26]
about: [3MQTWKBBBT]
sources:
  - url: https://en.wikipedia.org/wiki/Biholomorphism
---

## Statement

Let $D \subseteq \C^n$ be a [[bounded|09QSZVVM26]] connected open set and let $p \in D$.
Let $f \colon D \to D$ be a [[holomorphic map|3MQTWKBBBT]] with $f(p) = p$.
Suppose that the complex [[Jacobian matrix|047NDTEPCV]] of $f$ at $p$ is the identity matrix.
Then $f(z) = z$ for all $z \in D$.

## Remarks

The proof uses iteration.
Take $p = 0$ and suppose that $f(z) = z + P_k(z) + \cdots$, where $P_k$ is the first nonzero homogeneous term of degree $k \ge 2$ in the Taylor expansion of $f - \id$.
The $m$-th iterate of $f$ then has the expansion $z + m P_k(z) + \cdots$.
All iterates map $D$ into the bounded set $D$, so the Cauchy estimates bound their Taylor coefficients independently of $m$, which forces $P_k = 0$.

A consequence: if $g, h$ are [[biholomorphisms|FX92PP3HZR]] of $D$ onto a domain $D'$ with $g(p) = h(p)$ and the same Jacobian matrix at $p$, then $g = h$.
So an automorphism of a bounded domain is determined by its value and its derivative at one point.

Boundedness is necessary.
On $\C^2$ the map $f(z_1, z_2) = (z_1, z_2 + z_1^2)$ fixes $0$ and has the identity as Jacobian matrix at $0$, but it is not the identity map.

## Explanations

### L1 human

A holomorphic self-map of a bounded domain that fixes a point and looks like the identity to first order at that point must be the identity everywhere.
It is a rigidity result: first-order information pins down the whole map.
In one variable it is a cousin of the [[Schwarz lemma|0MB48XDBY3]].

### L2 human

The theorem is the basic tool for studying the automorphism group of a bounded domain.
It shows that the map sending an automorphism fixing $p$ to its Jacobian matrix at $p$ is injective.
With it one proves that automorphisms of a bounded circular domain fixing the origin are linear maps.
It is also a step toward showing that the automorphism group of a bounded domain is a Lie group.
