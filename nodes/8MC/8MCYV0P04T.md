---
tag: 8MCYV0P04T
kind: definition
name: Short exact sequence
msc: [18G35, "18E10"]
defines: KJKNJMGKZZ
uses: [JB7ZBFBA9C, Y9CZ3MTNF1, Y2NP1JFR86, RVXDSY04KG, S417YNEJ6M]
sources:
  - url: https://en.wikipedia.org/wiki/Exact_sequence
---

## Definition

Let $\mathcal{A}$ be an [[abelian category|Y9CZ3MTNF1]], for example the category of modules over a ring.
A *short exact sequence* in $\mathcal{A}$ is a diagram
$$0 \to A \xrightarrow{f} B \xrightarrow{g} C \to 0$$
of objects and morphisms of $\mathcal{A}$ such that:

1. $f$ is a [[monomorphism|Y2NP1JFR86]];
2. $g$ is an [[epimorphism|RVXDSY04KG]];
3. the image of $f$ equals the [[kernel|S417YNEJ6M]] of $g$.

## Remarks

Equivalently, the sequence is [[exact|JB7ZBFBA9C]] at $A$, at $B$ and at $C$.
Equivalently again, $g \circ f = 0$, $f$ is a kernel of $g$, and $g$ is a cokernel of $f$.
Then $C$ is isomorphic to the quotient $B / f(A)$, and $B$ is called an *extension* of $C$ by $A$.

Example: $0 \to \Z \xrightarrow{4} \Z \xrightarrow{\pi} \Z/4\Z \to 0$ is short exact, with $\pi$ the reduction modulo $4$.
Multiplication by $4$ is injective, $\pi$ is onto, and the image $4\Z$ of the first map is the kernel of $\pi$.

Non-example: $0 \to 2\Z \xrightarrow{\iota} \Z \xrightarrow{\pi} \Z/4\Z \to 0$, with $\iota$ the inclusion, fails clause 3.
Clauses 1 and 2 hold, but the image of $\iota$ is $2\Z$ while the kernel of $\pi$ is $4\Z$.
