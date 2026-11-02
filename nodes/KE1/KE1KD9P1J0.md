---
tag: KE1KD9P1J0
kind: definition
name: Padé table
msc: [41A21, "30B70", "30E10"]
defines: MDM8F48X18
uses: [75XCD68557, 072W67KFYK, 0HFSFVMWQB]
sources:
  - url: https://en.wikipedia.org/wiki/Pad%C3%A9_table
---

## Definition

Let $f(z) = \sum_{k \ge 0} c_k z^k$ be a [[formal power series|072W67KFYK]] with complex coefficients.
For integers $m, n \ge 0$ let $[m/n]_f$ be the [[Padé approximant|75XCD68557]] of $f$ with numerator degree at most $m$ and denominator degree at most $n$.
The *Padé table* of $f$ is the doubly infinite array $\big([m/n]_f\big)_{m, n \ge 0}$.
The table is *normal* if no rational function occurs at two different positions $(m, n)$.

## Remarks

The column $n = 0$ consists of the [[Taylor polynomials|0HFSFVMWQB]] of $f$.
By a theorem of Padé, the positions where a given rational function occurs form a square block, possibly infinite.
Example: for $f = e^z$ the table is normal, and $[1/1]_f = (2 + z)/(2 - z)$.
Non-example of normality: for $f = 1/(1 - z) = \sum z^k$, one has $[m/n]_f = 1/(1 - z)$ for all $m \ge 0$ and $n \ge 1$, since $(1 - z) f - 1 = 0$; so this table is not normal.
Orientation conventions differ: some authors put $m$ along rows and $n$ along columns, others the reverse.
