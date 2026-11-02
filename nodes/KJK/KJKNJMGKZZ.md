---
tag: KJKNJMGKZZ
kind: concept
name: Short exact sequence
msc: [18G35, "18E10"]
specializes: [JB7ZBFBA9C]
sources:
  - url: https://en.wikipedia.org/wiki/Exact_sequence
---

## Summary

A short exact sequence is an [[exact sequence|JB7ZBFBA9C]] $0 \to A \to B \to C \to 0$ whose first and last terms are zero.
It says that $A$ is a subobject of $B$ and that $C$ is the corresponding quotient $B/A$.
Short exact sequences are the basic input of homological algebra: functors are tested on them, and each gives a long exact sequence of derived functors.

## Explanations

### L1 human

A short exact sequence describes an object $B$ as built from a piece $A$ and what is left over, $C$.
The first map puts $A$ inside $B$ without collapsing anything.
The second map sends $B$ onto $C$ and kills exactly the copy of $A$.
For example, $0 \to \Z \xrightarrow{2} \Z \to \Z/2\Z \to 0$ shows the integers built from the even integers and the two classes "even" and "odd".
The middle object is not always the direct sum of the outer two, as this example shows.
