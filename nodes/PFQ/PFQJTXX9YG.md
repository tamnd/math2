---
tag: PFQJTXX9YG
kind: definition
name: Contraction semigroup
msc: [47D06, 47D03]
defines: XPWE94BV6N
uses: [06GZ956657, EVF180QJXY, 06EKW1AKXF]
sources:
  - url: https://en.wikipedia.org/wiki/C0-semigroup
---

## Definition

Let $X$ be a [[Banach space|06GZ956657]].
A *contraction semigroup* on $X$ is a [[strongly continuous semigroup|EVF180QJXY]] $(T(t))_{t \ge 0}$ of bounded operators on $X$ such that
$$\norm{T(t)} \le 1 \quad \text{for all } t \ge 0,$$
where $\norm{\cdot}$ is the [[operator norm|06EKW1AKXF]].

## Remarks

Example: on $L^p(\R)$ with $1 \le p < \infty$, let $(T(t)f)(s) = f(s + t)$.
Each $T(t)$ preserves the $L^p$ norm, so $\norm{T(t)} = 1$, and $t \mapsto T(t)f$ is continuous for every $f$, so this is a contraction semigroup.

Non-example: on $\C$, the semigroup $T(t)z = e^{t}z$ is strongly continuous, but $\norm{T(t)} = e^{t} > 1$ for $t > 0$.

The [[generator|60HSWZBTK9]] of a contraction semigroup is [[dissipative|3S7HJ5GQRF]].
Some authors write $C_0$ contraction semigroup to stress strong continuity.
