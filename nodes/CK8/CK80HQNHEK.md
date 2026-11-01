---
tag: CK80HQNHEK
kind: definition
name: q-analog
msc: [05A30, 11B65]
defines: GFSDMJHHVA
uses: [0BQMWCNS8S]
sources:
  - url: https://en.wikipedia.org/wiki/Q-analog
---

## Definition

Let $q$ be an indeterminate, or a complex number close to $1$.
A *q-analog* of an expression $E$ is an expression $E_q$, depending on $q$, such that $\lim_{q \to 1} E_q = E$.
A q-analog of an identity or a theorem is an identity or a theorem about q-analogs that reduces to the original one as $q \to 1$.
For an integer $n \ge 0$, the *q-integer* is
$$[n]_q = \frac{1 - q^n}{1 - q} = 1 + q + \cdots + q^{n-1},$$
and the *q-factorial* is $[n]_q! = [1]_q [2]_q \cdots [n]_q$, with $[0]_q! = 1$.

## Remarks

Example: $[n]_q$ is a q-analog of $n$, since $1 + q + \cdots + q^{n-1} \to n$ as $q \to 1$.
Likewise $[n]_q!$ is a q-analog of $n!$.
It is the generating function of the number of inversions over the [[permutations|0BQMWCNS8S]] of $\set{1, \ldots, n}$: $[n]_q! = \sum_{\pi} q^{\operatorname{inv}(\pi)}$.
For $n = 3$, the inversion numbers are $0, 1, 1, 2, 2, 3$, and $[3]_q! = (1)(1 + q)(1 + q + q^2) = 1 + 2q + 2q^2 + q^3$.

Non-example: $q^n$ is not a q-analog of $n$, since $q^n \to 1$ as $q \to 1$, and $1 \ne n$ for $n \ne 1$.

The definition by a limit alone does not fix a unique q-analog.
In practice a q-analog is chosen because it keeps the structure of the original, such as a recurrence or a combinatorial meaning.
Main examples are the [[Gaussian binomial coefficients|YS09Z1YNEK]], the q-Pochhammer symbol and the q-binomial theorem.
