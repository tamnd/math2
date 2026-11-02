---
tag: ZT01G7BTSV
kind: concept
name: L-infinity space
msc: ["46E30"]
specializes: [SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/L-infinity
same_as:
  wikidata: Q25109715
  wikipedia: L-infinity
---

## Summary

The space $L^\infty(\mu)$ consists of the essentially bounded measurable functions on a measure space, up to equality almost everywhere.
Its norm is the [[essential supremum|WPC2XRMB9Y]] of the absolute value.
It is the case $p = \infty$ of the [[Lp spaces|SASP14MA1Z]] and is a Banach space.
For a $\sigma$-finite measure it is the dual of $L^1(\mu)$.

## Explanations

### L1 human

A function lies in $L^\infty$ when it is bounded once one ignores a set of measure zero.
The norm is the smallest bound that holds outside such a set.
For example, the function on $\R$ equal to $\sin x$ at irrational $x$ and to $x$ at rational $x$ is unbounded, but its $L^\infty$ norm is $1$.
With the counting measure on $\N$ one gets the space $\ell^\infty$ of bounded sequences.
