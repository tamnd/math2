---
tag: BXQARMFY75
kind: statement
role: theorem
name: Mehler–Heine formula
msc: [33C45, 33C10]
uses: [QFYGJVA996, CZCMRDWDYW, TRD7DSF2KR]
about: [QFYGJVA996, CZCMRDWDYW]
sources:
  - url: https://en.wikipedia.org/wiki/Mehler–Heine_formula
same_as:
  wikidata: Q17098827
  wikipedia: Mehler–Heine formula
---

## Statement

Let $P_n$ be the [[Legendre polynomial|QFYGJVA996]] of degree $n$ and let $J_0$ be the [[Bessel function of the first kind|CZCMRDWDYW]] of order $0$.
Then
$$\lim_{n \to \infty} P_n\left( \cos \frac{z}{n} \right) = J_0(z),$$
uniformly for $z$ in each bounded subset of $\C$.

## Remarks

Proof idea: write $P_n(\cos \theta) = {}_2F_1\left( -n, n + 1; 1; \sin^2 \frac{\theta}{2} \right) = \sum_{k=0}^{n} \frac{(-n)_k (n + 1)_k}{(k!)^2} \sin^{2k} \frac{\theta}{2}$.
With $\theta = z/n$ and $k$ fixed, $(-n)_k (n + 1)_k \sim (-1)^k n^{2k}$ and $\sin^{2k} \frac{z}{2n} \sim \left( \frac{z}{2n} \right)^{2k}$.
So the $k$-th term tends to $\frac{(-1)^k}{(k!)^2} \left( \frac{z}{2} \right)^{2k}$, the $k$-th term of the series of $J_0(z)$, and a domination argument allows the termwise limit.
The same holds for [[Jacobi polynomials|TRD7DSF2KR]]: $\lim_{n \to \infty} n^{-\alpha} P_n^{(\alpha, \beta)}\left( \cos \frac{z}{n} \right) = \left( \frac{z}{2} \right)^{-\alpha} J_\alpha(z)$.
A consequence via Hurwitz's theorem: if $\theta_{n,k}$ is the $k$-th smallest zero of $\theta \mapsto P_n(\cos \theta)$ in $(0, \pi)$, then $n \theta_{n,k} \to j_{0,k}$, the $k$-th positive zero of $J_0$.

## Explanations

### L1 human

Near the end point $x = 1$, a Legendre polynomial of high degree oscillates faster and faster.
If one zooms in at the right scale, with the angle shrinking like $1/n$, the picture settles down to a fixed wave.
This limiting wave is the Bessel function $J_0$.

### L2 human

The formula describes the behaviour of orthogonal polynomials at the edge of their interval, where the oscillatory asymptotics in the interior break down.
In the interior, the classical asymptotic formulas give cosine waves with slowly varying amplitude; near $x = \pm 1$ Bessel functions take their place.
It explains why the zeros of $P_n$ closest to $1$, measured in the angle $\theta$, are about $j_{0,k}/n$.
Its versions for Jacobi and Laguerre polynomials, and their analogues for random matrices, describe the "hard edge" behaviour of eigenvalues.
