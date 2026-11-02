---
tag: K14ZBKYT81
kind: definition
name: Lie group
msc: ["22E15", "22E10"]
defines: 7JBRGCVJRB
uses: [G5S1M9, F45VQ47GPV, 0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_group
---

## Definition

A *real Lie group* is a [[group|G5S1M9]] $G$ that is also a finite-dimensional [[smooth manifold|F45VQ47GPV]], such that:

1. the multiplication map $\mu \colon G \times G \to G$, $\mu(g, h) = gh$, is [[smooth|0V33BNKZ9S]];
2. the inversion map $\iota \colon G \to G$, $\iota(g) = g^{-1}$, is smooth.

A *complex Lie group* is defined in the same way with a complex manifold and holomorphic maps.
A *homomorphism of Lie groups* is a group homomorphism that is a smooth map.

## Remarks

Example: the circle $S^1 = \set{z \in \C : \abs{z} = 1}$ with complex multiplication.
It is a smooth submanifold of $\C = \R^2$, and in the angle coordinate the product and the inverse are $(\theta, \varphi) \mapsto \theta + \varphi$ and $\theta \mapsto -\theta$, which are smooth.

Example: $GL_n(\R)$ is an open subset of $\R^{n^2}$, and the product of matrices is polynomial in the entries.
By Cramer's rule, the inverse is a rational function of the entries with nonvanishing denominator $\det$.

Non-example: the additive group $\Q$ with the topology induced from $\R$ is a topological group but not a Lie group.
It is not locally Euclidean, since no point of $\Q$ has a neighbourhood homeomorphic to an open set of some $\R^n$.

The two clauses can be merged: $G$ is a Lie group exactly when the map $(g, h) \mapsto g h^{-1}$ is smooth.
The dimension of $G$ is its dimension as a manifold.
