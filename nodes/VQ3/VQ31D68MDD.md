---
tag: VQ31D68MDD
kind: definition
name: Annihilator
msc: [13C99, 13A15]
defines: HB4XDKJTW8
uses: [0GYGHKX834, 09VDS2W1E8, 0MYSA6MYNA]
sources:
  - url: https://en.wikipedia.org/wiki/Annihilator_(ring_theory)
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]] and let $M$ be an $R$-[[module|09VDS2W1E8]].
The *annihilator* of $M$ is the set
$$\operatorname{Ann}_R(M) = \set{r \in R : rm = 0 \text{ for all } m \in M}.$$
For an element $m \in M$, the annihilator of $m$ is $\operatorname{Ann}_R(m) = \set{r \in R : rm = 0}$.

## Remarks

$\operatorname{Ann}_R(M)$ and $\operatorname{Ann}_R(m)$ are [[ideals|0MYSA6MYNA]] of $R$.
Example: $\operatorname{Ann}_\Z(\Z/6\Z) = 6\Z$; multiplication by $r$ kills the class of $1$ exactly when $6 \mid r$, and then it kills every class.
Non-example: $3 \notin \operatorname{Ann}_\Z(\Z/6\Z)$, since $3 \cdot 1 = 3 \ne 0$ in $\Z/6\Z$.
$M$ is a *faithful* module when $\operatorname{Ann}_R(M) = 0$.
For an ideal $J$ of $R$, the annihilator of the module $J$ is the [[ideal quotient|16J9DM8V57]] $(0 : J)$.
$M$ is naturally a module over $R/\operatorname{Ann}_R(M)$.
