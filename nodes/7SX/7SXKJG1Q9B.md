---
tag: 7SXKJG1Q9B
kind: concept
name: Direct limit of algebras
msc: [08B25, 18A30]
specializes: [X9HEQ29Q49]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_limit
---

## Summary

The direct limit of a directed system of [[algebras|QJGPT2W0FT]] is the algebra obtained by gluing the algebras of the system along its [[homomorphisms|KBXSZC6BV1]].
It is the [[direct limit|X9HEQ29Q49]] in the category of algebras of a fixed signature, and it is the union when the maps are inclusions.
Varieties are closed under direct limits, and every algebra is the direct limit of its finitely generated subalgebras.
The dual construction is the [[inverse limit of algebras|DE2KEQ85ZT]].

## Explanations

### L1 human

Imagine a growing sequence of algebras, each mapped into the next one.
The direct limit is what you get "at the end of the sequence".
An element lives in some stage, and two elements are equal if they become equal at some later stage.
For example, the groups $\Z/p\Z \to \Z/p^2\Z \to \Z/p^3\Z \to \cdots$, with each map $x \mapsto px$, have as direct limit the Prüfer $p$-group, the group of all complex roots of unity of $p$-power order.
The rationals $\Q$ under addition are the direct limit of the groups $\frac{1}{n!}\Z$, which is simply their union.
