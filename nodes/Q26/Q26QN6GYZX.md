---
tag: Q26QN6GYZX
kind: concept
name: Asymptotic analysis
msc: [41A60, "34E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Asymptotic_analysis
same_as:
  wikidata: Q752718
  wikipedia: Asymptotic analysis
---

## Summary

Asymptotic analysis describes the behaviour of functions near a limit point, such as $x \to \infty$ or a small parameter $\varepsilon \to 0$.
Its basic tools are [[big O|0TGV80E6A4]] and [[little o|00T5EPFQB9]] notation, [[asymptotic equivalence|0QR92XBV6H]] and asymptotic expansions.
An asymptotic expansion need not converge, yet a few of its terms often give an excellent approximation.
In differential equations, it gives approximate solutions when exact ones are out of reach, as in perturbation methods.

## Explanations

### L1 human

Asymptotic analysis asks what a function looks like when its argument becomes very large or very small.
It keeps the main terms and controls the size of what is left out.
For example, $x^2 + 3x + 7$ behaves like $x^2$ for large $x$, since the ratio tends to $1$.
A finer statement is $x^2 + 3x + 7 = x^2 + 3x + O(1)$.
Stirling's formula $n! \sim \sqrt{2 \pi n} \, (n / e)^n$ is a famous result of this kind.
