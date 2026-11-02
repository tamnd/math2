---
tag: KNYSF300GC
kind: definition
name: Incomplete beta function
msc: ["33B20"]
defines: WNVACS2S2Z
uses: [QHNWVSC6AQ]
sources:
  - url: https://en.wikipedia.org/wiki/Beta_function
    locator: Incomplete beta function
---

## Definition

Let $a > 0$ and $b > 0$ be real numbers and let $0 \le x \le 1$.
The *incomplete beta function* is
$$B(x; a, b) = \int_0^x t^{a-1} (1-t)^{b-1}\, dt.$$
The *regularised incomplete beta function* is $I_x(a, b) = B(x; a, b)/B(a, b)$, where $B(a, b) = B(1; a, b)$ is the [[beta function|QHNWVSC6AQ]].

## Remarks

Example: for $a = 2$ and $b = 1$, $B(x; 2, 1) = \int_0^x t\, dt = \frac{x^2}{2}$ and $B(2, 1) = \frac12$, so $I_x(2, 1) = x^2$.

Non-example of a valid argument: for $a = 0$ the integrand is $t^{-1}(1-t)^{b-1}$, whose integral diverges at $0$, so $B(x; 0, b)$ is not defined for $x > 0$.

The function $x \mapsto I_x(a, b)$ increases from $0$ to $1$ and is the distribution function of the [[beta distribution|0EW824Z7G2]] with parameters $a$ and $b$.
The substitution $t \mapsto 1 - t$ gives the symmetry $I_x(a, b) = 1 - I_{1-x}(b, a)$.
For positive integers $a$ and $n$ with $a \le n$, $I_p(a, n - a + 1)$ is the probability of at least $a$ successes in $n$ independent trials with success probability $p$.
