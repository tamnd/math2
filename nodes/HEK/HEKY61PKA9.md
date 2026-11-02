---
tag: HEKY61PKA9
kind: definition
name: Isomorphism of topological groups
msc: [22A05]
defines: T3A3JTW6Q4
uses: [92700QAB5Y, 9J5PQMG3HJ, 08MG7H8JW5, 0QT00PB5G2]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_group
---

## Definition

Let $G$ and $H$ be [[topological groups|92700QAB5Y]].
An *isomorphism of topological groups* from $G$ to $H$ is a map $f \colon G \to H$ that is both a [[group isomorphism|08MG7H8JW5]] and a [[homeomorphism|0QT00PB5G2]].
Equivalently, $f$ is a bijective [[continuous group homomorphism|9J5PQMG3HJ]] whose inverse $f^{-1} \colon H \to G$ is continuous.
The groups $G$ and $H$ are *isomorphic* if such a map exists.

## Remarks

Example: $\log \colon (\,(0, \infty), \cdot\,) \to (\R, +)$.
It is bijective, $\log(xy) = \log x + \log y$, and both $\log$ and its inverse $\exp$ are continuous.
Non-example: the identity map from $(\R, +)$ with the discrete topology to $(\R, +)$ with the usual topology.
It is a continuous bijective homomorphism, but its inverse is not continuous, since $\set{0}$ is open in the discrete topology and not in the usual one.
