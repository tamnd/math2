---
tag: Q4KF0MAGSC
kind: definition
name: Lacunary series
msc: [42A55, 30B10]
defines: NA3J9XQYGP
uses: [FZK2M8KGXQ, 0D6KXBHKC0]
sources:
  - url: https://en.wikipedia.org/wiki/Lacunary_function
---

## Definition

A strictly increasing sequence $(n_k)_{k \ge 1}$ of positive integers is *lacunary* (in the sense of Hadamard) if there is a number $q > 1$ with
$$\frac{n_{k+1}}{n_k} \ge q \quad \text{for all } k \ge 1.$$
A *lacunary trigonometric series* is a [[trigonometric series|FZK2M8KGXQ]] of the form
$$\sum_{k \ge 1} \left( a_k \cos n_k x + b_k \sin n_k x \right),$$
with real or complex coefficients $a_k, b_k$ and a lacunary sequence $(n_k)$.
A *lacunary power series* is a [[power series|0D6KXBHKC0]] $\sum_{k \ge 1} c_k z^{n_k}$ with a lacunary sequence $(n_k)$.

## Remarks

Example: $\sum_{k \ge 0} 2^{-k} \cos(2^k x)$ is lacunary with $q = 2$, since $2^{k+1}/2^k = 2$.

Non-example: $\sum_{k \ge 1} \frac{\cos(k^2 x)}{k^2}$ has frequencies $n_k = k^2$ with $n_{k+1}/n_k = (1 + 1/k)^2 \to 1$.
So no $q > 1$ is a lower bound for all ratios, and the series is not lacunary in the sense of Hadamard.

A theorem of Sidon says that if a lacunary trigonometric series is the Fourier series of a bounded function, then $\sum_k (\abs{a_k} + \abs{b_k}) < \infty$.
For power series the [[Hadamard gap theorem|DA8M8VZZHC]] applies.
Weaker gap conditions, such as $n_k / k \to \infty$ in the [[Fabry gap theorem|GE0HX2KMMZ]], are also studied.
