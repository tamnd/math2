---
tag: TWEYQ0XAY4
kind: definition
name: Quantum logic
msc: [81P10, 03G12, 06C15]
topics: [NJB94B39QK]
audience: research
defines: 2E9DMB7A6Q
uses: [HM2HHE3J51, 0XJXTBCB2T, 6FPKEFX0X4]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_logic
  - url: https://plato.stanford.edu/entries/qt-quantlog/
    locator: Quantum Logic and Probability Theory (SEP entry), section 1.2
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

## Notation

Closed subspaces correspond one to one to orthogonal projections: $M$ is the range of a unique projection $P_M$.
So authors also write $\mathcal{L}(H)$ for the set of projections, with $P \leq Q$ when $PQ = QP = P$, and $P^\perp = 1 - P$.
The bottom $\set{0}$ is written $0$, and the top $H$ is written $1$.

## Remarks

With this structure $\mathcal{L}(H)$ is an orthomodular lattice with least element $\set{0}$ and greatest element $H$.
Authors differ on the abstract notion: some use orthomodular partially ordered sets, often with countable joins of orthogonal elements.

Example: in $H = \C^2$, let $A$, $B$ and $C$ be the lines spanned by $(1, 0)$, $(0, 1)$ and $(1, 1)$.
Then $A \wedge (B \vee C) = A \wedge \C^2 = A$, while $(A \wedge B) \vee (A \wedge C) = \set{0}$.
So the distributive law of classical logic fails in $\mathcal{L}(\C^2)$.

Non-example: the hexagon ortholattice $O_6$, with $0 < a < b < 1$, $0 < b^\perp < a^\perp < 1$ and no other relations, is orthocomplemented.
It is not orthomodular, since $a \le b$ but $a \vee (a^\perp \wedge b) = a \vee 0 = a \ne b$; so it is not a quantum logic in the abstract sense.
For full proofs in $\R^2$ and for $O_6$, see [[distributivity fails in the subspace lattice of the plane|~e0e7fd0d]] and [[the hexagon ortholattice is not orthomodular|~1a47735b]].

## Explanations

### L1 human

A quantum logic is the set of yes-no questions about a quantum system.
Each question is a closed subspace: the states for which the answer is surely "yes".
"And" is intersection, "or" is the smallest closed subspace that contains both, and "not" is the perpendicular subspace.

### L2 human

The join must be the closure of $M + N$, because in infinite dimensions the sum of two closed subspaces need not be closed.
With these operations the structure is an ortholattice that satisfies the orthomodular law, but not the distributive law.
A trap is to take the union $M \cup N$ as the join; a union of two subspaces is usually not a subspace.

### L3 human

The abstract definition keeps the orthomodular law, the trace of the fact that $N = M \vee (M^\perp \wedge N)$ whenever $M \subseteq N$.
Variants use orthomodular posets or orthoalgebras, which need joins only of orthogonal elements.
These structures are the setting of Mackey's axioms and of Piron's representation theorem.
