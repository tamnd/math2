---
tag: 8MGH8PGJWR
kind: definition
name: Total ring of fractions
msc: [13B30]
defines: K5Z67HR9ET
uses: [0310REJJY8, 0NNRDW10RZ, AN9SKEZ3VY, 4C1AE84N5N]
sources:
  - url: https://en.wikipedia.org/wiki/Total_ring_of_fractions
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $S$ be the set of elements of $R$ that are not [[zero divisors|0NNRDW10RZ]].
So $s \in S$ means: $sa = 0$ implies $a = 0$, for all $a \in R$.
Then $S$ is a [[multiplicative set|AN9SKEZ3VY]].
The *total ring of fractions* of $R$ is the [[localization|4C1AE84N5N]]
$$Q(R) = S^{-1}R.$$

## Remarks

The canonical map $R \to Q(R)$, $a \mapsto a/1$, is injective, because no element of $S$ kills a nonzero element.
If $S'$ is a multiplicative set and $R \to S'^{-1}R$ is injective, then $S' \subseteq S$.

Example: if $R$ is an [[integral domain|0QVD7WBFGN]], then $S = R \setminus \set{0}$ and $Q(R)$ is the [[field of fractions|0F2PTGX1A2]] of $R$.
For $R = \Z \times \Z$, the non-zero-divisors are the pairs $(a, b)$ with $a \ne 0$ and $b \ne 0$, and $Q(R) \cong \Q \times \Q$.
For $R = \Z/6\Z$, the non-zero-divisors are $1$ and $5$, which are already units, so $Q(R) = R$.

Non-example: in $R = \Z \times \Z$, the set $T = \set{(1,0)^n : n \ge 0} = \set{(1,1), (1,0)}$ is multiplicative, but $(1, 0)$ is a zero divisor.
The localization $T^{-1}R \cong \Z$ is not the total ring of fractions, and $R \to T^{-1}R$ kills $(0, 1)$.
