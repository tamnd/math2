---
tag: MYY4EFGXVR
kind: definition
name: sl2 triple
msc: [17B05, 17B20]
defines: P1QPWKE7ZZ
uses: [5JJYBJ6A8K]
sources:
  - url: https://en.wikipedia.org/wiki/Representation_theory_of_SL2(R)
---

## Definition

Let $\mathfrak g$ be a [[Lie algebra|5JJYBJ6A8K]] over a field $k$.
An *$\mathfrak{sl}_2$-triple* in $\mathfrak g$ is a triple $(h, e, f)$ of elements of $\mathfrak g$ such that:

1. $h \ne 0$.
2. $[e, f] = h$.
3. $[h, e] = 2e$.
4. $[h, f] = -2f$.

## Remarks

Example: in $\mathfrak{sl}_2(k)$, take $e = E_{12}$, $h = E_{11} - E_{22}$ and $f = E_{21}$.
Then $[e, f] = E_{11} - E_{22} = h \ne 0$.
Also $he = E_{12}$ and $eh = -E_{12}$, so $[h, e] = 2e$; similarly $[h, f] = -2f$.

Non-example: $(h, e, 0)$ with $h \ne 0$ is never an $\mathfrak{sl}_2$-triple, since then $[e, f] = 0 \ne h$, so clause 2 fails.

If $(h, e, f)$ is an $\mathfrak{sl}_2$-triple, the linear map $\mathfrak{sl}_2(k) \to \mathfrak g$ sending the standard basis to $(h, e, f)$ is a Lie algebra homomorphism.
The element $e$ is called the nilpositive element and $f$ the nilnegative element of the triple.
Some authors list the triple as $(e, h, f)$.
