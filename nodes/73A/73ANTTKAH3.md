---
tag: 73ANTTKAH3
kind: statement
role: theorem
name: Fredholm property of elliptic operators
msc: [58J05, 47A53, 58J20]
uses: [MT9P2X85V8, CGBX1N9V8H, 8HWGKWD6ZM, 2V9Q4KHY1T, M4CEZ5K9HP, Z97HVFD6JE, M2NEP1K5AE, 2PVQY9PCT4]
about: [MT9P2X85V8, 8HWGKWD6ZM]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_operator
---

## Statement

Let $M$ be a compact smooth manifold without boundary, with a smooth positive density.
Let $E$ and $F$ be complex vector bundles over $M$ with Hermitian metrics.
Let $P \colon \Gamma(E) \to \Gamma(F)$ be an [[elliptic operator|MT9P2X85V8]] of order $m$.
Let $P^* \colon \Gamma(F) \to \Gamma(E)$ be its formal adjoint.
It is the [[differential operator|CGBX1N9V8H]] with $\int_M \ip{Pu}{v} = \int_M \ip{u}{P^* v}$ for all smooth sections $u$ and $v$.
For $s \in \R$, let $H^s(E)$ and $H^s(F)$ be the [[Sobolev spaces|M4CEZ5K9HP]] of sections.

1. For every $s \in \R$, $P$ extends to a bounded operator $P_s \colon H^{s+m}(E) \to H^s(F)$, and $P_s$ is a [[Fredholm operator|8HWGKWD6ZM]].
2. The kernel of $P_s$ consists of smooth sections and equals the kernel of $P$ on $\Gamma(E)$.
In particular it is finite-dimensional and does not depend on $s$.
3. The kernel of $P^*$ is a finite-dimensional space of smooth sections.
The range of $P_s$ is the set of $f \in H^s(F)$ with $\int_M \ip{f}{v} = 0$ for all $v$ in the kernel of $P^*$.
4. The [[index|2V9Q4KHY1T]] of $P_s$ equals $\dim \ker P - \dim \ker P^*$ and does not depend on $s$.

## Remarks

The proof constructs a [[parametrix|Z97HVFD6JE]] $Q$, a pseudodifferential operator of order $-m$ built from the inverse of the principal symbol, with $QP - I$ and $PQ - I$ smoothing.
Smoothing operators map $H^s$ into $H^{s+1}$, and by the Rellich lemma the inclusion $H^{s+1} \to H^s$ is [[compact|M2NEP1K5AE]] on a compact manifold.
So $P_s$ is invertible modulo compact operators, which is Atkinson's characterisation of Fredholm operators.
The parametrix also gives [[elliptic regularity|2PVQY9PCT4]]: if $Pu$ is smooth then $u$ is smooth, which yields part 2.

Example: on the circle $S^1 = \R / 2\pi\Z$, let $P = -d^2/dx^2$.
Its kernel and the kernel of $P^* = P$ are the constant functions, so the index is $1 - 1 = 0$, and the range consists of the functions with average zero.

Compactness of $M$ is needed.
On $\R$, the operator $d/dx \colon H^1(\R) \to L^2(\R)$ is elliptic and injective, but its range is dense and not closed, so it is not Fredholm.

## Explanations

### L1 human

An elliptic operator on a closed manifold behaves almost like an invertible matrix.
It kills only a finite-dimensional space of sections, and it misses only a finite-dimensional space of targets.
The difference of these two dimensions, the index, is a stable number that does not change when the operator is deformed through elliptic operators.

### L2 human

This theorem is the analytic foundation of index theory.
The index depends only on the homotopy class of the principal symbol through invertible symbols, which is why it can be computed topologically by the Atiyah–Singer index theorem.
It also underlies Hodge theory: applied to the Hodge Laplacian, it gives finite-dimensional spaces of harmonic forms and the orthogonal decomposition of forms.
