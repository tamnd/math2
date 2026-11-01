---
tag: EYXG11V76E
kind: statement
role: theorem
name: Cauchy formula for repeated integration
msc: [26A42, 26A33]
uses: [0X3WGX95FE, 0WZCHE1ZF9, 0NHGY0N0JB]
about: [0WZCHE1ZF9]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_formula_for_repeated_integration
same_as:
  wikidata: Q1429231
  wikipedia: Cauchy formula for repeated integration
---

## Statement

Let $a < b$ be real numbers, let $f \colon [a, b] \to \R$ be [[continuous|0X3WGX95FE]], and let $n \ge 1$ be an integer.
Define $F_0 = f$ and $F_k(x) = \int_a^x F_{k-1}(t) \, dt$ for $k \ge 1$ and $x \in [a, b]$.
Then for all $x \in [a, b]$,
$$F_n(x) = \frac{1}{(n - 1)!} \int_a^x (x - t)^{n - 1} f(t) \, dt.$$

## Remarks

The proof is by induction on $n$.
The case $n = 1$ is the definition.
For the step, note that both sides vanish at $x = a$.
Differentiating the right side under the integral sign gives the same formula with $n - 1$ in place of $n$.
The [[fundamental theorem of calculus|0NHGY0N0JB]] then gives equality.
Equivalently, one writes $F_n$ as an [[iterated integral|0WZCHE1ZF9]] over a simplex and integrates out all variables but the last one.
Example: for $f = 1$, $a = 0$ and $n = 2$, the right side is $\int_0^x (x - t) \, dt = x^2 / 2$, which is the twice repeated integral of $1$.

## Explanations

### L1 human

Integrating a function $n$ times in a row seems to need $n$ nested integrals.
Cauchy's formula collapses them into one integral with the weight $(x - t)^{n-1} / (n - 1)!$.

### L2 human

The formula is used in the proof of [[Taylor's theorem|03QHBVW4TT]] with the integral remainder.
Replacing $(n - 1)!$ by $\Gamma(n)$ and letting $n$ be any positive real number gives the [[Riemann–Liouville integral|JTKCZ44NN3]], the starting point of [[fractional calculus|T73XK15SA2]].
