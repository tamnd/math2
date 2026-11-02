---
tag: ABKND96G8P
kind: definition
name: Quotient of a topological group
msc: [22A05]
defines: 417ZRDCHY6
uses: [92700QAB5Y, 0X1JXT47GA, 03DEH43F4H, 0NQ1H2X495, 0CB0DX5BVV, 0KYX2N69J0, 0YCG648KDD, 0S1FJ8VEX9]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_group
---

## Definition

Let $G$ be a [[topological group|92700QAB5Y]] and let $H$ be a [[subgroup|0X1JXT47GA]] of $G$.
Let $G/H = \set{gH : g \in G}$ be the set of [[left cosets|03DEH43F4H]] of $H$, and let $\pi \colon G \to G/H$, $\pi(g) = gH$.
The *quotient* of $G$ by $H$ is the set $G/H$ with the [[quotient topology|0NQ1H2X495]] of $\pi$.
So a set $U \subseteq G/H$ is open if and only if $\pi^{-1}(U)$ is open in $G$.
If $H$ is a [[normal subgroup|0CB0DX5BVV]], then $G/H$ is also given the structure of the [[quotient group|0KYX2N69J0]].

## Remarks

The projection $\pi$ is continuous and an [[open map|0YCG648KDD]]: for $U$ open in $G$, the set $\pi^{-1}(\pi(U)) = UH$ is a union of the open sets $Uh$.
If $H$ is normal, then $G/H$ is a topological group, and $\pi$ is a continuous homomorphism.
The space $G/H$ is [[Hausdorff|0S1FJ8VEX9]] if and only if $H$ is closed in $G$.
Example: $\R/\Z$ is a compact Hausdorff topological group, isomorphic to the circle group through $x + \Z \mapsto e^{2\pi i x}$.
Non-example of the Hausdorff property: $\R/\Q$ carries the indiscrete topology, because $\Q$ is dense, so every nonempty open set of $\R$ meets every coset of $\Q$.
