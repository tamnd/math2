---
tag: XM4NTS5BGG
kind: statement
role: fact
name: Pentagon identity
msc: [18M05]
uses: [M3MSQ3NKAE, WV898P4X16]
about: [M3MSQ3NKAE]
sources:
  - url: https://en.wikipedia.org/wiki/Monoidal_category
---

## Statement

Let $(\mathcal{C}, \otimes, I, \alpha, \lambda, \rho)$ be a [[monoidal category|M3MSQ3NKAE]] and let $A, B, C, D$ be objects of $\mathcal{C}$.
Then the following [[diagram commutes|WV898P4X16]], as an equality of morphisms $((A \otimes B) \otimes C) \otimes D \to A \otimes (B \otimes (C \otimes D))$:
$$(\id_A \otimes \alpha_{B,C,D}) \circ \alpha_{A, B \otimes C, D} \circ (\alpha_{A,B,C} \otimes \id_D) = \alpha_{A,B,C \otimes D} \circ \alpha_{A \otimes B, C, D}.$$

## Remarks

The identity is one of the two axioms in the definition of a monoidal category, the other being the triangle identity.
The five objects obtained by bracketing $A \otimes B \otimes C \otimes D$ in all ways are the vertices of a pentagon, and the five instances of $\alpha$ are its edges.
The left side goes around three edges and the right side around the other two.
In $(\mathbf{Set}, \times)$ both sides send $(((a,b),c),d)$ to $(a,(b,(c,d)))$.
By Mac Lane's coherence theorem, the pentagon and triangle identities imply that all formal diagrams built from $\alpha$, $\lambda$ and $\rho$ commute.
Without the pentagon this fails: an associator with an extra sign on real vector spaces satisfies naturality but makes the two routes around the pentagon differ by $-1$.

## Explanations

### L1 human

There are five ways to put brackets in a product of four things, and the associator moves brackets one step at a time.
Going from the leftmost bracketing to the rightmost one can be done in two different ways around a pentagon.
The pentagon identity says both ways give the same result.
This is what makes "rebracketing" a well-defined operation that does not depend on the order of the moves.

### L2 human

The pentagon identity is the first nontrivial coherence condition for an associativity isomorphism.
Together with the triangle identity it implies, by Mac Lane's coherence theorem, that all other diagrams of associators and unitors commute, so one never has to check longer ones.
The same pentagon reappears in the definition of bicategories, in the 3-cocycle condition for associators on $\mathrm{Vec}_G$, and as the Stasheff associahedron $K_4$ in the theory of $A_\infty$-structures.
