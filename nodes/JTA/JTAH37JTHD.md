---
tag: JTAH37JTHD
kind: concept
name: Many-one reduction
msc: [03D30]
sources:
  - url: https://en.wikipedia.org/wiki/Many-one_reduction
same_as:
  wikidata: Q3300648
  wikipedia: Many-one reduction
---

## Summary

A many-one reduction from a set $A$ to a set $B$ of natural numbers is a total [[computable function|KZSB5E471K]] $f$ with $x \in A$ exactly when $f(x) \in B$.
It turns every question about membership in $A$ into one question about membership in $B$.
Many-one reductions compare how hard decision problems are, and they are the standard tool for proving that a problem is undecidable.

## Explanations

### L1 human

Think of $f$ as a translator: it rewrites each question about $A$ as a question about $B$ with the same answer.
If someone could answer questions about $B$, they could then answer questions about $A$.
So $A$ is at most as hard as $B$.
For example, the set of even numbers reduces to the set $\set{0}$ by sending each even number to $0$ and each odd number to $1$.
