---
tag: 0AYEPBQMAW
kind: definition
name: Eigenspace
msc: [15A18]
defines: 0G0RFPG8HR
uses: [0B5H4208Z9, 02YFME3RGW]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Eigenspaces, geometric multiplicity, and the eigenbasis
---

## Definition

Let $F$ be a field, let $V$ be a vector space over $F$, let $T \colon V \to V$ be an endomorphism, and let $\lambda \in F$.
The *eigenspace* of $T$ for $\lambda$ is
$$E_\lambda = \ker(T - \lambda \id_V) = \{v \in V : T(v) = \lambda v\}.$$

## Remarks

The eigenspace is a subspace of $V$; it is the [[kernel|0S23E6YE83]] of a linear map.
Its nonzero elements are the [[eigenvectors|0N6960W0BV]] of $T$ for $\lambda$.
$E_\lambda \ne 0$ if and only if $\lambda$ is an eigenvalue of $T$.
The dimension of $E_\lambda$ is the [[geometric multiplicity|099TWVJ909]] of $\lambda$.

## Explanations

### L1 human

The eigenspace collects all the vectors that the map stretches by the same factor $\lambda$, with the zero vector.
These vectors form a subspace, for example a line or a plane.
On this subspace, the map acts as multiplication by $\lambda$.
