---
tag: ~a6ebaeb5
kind: statement
role: theorem
name: Power series converge uniformly on smaller discs inside the radius of convergence
msc: [30B10, 40A30]
uses: [~9b386670, ~83292ea3, ~2034293f]
sources:
  - url: https://en.wikipedia.org/wiki/Radius_of_convergence
    locator: Definition
---

## Statement

Let $\sum_{n=0}^{\infty} a_n (x - c)^n$ be a [[power series|~9b386670]] with [[radius of convergence|~83292ea3]] $R > 0$.
Then for every $r$ with $0 < r < R$, the series converges absolutely and uniformly on $[c - r, c + r]$.

## Remarks

Choose $s$ with $r < s < R$. The series converges at $c + s$, so $|a_n| s^n \le C$ for some $C$. The [[M-test|~2034293f]] with $M_n = C (r/s)^n$ applies.
So the sum is continuous on $(c - R, c + R)$.
The convergence need not be uniform on the whole interval: $\sum x^n$ is not uniformly convergent on $(-1, 1)$. Mathlib states the result as `HasFPowerSeriesOnBall.tendstoUniformlyOn`.

## Explanations

### L1 human

Inside the interval of convergence, a power series converges uniformly once we stay away from the endpoints.
Near the endpoints, the convergence can get slower and slower.
