---
tag: GMY8XWETFV
kind: definition
name: Risch algorithm
msc: [68W30, 12H05, 33F10]
defines: VJ51B7J125
uses: [GA5PTQGC6G, 3J89REV9WQ, 0BYWRWFT4F, 8VRTPECBPZ]
sources:
  - url: https://en.wikipedia.org/wiki/Risch_algorithm
---

## Definition

Let $C$ be a field of characteristic $0$ in which the field operations and the test for equality are computable.
Let $F = C(x)(t_1, \dots, t_m)$ be a [[differential field|GA5PTQGC6G]] with [[derivation|3J89REV9WQ]] $'$ such that $x' = 1$ and the constants of $F$ are $C$.
Assume that each $t_i$ is a logarithm, an exponential or an algebraic element over $C(x)(t_1, \dots, t_{i-1})$.
The *Risch algorithm* is the procedure that takes $f \in F$ as input and does one of two things:

1. it returns an element $g$ of an elementary extension of $F$ with $g' = f$, that is, an elementary [[antiderivative|0BYWRWFT4F]] of $f$;
2. it reports, correctly, that no elementary extension of $F$ contains such an element $g$.

## Remarks

The procedure works down the tower.
It writes $f$ in terms of the last generator $t_m$ and uses [[Liouville's theorem|8VRTPECBPZ]] to predict the form of a possible antiderivative.
This reduces the problem to integration and to differential equations in the smaller field $C(x)(t_1, \dots, t_{m-1})$.
The cases of logarithms and exponentials (the transcendental case) are simpler than the algebraic case.

Example: for $F = \Q(x, e^x)$ and $f = x e^x$, the procedure looks for $g = q e^x$ with $q \in \Q(x)$ and $q' + q = x$, finds $q = x - 1$, and returns $g = (x - 1) e^x$.

Example: for $F = \Q(x, e^{x^2})$ and $f = e^{x^2}$, the same reduction asks for $q \in \Q(x)$ with $q' + 2x q = 1$; there is none, so the procedure reports that $e^{x^2}$ has no elementary antiderivative.

Non-example: a table of integrals finds many antiderivatives, but it fails clause 2, because it cannot certify that an integral not in the table is not elementary.

The algorithm needs a way to decide whether a constant expression equals $0$.
For constants built from $\pi$, $e$ and other transcendental numbers this is a hard problem, so in practice the algorithm is only as complete as the zero test for constants.
