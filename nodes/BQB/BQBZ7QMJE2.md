---
tag: BQBZ7QMJE2
kind: statement
role: theorem
name: Dahlquist barriers
msc: [65L06, 65L20]
uses: [BX4D85A79P, TDA94C2JYT]
about: [BX4D85A79P]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_multistep_method
---

## Statement

Consider a [[linear $k$-step method|BX4D85A79P]] $\sum_{i=0}^k \alpha_i y_{j+i} = h \sum_{i=0}^k \beta_i f_{j+i}$ with $\alpha_k = 1$ and characteristic polynomials $\rho(\zeta) = \sum_i \alpha_i \zeta^i$, $\sigma(\zeta) = \sum_i \beta_i \zeta^i$, where $\rho$ and $\sigma$ have no common root.
The method has *order* $p$ if $\rho(e^z) - z \sigma(e^z) = O(z^{p+1})$ as $z \to 0$.
It is *zero-stable* if every root of $\rho$ has modulus at most $1$ and the roots of modulus $1$ are simple.
It is *A-stable* if, for every complex $\lambda$ with $\operatorname{Re} \lambda < 0$ and every $h > 0$, every sequence produced by the method for $y' = \lambda y$ tends to $0$.

1. First Dahlquist barrier: a zero-stable linear $k$-step method has order $p \le k + 2$ if $k$ is even, and $p \le k + 1$ if $k$ is odd.
If it is moreover explicit, then $p \le k$.
2. Second Dahlquist barrier: an A-stable linear multistep method has order $p \le 2$, and no explicit linear multistep method is A-stable.

## Remarks

For the first barrier, the substitution $\zeta = \frac{1 + w}{1 - w}$ maps the left half plane $\operatorname{Re} w < 0$ onto the open unit disk.
It turns the order conditions into conditions on the power series of a rational function of $w$.
Zero-stability forces sign conditions on the coefficients that are incompatible with a higher order.
For the second barrier, A-stability means that $\rho(\zeta) - z \sigma(\zeta)$ has all its roots in the open unit disk whenever $\operatorname{Re} z < 0$.
Hence $\operatorname{Re} \frac{\rho(\zeta)}{\sigma(\zeta)} \ge 0$ for $\abs{\zeta} > 1$, and this positivity is incompatible with order greater than $2$.
Example: Simpson's two-step method $y_{j+2} - y_j = \frac{h}{3} (f_{j+2} + 4 f_{j+1} + f_j)$ has order $4 = k + 2$ and is zero-stable, so the first barrier is sharp for $k = 2$.
The trapezoidal rule $y_{j+1} - y_j = \frac{h}{2} (f_{j+1} + f_j)$ has order $2$ and is A-stable, so the second barrier is sharp; among A-stable methods of order $2$ it has the smallest error constant.
The [[backward differentiation formulas|TDA94C2JYT]] of order $3$ to $6$ are zero-stable but not A-stable, as the second barrier requires.

## Explanations

### L1 human

One might hope to make a multistep method more accurate just by using more old values and choosing the weights cleverly.
The first barrier says that this hope fails beyond a fixed limit: past that order, the method becomes unstable and useless.
The second barrier says that methods that are safe for every decaying problem, however stiff, cannot be more than second-order accurate.
So accuracy and stability pull against each other, and the barriers say exactly where.

### L2 human

A $k$-step method can reach order $2k$, but such methods are not zero-stable for $k \ge 3$.
The first barrier explains why practical codes use Adams methods instead, of order $k$ or $k + 1$ for $k$ steps.
The second barrier explains why stiff solvers use [[BDF methods|TDA94C2JYT]].
Above order $2$ these methods give up full A-stability, but they keep stability in a large sector of the left half plane.
It also motivates implicit Runge–Kutta methods, which escape the barrier because they are not linear multistep methods: the Gauss–Legendre methods are A-stable of every even order.
Both barriers were proved by Germund Dahlquist.
