---
tag: RQYX6E42D0
kind: definition
name: Borel summation
msc: ["40G10", "30E15"]
defines: 8DJPSYSHGJ
uses: [0JH4MN4K1C, 0VP56B4EMX, 0660QX1VPR, 0M3YQJ81NB, 05XT5AVJBK]
sources:
  - url: https://en.wikipedia.org/wiki/Borel_summation
---

## Definition

Let $\sum_{k \ge 0} a_k$ be a [[series|0JH4MN4K1C]] of complex numbers.
Its *Borel transform* is the [[power series|0VP56B4EMX]]
$$\mathcal{B}(t) = \sum_{k \ge 0} \frac{a_k}{k!} t^k.$$
The series $\sum_k a_k$ is *Borel summable* if:

1. $\mathcal{B}$ has a positive [[radius of convergence|0660QX1VPR]];
2. $\mathcal{B}$ has an [[analytic continuation|0M3YQJ81NB]] to an open set that contains the half-line $[0, \infty)$, still written $\mathcal{B}$;
3. the improper integral $\int_0^\infty e^{-t} \mathcal{B}(t) \, dt$ converges.

The value of this integral is the *Borel sum* of the series.

## Remarks

Example: for $a_k = z^k$ with a complex number $z$, $\mathcal{B}(t) = e^{zt}$, and the integral converges exactly when $\operatorname{Re} z < 1$, with value $1/(1 - z)$.
So the geometric series is Borel summable to $1/(1-z)$ on the half-plane $\operatorname{Re} z < 1$, also where it diverges, such as at $z = -1$, where the sum is $1/2$.
Non-example: for $a_k = (k!)^2$, the Borel transform $\sum_k k! \, t^k$ has radius of convergence $0$, so clause 1 fails.
The method is regular: a convergent series is Borel summable, and its Borel sum is its ordinary sum.
For a power series $\sum_k a_k z^k$, the Borel sum is $\int_0^\infty e^{-t} \mathcal{B}(zt) \, dt$, which is a [[Laplace transform|05XT5AVJBK]] of $\mathcal{B}$ up to a change of variable.
A weaker variant, the weak Borel method, uses the limit of $e^{-t} \sum_{n \ge 0} s_n t^n/n!$ as $t \to \infty$, where $s_n$ are the partial sums.
