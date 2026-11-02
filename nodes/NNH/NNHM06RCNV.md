---
tag: NNHM06RCNV
kind: definition
name: Approximation theory
msc: [41A65, 41A10, 41A50]
defines: YPJSH79SHQ
uses: [03J5RAKB30, VNWH2KADN7, 7N4988HN3P, YDN0T4MEX0]
sources:
  - url: https://en.wikipedia.org/wiki/Approximation_theory
---

## Definition

Let $X$ be a [[normed vector space|03J5RAKB30]] of functions, and let $A_0 \subseteq A_1 \subseteq A_2 \subseteq \cdots$ be nonempty subsets of $X$, the approximating classes.
*Approximation theory* is the study of the following questions for $f \in X$.

1. Existence: does $f$ have a [[best approximation|7N4988HN3P]] from $A_n$?
2. Uniqueness and characterization: is it unique, and which conditions single it out?
3. Rates: how fast does the [[error of best approximation|YDN0T4MEX0]] $E(f, A_n)$ tend to $0$ as $n \to \infty$, and how does this rate depend on $f$?
4. Construction: which explicit methods give good [[approximations|VNWH2KADN7]] of $f$ from $A_n$?

## Remarks

Example: $X = C[a, b]$ with the supremum norm and $A_n$ the polynomials of degree at most $n$.
Here a best approximation exists and is unique, it is characterized by the equioscillation theorem, and $E(f, A_n) \to 0$ for every $f$ by the Weierstrass approximation theorem.

Non-example: a single numerical estimate, such as $\abs{e^x - (1 + x)} \le 1$ on $[0, 1]$, is an approximation result but does not by itself pose these questions.
The theory studies whole families $A_n$ and all $f$ in a class.

Other common choices are trigonometric polynomials, splines with $n$ knots, rational functions of degree $n$, and $L^p$ norms instead of the supremum norm.
