---
tag: KF719SZD5T
kind: concept
name: Additive function
msc: [39B22, 39B52]
specializes: [0JYTG5K9Y4]
sources:
  - url: https://en.wikipedia.org/wiki/Additive_map
same_as:
  wikidata: Q22963169
  wikipedia: Additive map
---

## Summary

An additive function is a function $f$ with $f(x + y) = f(x) + f(y)$ for all $x$ and $y$, that is, a solution of [[Cauchy's functional equation|ZBMEVWN100]].
Between abelian groups it is the same thing as a [[group homomorphism|0JYTG5K9Y4]].
Every linear map is additive, and on the real line the continuous additive functions are exactly $x \mapsto cx$.
With the axiom of choice there are also wild additive functions on $\R$ whose graphs are dense in the plane.
In number theory the phrase "additive function" has another meaning, for arithmetic functions with $f(mn) = f(m) + f(n)$ when $m$ and $n$ are coprime.

## Explanations

### L1 human

An additive function turns sums into sums: the output for $x + y$ is the output for $x$ plus the output for $y$.
Doubling, $f(x) = 2x$, is additive, because $2(x + y) = 2x + 2y$.
Squaring is not, because $(x + y)^2$ is not $x^2 + y^2$ in general.
Adding a constant is not either: $f(x) = x + 1$ gives $f(0 + 0) = 1$ but $f(0) + f(0) = 2$.
