---
tag: 0RDRPBMNAC
kind: statement
role: proposition
name: Cesàro means of a convergent sequence converge
msc: [40G05]
uses: [0P0DJHBGBB, 0XKWSSY8P2]
sources:
  - url: https://en.wikipedia.org/wiki/Cesàro_summation
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Stolz–Cesàro_theorem
    locator: Arithmetic mean
---

## Statement

Let $(a_n)_{n \ge 1}$ be a real sequence that converges to a real number $L$.
For $n \ge 1$, let $\sigma_n = (a_1 + \cdots + a_n)/n$ be its [[Cesàro mean|0P0DJHBGBB]].
Then $\sigma_n \to L$ as $n \to \infty$.

## Remarks

For the proof, let $\varepsilon > 0$ and take $N$ with $|a_k - L| < \varepsilon$ for $k > N$. For $n > N$,
$$|\sigma_n - L| \le \frac{1}{n} \sum_{k=1}^{N} |a_k - L| + \frac{n - N}{n} \varepsilon.$$
The first term tends to $0$, so $|\sigma_n - L| < 2\varepsilon$ for large $n$.
The converse fails. The means of $(-1)^n$ tend to $0$, but $(-1)^n$ diverges.
The statement is a special case of the [[Stolz–Cesàro theorem|0Q3AKZV74D]] with $b_n = n$.

## Explanations

### L1 human

If the terms settle near $L$, then the running average also settles near $L$.
The early terms that are far from $L$ count less and less, because we divide by $n$.
