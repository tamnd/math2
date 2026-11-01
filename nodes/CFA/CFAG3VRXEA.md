---
tag: CFAG3VRXEA
kind: concept
name: Group homology
msc: [20J06, 20J05]
sources:
  - url: https://en.wikipedia.org/wiki/Group_cohomology
---

## Summary

Group homology attaches to a [[group|G5S1M9]] $G$ and a $G$-module $M$ a sequence of abelian groups $H_n(G, M)$, for $n \ge 0$.
It is defined with the [[Tor functors|DDQRERAQCV]] over the group ring $\Z[G]$, and it is dual to group cohomology.
In low degrees it has concrete meaning: $H_1(G, \Z)$ is the abelianization of $G$, and $H_2(G, \Z)$ is given by [[Hopf's formula|S31M1ZYJRK]].
Topologically, $H_n(G, \Z)$ is the singular homology of a [[classifying space|WA796ZCNRX]] of $G$.

## Explanations

### L1 human

Group homology is a list of abelian groups, one for each degree, that record algebraic information about a group.
The first homology group records what is left of the group when every two elements are forced to commute.
For the integers $\Z$, the first homology is $\Z$ and all higher ones vanish, matching the circle, whose loops are counted by $\Z$.
For the group $\Z^2$, the second homology is $\Z$, matching the single two-dimensional hole of the torus.
