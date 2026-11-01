---
tag: AK1ZRCXR32
kind: concept
name: Noetherian module
msc: ["13E05", "16P40"]
specializes: [0NZ8JA25WK]
sources:
  - url: https://en.wikipedia.org/wiki/Noetherian_module
same_as:
  wikidata: Q2444982
  wikipedia: Noetherian module
---

## Summary

A Noetherian module is a module in which every increasing chain of submodules stops after finitely many steps.
Equivalently, every submodule is finitely generated.
A ring is a [[Noetherian ring|0670T59HGE]] exactly when it is a Noetherian module over itself.
This finiteness condition makes induction arguments work and underlies most of commutative algebra.

## Explanations

### L1 human

Think of building bigger and bigger submodules, one step at a time.
In a Noetherian module you cannot keep growing forever: the chain must become constant.
For example, in $\Z$ seen as a module over itself, the chain $(12) \subset (6) \subset (3) \subset \Z$ cannot be made infinitely long upward.
By contrast, in $\Q$ seen as a $\Z$-module, the chain $\Z \subset \frac{1}{2}\Z \subset \frac{1}{4}\Z \subset \cdots$ goes on forever.
