---
tag: QYZXXXFM53
kind: definition
name: Spectral space
msc: [54F65, 06D50, 14A05]
defines: G3W2WXY2VN
uses: [0CQHFPGJ45, 0TVJZYB6SH, 0NA0732YAG, 4N4DNDR22Z]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_space
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
A subset of $X$ is *compact* if every cover of it by open sets of $X$ has a finite subcover; no Hausdorff condition is assumed.
The space $X$ is *spectral* if:

1. $X$ is [[compact|0TVJZYB6SH]];
2. the compact open subsets of $X$ form a [[basis|0NA0732YAG]] of the topology of $X$;
3. the intersection of any two compact open subsets of $X$ is compact;
4. $X$ is [[sober|4N4DNDR22Z]]: every irreducible closed subset of $X$ is the closure of exactly one point.

Here a closed set is *irreducible* if it is nonempty and is not the union of two closed proper subsets.

## Remarks

A sober space is [[T0|07SG12TQH3]], so every spectral space is T0.

Example: the prime spectrum $\operatorname{Spec} \Z$ with the Zariski topology.
Its open sets are $\emptyset$ and the complements of finite sets of nonzero primes, each of which is compact.
The irreducible closed sets are the points $(p)$ for primes $p$ and the whole space, which is the closure of $(0)$.

Non-example: the interval $[0, 1]$ with its usual topology.
It is compact and sober, but it is connected, so its only compact open subsets are $\emptyset$ and $[0, 1]$, and these do not form a basis; clause 2 fails.

[[Hochster's theorem|C82AXZK2BS]] says that the spectral spaces are exactly the spaces homeomorphic to the spectrum of a commutative ring.
A Hausdorff spectral space is the same as a [[Stone space|ZV38HA5PAQ]].
