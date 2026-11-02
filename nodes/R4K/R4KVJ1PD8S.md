---
tag: R4KVJ1PD8S
kind: statement
role: theorem
name: Neumann's addition theorem
msc: [33C10]
uses: [CZCMRDWDYW, 0PHAC833JF]
about: [CZCMRDWDYW]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_function
---

## Statement

Let $n$ be an integer and let $J_k$ denote the [[Bessel function of the first kind|CZCMRDWDYW]] of integer order $k$.
For all $x, y \in \C$,
$$J_n(x + y) = \sum_{k=-\infty}^{\infty} J_k(x)\, J_{n-k}(y),$$
where the series converges absolutely.

## Remarks

The proof uses the [[generating function|0PHAC833JF]] $G(z, t) = \exp\left( \frac{z}{2}\left( t - \frac{1}{t} \right) \right) = \sum_{k \in \Z} J_k(z)\, t^k$.
Since $G(x + y, t) = G(x, t)\, G(y, t)$, multiplying the two Laurent series in $t$ and comparing the coefficients of $t^n$ gives the formula.
Example: with $n = 0$ and $y = -x$, one gets $1 = J_0(0) = \sum_{k} J_k(x) J_{-k}(-x) = \sum_k J_k(x)^2$, using $J_{-k}(-x) = J_k(x)$; so $J_0(x)^2 + 2\sum_{k \ge 1} J_k(x)^2 = 1$.
This identity shows $\abs{J_0(x)} \le 1$ and $\abs{J_k(x)} \le \frac{1}{\sqrt{2}}$ for $k \ge 1$ and real $x$.
The formula as written is for integer orders; for non-integer orders there are related addition theorems of Graf and Gegenbauer.

## Explanations

### L1 human

The value of a Bessel function at a sum $x + y$ is built from its values at $x$ and at $y$.
This is the Bessel analogue of the rule $e^{x+y} = e^x e^y$, and indeed it comes from that rule applied to the generating function.

### L2 human

The theorem is a convolution identity: the sequence $(J_k(x + y))_k$ is the convolution of $(J_k(x))_k$ and $(J_k(y))_k$.
In terms of Fourier series, it says that $e^{i(x+y)\sin\theta} = e^{ix\sin\theta} e^{iy\sin\theta}$, read coefficient by coefficient.
Its consequence $\sum_k J_k(x)^2 = 1$ gives uniform bounds on Bessel functions of integer order on the real line.
