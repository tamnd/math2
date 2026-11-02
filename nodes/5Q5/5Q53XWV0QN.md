---
tag: 5Q53XWV0QN
kind: concept
name: De Morgan algebra
msc: ["06D30"]
specializes: [0HM0HQCK6N]
sources:
  - url: https://en.wikipedia.org/wiki/De_Morgan_algebra
same_as:
  wikidata: Q5244640
  wikipedia: De Morgan algebra
---

## Summary

A De Morgan algebra is a bounded [[distributive lattice|0HM0HQCK6N]] with a negation $\sim$ that is an involution and satisfies [[De Morgan's laws|09PKJKA6J0]].
Unlike the complement of a [[Boolean algebra|0XADJKM699]], this negation need not satisfy $a \wedge {\sim} a = 0$ or $a \vee {\sim} a = 1$.
De Morgan algebras give the algebraic semantics of several many-valued and relevance logics.
Every Boolean algebra is a De Morgan algebra.

## Explanations

### L1 human

Take the numbers from $0$ to $1$ as degrees of truth, with "and" as the minimum, "or" as the maximum, and "not $x$" as $1 - x$.
This negation turns "and" into "or" and back, and doing it twice gives the start again.
But the statement "$x$ and not $x$" need not be fully false: for $x = 1/2$ it has truth degree $1/2$.
A De Morgan algebra keeps these rules of negation and drops the laws $x \wedge {\sim} x = 0$ and $x \vee {\sim} x = 1$.
