---
tag: 273NZSYWZA
kind: definition
name: Subnormal operator
msc: [47B20]
defines: 81MZ023K1A
uses: [HM2HHE3J51, 0ACX5QT8TE]
sources:
  - url: https://en.wikipedia.org/wiki/Subnormal_operator
---

## Definition

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]] and let $S \colon H \to H$ be a bounded linear operator.
The operator $S$ is *subnormal* when there are a Hilbert space $K \supseteq H$, with $H$ closed in $K$, and a bounded normal operator $N \colon K \to K$ such that

1. $N(H) \subseteq H$, that is, $H$ is an [[invariant subspace|0ACX5QT8TE]] of $N$;
2. $Nx = Sx$ for all $x \in H$.

Such an $N$ is a *normal extension* of $S$.

## Remarks

Example: the unilateral shift $S$ on $\ell^2(\N)$ is subnormal.
View $\ell^2(\N)$ as the sequences in $\ell^2(\Z)$ that vanish at negative indices, and let $N$ be the bilateral shift $(Nx)_n = x_{n-1}$, which is unitary, hence normal.
$N$ maps sequences vanishing at negative indices to sequences of the same kind, and it agrees with $S$ there.

Non-example: $S = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ on $\C^2$ is not subnormal.
A subnormal operator is hyponormal, that is $S^*S - SS^* \ge 0$, but here $S^*S - SS^* = \mathrm{diag}(-1, 1)$, which is not positive.

A normal extension $N$ can be chosen minimal: $K$ is the smallest closed subspace containing $H$ and invariant under $N$ and $N^*$.
The minimal normal extension is unique up to unitary equivalence.
