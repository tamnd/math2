---
tag: WFG4YMBYVQ
kind: concept
name: Hilbert symbol
msc: [11S31, "11E08"]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_symbol
same_as:
  wikidata: Q740060
  wikipedia: Hilbert symbol
---

## Summary

The Hilbert symbol $(a, b)_K$ of two nonzero elements of a [[local field|J85FZEQG38]] $K$ of characteristic other than $2$ is $1$ or $-1$.
It is $1$ exactly when the equation $z^2 = a x^2 + b y^2$ has a solution other than $(0, 0, 0)$.
It is symmetric and bimultiplicative, and it is a basic tool for [[quadratic forms|0RBQS1JJCR]] over local fields.
Over $\Q$, the product of all local Hilbert symbols is $1$, a statement equivalent to [[quadratic reciprocity|085MJS6907]].

## Explanations

### L1 human

The Hilbert symbol answers a yes-or-no question: does a certain quadratic equation have a nonzero solution in the field?
Over the real numbers, $z^2 = a x^2 + b y^2$ has a nonzero solution unless both $a$ and $b$ are negative.
So $(a, b)_\R = -1$ exactly when $a < 0$ and $b < 0$.
Over $\Q_p$ the answer depends on [[Legendre symbols|0JTC045NNZ]] modulo $p$, and it can be computed by a short formula.
