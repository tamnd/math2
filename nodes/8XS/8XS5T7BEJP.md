---
tag: 8XS5T7BEJP
kind: definition
name: Statistical convergence
msc: [40A35, "11B05"]
defines: ZW6EHSMANH
uses: [0QE8STGJH2, RVG9Z8NYA6, 0W4CN9E2W5, 750MCA763X]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_density
---

## Definition

Let $(x_n)_{n \ge 1}$ be a [[sequence|0QE8STGJH2]] of real or complex numbers and let $L$ be a number.
The sequence *converges statistically* to $L$ if for every $\varepsilon > 0$ the set
$$\set{n \ge 1 : \abs{x_n - L} \ge \varepsilon}$$
has [[natural density|RVG9Z8NYA6]] $0$.

## Remarks

Every [[convergent sequence|0W4CN9E2W5]] with limit $L$ converges statistically to $L$, since each of the sets above is finite and finite sets have density $0$.
The statistical limit is unique when it exists.

Example: let $x_n = 1$ if $n$ is a perfect square and $x_n = 0$ otherwise.
For $0 < \varepsilon \le 1$, the set of $n$ with $\abs{x_n} \ge \varepsilon$ is the set of squares, which has at most $\sqrt{N}$ elements up to $N$, so its density is $0$.
Hence $(x_n)$ converges statistically to $0$, although it does not converge.

Non-example: $x = (1, 0, 1, 0, \dots)$ does not converge statistically.
For any $L$, one of $\abs{1 - L}$ and $\abs{L}$ is at least $1/2$.
So for $\varepsilon = 1/2$ the set above contains all odd or all even $n$, and its density is not $0$.

A sequence converges statistically to $L$ if and only if there is a set $K$ of density $1$ such that $x_n \to L$ as $n \to \infty$ through $K$.
A bounded sequence converges statistically to $L$ if and only if $\frac{1}{n} \sum_{k=1}^{n} \abs{x_k - L} \to 0$, which is the condition of [[strong Cesàro summability|750MCA763X]] with exponent $1$ applied to the sequence $(x_n)$.
