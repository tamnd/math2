---
tag: 0CT6CBGTYY
kind: statement
role: theorem
name: Exponential growth beats polynomial growth
msc: [26A12, 33B10]
uses: [0RMVS7RXZX, 0Y12QYTJK3]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_growth
    locator: Other growth rates
---

## Statement

For every natural number $n$,
$$\lim_{x \to \infty} \frac{e^x}{x^n} = \infty.$$

## Remarks

For $x > 0$, the series gives $e^x > \frac{x^{n+1}}{(n+1)!}$. So $\frac{e^x}{x^n} > \frac{x}{(n+1)!}$, which [[tends to infinity|0Y12QYTJK3]].
Equivalently, $x^n e^{-x} \to 0$ as $x \to \infty$. The same holds for real exponents $n$.
So for each polynomial $p$, $p(x) e^{-x} \to 0$ as $x \to \infty$. Mathlib states the main claim as `Real.tendsto_exp_div_pow_atTop`.

## Explanations

### L1 human

The exponential function eventually grows faster than every power of $x$.
For example, $e^x > x^{10}$ for all $x \ge 36$, but not for $x = 35$.
