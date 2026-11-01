---
tag: RGT9HH7SQQ
kind: definition
name: Hardy–Littlewood circle method
msc: [11P55, 11P05]
defines: ZQFBEX62D0
uses: [97PBMQCPPM, 7VWGA444K3, C01Z9QRGZY]
sources:
  - url: https://en.wikipedia.org/wiki/Hardy–Ramanujan–Littlewood_circle_method
---

## Definition

For real $\alpha$ write $e(\alpha) = e^{2\pi i \alpha}$.
Let $\mathcal{S}$ be a finite set of positive integers, and let $s \ge 1$ and $N \ge 1$ be integers.
Let $r(N)$ be the number of $s$-tuples $(x_1, \ldots, x_s) \in \mathcal{S}^s$ with $x_1 + \cdots + x_s = N$.
Let $f(\alpha) = \sum_{x \in \mathcal{S}} e(x\alpha)$, an [[exponential sum|97PBMQCPPM]].
The *circle method* consists of the following steps.

1. Write $r(N) = \int_0^1 f(\alpha)^s\, e(-N\alpha)\, d\alpha$.
2. Choose a parameter $Q$ and split the circle $[0, 1)$ into *major arcs* $\mathfrak{M}$ and *minor arcs* $\mathfrak{m} = [0, 1) \setminus \mathfrak{M}$. The major arcs are the points near a rational $a/q$ with $q \le Q$ and $\gcd(a, q) = 1$.
3. On $\mathfrak{M}$, approximate $f$ by explicit functions to get a main term, usually the product of a singular series and a singular integral.
4. On $\mathfrak{m}$, bound $\abs{f}$ uniformly, for example by Weyl's inequality or Vinogradov's estimates, to show that $\int_{\mathfrak{m}}$ is smaller than the main term.

## Remarks

Step 1 holds because $\int_0^1 e(m\alpha)\, d\alpha$ equals $1$ for $m = 0$ and $0$ for every other integer $m$; expanding $f(\alpha)^s$ gives one term $e((x_1 + \cdots + x_s - N)\alpha)$ for each tuple.
Example: for $\mathcal{S} = \set{1, 2}$, $s = 2$ and $N = 3$, $f(\alpha)^2 e(-3\alpha) = e(-\alpha) + 2 + e(\alpha)$, whose integral is $2$, matching the tuples $(1, 2)$ and $(2, 1)$.
Non-example: the interval of integration must be a full period; $\int_0^{1/2} e(\alpha)\, d\alpha = i/\pi \ne 0$, so integrating over $[0, 1/2)$ does not isolate the solutions.
For [[Waring's problem|7VWGA444K3]], $\mathcal{S}$ is the set of $k$-th powers up to $N$; for [[Vinogradov's theorem|C01Z9QRGZY]], one uses primes weighted by $\log p$.
Hardy and Ramanujan worked with power series $\sum a_n z^n$ and integrals over a circle $\abs{z} = \rho < 1$, which is the origin of the name.
