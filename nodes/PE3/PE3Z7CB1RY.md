---
tag: PE3Z7CB1RY
kind: definition
name: Absolute summability
msc: [40F05, 40C05]
defines: A82GRSZMVW
uses: [M6311DWJ1E, 0NB643K60Q, 0YBDSJARWN, N8ZGG7EW6J]
sources:
  - url: https://en.wikipedia.org/wiki/Absolute_convergence
---

## Definition

Let $A = (a_{nk})_{n, k \ge 0}$ be an infinite matrix of real or complex numbers, viewed as a [[matrix summability method|M6311DWJ1E]].
Let $\sum_{k \ge 0} a_k$ be a series with [[partial sums|0NB643K60Q]] $s_k = a_0 + \dots + a_k$.
Assume that for every $n$ the series $t_n = \sum_{k \ge 0} a_{nk} s_k$ converges.
The series $\sum a_k$ is *absolutely $A$-summable* (or $\abs{A}$-summable) if
$$\sum_{n \ge 1} \abs{t_n - t_{n-1}} < \infty.$$

## Remarks

If $\sum_{n \ge 1} \abs{t_n - t_{n-1}}$ is finite, then $(t_n)$ is a Cauchy sequence, so it converges.
Thus an absolutely $A$-summable series is $A$-summable.

Example: for the identity matrix, $t_n = s_n$ and $t_n - t_{n-1} = a_n$.
So absolute summability by the identity method is [[absolute convergence|0YBDSJARWN]].

Non-example: Grandi's series $1 - 1 + 1 - \cdots$ is [[Cesàro summable|N8ZGG7EW6J]] to $1/2$, but not absolutely Cesàro summable.
Its partial sums are $1, 0, 1, 0, \dots$, so the Cesàro means are $t_{2m} = (m + 1)/(2m + 1)$ and $t_{2m+1} = 1/2$.
Then $\abs{t_{2m} - t_{2m-1}} = 1/(2(2m + 1))$, and the sum of these numbers diverges.

For the Cesàro method the notation is $\abs{C, 1}$.
For Abel summation one says that $\sum a_n$ is absolutely Abel summable when $x \mapsto \sum a_n x^n$ has bounded variation on $[0, 1)$.
