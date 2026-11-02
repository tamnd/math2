---
tag: XDYMCB41NG
kind: definition
name: Section of a vector bundle
msc: [55R25, 58A05]
defines: WWX7H5W1RP
uses: [CX4M8K61AB, F45VQ47GPV, 0V33BNKZ9S, 000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Section_(fiber_bundle)
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]] and let $k \ge 0$.
A *smooth vector bundle* of rank $k$ over $M$ is a smooth [[fiber bundle|CX4M8K61AB]] $\pi \colon E \to M$ with fiber $\R^k$ and the following structure.
Each fiber $E_p = \pi^{-1}(p)$ is a real [[vector space|000AYPA9AJ]], and the local trivializations $\pi^{-1}(U) \to U \times \R^k$ can be chosen linear on each fiber.
A *smooth section* of $E$ is a [[smooth|0V33BNKZ9S]] map $s \colon M \to E$ such that
$$\pi \circ s = \id_M,$$
that is, $s(p) \in E_p$ for every $p \in M$.
The set of smooth sections is written $\Gamma(E)$.

## Remarks

The zero section $p \mapsto 0_p$ is a section of every vector bundle.
For the trivial bundle $E = M \times \R^k$, the sections are the maps $p \mapsto (p, u(p))$ with $u \colon M \to \R^k$ smooth.
A smooth vector field on $M$ is a section of the [[tangent bundle|WY6K3P4YCG]] $TM$.

Non-example: on $E = S^1 \times \R$, the map $s(p) = (-p, 0)$ is smooth, but $\pi(s(p)) = -p \neq p$, so it is not a section.

Sections are added and multiplied by smooth functions pointwise, so $\Gamma(E)$ is a module over $C^\infty(M)$.
The same definition, without linearity, gives sections of any fiber bundle; continuous sections are defined with continuous maps.

## Explanations

### L1 human

A section of a vector bundle is a smooth choice of one vector in the fiber over each point of the base.
