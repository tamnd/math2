---
tag: T440VB9JJM
kind: definition
name: Primal algebra
msc: [08A40]
defines: XD01Y7B6XW
uses: [TDZVCWYJ9F, N9M2N27END, 070R982G4B, QWSBDFM47K]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_completeness
---

## Definition

Let $A$ be an algebra whose universe is a [[finite set|070R982G4B]] with at least two elements.
The algebra $A$ is *primal* if every operation $f \colon A^n \to A$ with $n \ge 1$ is a [[term operation|N9M2N27END]] of $A$.
Equivalently, the set of basic operations of $A$ is [[functionally complete|TDZVCWYJ9F]].

## Remarks

Example: the ring $(\Z_p, +, \cdot, -, 0, 1)$ for a prime $p$ is primal.
Check: the polynomial $\delta(x) = 1 - x^{p - 1}$ equals $1$ at $0$ and $0$ elsewhere, by Fermat's little theorem.
Then $f(a_1, \dots, a_n) = \sum_{b \in \Z_p^n} f(b) \prod_{i} \delta(a_i - b_i)$, and each $f(b)$ is a sum of copies of $1$.
Non-example: the field $\F_4$ with its ring operations is not primal.
Its Frobenius map $x \mapsto x^2$ is an automorphism, and term operations commute with automorphisms.
A constant operation with value outside $\F_2$ does not commute with it, so it is not a term operation.
Every primal algebra is [[quasi-primal|QWSBDFM47K]].
