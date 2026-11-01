---
tag: N155BSJ2DN
kind: concept
name: Operator monotone function
msc: [47A63, 15A45, 26A48]
specializes: [0A7KV2WB7A]
sources:
  - url: https://en.wikipedia.org/wiki/Operator_monotone_function
same_as:
  wikidata: Q55627738
  wikipedia: Operator monotone function
---

## Summary

A real function $f$ on an interval is operator monotone if it keeps the order between [[Hermitian matrices|0P17NGQQMQ]]: from $A \le B$ it follows that $f(A) \le f(B)$.
Here $A \le B$ is the [[Loewner order|9G9S92T1VJ]], and $f(A)$ is defined through the eigenvalues of $A$.
Every operator monotone function is a [[monotone function|0A7KV2WB7A]], but the converse fails, so operator monotonicity is a much stronger condition.
[[Löwner's theorem|PA7ZQ6C6SP]] describes these functions through complex analysis.

## Explanations

### L1 human

For numbers, an increasing function keeps the order: if $a \le b$ then $f(a) \le f(b)$.
Hermitian matrices can also be compared: $A \le B$ means that $B - A$ has no negative eigenvalues.
An operator monotone function is one that keeps this matrix order, for matrices of every size.
The square root $\sqrt{t}$ and the logarithm $\log t$ on $(0, \infty)$ do this, while the square $t^2$ does not, even though it is increasing on $[0, \infty)$.
