---
tag: 7TXCCCA17A
kind: statement
role: proposition
name: Log-modulus of a holomorphic function is subharmonic
msc: [31A05, 30A99]
uses: [0NAHXR1FRH, Z1MHMGFNFW, 0DEB0JMN0W, 031BG625Y3, 02BH3MCBQB, E820CTMJVM]
about: [Z1MHMGFNFW, 0NAHXR1FRH]
sources:
  - url: https://en.wikipedia.org/wiki/Subharmonic_function
---

## Statement

Let $\Omega \subseteq \C$ be an [[open set|02BH3MCBQB]] and let $f$ be [[holomorphic|0NAHXR1FRH]] on $\Omega$, not identically zero on any connected component of $\Omega$.
Then the function $u = \log\abs{f}$, with $u(z) = -\infty$ where $f(z) = 0$, is [[subharmonic|Z1MHMGFNFW]] on $\Omega$.
Moreover $u$ is [[harmonic|0DEB0JMN0W]] on the open set $\set{z \in \Omega : f(z) \ne 0}$.

## Remarks

Proof idea: let $a$ be a point with $f(a) \ne 0$.
On a small disc about $a$ there is a holomorphic $g$ with $f = e^{g}$, so $u = \operatorname{Re} g$ there.
The [[real part of a holomorphic function is harmonic|031BG625Y3]], so $u$ is harmonic near $a$.
At a zero $a$ of $f$, $u(a) = -\infty$, and $-\infty$ is at most any mean of $u$, so the sub-mean inequality holds at $a$.
The function $u$ is continuous as a map into $[-\infty, \infty)$, so it is upper semicontinuous.

Example: for $f(z) = z$, $u(z) = \log\abs{z}$ is harmonic off $0$ and equals $-\infty$ at $0$.
Its mean over the circle of radius $r$ about $0$ is $\log r > -\infty = u(0)$.
Composing with the convex increasing function $t \mapsto e^{pt}$ shows that $\abs{f}^p$ is subharmonic for every $p > 0$, by [[convex functions of subharmonic functions|E820CTMJVM]].
The function $\log\abs{f}$ is not harmonic on all of $\Omega$ when $f$ has zeros.
Its Laplacian in the sense of distributions is $2\pi \sum_a m_a \delta_a$, where $a$ runs over the zeros of $f$ and $m_a$ is the multiplicity of $a$.

## Explanations

### L1 human

Take a holomorphic function, look at the size $\abs{f}$ of its values, and take the logarithm.
The result is harmonic, except at the zeros of $f$, where it dives down to $-\infty$.
Those dives only push values below the average, so the function is subharmonic.

### L2 human

This is the main bridge from complex analysis to potential theory.
Applied to $\log\abs{f}$, the maximum principle for subharmonic functions gives the maximum modulus principle, and the convexity results for subharmonic functions give Hadamard's three-circle theorem.
Jensen's formula is the mean value formula for $\log\abs{f}$, with the zeros of $f$ as the correction term.
