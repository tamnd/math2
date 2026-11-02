---
tag: WFPYZ0XDRN
kind: definition
name: Anderson localization
msc: [82B44, 47B80, 81Q10]
defines: MXEZM0QJ1K
uses: [0NEGN5CRSC, BMKATJ802A, 0BQAA2BK3Q, 00MRN0FARV]
sources:
  - url: https://en.wikipedia.org/wiki/Anderson_localization
---

## Definition

Let $d \ge 1$ and let $H$ be a bounded [[self-adjoint operator|0NEGN5CRSC]] on $\ell^2(\Z^d)$.
Let $I \subseteq \R$ be an interval.
The operator $H$ exhibits *Anderson localization* in $I$ if:

1. the [[spectrum|BMKATJ802A]] of $H$ in $I$ is pure point: the spectral subspace of $H$ for $I$ has an orthonormal basis of eigenvectors;
2. every eigenvector $\psi$ of $H$ with [[eigenvalue|0BQAA2BK3Q]] in $I$ decays exponentially: there are $C_\psi > 0$ and $\mu_\psi > 0$ with $\abs{\psi(n)} \le C_\psi e^{-\mu_\psi\abs{n}}$ for all $n \in \Z^d$.

The main case is the *Anderson model* $H_\omega = -\Delta + \lambda V_\omega$, where $(\Delta u)(n) = \sum_{\abs{m - n} = 1}(u(m) - u(n))$, $\lambda > 0$, and $V_\omega(n)$, $n \in \Z^d$, are [[independent identically distributed random variables|00MRN0FARV]].
One says the model exhibits Anderson localization in $I$ if $H_\omega$ does so for almost every $\omega$.

## Remarks

Example: a diagonal operator $(Hu)(n) = v(n)u(n)$ with a bounded real sequence $v$ exhibits localization in every interval.
Its eigenvectors $\delta_n$ have one nonzero entry, so they decay faster than any exponential.

Non-example: the free operator $-\Delta$ on $\ell^2(\Z)$ has spectrum $[0, 4]$ and no eigenvalues at all, since its Fourier transform is multiplication by $2 - 2\cos k$.
So clause 1 fails in every interval that meets $[0, 4]$.

For the Anderson model with a bounded density of the $V_\omega(n)$, localization holds in $d = 1$ for the whole spectrum, and in every dimension for large $\lambda$.
The strongest form, dynamical localization, also bounds the spreading of $e^{-itH}\psi$ uniformly in time.
