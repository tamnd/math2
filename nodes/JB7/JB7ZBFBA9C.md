---
tag: JB7ZBFBA9C
kind: concept
name: Exact sequence
msc: [18G35, 13D02, "18E10"]
sources:
  - url: https://en.wikipedia.org/wiki/Exact_sequence
same_as:
  wikidata: Q1326955
  wikipedia: Exact sequence
---

## Summary

An exact sequence is a chain of modules and linear maps in which the image of each map equals the [[kernel|0W88CEGQP1]] of the next.
Short exact sequences $0 \to A \to B \to C \to 0$ describe $B$ as built from a submodule $A$ and a quotient $C$.
Exact sequences are the language of homological algebra: one asks which functors, such as $\Hom$ and the [[tensor product|F0HQXQ0HCD]], preserve them.
The same notion makes sense for groups and in any abelian category.

## Explanations

### L1 human

An exact sequence is a row of modules connected by maps, where what one map produces is exactly what the next map kills.
So nothing is lost and nothing extra appears between two steps.
The basic example is $0 \to \Z \xrightarrow{2} \Z \to \Z/2\Z \to 0$.
Here multiplication by $2$ is injective, its image $2\Z$ is exactly the set of integers that become $0$ modulo $2$, and reduction modulo $2$ is onto.
