---
tag: NVVGA3KEWE
kind: concept
name: Associated bundle
msc: [55R10, 57R22]
specializes: [CX4M8K61AB]
sources:
  - url: https://en.wikipedia.org/wiki/Associated_bundle
same_as:
  wikidata: Q427018
  wikipedia: Associated bundle
---

## Summary

Let $P \to B$ be a [[principal bundle|8E37E74XVP]] with group $G$, and let $G$ act on a space $F$.
The associated bundle $P \times_G F$ is a [[fiber bundle|CX4M8K61AB]] over $B$ with fiber $F$.
It is built by gluing copies of $F$ along $B$ with the same twisting as $P$.
In this way one principal bundle produces many bundles: vector bundles, sphere bundles, bundles of frames and so on.
For example, the tangent bundle of a manifold is associated to its frame bundle through the action of $GL_n(\R)$ on $\R^n$.

## Explanations

### L1 human

A principal bundle records only how the fibers are twisted, by elements of a group, as one moves around the base.
An associated bundle uses this twisting recipe on another fiber, any space on which the group acts.
For example, the circle double cover $S^1 \to S^1$, $z \mapsto z^2$, records a single flip as one goes around once.
Applying this flip to a line, by $t \mapsto -t$, gives the Möbius band.
