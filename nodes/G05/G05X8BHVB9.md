---
tag: G05X8BHVB9
kind: definition
name: Ideal quotient
msc: [13A15]
defines: 16J9DM8V57
uses: [0GYGHKX834, 0MYSA6MYNA]
sources:
  - url: https://en.wikipedia.org/wiki/Ideal_quotient
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]] and let $I$ and $J$ be [[ideals|0MYSA6MYNA]] of $R$.
The *ideal quotient* of $I$ by $J$ is the set
$$(I : J) = \set{r \in R : rj \in I \text{ for all } j \in J}.$$

## Remarks

$(I : J)$ is an ideal of $R$ and $I \subseteq (I : J)$.
Example: in $\Z$, $(12\Z : 4\Z) = 3\Z$; for $r \in \Z$, $4r \in 12\Z$ holds exactly when $3 \mid r$, and then $rj \in 12\Z$ for every multiple $j$ of $4$.
Non-example: $1 \notin (12\Z : 4\Z)$, since $1 \cdot 4 = 4 \notin 12\Z$.
If $J \subseteq I$, then $(I : J) = R$.
The quotient $(0 : J)$ is the [[annihilator|HB4XDKJTW8]] of $J$.
Other notations are $I : J$ and $(I :_R J)$; the name *colon ideal* is also used.
