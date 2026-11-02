---
tag: MTWNAJMH1D
kind: statement
role: theorem
name: Galois correspondence for coverings
msc: [57M10, 55R05]
uses: [3XZRRE165N, S1XK3HXHFX, BH32RQBX6A, R3SHZX0NZR, 0WB6DH499T, 1ZVR8BRK65, 0CB0DX5BVV, 0YGN3VAA0D, 0KYX2N69J0]
about: [3XZRRE165N, BH32RQBX6A]
sources:
  - url: https://en.wikipedia.org/wiki/Covering_space
---

## Statement

Let $X$ be a [[path-connected|0WB6DH499T]], [[locally path-connected|1ZVR8BRK65]] and [[semilocally simply connected|R3SHZX0NZR]] space, and let $x_0 \in X$.
For a [[covering map|3XZRRE165N]] $p \colon (\tilde X, \tilde x_0) \to (X, x_0)$ with $\tilde X$ path-connected, let $H_p = p_* \pi_1(\tilde X, \tilde x_0)$ in the [[fundamental group|S1XK3HXHFX]] $\pi_1(X, x_0)$.
Let $G(p)$ be the [[deck transformation group|BH32RQBX6A]] of $p$.
Then:

1. For two such coverings $p_1$ and $p_2$, there is a map $f \colon (\tilde X_1, \tilde x_1) \to (\tilde X_2, \tilde x_2)$ with $p_2 \circ f = p_1$ if and only if $H_{p_1} \subseteq H_{p_2}$.
2. The group $G(p)$ acts transitively on the fibre $p^{-1}(x_0)$ if and only if $H_p$ is a [[normal subgroup|0CB0DX5BVV]] of $\pi_1(X, x_0)$.
3. The group $G(p)$ is isomorphic to $N(H_p)/H_p$, where $N(H_p)$ is the [[normaliser|0YGN3VAA0D]] of $H_p$ in $\pi_1(X, x_0)$.
4. In particular, if $H_p$ is normal, then $G(p) \cong \pi_1(X, x_0)/H_p$, a [[quotient group|0KYX2N69J0]], and $G(p) \cong \pi_1(X, x_0)$ when $\tilde X$ is simply connected.

## Remarks

The first clause is the lifting criterion applied to $p_1$ and $p_2$.
For the third clause, a loop $\gamma$ at $x_0$ lifts to a path from $\tilde x_0$ to a point $\tilde x_1$ of the fibre.
A deck transformation sending $\tilde x_0$ to $\tilde x_1$ exists exactly when $[\gamma]$ normalises $H_p$, and it is unique, which gives a surjection $N(H_p) \to G(p)$ with kernel $H_p$.
For the covering $S^1 \to S^1$, $z \mapsto z^n$, the subgroup is $n\Z \subseteq \Z$, which is normal, and the deck group is $\Z / n\Z$, acting by rotations through multiples of $2\pi / n$.
Together with the [[classification of covering spaces|YY277RBF8Z]], these facts form a dictionary between coverings and subgroups.

## Explanations

### L1 human

Coverings of a space behave like field extensions in Galois theory.
Bigger subgroups of the fundamental group belong to smaller coverings, and one covering sits over another exactly when the subgroups are nested.
The most symmetric coverings belong to normal subgroups, and their symmetry group is the quotient group.

### L2 human

The universal cover plays the part of the algebraic closure, and the fundamental group plays the part of the absolute Galois group.
Normal coverings correspond to Galois extensions, and the deck group corresponds to the Galois group.
The analogy becomes an exact theorem in Grothendieck's theory of the étale fundamental group, where finite étale coverings replace topological coverings.
In practice, the statement computes deck groups and tells which quotients of $\pi_1(X)$ arise as symmetry groups of coverings.
