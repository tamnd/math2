---
tag: 6GACD52XKX
kind: definition
name: Generic point
msc: [14A15, 54D10]
defines: 3A19C4YXGE
uses: [0CQHFPGJ45, 0ZCK8DQYN1, 0QEAJB91GZ, 5A35TYZD02, 4N4DNDR22Z]
sources:
  - url: https://en.wikipedia.org/wiki/Generic_point
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]] and let $Z \subseteq X$ be a [[closed set|0ZCK8DQYN1]].
A point $\eta \in Z$ is a *generic point* of $Z$ if the [[closure|0QEAJB91GZ]] of $\set{\eta}$ is $Z$.
A generic point of $X$ is a generic point of the closed set $X$.

## Remarks

A closed set with a generic point is irreducible: it is not the union of two smaller closed sets.
In a [[scheme|5A35TYZD02]], every irreducible closed subset has a unique generic point, so the underlying space of a scheme is a [[sober space|4N4DNDR22Z]].
Example: in $X = \operatorname{Spec} \Z$, the closure of $\set{(0)}$ is $V(0) = X$, because $(0)$ is contained in every prime ideal.
So $(0)$ is the generic point of $X$.
Non-example: the point $(p)$, for a prime $p$, is not a generic point of $X$, since $\set{(p)}$ is already closed.
Non-example: $X$ itself has no generic point when $X = \operatorname{Spec} k[x, y]/(xy)$ for a field $k$, since $X$ is the union of the two lines $V(x)$ and $V(y)$.
