---
tag: PSZKJY4QH3
kind: statement
role: theorem
name: Jankov's theorem on continuum many intermediate logics
msc: ["03B55", "03B20"]
topics: [38EQ20GR7M]
audience: research
uses: [H5NSKEP3P2, D25R70HQ7C, 0WC28W9DNM, 03HF498P1J]
about: [H5NSKEP3P2]
proofs: [WFRC97WNBY]
sources:
  - url: https://plato.stanford.edu/entries/logic-intuitionistic/
    locator: 6.1 Subintuitionistic and Intermediate Logics
  - url: https://eprints.illc.uva.nl/id/document/492
    locator: Section 5.4, Theorem 107 and Corollary 108
---

## Statement

For finite rooted Kripke frames $F$ and $G$, write $F \leq G$ if $F$ is a p-morphic image of a generated subframe of $G$.

**Theorem (Jankov).** There are exactly $2^{\aleph_0}$ [[intermediate logics|H5NSKEP3P2]].
More precisely, there is an infinite sequence $(F_n)_{n \in \mathbb{N}}$ of finite rooted frames such that the logics $\mathrm{Log}\set{F_n : n \in S}$, for nonempty $S \subseteq \mathbb{N}$, are pairwise distinct.

The proof is in [[the proof by Jankov formulas|WFRC97WNBY]].

## Remarks

### Why each hypothesis is needed

1. The sequence must be an [[antichain|03HF498P1J]] for $\leq$. For a chain $F_1 \leq F_2 \leq \dots$, the logics $\mathrm{Log}\set{F_n : n \in S}$ depend only on $\sup S$, so there are only countably many.
2. The frames must be finite, or at least the Jankov formula must characterize $\leq$ on them. For infinite frames the relation $\leq$ is not antisymmetric.

### Consequences

1. There are only countably many finitely axiomatizable intermediate logics, so most intermediate logics are not finitely axiomatizable.
2. In the same way, most intermediate logics are not recursively axiomatizable, and most are undecidable.
3. The lattice of intermediate logics has cardinality of the [[continuum|0WC28W9DNM]], and so has the lattice of varieties of Heyting algebras.

### Converse

The upper bound holds for every countable language: a logic is a set of formulas, and there are countably many formulas.
So the theorem is sharp.

### Generalizations

1. Wroński showed that there are continuum many intermediate logics with the disjunction property.
2. The same method gives continuum many normal extensions of $\mathsf{S4}$ and of $\mathsf{Grz}$, by the [[Blok-Esakia theorem|BB9TA5Q9PN]].

## History

Jankov proved the theorem in 1968, with an infinite sequence of finite rooted frames, in the paper on strongly independent superintuitionistic calculi.
The modern proof uses his characteristic formula of a finite subdirectly irreducible Heyting algebra, now called the Jankov formula.

## Explanations

### L1 human

Between intuitionistic and classical logic there are uncountably many logics.
The reason is that one can find infinitely many finite models, none of which can be built from another.
Each set of these models gives its own logic, and there are uncountably many sets.

### L2 human

1. Each finite rooted frame $F$ has a formula $\chi(F)$ that fails on a finite frame $G$ exactly when $F \leq G$.
2. Choose an infinite antichain of such frames.
3. For each set $S$ of indices, take the logic of the frames indexed by $S$.
4. The formula $\chi(F_n)$ belongs to this logic exactly when $n \notin S$.

The typical use is as the first fact about the size and complexity of the lattice of intermediate logics.
A trap: the argument needs the logics of sets of frames, not the logics axiomatized by sets of formulas, to keep the bookkeeping simple.

### L3 human

Algebraically, the theorem says that the variety of Heyting algebras has continuum many subvarieties.
Each finite subdirectly irreducible Heyting algebra splits the lattice of subvarieties, and an antichain of them gives an independent family of splittings.
