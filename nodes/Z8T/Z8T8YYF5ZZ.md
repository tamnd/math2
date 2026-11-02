---
tag: Z8T8YYF5ZZ
kind: example
name: Fourier series of Bernoulli polynomials
msc: [42A16, 11B68]
illustrates: [G12KXDHPPS]
uses: [BXQKBJJGFG, 5NN2YZZR3V, 1XWBY4N0VT]
sources:
  - url: https://en.wikipedia.org/wiki/Bernoulli_polynomials
---

## Example

Let $B_k$ be the $k$-th [[Bernoulli polynomial|BXQKBJJGFG]], and let $k \ge 2$ be an integer.
Then for every $x \in [0, 1]$,
$$B_k(x) = -\frac{k!}{(2\pi i)^k} \sum_{n \in \Z, \, n \ne 0} \frac{e^{2\pi i n x}}{n^k},$$
and the series converges absolutely and uniformly on $[0, 1]$.
So the $1$-periodic function equal to $B_k$ on $[0, 1)$ has the [[Fourier coefficients|5NN2YZZR3V]] $0$ at $n = 0$ and $-\frac{k!}{(2\pi i n)^k}$ at $n \ne 0$, for period $1$.

Check of the coefficients: $\int_0^1 B_k(x) \, dx = 0$ for $k \ge 1$, which gives the coefficient at $n = 0$.
For $n \ne 0$, integration by parts with $B_k' = k B_{k-1}$ and $B_k(1) = B_k(0)$ for $k \ge 2$ gives $\int_0^1 B_k(x) e^{-2\pi i n x} \, dx = \frac{k}{2\pi i n} \int_0^1 B_{k-1}(x) e^{-2\pi i n x} \, dx$.
For $k = 1$, $\int_0^1 (x - \frac{1}{2}) e^{-2\pi i n x} \, dx = -\frac{1}{2\pi i n}$, and induction gives $-\frac{k!}{(2\pi i n)^k}$.
For $k \ge 2$ the coefficients are summable and the periodic extension is continuous, so the series converges uniformly to it.

## Remarks

Grouping $n$ and $-n$ gives real forms; for $k = 2m$ with $m \ge 1$,
$$B_{2m}(x) = (-1)^{m+1} \frac{2 \, (2m)!}{(2\pi)^{2m}} \sum_{n=1}^{\infty} \frac{\cos 2\pi n x}{n^{2m}}.$$
At $x = 0$, where $B_{2m}(0)$ is the Bernoulli number $B_{2m}$, this is Euler's formula $\zeta(2m) = (-1)^{m+1} \frac{(2\pi)^{2m} B_{2m}}{2 \, (2m)!}$ for the [[Riemann zeta function|1XWBY4N0VT]].
For $m = 1$ it gives $\zeta(2) = \frac{\pi^2}{6}$, and for $m = 2$ it gives $\zeta(4) = \frac{\pi^4}{90}$.
For $k = 1$ the same series, $-\sum_{n \ge 1} \frac{\sin 2\pi n x}{\pi n}$, converges to $x - \frac{1}{2}$ only for $0 < x < 1$; at $x = 0$ it gives $0$, the midpoint of the jump.

## Explanations

### L1 human

The Bernoulli polynomials, repeated periodically, have very simple Fourier coefficients: a constant times $1/n^k$.
Reading the formula at a single point turns it into an exact value of a series such as $\sum 1/n^2$ or $\sum 1/n^4$.
This is the cleanest route to the values of the zeta function at even integers.
