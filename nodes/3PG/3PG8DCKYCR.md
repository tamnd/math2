---
tag: 3PG8DCKYCR
kind: definition
name: Pseudorandom generator
msc: [68Q87, 68Q10, 68W20]
defines: MD9THSA21A
uses: [SQXNFGVADX]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudorandom_generator
---

## Definition

Let $\ell, s \colon \N \to \N$ and let $\varepsilon > 0$.
Let $G_n \colon \set{0,1}^{\ell(n)} \to \set{0,1}^n$ be functions, one for each $n \ge 1$.
The family $(G_n)$ is a *pseudorandom generator* against circuits of size $s$ with error $\varepsilon$ if the following holds.
Let $n \ge 1$ and let $C$ be a [[Boolean circuit|SQXNFGVADX]] with $n$ inputs and size at most $s(n)$.
Then
$$\Big| \Pr_{y}\big[C(G_n(y)) = 1\big] - \Pr_{z}\big[C(z) = 1\big] \Big| < \varepsilon,$$
where $y$ is uniform in $\set{0,1}^{\ell(n)}$ and $z$ is uniform in $\set{0,1}^n$.
The function $\ell$ is the *seed length*.
For derandomization one also asks that $G_n$ be computable in time $2^{O(\ell(n))}$.

## Remarks

Example: the identity map $G_n(y) = y$ with $\ell(n) = n$ is a generator against all circuits with error $\varepsilon$ for every $\varepsilon > 0$.
The two distributions are equal, so the difference is $0$; the generator is useless because it does not stretch.

Non-example: the map $G_n(y) = y y_1$, which repeats the first bit, with $\ell(n) = n - 1$, fails for every $\varepsilon \le 1/2$ as soon as $s(n) \ge 5$.
The circuit $(z_1 \wedge z_n) \vee (\neg z_1 \wedge \neg z_n)$, with five gates, tests whether the first and last bits are equal; it accepts every output of $G_n$ but only half of all strings.

If there is a generator against circuits of size $n$ with error $1/10$, seed length $O(\log n)$, computable in time polynomial in $n$, then $\mathrm{BPP} = \mathrm{P}$.
Impagliazzo and Wigderson showed that such generators exist if some problem in $\mathrm{E} = \mathrm{DTIME}(2^{O(n)})$ requires circuits of size $2^{\Omega(n)}$.

In cryptography a pseudorandom generator must instead be computable in polynomial time and fool every polynomial-size circuit with error smaller than any inverse polynomial for large $n$, with $\ell(n) < n$.
Such generators exist if and only if [[one-way functions|RA37YDW2TY]] exist.
