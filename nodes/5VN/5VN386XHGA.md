---
tag: 5VN386XHGA
kind: statement
role: theorem
name: High indices theorem
msc: ["40E15", "40E05"]
uses: [EZXPY4A19C, 0CVVKY7GY2, 0S4EMDQS2F, 8SK3GQ4S0M, DA8M8VZZHC]
about: [D6XWK1NRY1, EZXPY4A19C]
sources:
  - url: https://en.wikipedia.org/wiki/Lacunary_function
---

## Statement

Let $(n_k)_{k \ge 1}$ be a strictly increasing sequence of positive integers, and assume there is a real $q > 1$ with $n_{k+1} / n_k \ge q$ for all $k$.
Let $(a_k)_{k \ge 1}$ be complex numbers such that the power series
$$f(x) = \sum_{k \ge 1} a_k x^{n_k}$$
converges for $0 \le x < 1$, and assume $f(x) \to s$ as $x \to 1^-$.
Then the series $\sum_{k \ge 1} a_k$ [[converges|0CVVKY7GY2]] and its sum is $s$.

## Remarks

In the language of [[Abel summation|EZXPY4A19C]], the theorem says that a series with Hadamard gaps that is Abel summable is convergent.
So the gap condition acts as a Tauberian condition, and no condition on the size of the coefficients $a_k$ is needed.
The proof is considerably harder than that of [[Tauber's theorem|8SK3GQ4S0M]].
The gap hypothesis cannot be dropped: $\sum_{n \ge 0} (-1)^n x^n = 1/(1 + x) \to 1/2$ as $x \to 1^-$, but $\sum (-1)^n$ diverges.
As a consequence, $f(x) = \sum_{k \ge 0} (-1)^k x^{2^k}$ has no limit as $x \to 1^-$, because $\sum_k (-1)^k$ diverges.

## Explanations

### L1 human

A power series with very sparse exponents, such as $x^2, x^4, x^8, \dots$, cannot hide divergence behind smoothing.
If its value approaches a limit as $x$ goes up to $1$, then the series of coefficients already converges to that limit.
For ordinary series this is false, so the theorem shows how strong a constraint sparse exponents are.

### L2 human

[[Abel's theorem|0S4EMDQS2F]] goes from convergence to Abel summability, and Tauberian theorems go back under extra hypotheses.
Usual Tauberian conditions bound the terms, as in $n a_n = O(1)$.
Here the extra hypothesis is only on where the nonzero terms sit.
The same gap condition appears in the [[Hadamard gap theorem|DA8M8VZZHC]], where it forces the unit circle to be a natural boundary.
