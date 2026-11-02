---
tag: DW7FG506QJ
kind: concept
name: Validated numerics
msc: [65G20, 65G30, 65G40]
sources:
  - url: https://en.wikipedia.org/wiki/Validated_numerics
same_as:
  wikidata: Q63307393
  wikipedia: Validated numerics
---

## Summary

Validated numerics, also called verified or rigorous computation, is numerical computation whose output comes with a mathematical guarantee.
Instead of a single approximate number, it returns a set, usually an interval or a box, that provably contains the exact answer.
All [[round-off errors|CPN6SD3BTV]] and [[truncation errors|4AKCQERM89]] are bounded, typically with [[interval arithmetic|QPKKTE1ZY0]] or [[affine arithmetic|YPE8E9CVXP]] and directed rounding.
Its results can serve as steps of a proof; an example is Warwick Tucker's computer-assisted proof that the Lorenz attractor exists.

## Explanations

### L1 human

An ordinary numerical program says "the answer is about $1.41421$" and hopes the digits are right.
A validated program says "the answer lies between $1.414213$ and $1.414214$", and this claim is certain, rounding errors included.
It does this by computing with intervals and by rounding lower bounds down and upper bounds up.
Such enclosures can turn a computer calculation into part of a mathematical proof.
