---
tag: YY277RBF8Z
kind: statement
role: theorem
name: Classification of covering spaces
msc: [57M10, 55R05]
uses: [3XZRRE165N, S1XK3HXHFX, R3SHZX0NZR, 0WB6DH499T, 1ZVR8BRK65, 0H11ZPX4ND]
about: [3XZRRE165N, S1XK3HXHFX]
sources:
  - url: https://en.wikipedia.org/wiki/Covering_space
---

## Statement

Let $X$ be a [[path-connected|0WB6DH499T]], [[locally path-connected|1ZVR8BRK65]] and [[semilocally simply connected|R3SHZX0NZR]] space, and let $x_0 \in X$.
Two pointed covering maps $p_1 \colon (\tilde X_1, \tilde x_1) \to (X, x_0)$ and $p_2 \colon (\tilde X_2, \tilde x_2) \to (X, x_0)$ are *isomorphic* if there is a homeomorphism $h \colon \tilde X_1 \to \tilde X_2$ with $p_2 \circ h = p_1$ and $h(\tilde x_1) = \tilde x_2$.
Then:

1. Consider pointed [[covering maps|3XZRRE165N]] $p \colon (\tilde X, \tilde x_0) \to (X, x_0)$ with $\tilde X$ path-connected. The rule $p \mapsto p_*\bigl(\pi_1(\tilde X, \tilde x_0)\bigr)$ is a bijection from their isomorphism classes onto the subgroups of the [[fundamental group|S1XK3HXHFX]] $\pi_1(X, x_0)$.
2. Consider isomorphisms that need not preserve base points. Then the same rule gives a bijection from isomorphism classes of covering maps with path-connected total space onto the [[conjugacy classes|0H11ZPX4ND]] of subgroups of $\pi_1(X, x_0)$.

## Remarks

The covering that belongs to a subgroup $H$ is built like the universal cover from homotopy classes of paths that start at $x_0$.
Two such classes are identified when the paths end at the same point and differ by a loop whose class lies in $H$.
Injectivity uses the lifting criterion: a map from a path-connected, locally path-connected space lifts through a covering exactly when its image on $\pi_1$ lies in the image of the covering.
Changing the base point inside the fibre replaces the subgroup by a conjugate, which explains the second clause.
For $X = S^1$, the subgroups of $\pi_1(S^1) = \Z$ are $n\Z$ with $n \ge 0$; they belong to the coverings $z \mapsto z^n$ for $n \ge 1$ and to the universal cover $\R \to S^1$ for $n = 0$.
Without the semilocal condition the trivial subgroup may have no covering: the [[Hawaiian earring|73EBKQPP8Q]] has no simply connected covering space.

## Explanations

### L1 human

For a reasonable space, the connected coverings are described completely by the subgroups of its fundamental group.
The whole group belongs to the space itself, the trivial subgroup to the universal cover, and the other subgroups to the coverings in between.
So a topological question, which coverings exist, becomes an algebraic one, which subgroups exist.

### L2 human

The theorem is the topological analogue of the fundamental theorem of Galois theory, with the universal cover in the role of an algebraic closure.
It is used to build coverings with given properties.
For example, each subgroup of a free group gives a covering of a graph, and this yields a quick proof that subgroups of free groups are free.
Further properties of the correspondence, about deck transformations and normal subgroups, are collected in the [[Galois correspondence for coverings|MTWNAJMH1D]].
