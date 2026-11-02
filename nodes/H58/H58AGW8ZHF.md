---
tag: H58AGW8ZHF
kind: definition
name: Elementary equivalence
msc: [03C07]
defines: P3B1V182N4
uses: [983GZBQYT4, DKFGQTRYZE]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_equivalence
---

## Definition

Let $L$ be a signature and let $\mathcal{M}$ and $\mathcal{N}$ be $L$-[[structures|983GZBQYT4]].
The structures $\mathcal{M}$ and $\mathcal{N}$ are elementarily equivalent, written $\mathcal{M} \equiv \mathcal{N}$, when for every $L$-[[sentence|DKFGQTRYZE]] $\varphi$,
$$\mathcal{M} \models \varphi \iff \mathcal{N} \models \varphi.$$

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
It is weaker than isomorphism: by the [[Löwenheim–Skolem theorem|484M0TZ1S7]], an infinite structure in a countable signature is elementarily equivalent to structures of every infinite size.
