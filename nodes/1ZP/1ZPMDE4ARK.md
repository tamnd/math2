---
tag: 1ZPMDE4ARK
kind: concept
name: Split exact sequence
msc: [18G35, "18E10"]
specializes: [KJKNJMGKZZ]
sources:
  - url: https://en.wikipedia.org/wiki/Split_exact_sequence
same_as:
  wikidata: Q65122157
  wikipedia: Split exact sequence
---

## Summary

A split exact sequence is a [[short exact sequence|KJKNJMGKZZ]] $0 \to A \to B \to C \to 0$ in which the middle object is the [[biproduct|BZEJKTQ76T]] $A \oplus C$, compatibly with the two maps.
These are the trivial extensions: $B$ is just $A$ and $C$ placed side by side.
By the [[splitting lemma|7ZGQKWYKQS]], a short exact sequence splits as soon as one of its two maps has a one-sided inverse.

## Explanations

### L1 human

Every short exact sequence builds $B$ from a piece $A$ and a quotient $C$.
In a split sequence the gluing is trivial, and $B$ is simply the direct sum of $A$ and $C$.
For example, $0 \to \Z \to \Z \oplus \Z/2\Z \to \Z/2\Z \to 0$ is split.
The sequence $0 \to \Z \xrightarrow{2} \Z \to \Z/2\Z \to 0$ is not, since $\Z$ is not $\Z \oplus \Z/2\Z$.
Over a field every short exact sequence of vector spaces splits, which is why linear algebra has no interesting extensions.
