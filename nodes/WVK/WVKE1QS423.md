---
tag: WVKE1QS423
kind: definition
name: Bézout domain
msc: [13F05, 13G05]
defines: HGEX40P0Z0
uses: [09S3PFBEPM, 0MYSA6MYNA, 00A2EDFT9Q]
sources:
  - url: https://en.wikipedia.org/wiki/B%C3%A9zout_domain
---

## Definition

Let $R$ be an [[integral domain|09S3PFBEPM]].
$R$ is a *Bézout domain* if every finitely generated [[ideal|0MYSA6MYNA]] of $R$ is [[principal|00A2EDFT9Q]].

## Remarks

Equivalent form: for all $a, b \in R$ the ideal $(a, b)$ is principal; the general case follows by induction on the number of generators.
Then $(a, b) = (d)$ for a gcd $d$ of $a$ and $b$, and $d = ax + by$ for some $x, y \in R$.
Example: every [[principal ideal domain|0RZYDVZ475]], such as $\Z$ or $\Q[x]$, is a Bézout domain.
Non-example: in $\Z[x]$ the ideal $(2, x)$ is not principal.
A generator would divide $2$, so it would be $\pm 1$ or $\pm 2$.
But $(2, x) \ne \Z[x]$, because its elements have even constant term, and $2$ does not divide $x$.
A Bézout domain is a [[GCD domain|ACDEK1GD9G]]; a Noetherian Bézout domain is a principal ideal domain.
