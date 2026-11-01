---
tag: DWV8BQP6GA
kind: definition
name: Perfectly normal space
msc: [54D15]
defines: VK3ZMD1BCP
uses: [0CQHFPGJ45, 0NSR9V8TED, 0ZCK8DQYN1, 02BH3MCBQB, V1TBNP8R3S, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_space
---

## Definition

A [[topological space|0CQHFPGJ45]] $X$ is *perfectly normal* when the following two conditions hold.

1. $X$ is a [[normal space|0NSR9V8TED]].
2. Every [[closed set|0ZCK8DQYN1]] of $X$ is a [[G-delta set|V1TBNP8R3S]], that is, a countable intersection of [[open sets|02BH3MCBQB]].

## Remarks

Equivalently, for all disjoint closed sets $A, B \subseteq X$ there is a [[continuous function|0X3WGX95FE]] $f \colon X \to [0, 1]$ with $f^{-1}(0) = A$ and $f^{-1}(1) = B$.
Another equivalent form: every closed set is $f^{-1}(0)$ for some continuous $f \colon X \to \R$.
A perfectly normal space is [[completely normal|9HBDQ2W9CF]].
A perfectly normal $T_1$ space is called a $T_6$ space.

Example: every metric space $(X, d)$ is perfectly normal.
It is normal, and a closed set $A$ equals $\bigcap_{n \ge 1} \set{x : d(x, A) < 1/n}$, an intersection of countably many open sets.

Non-example: the space $[0, \omega_1]$ of countable ordinals together with $\omega_1$, with the order topology, is compact Hausdorff and so normal.
The closed set $\set{\omega_1}$ is not a G-delta set: any countably many neighbourhoods $(\alpha_n, \omega_1]$ contain $(\sup_n \alpha_n, \omega_1]$, which has more than one point.
So clause 2 fails.
