---
tag: Y2GYM93C1W
kind: statement
role: theorem
name: Borg–Marchenko uniqueness theorem
msc: [34A55, 34B20, 34L40]
uses: [89AA6XJY5K, 6J9FXT6HAV, XT8PA31VAX]
about: [XT8PA31VAX]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_scattering_transform
---

## Statement

Let $q_1, q_2 \colon [0, \infty) \to \R$ be integrable on each interval $[0, R]$ with $R > 0$.
Assume that both [[Schrödinger operators|89AA6XJY5K]] $-y'' + q_j y$ are in the [[limit-point case|6J9FXT6HAV]] at $\infty$.
Let $m_1$ and $m_2$ be their [[Weyl–Titchmarsh functions|XT8PA31VAX]].
If $m_1(z) = m_2(z)$ for all $z \in \C \setminus \R$, then $q_1 = q_2$ almost everywhere on $[0, \infty)$.

## Remarks

The function $m$ determines the spectral measure through its Herglotz representation, and the spectral measure determines $q$ by Gelfand–Levitan theory; this gives one proof when $q$ is regular enough.
Example: if $m(z) = i\sqrt{z}$ for all non-real $z$, then $q = 0$ almost everywhere, since this is the $m$-function of $q = 0$.
The hypothesis cannot be weakened to equality of the spectra: in general the spectrum alone does not determine $q$.
There is also a local version: if $m_1(z) - m_2(z)$ decays fast enough as $z \to \infty$ along suitable rays, then $q_1 = q_2$ on an initial interval $[0, a]$.

## Explanations

### L1 human

The theorem says that one complex function, the $m$-function, pins down the potential completely.
Two different potentials on a half-line cannot have the same $m$-function.

### L2 human

This is the basic uniqueness result of inverse spectral theory for one-dimensional Schrödinger operators.
It sits beside the [[Gelfand–Levitan|R4MRNP9EQT]] reconstruction, which turns the same data into an explicit formula for $q$.
The local version shows that the asymptotic behaviour of $m(z)$ for large $\abs{z}$ already determines $q$ on an initial interval.
