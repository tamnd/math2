---
tag: H58AGW8ZHF
kind: definition
name: Elementary equivalence
msc: ["03C07"]
topics: [AY09KYSW81]
audience: ug2
defines: P3B1V182N4
uses: [983GZBQYT4, DKFGQTRYZE]
formal:
  - system: lean4
    library: mathlib
    decl: FirstOrder.Language.ElementarilyEquivalent
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_equivalence
    locator: Elementarily equivalent structures
  - book: isbn:9780387987606
    locator: Chapter 1
---

## Definition

Let $L$ be a signature and let $\mathcal{M}$ and $\mathcal{N}$ be $L$-[[structures|983GZBQYT4]].
The structures $\mathcal{M}$ and $\mathcal{N}$ are elementarily equivalent, written $\mathcal{M} \equiv \mathcal{N}$, when for every $L$-[[sentence|DKFGQTRYZE]] $\varphi$,
$$\mathcal{M} \models \varphi \iff \mathcal{N} \models \varphi.$$

## Notation

Mathlib states the relation as `L.ElementarilyEquivalent M N`, with the notation `M ≅[L] N`, and defines it as equality of the complete theories of $M$ and $N$.

## Remarks

Equivalently, $\mathcal{M} \equiv \mathcal{N}$ when $\mathrm{Th}(\mathcal{M}) = \mathrm{Th}(\mathcal{N})$, where $\mathrm{Th}$ is the set of sentences true in a structure.

Example: $(\Q, <) \equiv (\R, <)$.
Both are dense linear orders without endpoints, and the theory of dense linear orders without endpoints is complete.

Non-example: $(\Z, <) \not\equiv (\Q, <)$.
The sentence $\forall x \, \forall y \, (x < y \to \exists z \, (x < z \land z < y))$ is true in $(\Q, <)$ and false in $(\Z, <)$, with $x = 0$ and $y = 1$.

Isomorphic structures are elementarily equivalent.
The example shows that the converse fails, since $\Q$ and $\R$ have different cardinalities.

## Explanations

### L1 human

Elementary equivalence says that first-order logic cannot tell two structures apart.
It is weaker than isomorphism: by the [[Löwenheim-Skolem theorem|484M0TZ1S7]], an infinite structure in a countable signature is elementarily equivalent to structures of every infinite size.

### L2 human

We check that $(\N, <) \not\equiv (\Z, <)$.

1. Let $\sigma = \exists x \, \forall y \, \neg(y < x)$, "there is a least element".
2. In $\N$, take $x = 0$: no natural number is less than $0$. So $(\N, <) \models \sigma$.
3. In $\Z$, for every $x$ the integer $y = x - 1$ satisfies $y < x$. So $(\Z, <) \models \neg\sigma$.

A trap is to argue from the fact that $(\N, <)$ is a substructure of $(\Z, <)$; substructures need not be elementarily equivalent to the larger structure.
