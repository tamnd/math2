---
tag: SWHVQD9YEB
kind: statement
role: theorem
name: Burkholder–Davis–Gundy inequality
msc: [60G44, "60E15"]
uses: [ZWJ9G89W3T, ZBYC3MFW89, WND87FBAKC, 0DCT0QZVQ1]
about: [XC2YPC2BSW, X4DHMZD5JA]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_variation
---

## Statement

Let $p > 0$.
There are constants $0 < c_p \le C_p < \infty$, depending only on $p$, with the following property.
Let $(M_t)_{t \ge 0}$ be a continuous [[local martingale|ZWJ9G89W3T]] with $M_0 = 0$, with [[quadratic variation|ZBYC3MFW89]] $[M]$, and let $\tau$ be a [[stopping time|WND87FBAKC]].
Let $M^*_\tau = \sup_{0 \le s \le \tau} \abs{M_s}$.
Then
$$c_p\, E\bigl[[M]_\tau^{p/2}\bigr] \le E\bigl[(M^*_\tau)^p\bigr] \le C_p\, E\bigl[[M]_\tau^{p/2}\bigr].$$

## Remarks

For $p = 2$ the inequality follows from [[Doob's martingale inequality|4G53E7BRXF]] in its $L^2$ form and the identity $E[M_\tau^2] = E[[M]_\tau]$ for suitable $\tau$, with $c_2 = 1$ and $C_2 = 4$.
For other $p$, one standard proof applies Itô's formula to $\abs{M}^p$ or uses a good-$\lambda$ inequality comparing the laws of $M^*$ and $[M]^{1/2}$.
Example: for a Wiener process $W$ and a fixed time $t$, $[W]_t = t$, so $E[\sup_{s \le t} \abs{W_s}^p]$ is between $c_p t^{p/2}$ and $C_p t^{p/2}$.
For càdlàg local martingales the inequality holds for $p \ge 1$, with the same form.
The constants do not depend on $M$ or $\tau$, and this uniformity is what makes the inequality useful.

## Explanations

### L1 human

The size of the largest swing of a fair game is comparable to the square root of its accumulated squared fluctuations.
Both quantities measure how much the game has moved, and the inequality says they agree up to constant factors.
It holds in every $L^p$ norm.

### L2 human

The inequality lets one bound moments of a stochastic integral $\int_0^t H_s \, dW_s$ by moments of $\int_0^t H_s^2 \, ds$.
It is a key estimate in proving existence, uniqueness and moment bounds for solutions of stochastic differential equations.
It also shows that a continuous local martingale with $E[[M]_\infty^{1/2}] < \infty$ is a uniformly integrable martingale.
