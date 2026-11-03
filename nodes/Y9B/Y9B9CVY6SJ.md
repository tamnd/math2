---
tag: Y9B9CVY6SJ
kind: concept
name: Beta reduction
msc: [03B40, 68N18]
sources:
  - url: https://en.wikipedia.org/wiki/Lambda_calculus
    locator: β-reduction
---

## Summary

Beta reduction is the computation rule of the [[lambda calculus|BD756KR8FM]].
It replaces a function applied to an argument, $(\lambda x.\, M)\, N$, by the body $M$ with $N$ substituted for $x$.
Every computation in the untyped lambda calculus is a sequence of such steps.
Its basic properties, confluence and normalization, are the subject of the [[Church–Rosser theorem|7NNF74EYDX]] and of [[normal forms|FPD6AN79QX]].

## Explanations

### L1 human

Beta reduction is "plugging in the argument".
The term $\lambda x.\, x + 1$ is the function that adds one, and applying it to $5$ gives $(\lambda x.\, x + 1)\, 5$.
One beta step turns this into $5 + 1$.
In the pure lambda calculus there are no numbers, but the rule is the same: wherever a function meets its argument, substitute.
A term can contain several such places, and one may reduce them in any order.
