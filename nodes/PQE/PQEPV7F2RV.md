---
tag: PQEPV7F2RV
kind: statement
role: theorem
name: Equivalence of Boolean rings and Boolean algebras
msc: ["06E20", "06E05"]
uses: [0XADJKM699, 0RCV1ZFP8G, 0ME21QN125]
about: [0XADJKM699, 0RCV1ZFP8G]
sources:
  - url: https://en.wikipedia.org/wiki/Boolean_ring
---

## Statement

1. Let $(B, \wedge, \vee, \neg, 0, 1)$ be a [[Boolean algebra|0XADJKM699]].
Put $a + b = (a \wedge \neg b) \vee (\neg a \wedge b)$ and $a \cdot b = a \wedge b$.
Then $(B, +, \cdot, 0, 1)$ is a [[Boolean ring|0RCV1ZFP8G]].
2. Let $(R, +, \cdot, 0, 1)$ be a Boolean ring.
Put $a \wedge b = ab$, $a \vee b = a + b + ab$ and $\neg a = 1 + a$.
Then $(R, \wedge, \vee, \neg, 0, 1)$ is a Boolean algebra.
3. The two constructions are inverse to each other.
4. A map between Boolean algebras is a homomorphism if and only if it is a unital ring homomorphism of the matching rings.

## Remarks

The proof is a direct check of axioms.
In a Boolean ring, $(a + b)^2 = a + b$ gives $ab + ba = 0$, and $a = -a$ follows from $(a + a)^2 = a + a$, so the ring is commutative of characteristic $2$; this makes the lattice laws routine.
In the other direction, the key point is that $+$ is associative, which reduces to the distributive laws and [[De Morgan's laws|0XYVDWGQX2]].
For the power set of a set $X$, the ring addition is the [[symmetric difference|0ME21QN125]] $A \mathbin{\triangle} B$ and the product is $A \cap B$.
In categorical terms, the theorem gives an isomorphism between the category of Boolean algebras and the category of Boolean rings.

## Explanations

### L1 human

Boolean algebras use "and", "or" and "not"; Boolean rings use "exclusive or" and "and" as plus and times.
The theorem says that these are two notations for the same thing.
One can always translate between them without losing anything.

### L2 human

The ring view brings tools of commutative algebra to Boolean algebras.
Ideals of the ring are exactly the ideals of the Boolean algebra, and prime ideals are maximal, with quotient the field $\F_2$.
So ultrafilters, which are complements of maximal ideals, correspond to ring homomorphisms onto $\F_2$, and the Stone space of the algebra is the prime spectrum of the ring.
This is the bridge used in one standard proof of [[Stone's representation theorem|S4QJ395PA5]].
