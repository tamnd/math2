---
tag: 8ZHBEVTFZ9
kind: proof
name: Proof that the inclusion of a subspace is continuous
msc: [54B05]
proves: 065J822CKN
uses: [0D5YHQGDJY, 0SY9ECQ19Q, 0FGCFY1AZX]
sources:
  - url: https://en.wikipedia.org/wiki/Subspace_topology
    locator: Properties
---

## Proof

We compute preimages of open sets.

1. Let $U$ be open in $X$. The [[preimage|0FGCFY1AZX]] is $\iota^{-1}(U) = \set{s \in S : \iota(s) \in U}$.
2. Since $\iota(s) = s$, this is $\set{s \in S : s \in U} = S \cap U$.
3. By the definition of the [[subspace topology|0D5YHQGDJY]], $S \cap U$ is open in $S$.
4. So the preimage of each open set of $X$ is open in $S$, and $\iota$ is [[continuous|0SY9ECQ19Q]].

## Idea

The subspace topology is built from the sets $S \cap U$ with $U$ open in $X$. These are exactly the preimages of open sets under the inclusion, so the inclusion is continuous by design.
