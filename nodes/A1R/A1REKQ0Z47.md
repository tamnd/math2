---
tag: A1REKQ0Z47
kind: proof
name: Proof of Well-ordering theorem
msc: ["03E25"]
proves: 0N109NG5ZX
sources:
  - wikipedia: en:33458@r1344684772
    locator: Well-ordering theorem, section Proof of axiom of choice
    note: adopted
    mention: wikipedia://en/33458#G238
    sections: [Proof]
---

## Proof

The axiom of choice can be proven from the well-ordering theorem as follows.

To make a choice function for a collection of non-empty sets, $E$, take the union of the sets in $E$ and call it $X$. There exists a well-ordering of $X$; let $R$ be such an ordering. The function that to each set $S$ of $E$ associates the smallest element of $S$, as ordered by (the restriction to $S$ of) $R$, is a choice function for the collection $E$.

An essential point of this proof is that it involves only a single arbitrary choice, that of $R$; applying the well-ordering theorem to each member $S$ of $E$ separately would not work, since the theorem only asserts the existence of a well-ordering, and choosing for each $S$ a well-ordering would require just as many choices as simply choosing an element from each $S$.
