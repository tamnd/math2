---
tag: WQRT86VYA6
kind: statement
role: theorem
name: Jackson's inequality
msc: [41A17, 42A10, 41A25]
uses: [J3NJQ5FZJ5, AXCJBSQZWF, 0ATF6Q0633, YDN0T4MEX0, 9MZFTX77CD]
about: [TDKKST5AWA]
sources:
  - url: https://en.wikipedia.org/wiki/Jackson%27s_inequality
same_as:
  wikidata: Q4317418
  wikipedia: Jackson's inequality
---

## Statement

Let $r \ge 0$ be an integer.
For a continuous $2\pi$-[[periodic function|0ATF6Q0633]] $g$, let $\omega(g, \delta) = \sup_{\abs{x - y} \le \delta} \abs{g(x) - g(y)}$ be its [[modulus of continuity|AXCJBSQZWF]].
For $n \ge 1$, let $E_n(f) = \inf_T \max_x \abs{f(x) - T(x)}$, the infimum over real [[trigonometric polynomials|J3NJQ5FZJ5]] $T$ of degree at most $n$.
Then there is a constant $C_r$, depending only on $r$, such that every $2\pi$-periodic $f$ with $r$ continuous derivatives satisfies
$$E_n(f) \le \frac{C_r}{n^r} \, \omega\left(f^{(r)}, \frac{1}{n}\right) \qquad \text{for all } n \ge 1.$$

## Remarks

Proof idea for $r = 0$: approximate $f$ by its convolution with the [[Jackson kernel|9MZFTX77CD]] $J_m$ of degree at most $n$.
The kernel is nonnegative with mean $1$, so $\abs{f - f * J_m} \le \frac{1}{2\pi} \int \omega(f, \abs{t}) J_m(t) \, dt$.
With $\omega(f, \abs{t}) \le (1 + n\abs{t}) \, \omega(f, 1/n)$ and $\frac{1}{2\pi} \int \abs{t} J_m(t) \, dt = O(1/n)$, the bound follows.
The case $r \ge 1$ follows by induction on $r$, using $E_n(f) \le \frac{C}{n} E_n(f')$ for continuously differentiable $2\pi$-periodic $f$.

Example: if $f$ is Lipschitz with constant $L$, then $\omega(f, 1/n) \le L/n$, so $E_n(f) \le C_0 L / n$.

The same bounds hold for algebraic polynomials of degree at most $n$ on $[-1, 1]$ when $r = 0$, through the substitution $x = \cos \theta$.
For $\abs{f^{(r)}} \le 1$ with $r \ge 1$, the sharp bound is $E_n(f) \le K_r / (n + 1)^r$, where $K_r$ is the [[Favard constant|9K1W9Q49NR]], by [[Favard's theorem|JYX6N8A2P6]].

## Explanations

### L1 human

The smoother a periodic function is, the better trigonometric polynomials of a given degree can approximate it.
Jackson's inequality makes this precise: each derivative gains a factor $1/n$, and the modulus of continuity of the last derivative gives the rest.

### L2 human

This is the basic direct theorem of approximation theory.
Its converse, Bernstein's inverse theorem, shows that the rates it gives are the right ones when $0 < \alpha < 1$ in the Hölder scale.
Together with [[Bernstein's inequality|F0YGC89S9R]], it underlies the characterisation of smoothness classes by approximation rates.
For interpolation and Fourier partial sums, it combines with Lebesgue constants to give convergence results such as the Dini–Lipschitz test.
