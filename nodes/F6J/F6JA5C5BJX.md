---
tag: F6JA5C5BJX
kind: concept
name: Computation tree logic
msc: [03B44, 68Q60, 03B70]
specializes: [C3RZY20ETK]
sources:
  - url: https://en.wikipedia.org/wiki/Computation_tree_logic
same_as:
  wikidata: Q1040040
  wikipedia: Computation tree logic
---

## Summary

Computation tree logic (CTL) is a branching-time temporal logic.
Its formulas are evaluated at states of a [[Kripke structure|NGHWZ9Y7ZV]].
Each temporal operator is paired with a path quantifier: $E$ ("along some path") or $A$ ("along all paths").
CTL can be model checked in time linear in the size of the structure and of the formula.
This made it a basis of [[model checking|VNY0VXVZ53]].
Its expressive power is incomparable with that of [[linear temporal logic|RMJ56ZPA63]].

## Explanations

### L1 human

From a given state, a system may evolve in many ways, and these futures form a branching tree.
CTL lets you speak about this tree.
"$EF\,\mathit{done}$" says that some future reaches a finished state.
"$AG\,\mathit{safe}$" says that every future stays safe forever.
"$AG\,EF\,\mathit{reset}$" says that from every reachable state, a reset is still possible.
