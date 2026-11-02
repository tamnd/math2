---
tag: K02CEYQBCX
kind: definition
name: Distinguished boundary of a polydisc
msc: [32A10, 32A26]
defines: A6HN207Y2T
uses: [DJBWP7D3M8, 060W5CBZP6]
sources:
  - url: https://en.wikipedia.org/wiki/Polydisc
---

## Definition

Let $P(a, r)$ be the [[polydisc|DJBWP7D3M8]] in $\C^n$ with centre $a = (a_1, \dots, a_n)$ and polyradius $r = (r_1, \dots, r_n)$, each $r_j > 0$.
Its *distinguished boundary* is the set
$$T(a, r) = \set{z \in \C^n : \abs{z_j - a_j} = r_j \text{ for } j = 1, \dots, n}.$$

## Remarks

The set $T(a, r)$ is the product of the $n$ [[circles|060W5CBZP6]] $\abs{z_j - a_j} = r_j$, so it is a real torus of dimension $n$.
It is also called the *skeleton* of the polydisc, and it is written $\partial_0 P(a, r)$ in some texts.
Example: $(1, -i)$ lies in the distinguished boundary of the unit polydisc of $\C^2$, since $\abs{1} = 1$ and $\abs{-i} = 1$.
Non-example: $(1, 0)$ lies in the topological boundary of the unit polydisc but not in its distinguished boundary, since $\abs{0} \ne 1$.
For $n = 1$ the distinguished boundary is the whole boundary circle.
If $f$ is continuous on the closed polydisc and holomorphic on $P(a, r)$, then $\max \abs{f}$ over the closed polydisc equals $\max \abs{f}$ over $T(a, r)$.
