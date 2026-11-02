---
tag: 6YT8ZM6B0F
kind: statement
role: lemma
name: Abel's lemma for multiple power series
msc: [32A05]
uses: [R3QTCPTJK7, DJBWP7D3M8, 08VZ57PT26]
about: [R3QTCPTJK7]
sources:
  - url: https://en.wikipedia.org/wiki/Function_of_several_complex_variables
---

## Statement

Let $\sum_{\alpha \in \N^n} c_\alpha z^\alpha$ be a [[power series in several variables|R3QTCPTJK7]] with centre $0$.
Let $w \in \C^n$ and $M \ge 0$ be such that $\abs{c_\alpha w^\alpha} \le M$ for every $\alpha \in \N^n$.
Let $0 < \rho < 1$ and $K_\rho = \set{z \in \C^n : \abs{z_j} \le \rho \abs{w_j} \text{ for } j = 1, \dots, n}$.
Then $\sum_\alpha \abs{c_\alpha z^\alpha} \le M (1 - \rho)^{-n}$ for every $z \in K_\rho$, and the series converges absolutely and [[uniformly|08VZ57PT26]] on $K_\rho$.

## Remarks

For $z \in K_\rho$ one has $\abs{c_\alpha z^\alpha} \le \abs{c_\alpha w^\alpha} \rho^{\abs{\alpha}} \le M \rho^{\abs{\alpha}}$, and $\sum_{\alpha \in \N^n} \rho^{\abs{\alpha}} = (1 - \rho)^{-n}$ is a product of $n$ geometric series; the Weierstrass M-test concludes.
If all $w_j \ne 0$, every compact subset of the [[polydisc|DJBWP7D3M8]] $\set{\abs{z_j} < \abs{w_j}}$ lies in some $K_\rho$, so the series converges absolutely there, uniformly on compact subsets.
In particular, convergence at one point $w$ with all $w_j \ne 0$ already gives convergence on this whole open polydisc.
Example: for $\sum_{k \ge 0} (z_1 z_2)^k$ and $w = (2, 1/2)$, all terms have modulus $1$, so the series converges on $\set{\abs{z_1} < 2, \abs{z_2} < 1/2}$.
The same series also converges on $\set{\abs{z_1} < 1/2, \abs{z_2} < 2}$, so its domain of convergence $\set{\abs{z_1 z_2} < 1}$ is larger than any single polydisc given by the lemma.

## Explanations

### L1 human

If the terms of a power series stay bounded at one point, the series converges at every point that is strictly smaller in each coordinate.
The reason is that the terms are then dominated by a convergent geometric series.
This is the same idea as for power series in one variable, done coordinate by coordinate.

### L2 human

The lemma is the first step in describing where a power series converges.
It shows that the domain of convergence is a union of polydiscs centred at $0$, hence a complete Reinhardt domain.
Combined with Hölder's inequality it gives the [[logarithmic convexity of the domain of convergence|D8S8JWE45R]].
It also shows that the sum is a uniform limit of polynomials on compact sets, hence holomorphic.
