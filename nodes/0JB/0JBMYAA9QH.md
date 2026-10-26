---
tag: 0JBMYAA9QH
kind: statement
role: proposition
name: Ratio formula for the radius of convergence
msc: [30B10]
uses: [0660QX1VPR, 0QNY6ZBXPN]
sources:
  - url: https://en.wikipedia.org/wiki/Radius_of_convergence
    locator: Theoretical radius
---

## Statement

Let $\sum a_n (x - c)^n$ be a real power series with $a_n \ne 0$ for all large $n$.
Assume that $|a_{n+1}| / |a_n| \to L$ as $n \to \infty$, for some $L$ in $[0, \infty]$.
Then the [[radius of convergence|0660QX1VPR]] of the series is $R = 1/L$, with the conventions $1/0 = \infty$ and $1/\infty = 0$.

## Remarks

The proof applies the [[ratio test|0QNY6ZBXPN]] to $\sum a_n (x - c)^n$. The ratio of consecutive terms tends to $L |x - c|$.
The formula needs the limit to exist. The [[Cauchy–Hadamard theorem|07E5MB1CA2]] works without this assumption.
For example, $\sum x^n / n!$ has $L = 0$ and $R = \infty$.
Mathlib states a form for nonzero $L$ as `FormalMultilinearSeries.ofScalars_radius_eq_inv_of_tendsto`.

## Explanations

### L1 human

When the ratio of consecutive coefficients settles to $L$, the coefficients behave like $L^n$.
So the series behaves like a geometric series with ratio $L |x - c|$.
