---
tag: ~ef08fdf5
kind: statement
role: theorem
name: The gamma function extends the factorial
msc: [33B15]
uses: [~9284c63c, ~d8fc6f04, ~7559c6fd]
sources:
  - url: https://en.wikipedia.org/wiki/Gamma_function
    locator: General
---

## Statement

For each $s > 0$, the [[gamma function|~9284c63c]] satisfies $\Gamma(s + 1) = s \, \Gamma(s)$.
For each natural number $n$, $\Gamma(n + 1) = n!$.

## Remarks

[[Integration by parts|~d8fc6f04]] on $[\varepsilon, b]$, with $u = t^s$ and $v = -e^{-t}$, gives the recursion in the limit.
The [[integral of $e^{-t}$|~7559c6fd]] gives $\Gamma(1) = 1$. Induction on $n$ then gives $\Gamma(n + 1) = n!$.
Also $\Gamma(1/2) = \sqrt{\pi}$, by the substitution $t = x^2$ and the Gaussian integral.
Mathlib states it as `Real.Gamma_nat_eq_factorial`.

## History

Leonhard Euler announced the integral representation in a letter to Christian Goldbach, dated 8 January 1730.

## Explanations

### L1 human

The recursion $\Gamma(s + 1) = s \, \Gamma(s)$ is the same as the rule $(n + 1)! = (n + 1) \cdot n!$.
So the gamma function agrees with the factorial at the integers, shifted by one.
