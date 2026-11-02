---
tag: VRP0HESPYD
kind: definition
name: Lie pseudogroup
msc: [58H05, 58A20]
defines: E3EYXM7GJN
uses: [3017J7P6JD, 1QE0Z0756D, F45VQ47GPV, 0KZZ70ZHXP, HNVW0E732J]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudogroup
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]] and let $k \ge 0$ be an integer.
Let $J^k_\times(M)$ be the set of $k$-[[jets|1QE0Z0756D]] $j^k_x f$ of local [[diffeomorphisms|0KZZ70ZHXP]] $f$ of $M$ at points $x$ of their domains.
It is a [[Lie groupoid|HNVW0E732J]] over $M$, with composition of jets as multiplication.
Let $\Gamma$ be a [[pseudogroup|3017J7P6JD]] of local diffeomorphisms of $M$.
It is a *Lie pseudogroup of order $k$* if there is a subgroupoid $R \subseteq J^k_\times(M)$ with these properties.

1. $R$ is a closed embedded submanifold of $J^k_\times(M)$.
2. A local diffeomorphism $f \colon U \to V$ of $M$ lies in $\Gamma$ if and only if $j^k_x f \in R$ for every $x \in U$.

## Remarks

The condition $j^k_x f \in R$ for all $x$ is a system of partial differential equations of order $k$ for $f$, and $\Gamma$ is its set of local invertible solutions.
Definitions in the literature differ in details, for example in requiring the equations to be analytic or involutive.

Example: let $g$ be a Riemannian metric on $M$, and let $R \subseteq J^1_\times(M)$ be the set of $1$-jets whose derivative $T_x M \to T_y M$ is a linear isometry from $g_x$ to $g_y$.
It is a closed subgroupoid and a submanifold, and a local diffeomorphism has all its $1$-jets in $R$ exactly when it is a local isometry.
So local isometries form a Lie pseudogroup of order $1$.
In the same way, area-preserving maps of $\R^2$ are the local diffeomorphisms whose $1$-jets satisfy $\det Df = 1$.

Non-example: the pseudogroup of all local homeomorphisms of $\R^n$ is not a Lie pseudogroup.
It contains maps that are not smooth, so it is not even a pseudogroup of local diffeomorphisms.

## Explanations

### L1 human

A Lie pseudogroup is the set of all local invertible solutions of a system of differential equations.
Examples are the maps that preserve a metric or an area form.
