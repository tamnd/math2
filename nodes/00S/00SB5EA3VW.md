---
tag: 00SB5EA3VW
kind: definition
name: Asymptotic equivalence
msc: [41A60]
defines: 0QR92XBV6H
uses: [04TSHB9H8D]
sources:
  - url: https://en.wikipedia.org/wiki/Asymptotic_analysis
    locator: Definition
---

## Definition

Let $f$ and $g$ be real functions defined on an interval $[x_0, \infty)$.
The functions are asymptotically equivalent as $x \to \infty$ if $f(x) - g(x) = o(g(x))$ as $x \to \infty$, in the sense of [[little o notation|04TSHB9H8D]].
We then write $f(x) \sim g(x)$.

## Remarks

If $g(x) \ne 0$ for large $x$, then $f \sim g$ means that $f(x)/g(x) \to 1$.
The relation $\sim$ is an equivalence relation.
For example, $x^2 + x \sim x^2$. [[Stirling's formula|0KC0F51T6A]] states $n! \sim \sqrt{2 \pi n}\, (n/e)^n$.
Mathlib defines it for filters, as `Asymptotics.IsEquivalent`.

## Explanations

### L1 human

Two functions are asymptotically equivalent if their ratio tends to $1$.
Their difference may still grow, but it is small compared with the functions.
