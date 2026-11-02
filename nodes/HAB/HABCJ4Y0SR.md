---
tag: HABCJ4Y0SR
kind: statement
role: theorem
name: Hodge decomposition
msc: [14C30, 32Q15, 58A14]
uses: [6N7BC70CX0, GX74C07T0G, PQ6Q143ARJ, A127WFVYKW]
about: [6N7BC70CX0]
sources:
  - url: https://en.wikipedia.org/wiki/Hodge_theory
---

## Statement

Let $X$ be a compact Kähler manifold of complex dimension $n$, and let $0 \le k \le 2n$.
Let $\Omega^p_X$ be the sheaf of holomorphic $p$-forms on $X$.
Let $H^{p,q}(X)$ be the space of classes in $H^k(X, \C)$ represented by a closed form of type $(p, q)$.
Then:

1. The [[singular cohomology|6N7BC70CX0]] with complex coefficients decomposes as a direct sum
$$H^k(X, \C) = \bigoplus_{p + q = k} H^{p,q}(X).$$
2. Complex conjugation on $H^k(X, \C) = H^k(X, \R) \otimes \C$ maps $H^{p,q}(X)$ onto $H^{q,p}(X)$.
3. There are natural isomorphisms $H^{p,q}(X) \cong H^q(X, \Omega^p_X)$ with [[sheaf cohomology|PQ6Q143ARJ]], which is Dolbeault cohomology.

## Remarks

The idea of the proof: by the [[Hodge theorem|A127WFVYKW]], each class in [[de Rham cohomology|GX74C07T0G]] has a unique harmonic representative for the Laplacian $\Delta_d$.
The Kähler identities give $\Delta_d = 2\Delta_{\bar\partial}$, so $\Delta_d$ preserves the type $(p, q)$ of forms, and the harmonic part of a form splits by type.
The $\Delta_{\bar\partial}$-harmonic $(p,q)$-forms represent Dolbeault cohomology, which gives part 3; part 2 holds because $\Delta_d$ is a real operator.

Example: for a compact Riemann surface of genus $g$, $H^1(X, \C) = H^{1,0} \oplus H^{0,1}$ with $H^{1,0}$ the $g$-dimensional space of holomorphic $1$-forms, so $b_1 = 2g$.

Consequence: the Hodge numbers $h^{p,q} = \dim H^{p,q}$ satisfy $h^{p,q} = h^{q,p}$, so every odd Betti number $b_{2m+1} = \sum_{p+q = 2m+1} h^{p,q}$ is even.
The Kähler hypothesis is needed: the Hopf surface, diffeomorphic to $S^1 \times S^3$, is a compact complex manifold with $b_1 = 1$, so no such decomposition with symmetry exists on it.

## Explanations

### L1 human

The cohomology of a compact Kähler manifold, such as a smooth projective complex variety, splits into pieces labelled by pairs $(p, q)$.
The piece $(p, q)$ comes from forms with $p$ holomorphic and $q$ antiholomorphic differentials.
The pieces $(p, q)$ and $(q, p)$ are mirror images under complex conjugation.

### L2 human

The decomposition makes $H^k(X, \Z)$ modulo torsion into a Hodge structure of weight $k$, which is the starting point of period maps and of the Torelli problem.
Combined with the hard Lefschetz theorem and the Hodge–Riemann bilinear relations, it gives polarized Hodge structures.
It also links topology to holomorphic invariants: for example $h^{1,0}$, the number of independent holomorphic $1$-forms, equals half the first Betti number.
