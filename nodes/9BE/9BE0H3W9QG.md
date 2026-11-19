---
tag: 9BE0H3W9QG
kind: statement
role: theorem
name: Undecidability of the Halpern–Shoham interval logic
msc: ["03B44", "03B25", "03D35"]
topics: [CQM9SRN8PM]
audience: research
uses: [991B5RR6X4, 0FRXBVVR03, AJH5HPD2B7, BBYNPDWR5R, 3J6YG01N22]
about: [991B5RR6X4]
proofs: [NTRTEF0KVV]
sources:
  - book: isbn:9780198537694
    locator: Gabbay, Hodkinson and Reynolds, Temporal Logic, volume 1
  - url: https://en.wikipedia.org/wiki/Allen%27s_interval_algebra
    locator: section Relations
---

## Statement

Let HS be the [[interval temporal logic|991B5RR6X4]] of Halpern and Shoham, with the modalities $\langle A \rangle$, $\langle B \rangle$, $\langle E \rangle$ and their inverses, over intervals $[a, b]$ of a [[linear order|0FRXBVVR03]].
Let $\mathcal{C}$ be a class of linear orders that contains at least one order with an infinite ascending sequence $x_0 < x_1 < x_2 < \cdots$, or an infinite descending sequence.
Then the set of HS formulas valid over $\mathcal{C}$ is not [[decidable|3J6YG01N22]].
Equivalently, satisfiability of HS formulas over $\mathcal{C}$ is undecidable.

In particular, HS is undecidable over $(\mathbb{N}, <)$, $(\mathbb{Z}, <)$, $(\mathbb{Q}, <)$, $(\mathbb{R}, <)$ and over the class of all linear orders.

## Remarks

### Why each hypothesis is needed

1. Some infinite chain is needed for this proof, which builds an infinite grid. Over a class of orders of bounded finite size, satisfiability is decidable: a formula with $k$ atoms has finitely many models there up to isomorphism, and each can be checked.
2. The full set of modalities matters. The fragment with only $\langle A \rangle$ and $\langle \bar A \rangle$ is decidable over all linear orders and over $\mathbb{N}$.
3. Linearity of time is part of the semantics. The proof uses that the intervals between points of a chain form a grid.

### Consequences

1. No algorithm decides whether an HS specification is satisfiable over $\mathbb{N}$.
2. Practical interval logics either restrict the modalities, restrict the models, or use the chop operator with restrictions, as in Moszkowski's ITL tools.

### Generalizations

Some small fragments of HS remain undecidable, while others, such as the fragment with $\langle A \rangle$ and $\langle \bar A \rangle$, are decidable.
The fragments have been classified for the main classes of linear orders.

## History

Halpern and Shoham proved the theorem in "A propositional modal logic of time intervals", in 1986, with the journal version in the Journal of the ACM in 1991.
Their proof encodes computations of Turing machines in models of HS formulas.
Later proofs for fragments reduce tiling problems for an octant of the plane, as below.

## Explanations

### L1 human

A computer cannot decide, for every sentence of this interval logic, whether it is always true.
The reason is that intervals over an infinite time line behave like the squares of an infinite grid.
On such a grid one can draw the run of any computer program, and then the question "does the program stop?" becomes a question about the logic.

### L2 human

We see the grid inside the intervals.

1. Take points $x_0 < x_1 < x_2 < \cdots$.
2. The interval $[x_i, x_j]$, with $i < j$, is the grid cell in column $i$ and row $j$.
3. The cell $[x_i, x_{j+1}]$ is reached from $[x_i, x_j]$ with the inverse of $B$, since $[x_i, x_j]$ begins it.
4. The cell $[x_{i+1}, x_j]$ is reached with $E$, since it ends $[x_i, x_j]$.

A trap: the grid uses only the points $x_i$; the formula must force such points, which is the technical core of the proof.

### L3 human

HS is a two-dimensional modal logic over the half-plane above the diagonal.
Products of linear modal logics are undecidable for similar grid reasons.
The proof needs a modal way to reach the "next" point, which is why discreteness or a chain of marked points is forced by the formula.
