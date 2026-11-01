---
tag: 7PEE48WBQF
kind: concept
name: Combinatorial species
msc: [05A15, 18B99]
sources:
  - url: https://en.wikipedia.org/wiki/Combinatorial_species
same_as:
  wikidata: Q4457949
  wikipedia: Combinatorial species
---

## Summary

A combinatorial species is a rule that assigns to each finite set the structures of a given kind on it, see the [[definition|K9VZKJACKT]].
The rule must be compatible with renaming the elements, which makes it a functor on finite sets and bijections.
Each species has an [[exponential generating function|0JHXPVFKT0]], and operations on species match operations on these series.
The theory was introduced by André Joyal and gives a conceptual basis for the [[symbolic method|JP11D90EJC]] for labelled structures.

## Explanations

### L1 human

Think of a kind of structure, such as "a linear order", "a graph" or "a rooted tree", that you can put on any set of labels.
The species records, for each set of labels, all such structures on it.
Renaming the labels moves structures to structures, in a consistent way.
For example, the species of linear orders gives $n!$ structures on a set of $n$ labels, and the species of graphs gives $2^{\binom{n}{2}}$.
