---
tag: PJA5H9ZW4S
kind: definition
name: Lifting idempotents
msc: [16U40, 16L30]
defines: 2SRDN8EJG3
uses: [0894J980RK, 0DDA6CY7GJ, 0X4JKZXJ86]
sources:
  - url: https://en.wikipedia.org/wiki/Idempotent_(ring_theory)
---

## Definition

Let $R$ be a [[ring|0894J980RK]] and $I$ a [[two-sided ideal|0DDA6CY7GJ]] of $R$.
An [[idempotent|0X4JKZXJ86]] $x + I$ of $R/I$ *lifts* to $R$ if there is $e \in R$ with $e^2 = e$ and $e - x \in I$.
*Idempotents lift modulo $I$* if every idempotent of $R/I$ lifts, that is, for every $x \in R$ with $x^2 - x \in I$ there is $e \in R$ with $e^2 = e$ and $e - x \in I$.

## Remarks

Example: idempotents lift modulo $I = 4\Z/8\Z$ in $R = \Z/8\Z$.
The idempotents of $R/I \cong \Z/4\Z$ are $0$ and $1$, and they lift to the idempotents $0$ and $1$ of $R$.
Non-example: idempotents do not lift modulo $6\Z$ in $\Z$.
The class of $3$ is idempotent in $\Z/6\Z$, since $9 - 3 = 6$, but the idempotents of $\Z$ are $0$ and $1$, and neither $3 - 0$ nor $3 - 1$ lies in $6\Z$.
Idempotents lift modulo every nil ideal, and modulo every ideal of a ring that is complete with respect to the $I$-adic topology.
A semilocal ring in which idempotents lift modulo the Jacobson radical is called [[semiperfect|ZRC2S3ECFK]].
