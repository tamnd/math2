---
tag: 7B53ZGXXEQ
kind: concept
name: Brouwer–Heyting–Kolmogorov interpretation
msc: ["03F55", "03B20"]
uses: [Q11N8X99FK, G958EQ8CWW]
sources:
  - url: https://en.wikipedia.org/wiki/Brouwer–Heyting–Kolmogorov_interpretation
same_as:
  wikidata: Q3153567
  wikipedia: Brouwer–Heyting–Kolmogorov interpretation
---

## Summary

The Brouwer–Heyting–Kolmogorov interpretation, or BHK interpretation, explains the meaning of the logical connectives in [[intuitionistic logic|Q11N8X99FK]].
It says what counts as a proof of a compound statement in terms of proofs of its parts.
It is an informal explanation, not a formal semantics, and it expresses the view of [[constructivism|G958EQ8CWW]].
Realizability and the Curry–Howard correspondence are precise versions of it.

## Explanations

### L1 human

In classical logic, a statement is true or false, and the connectives act on truth values.
In the BHK interpretation, one asks instead what a proof of the statement is.
A proof of "$A$ and $B$" is a pair of proofs, one for each.
A proof of "if $A$ then $B$" is a method that turns each proof of $A$ into a proof of $B$.
So a proof of "$A$ or not $A$" would have to decide which one holds, and in general no such method is known.
