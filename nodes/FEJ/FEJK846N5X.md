---
tag: FEJK846N5X
kind: statement
role: theorem
name: Margulis arithmeticity theorem
msc: ["22E40", 20G30, 11F06]
uses: [XJS07AJ50Y, BTYF5Y5PFY, 4XWG6S7R4Z, GA81VVQHEP, 0DTXBQPA2S]
about: [BTYF5Y5PFY, 4XWG6S7R4Z]
sources:
  - url: https://en.wikipedia.org/wiki/Arithmetic_group
---

## Statement

Let $G$ be a connected [[semisimple Lie group|XJS07AJ50Y]] with finite centre and no compact factors, of real rank at least $2$.
Let $\Gamma$ be an irreducible [[lattice|BTYF5Y5PFY]] in $G$: for every noncompact closed normal subgroup $N$ of $G$, the product $\Gamma N$ is dense in $G$.
Then $\Gamma$ is arithmetic.
That is, there are a semisimple [[linear algebraic group|GA81VVQHEP]] $H \subseteq \mathrm{GL}_n$ over $\Q$ and a continuous surjective homomorphism $\phi \colon H(\R)^\circ \to G$ with compact kernel with the following property.
The groups $\phi(H(\Z) \cap H(\R)^\circ)$ and $\Gamma$ are commensurable: their intersection has finite [[index|0DTXBQPA2S]] in both.

## Remarks

The proof rests on the [[Margulis superrigidity theorem|DSKV65NHZZ]].
Superrigidity is applied to $\Gamma$ in real, complex and $p$-adic groups.
It shows that, in suitable coordinates, the matrix entries of $\mathrm{Ad}(\Gamma)$ lie in a number field and have bounded denominators.
From this one builds the $\Q$-group $H$.

Example: $\mathrm{SL}_n(\R)$ with $n \ge 3$ has real rank $n - 1 \ge 2$.
So every lattice in it is commensurable, up to conjugation, with a group built from an algebraic group over $\Q$, such as $\mathrm{SL}_n(\Z)$.

The rank condition cannot be dropped completely.
Gromov and Piatetski-Shapiro constructed non-arithmetic lattices in $\mathrm{SO}(n, 1)$ for every $n \ge 2$.
Mostow, and Deligne and Mostow, found non-arithmetic lattices in $\mathrm{SU}(2, 1)$ and $\mathrm{SU}(3, 1)$.
In real rank $1$, the groups $\mathrm{Sp}(n, 1)$ and the rank one form of $F_4$ still have only arithmetic lattices, by Corlette and Gromov–Schoen.

## Explanations

### L1 human

The simplest way to build a lattice is to take the integer points of a group defined by equations, like $\mathrm{SL}_3(\Z)$ inside $\mathrm{SL}_3(\R)$.
Margulis proved that in the big groups of higher rank, there is no other way.
Every lattice there is built from integer points, after allowing finite index changes and a few standard operations.

### L2 human

Together with the [[Borel–Harish-Chandra theorem|3B451RD8AJ]], this gives a complete description of irreducible lattices in higher rank.
It turns questions about lattices into questions about algebraic groups over number fields.
In rank one, arithmeticity can fail, and hyperbolic manifolds give many non-arithmetic examples.
