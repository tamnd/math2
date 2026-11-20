---
tag: J15KTB0NH5
kind: statement
role: theorem
name: Elementarily equivalent finite structures are isomorphic
aliases: [finite-elementary-equivalence-implies-isomorphism]
msc: ["03C07", "03C13"]
topics: [AY09KYSW81]
audience: ug2
about: [P3B1V182N4, PZMGQMDN25]
uses: [P3B1V182N4, PZMGQMDN25, EY20BF96SJ, 070R982G4B, DKFGQTRYZE]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_equivalence
    locator: Elementarily equivalent structures
  - book: isbn:9780387987606
    locator: Chapter 1
---

## Statement

Let $L$ be a signature, and let $\mathcal{M}$ and $\mathcal{N}$ be $L$-structures.
Suppose that $\mathcal{M}$ is [[finite|070R982G4B]] and that $\mathcal{M} \equiv \mathcal{N}$, that is, $\mathcal{M}$ and $\mathcal{N}$ are [[elementarily equivalent|P3B1V182N4]].
Then $\mathcal{N}$ is finite with the same number of elements as $\mathcal{M}$, and $\mathcal{M} \cong \mathcal{N}$.
The signature $L$ may be infinite.

## Remarks

### Why each hypothesis is needed

- Finiteness is needed. The orders $(\Q, <)$ and $(\R, <)$ are elementarily equivalent, since both are models of the complete theory of dense linear orders without endpoints, but they are not [[isomorphic|PZMGQMDN25]], since $\Q$ is countable and $\R$ is not; see [[this example|TZZVG88865]].
- Equal cardinality of infinite structures is not enough either. The field $\overline{\Q}$ of algebraic numbers and the algebraic closure of $\Q(t)$ are countable models of the complete theory of algebraically closed fields of characteristic $0$, so they are elementarily equivalent. They are not isomorphic, since their transcendence degrees over $\Q$ are $0$ and $1$.
- Elementary equivalence cannot be weakened to agreement on sentences of bounded quantifier depth. For each $k$, the linear orders with $2^k$ and $2^k + 1$ elements agree on all sentences of quantifier depth at most $k$, by the [[Ehrenfeucht-Fraïssé game|2RE7YAZK8R]], and they are not isomorphic.

### Consequences

- A finite structure in a finite signature is described up to isomorphism by one sentence, its diagram sentence from step 2 of the proof.
- The theory of a finite structure has no models other than its isomorphic copies; in particular it has no infinite model.
- For finite structures, the [[theory of a structure|X9HV9C6X4F]] is a complete invariant: $\mathcal{M} \cong \mathcal{N}$ if and only if $\operatorname{Th}(\mathcal{M}) = \operatorname{Th}(\mathcal{N})$.

### Converse

The converse holds for all structures, finite or infinite: [[isomorphic structures are elementarily equivalent|NDTJ2E895C]].

### Generalizations

- The same proof works for many-sorted structures with finitely many elements in each sort.
- For infinite structures the analogue fails, and the [[Löwenheim-Skolem theorem|484M0TZ1S7]] shows that every infinite structure in a countable signature is elementarily equivalent to structures of every infinite cardinality.

## History

The fact belongs to the basic material of model theory and appears in the standard textbooks; we do not attribute it to a single author.

## Explanations

### L1 human

For finite structures, first-order logic sees everything.
If two finite structures answer every first-order question in the same way, they are copies of each other.
The reason is that one long sentence can list all the elements of a finite structure and everything about them.

### L2 human

We apply the theorem to a cyclic group of order $4$, in the signature $\set{\cdot, e}$.

1. Let $\mathcal{N}$ be a group with $\mathcal{N} \equiv (\Z/4\Z, +, 0)$.
2. The sentence "there are exactly $4$ elements" holds in $\Z/4\Z$, so $\mathcal{N}$ has $4$ elements.
3. The sentence $\exists x \, \neg(x \cdot x = e)$ holds in $\Z/4\Z$ with $x = 1$, so $\mathcal{N}$ has an element $b$ with $b \cdot b \ne e$. The order of $b$ divides $4$ and is not $1$ or $2$, so it is $4$.
4. So $\mathcal{N}$ is cyclic of order $4$, which agrees with the theorem.

The typical use of the theorem is to show that two finite structures are not elementarily equivalent by showing that they are not isomorphic.
A trap is to try the same for infinite structures.

### L3 human

The proof for an infinite signature is a compactness argument in disguise: the sets of partial isomorphisms for finite subsignatures form an inverse system of nonempty finite sets, and its inverse limit is nonempty.
In finite model theory, elementary equivalence is too fine to be useful, since it is isomorphism.
The useful relations are agreement up to quantifier depth $k$, measured by the Ehrenfeucht-Fraïssé game, and agreement in finite-variable logics; see the sub-area on [[finite model theory|CBPS8B13S4]].
