---
tag: 0E3X2G1ZQB
kind: object
name: Algebra of endomorphisms
msc: ["15A04", "16S50"]
topics: [9080WQTZ3M]
audience: ug1
instance_of: [0X9MBPP2Z3]
uses: [0PTF1PTJK0, 0VPCJWGMP9, 1TZSV19D85]
sources:
  - url: https://en.wikipedia.org/wiki/Endomorphism_ring
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Endomorphisms and automorphisms
---

## Description

Let $F$ be a field and let $V$ be a vector space over $F$.
The *algebra of endomorphisms* $\End_F(V)$ is the set of [[endomorphisms|0PTF1PTJK0]] of $V$.
Its addition and scalar multiplication are pointwise, as in the [[space of linear maps|0VPCJWGMP9]] $\Hom_F(V, V)$.
Its multiplication is composition, $ST = S \circ T$.
With these operations, it is an [[associative algebra|1TZSV19D85]] over $F$, with the identity map $\id_V$ as unit.
So $S(T + U) = ST + SU$, $(S + T)U = SU + TU$ and $a(ST) = (aS)T = S(aT)$ for all $S, T, U \in \End_F(V)$ and $a \in F$.

## Remarks

- The general notion, with examples and non-examples, is the concept of the [[algebra of endomorphisms|5JA4CYT1TB]].
- The algebra axioms are proved in the [[theorem on the algebra structure|7BDGQ1Q46E]].
- If $\dim V = n$, a basis of $V$ gives an algebra isomorphism $\End_F(V) \cong M_n(F)$.
- For $\dim V \ge 2$, the algebra is not commutative. Its centre consists of the scalar maps $a \id_V$, by the [[centre theorem|ZQPD85QCC8]].
- Its group of units is the group $GL(V)$ of linear automorphisms of $V$.

## Explanations

### L1 human

The endomorphisms of a space can be added, scaled and composed.
Composition plays the role of multiplication.
This makes them a ring that is also a vector space, like the square matrices.

### L2 human

For $V = \R^2$, the object is the algebra of $2 \times 2$ real matrices, once the standard basis is fixed.
The trap is to assume that $ST = TS$; in general, the order of composition matters.
