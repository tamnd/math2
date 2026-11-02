---
tag: YHGS413E8B
kind: statement
role: theorem
name: Automorphism group of a bounded domain is a Lie group
msc: [32M05, 32H02]
uses: [FX92PP3HZR, 7JBRGCVJRB, EQHPSKC5SY, ZVFVBVJMCB]
about: [7JBRGCVJRB]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_symmetric_space
---

## Statement

Let $D \subset \C^n$ be a bounded domain, that is, a bounded connected open set.
Let $\Aut(D)$ be the group of [[biholomorphisms|FX92PP3HZR]] $D \to D$, with the topology of uniform convergence on compact subsets.
Then $\Aut(D)$ is a real [[Lie group|7JBRGCVJRB]], and it acts properly on $D$.
In particular, for each $p \in D$ the isotropy group $\set{f \in \Aut(D) : f(p) = p}$ is compact.

## Remarks

The theorem is due to Henri Cartan.
Since $D$ is bounded, [[Montel's theorem|ZVFVBVJMCB]] makes families of automorphisms normal, and a limit argument shows that the action is proper.
By [[Cartan's uniqueness theorem|EQHPSKC5SY]], an automorphism $f$ with $f(p) = p$ is determined by its derivative $f'(p)$.
So the isotropy group embeds as a compact subgroup of $GL_n(\C)$, and the whole group is locally compact and finite-dimensional.

Example: for the unit disc $\Delta$, $\Aut(\Delta)$ consists of the maps $z \mapsto e^{i\theta}(z - a)/(1 - \bar a z)$ with $\theta \in \R$ and $\abs{a} < 1$.
It is a $3$-dimensional Lie group, isomorphic to $PSU(1, 1)$, and the isotropy group of $0$ is the circle of rotations.

Boundedness cannot be dropped.
For $n \ge 2$, $\Aut(\C^n)$ contains the maps $(z_1, z_2, \dots) \mapsto (z_1, z_2 + g(z_1), \dots)$ for every entire function $g$, so it is not a finite-dimensional Lie group.

## Explanations

### L1 human

The holomorphic symmetries of a bounded region in $\C^n$ form a group.
The theorem says this group is as nice as a group of matrices: it is a smooth finite-dimensional manifold, and its operations are smooth.
Moreover, the symmetries fixing a point form a compact group.

### L2 human

This is the starting point for the study of homogeneous and symmetric bounded domains.
If $\Aut(D)$ acts transitively, then $D \cong \Aut(D)/K$ with $K$ compact, and $D$ becomes a homogeneous space of a Lie group.
Combined with the invariant Bergman metric, this leads to Cartan's classification of bounded symmetric domains.
For unbounded domains the group can be infinite-dimensional, as for $\C^n$.
