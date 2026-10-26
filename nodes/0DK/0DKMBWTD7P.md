---
tag: 0DKMBWTD7P
kind: statement
role: proposition
name: Cosets have the same cardinality as the subgroup
msc: [20A05]
uses: [05FD317V2W, 060Z37VVB6]
sources:
  - url: https://en.wikipedia.org/wiki/Coset
    locator: Properties
---

## Statement

Let $G$ be a [[group|G5S1M9]], let $H$ be a [[subgroup|0X1JXT47GA]] of $G$, and let $g \in G$.
Then the map $h \mapsto gh$ is a bijection from $H$ to the [[left coset|03DEH43F4H]] $gH$. The map $h \mapsto hg$ is a bijection from $H$ to the [[right coset|0NE1DK7H4T]] $Hg$.
In particular, $|gH| = |Hg| = |H|$.

## Remarks

The inverse of $h \mapsto gh$ is $x \mapsto g^{-1}x$.
This fact and the partition of $G$ into left cosets give the proof of [[Lagrange's theorem|3C53TD]].

## Explanations

### L1 human

Multiplying by a fixed element never makes two different elements equal, by cancellation.
Thus a coset has exactly as many elements as the subgroup.
All cosets of a subgroup have the same size.
