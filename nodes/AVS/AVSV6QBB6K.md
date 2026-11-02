---
tag: AVSV6QBB6K
kind: definition
name: Poisson–Mellin–Newton cycle
msc: [44A15, 39A70, 68W40]
defines: Y0PGRJHBYR
uses: [N5PVGRJE1T, 0H5SYBSED9, ZN4NMX1DB4, 0NAHXR1FRH]
sources:
  - url: https://en.wikipedia.org/wiki/N%C3%B8rlund%E2%80%93Rice_integral
---

## Definition

Let $(f_n)_{n \ge 0}$ be a sequence of complex numbers.
The *Poisson–Mellin–Newton cycle* of $(f_n)$ is the following chain of three objects.

1. The *Poisson generating function* $g(t) = e^{-t} \sum_{n \ge 0} f_n \frac{t^n}{n!}$, for $t > 0$ where the series converges.
2. The *Newton coefficients* $b_m = \sum_{k=0}^{m} \binom{m}{k} (-1)^k f_k$, which satisfy $g(t) = \sum_{m \ge 0} b_m \frac{(-t)^m}{m!}$ and $f_n = \sum_{k=0}^{n} \binom{n}{k} (-1)^k b_k$.
3. The [[Mellin transform|N5PVGRJE1T]] $\varphi(s) = \int_0^\infty g(t)\, t^{s-1}\, dt$, where it converges.

Assume that $b_m = b(m)$ for a function $b$ that is [[holomorphic|0NAHXR1FRH]] and of moderate growth in a half-plane.
Then the cycle closes by the relations
$$\varphi(s) = \Gamma(s)\, b(-s), \qquad f_n = \frac{(-1)^n}{2\pi i} \oint_{C} b(s)\, \frac{n!}{s (s - 1) \cdots (s - n)}\, ds,$$
where $C$ is a positively oriented contour that encircles the points $0, 1, \dots, n$ and no singularity of $b$.

## Remarks

The two identities in clause 2 come from multiplying the power series of $e^{-t}$ and $\sum f_n t^n / n!$ and comparing coefficients.
The map $(f_n) \mapsto (b_m)$ is the binomial transform, and it is its own inverse.
The first closing relation is an instance of [[Ramanujan's master theorem|ZN4NMX1DB4]], which needs growth conditions on $b$.
The second is the Nörlund–Rice integral: the residue of $n!\,/\,(s (s-1) \cdots (s-n))$ at $s = k$ is $(-1)^{n-k} \binom{n}{k}$, so the residue theorem gives back $f_n = \sum_k \binom{n}{k} (-1)^k b(k)$.
Here $\Gamma$ is the [[gamma function|0H5SYBSED9]].

Example: $f_n = (1/2)^n$.
Then $g(t) = e^{-t/2}$, the Newton coefficients are $b_m = (1 - 1/2)^m = 2^{-m}$, so $b(s) = 2^{-s}$.
Indeed $\varphi(s) = 2^{s}\, \Gamma(s) = \Gamma(s)\, b(-s)$ for $\operatorname{Re} s > 0$.

Non-example: for $f_n = (n!)^2$ the series $\sum_n f_n t^n / n!$ diverges for every $t > 0$, so there is no Poisson generating function and the cycle does not start.
