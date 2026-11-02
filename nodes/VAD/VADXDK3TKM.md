---
tag: VADXDK3TKM
kind: statement
role: theorem
name: Krein–Rutman theorem
msc: [47B65, 47A10, 46A40]
uses: [06GZ956657, M2NEP1K5AE, 9V7YQA85PC, 0N6960W0BV]
about: [M2NEP1K5AE, 9V7YQA85PC]
sources:
  - url: https://en.wikipedia.org/wiki/Krein%E2%80%93Rutman_theorem
same_as:
  wikidata: Q6436614
  wikipedia: Krein–Rutman theorem
---

## Statement

Let $X$ be a real [[Banach space|06GZ956657]] and let $K \subseteq X$ be a closed convex cone with $K \cap (-K) = \set{0}$.
Assume that $K$ is total, that is, the set $K - K = \set{u - v : u, v \in K}$ is dense in $X$.
Let $T \colon X \to X$ be a [[compact operator|M2NEP1K5AE]] with $T(K) \subseteq K$ and with [[spectral radius|9V7YQA85PC]] $r(T) > 0$.
Then $r(T)$ is an eigenvalue of $T$ with an [[eigenvector|0N6960W0BV]] in $K$: there is $u \in K$, $u \ne 0$, with $Tu = r(T) u$.

## Remarks

Proof idea: for $\lambda > r(T)$ the resolvent $(\lambda I - T)^{-1} = \sum_{n \ge 0} T^n / \lambda^{n+1}$ maps $K$ into $K$.
Using totality of the cone one shows that $r(T)$ lies in the spectrum and that the resolvent blows up along vectors of $K$ as $\lambda$ decreases to $r(T)$.
Normalizing $(\lambda I - T)^{-1} x$ for suitable $x \in K$ and using compactness of $T$ to pass to a limit gives a nonzero eigenvector in $K$.

Example: let $X = \R^n$, let $K$ be the vectors with nonnegative entries, and let $T$ be a matrix with nonnegative entries and $r(T) > 0$.
The theorem gives the weak form of the [[Perron–Frobenius theorem|62NS7PV1M9]]: $r(T)$ is an eigenvalue with a nonnegative eigenvector.

The hypothesis $r(T) > 0$ is needed: the Volterra operator $(Vf)(x) = \int_0^x f(t)\,dt$ on $C[0, 1]$ is compact and maps nonnegative functions to nonnegative functions, but $r(V) = 0$ and $V$ has no eigenvalue at all.

A stronger form holds when $K$ has nonempty interior and $T$ maps $K \setminus \set{0}$ into the interior of $K$.
Then $r(T) > 0$, it is a simple eigenvalue with an eigenvector in the interior of $K$, and every other eigenvalue $\lambda$ satisfies $\abs{\lambda} < r(T)$.

## Explanations

### L1 human

A positive operator here is one that sends nonnegative things to nonnegative things, such as a matrix with nonnegative entries acting on vectors with nonnegative entries.
The theorem says that, under a compactness condition, the largest growth rate of such an operator is achieved by a nonnegative eigenvector.
It extends the Perron–Frobenius theorem from matrices to infinite-dimensional spaces.

### L2 human

The theorem is a main tool for principal eigenvalues of elliptic operators.
The inverse of such an operator, with suitable boundary conditions, is compact and positive on a space of continuous functions, so it has a positive eigenfunction.
This gives the existence of a positive first eigenfunction of the Dirichlet Laplacian and similar results in population dynamics and bifurcation theory.
