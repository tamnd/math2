---
tag: FJZXB1N7TP
kind: statement
role: theorem
name: Bott's Morse-theoretic proof of periodicity
msc: [55R45, "58E10", "58E05"]
uses: [CZCWFPNS4N, 0R9R0Y1HDK, CYPA882RB9, NSYMQMHPDN, MAX2ZYG6H9, 2JFF5F3EGF, P976WYEFMB]
about: [0R9R0Y1HDK, MAX2ZYG6H9]
sources:
  - url: https://en.wikipedia.org/wiki/Bott_periodicity_theorem
---

## Statement

Let $m \ge 1$.
Give the [[special unitary group|CZCWFPNS4N]] $SU(2m)$ the bi-invariant Riemannian metric induced by $\langle A, B \rangle = \operatorname{Re} \tr(A^* B)$.
Let $\Omega$ be the space of paths in $SU(2m)$ from the identity $I$ to $-I$.

1. The minimal [[geodesics|NSYMQMHPDN]] from $I$ to $-I$ form a space homeomorphic to the complex [[Grassmannian|CYPA882RB9]] $G_m(\C^{2m})$ of $m$-dimensional subspaces of $\C^{2m}$.
2. Every geodesic from $I$ to $-I$ that is not minimal has [[Morse index|MAX2ZYG6H9]] at least $2m + 2$, as a critical point of the energy on $\Omega$.
3. Hence the inclusion of $G_m(\C^{2m})$ into $\Omega$ induces isomorphisms $\pi_i(G_m(\C^{2m})) \cong \pi_i(\Omega) \cong \pi_{i+1}(SU(2m))$ for $0 \le i \le 2m$.
4. Consequently, for the stable [[unitary group|0R9R0Y1HDK]] $U = \bigcup_n U(n)$, there are isomorphisms of [[homotopy groups|P976WYEFMB]] $\pi_{i}(U) \cong \pi_{i+2}(U)$ for all $i \ge 0$.

## Remarks

A geodesic from $I$ in $SU(2m)$ has the form $t \mapsto \exp(t X)$ with $X$ skew-Hermitian.
It ends at $-I$ at time $1$ exactly when the eigenvalues of $X$ are $i \pi k_j$ with odd integers $k_j$ summing to $0$.
The geodesic is minimal exactly when $m$ of the $k_j$ equal $1$ and $m$ equal $-1$.
Such an $X$ is determined by its $m$-dimensional eigenspace for the eigenvalue $i \pi$, which gives the Grassmannian.
The index of a geodesic is computed from the curvature of $SU(2m)$ through the [[Morse index theorem for geodesics|YZ4268SK8G]], and it grows with the $\abs{k_j}$.
Morse theory on the path space then shows that $\Omega$ is obtained from the space of minimal geodesics by attaching cells of dimension at least $2m + 2$.
This gives the third statement.
The last statement follows from the third through the fibration $U(m) \to V_m(\C^{2m}) \to G_m(\C^{2m})$.
Its total space, the Stiefel manifold of orthonormal $m$-frames in $\C^{2m}$, is $2m$-connected.
So $\pi_i(G_m(\C^{2m})) \cong \pi_{i-1}(U(m))$ for $1 \le i \le 2m$, and both sides stabilize as $m$ grows.

In the same way, a chain of eight such steps through symmetric spaces gives the real periodicity $\pi_i(O) \cong \pi_{i+8}(O)$ for the stable orthogonal group $O$.
For example, $U$ is connected and $\pi_1(U) \cong \Z$ by the determinant, so $\pi_{2k+1}(U) \cong \Z$ and $\pi_{2k}(U) = 0$ for all $k \ge 0$.

## Explanations

### L1 human

Bott periodicity says that the homotopy groups of the infinite unitary group repeat with period two.
Bott proved it by looking at geodesics in the group $SU(2m)$ joining the identity to its negative.
The shortest such geodesics form a Grassmannian, and all the longer ones are unstable in many directions.
So, up to a high dimension, the space of all paths looks like the space of shortest geodesics, and this identification gives the periodicity.

### L2 human

The argument is a model application of Morse theory on path spaces.
One computes the space of minimal critical points of the energy and a lower bound for the indices of all other critical points.
Then the path space and the minimal set have the same homotopy groups up to the bound.
The same method, applied to $Sp(n)$ and to symmetric spaces such as $SO(2n)/U(n)$, yields the eight-fold periodicity of the orthogonal group.
Bott periodicity is the foundation of topological K-theory, where it appears as $\tilde{K}(S^{n+2}) \cong \tilde{K}(S^n)$.
