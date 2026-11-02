---
tag: 2FR1BWY3H6
kind: definition
name: dg category
msc: [18G35, 18D20, "16E45"]
defines: KTN8HTSY3R
uses: [A2DE66937D, BPH9SJ30Y0, WQ82C0M3QB]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_graded_category
---

## Definition

Let $k$ be a commutative ring.
A *dg category* over $k$ is a [[category|A2DE66937D]] $\mathcal{C}$ [[enriched|BPH9SJ30Y0]] over the monoidal category of cochain complexes of $k$-modules.
In detail, for objects $x, y$ of $\mathcal{C}$ there is a [[chain complex|WQ82C0M3QB]] $\Hom(x, y) = \bigoplus_{n \in \Z} \Hom^n(x, y)$ of $k$-modules with differential $d$ of degree $+1$, such that:

1. For objects $x, y, z$ there are $k$-bilinear composition maps $\Hom^p(y, z) \times \Hom^q(x, y) \to \Hom^{p+q}(x, z)$, written $(g, f) \mapsto g \circ f$.
2. Composition is associative.
3. Each object $x$ has an identity $1_x \in \Hom^0(x, x)$ with $d(1_x) = 0$, which is a unit for composition.
4. The Leibniz rule holds: $d(g \circ f) = d(g) \circ f + (-1)^{p} g \circ d(f)$ for $g \in \Hom^p(y, z)$ and $f \in \Hom^q(x, y)$.

Clauses 1 and 4 say that composition is a map of complexes $\Hom(y, z) \otimes_k \Hom(x, y) \to \Hom(x, z)$.

## Remarks

Example: the dg category $C_{dg}(k)$ has as objects the cochain complexes $X$ of $k$-modules, with $\Hom^n(X, Y) = \prod_{i} \Hom_k(X^i, Y^{i+n})$.
For $f$ of degree $n$ the differential is $d(f) = d_Y \circ f - (-1)^n f \circ d_X$.
One checks $d^2(f) = d_Y^2 \circ f - f \circ d_X^2 = 0$, because the two middle terms $\pm d_Y \circ f \circ d_X$ cancel, and the Leibniz rule follows from the same sign computation.
The closed morphisms of degree $0$ are the chain maps, and the exact ones are the null-homotopic chain maps.

Non-example: over $k = \Q$, use the same graded maps but drop the sign, so $d(f) = d_Y \circ f + f \circ d_X$.
Then $d^2(f) = 2\, d_Y \circ f \circ d_X$.
Let $C$ be the complex with $C^0 = C^1 = \Q$ and differential the identity, and let $f \in \Hom^{-1}(C, C)$ be the identity map $C^1 \to C^0$.
Then $d^2(f)$ is $2 \ne 0$ on $C^0$, so $\Hom(C, C)$ is not a complex.

A dg category with one object is the same as a differential graded algebra.
