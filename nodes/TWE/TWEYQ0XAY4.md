---
tag: TWEYQ0XAY4
kind: definition
name: Quantum logic
msc: [81P10, 03G12, 06C15]
defines: 2E9DMB7A6Q
uses: [HM2HHE3J51, 0XJXTBCB2T, 6FPKEFX0X4]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_logic
---

## Definition

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]].
The *quantum logic* of $H$ is the set $\mathcal{L}(H)$ of closed linear subspaces of $H$, with the following structure:

1. the order is inclusion $\subseteq$;
2. the meet $M \wedge N$ is the intersection $M \cap N$;
3. the join $M \vee N$ is the closure of the sum $M + N$;
4. the negation $M^\perp$ is the [[orthogonal complement|0XJXTBCB2T]] of $M$.

The elements of $\mathcal{L}(H)$ are called *propositions*.
More abstractly, a *quantum logic* is an [[orthomodular lattice|6FPKEFX0X4]], whose elements are the propositions.

## Remarks

With this structure $\mathcal{L}(H)$ is an orthomodular lattice with least element $\set{0}$ and greatest element $H$.
Authors differ on the abstract notion: some use orthomodular partially ordered sets, often with countable joins of orthogonal elements.

Example: in $H = \C^2$, let $A$, $B$ and $C$ be the lines spanned by $(1, 0)$, $(0, 1)$ and $(1, 1)$.
Then $A \wedge (B \vee C) = A \wedge \C^2 = A$, while $(A \wedge B) \vee (A \wedge C) = \set{0}$.
So the distributive law of classical logic fails in $\mathcal{L}(\C^2)$.

Non-example: the hexagon ortholattice $O_6$, with $0 < a < b < 1$, $0 < b^\perp < a^\perp < 1$ and no other relations, is orthocomplemented.
It is not orthomodular, since $a \le b$ but $a \vee (a^\perp \wedge b) = a \vee 0 = a \ne b$; so it is not a quantum logic in the abstract sense.
