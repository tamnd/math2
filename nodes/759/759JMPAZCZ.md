---
tag: 759JMPAZCZ
kind: definition
name: Advanced Z-transform
msc: [44A55, 93C57]
defines: K0V6T18367
uses: [EPG6JPVJE7, 5FY0JQGHYZ]
sources:
  - url: https://en.wikipedia.org/wiki/Advanced_z-transform
---

## Definition

Let $f \colon [0, \infty) \to \C$ be a function, let $T > 0$ be a sampling period, and let $m$ be a real number with $0 \le m \le T$.
The *advanced Z-transform* of $f$ is
$$F(z, m) = \sum_{k = 0}^{\infty} f(kT + m) \, z^{-k},$$
for the complex $z$ where the series converges absolutely.
So $F(\cdot, m)$ is the [[unilateral Z-transform|EPG6JPVJE7]] of the sequence $(f(kT + m))_{k \ge 0}$.

## Remarks

For $m = 0$ it is the ordinary [[Z-transform|5FY0JQGHYZ]] of the samples $f(kT)$.
Example: for $f(t) = e^{-at}$ with $a \in \C$, $F(z, m) = e^{-am} \sum_{k \ge 0} (e^{-aT} z^{-1})^k = e^{-am} \, z/(z - e^{-aT})$ for $\abs{z} > \abs{e^{-aT}}$.
For $f(t) = t$, $F(z, m) = \sum_{k \ge 0} (kT + m) z^{-k} = Tz/(z - 1)^2 + m z/(z - 1)$ for $\abs{z} > 1$.
Non-example: the sum $\sum_k f(k T + m) z^{-k}$ with $m$ outside $[0, T]$ is not covered; for $m = T$ it is not a new transform either, since $F(z, T) = z (F(z, 0) - f(0))$.
Some texts call a closely related transform, with a delay parameter in place of the advance, the modified Z-transform.
