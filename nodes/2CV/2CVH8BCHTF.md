---
tag: 2CVH8BCHTF
kind: statement
role: theorem
name: Grauert's Oka principle for vector bundles
msc: [32Q56, 32L05]
uses: [HMCD0JBFST, TKA958Z4KZ, P4DZM975BV, S1CJV1PA3D, NXEAT9DMWD]
about: [HMCD0JBFST, TKA958Z4KZ]
sources:
  - url: https://en.wikipedia.org/wiki/Stein_manifold
---

## Statement

Let $X$ be a [[Stein manifold|HMCD0JBFST]].

1. Two [[holomorphic vector bundles|TKA958Z4KZ]] on $X$ are holomorphically isomorphic if and only if they are isomorphic as topological complex [[vector bundles|P4DZM975BV]].
2. Every topological complex vector bundle on $X$ is topologically isomorphic to a holomorphic vector bundle.

## Remarks

Grauert proved the theorem in 1958, for holomorphic principal bundles over Stein spaces whose structure group is a complex Lie group.
Vector bundles of rank $r$ are the case of the group $GL_r(\C)$.
For line bundles it is the [[Oka principle|S1CJV1PA3D]] of 1939, which follows from the exponential sequence.
For higher rank the group $GL_r(\C)$ is not commutative, and the proof needs a new, nonlinear method.
Grauert deformed continuous transition functions to holomorphic ones by successive approximation over an exhaustion of $X$, using a Runge-type approximation for maps into complex Lie groups.
Example: on $\C^n$, which is contractible, every topological complex vector bundle is trivial, so every holomorphic vector bundle on $\C^n$ is holomorphically trivial.
The Stein hypothesis is needed.
On the projective line, the rank $2$ bundle $\mathcal{O}(1) \oplus \mathcal{O}(-1)$ and the trivial bundle of rank $2$ are topologically isomorphic, since both have first Chern class $0$.
They are not holomorphically isomorphic, since the first has a nonzero holomorphic section that vanishes at a point.

## Explanations

### L1 human

A vector bundle attaches a vector space to each point of a space.
Holomorphic vector bundles carry much more structure than continuous ones, and in general there are many more of them.
Grauert's theorem says that on a Stein manifold this extra structure brings nothing new: the holomorphic classification is the same as the topological one.

### L2 human

The theorem reduces the classification of holomorphic vector bundles on a Stein manifold to homotopy theory.
Bundles of rank $r$ correspond to homotopy classes of maps from $X$ to the classifying space of $GL_r(\C)$.
It is the starting point of modern Oka theory.
This theory asks for which target manifolds $Y$ the same principle holds for holomorphic maps from Stein manifolds to $Y$; these targets are the [[Oka manifolds|NXEAT9DMWD]].
