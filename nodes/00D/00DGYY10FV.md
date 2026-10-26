---
tag: 00DGYY10FV
kind: statement
role: theorem
name: The logarithm grows slower than any power
msc: [26A12, 33B10]
uses: [0CT6CBGTYY, 04TSHB9H8D, 0044CPHJBV]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_logarithm
    locator: Definition and properties
---

## Statement

For every real $a > 0$,
$$\lim_{x \to \infty} \frac{\ln x}{x^a} = 0.$$
That is, $\ln x = o(x^a)$ as $x \to \infty$.

## Remarks

Substitute $x = e^{t/a}$. Then $\frac{\ln x}{x^a} = \frac{t / a}{e^{t}}$, which tends to $0$ by [[exponential growth|0CT6CBGTYY]].
In [[little o notation|04TSHB9H8D]], $\ln x = o(x)$. Mathlib states this case as `Real.isLittleO_log_id_atTop`.
Similarly, $x^a \ln x \to 0$ as $x \to 0^+$.

## Explanations

### L1 human

The logarithm goes to infinity, but very slowly.
Each positive power of $x$, even $x^{0.001}$, eventually beats it.
