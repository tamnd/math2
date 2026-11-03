---
tag: C1ETR2KJKY
kind: statement
role: theorem
name: Boole's expansion theorem
msc: [94C11, "06E30"]
uses: [0X05GS525E]
about: [0X05GS525E]
sources:
  - url: https://en.wikipedia.org/wiki/Boole%27s_expansion_theorem
same_as:
  wikidata: Q2277040
  wikipedia: Boole's expansion theorem
---

## Statement

Let $n \ge 1$ and let $f \colon \set{0,1}^n \to \set{0,1}$ be a [[Boolean function|0X05GS525E]].
Then for all $x_1, \dots, x_n \in \set{0,1}$,
$$f(x_1, x_2, \dots, x_n) = \big(x_1 \wedge f(1, x_2, \dots, x_n)\big) \vee \big(\neg x_1 \wedge f(0, x_2, \dots, x_n)\big).$$

## Remarks

The proof is a check of the two cases: for $x_1 = 1$ the right side reduces to $f(1, x_2, \dots, x_n)$, and for $x_1 = 0$ it reduces to $f(0, x_2, \dots, x_n)$.
The functions $f(1, \cdot)$ and $f(0, \cdot)$ are the positive and negative cofactors of $f$ with respect to $x_1$.
The two terms are never true together, so $\vee$ may be replaced by exclusive or.
Example: for the majority function $f(x, y, z) = (x \wedge y) \vee (x \wedge z) \vee (y \wedge z)$, the cofactors are $y \vee z$ and $y \wedge z$, so $f = (x \wedge (y \vee z)) \vee (\neg x \wedge (y \wedge z))$.
Expanding on all variables in turn gives the full [[disjunctive normal form|0GVDFAY4KW]] of $f$.
The same identity holds for Boolean polynomials over any Boolean algebra.

## Explanations

### L1 human

To understand a logical function, split into two cases: the first input is true, or it is false.
In each case you get a simpler function of the remaining inputs, and the original function picks the right one.
This is how a two-way switch, a multiplexer, works.

### L2 human

The expansion is often called the Shannon expansion, after its use by Claude Shannon in switching circuits.
Applied recursively in a fixed variable order and with shared subresults, it gives binary decision diagrams.
It also underlies the case splitting in algorithms for the [[Boolean satisfiability problem|3QKF32ZAKN]].
