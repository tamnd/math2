---
tag: KWJS2QYJ1K
kind: statement
role: theorem
name: Stanley–Wilf conjecture
msc: [05A05, 05A16]
uses: [1H8Z1WMG23, 05RWFKVTJ7]
about: [1H8Z1WMG23]
sources:
  - url: https://en.wikipedia.org/wiki/Stanley%E2%80%93Wilf_conjecture
same_as:
  wikidata: Q7600088
  wikipedia: Stanley–Wilf conjecture
---

## Statement

Let $\sigma$ be a [[permutation|05RWFKVTJ7]] of $\set{1, \ldots, k}$ for some $k \ge 1$.
For $n \ge 1$, let $\operatorname{Av}_n(\sigma)$ be the set of permutations of $\set{1, \ldots, n}$ that avoid $\sigma$ as a [[pattern|1H8Z1WMG23]].
Then there is a constant $c_\sigma$ such that $\abs{\operatorname{Av}_n(\sigma)} \le c_\sigma^{\,n}$ for all $n \ge 1$.

## Remarks

The conjecture was proved by Adam Marcus and Gábor Tardos in 2004.
They proved the Füredi–Hajnal conjecture on $0$-$1$ matrices that avoid a permutation matrix, and Martin Klazar had shown earlier that it implies the Stanley–Wilf conjecture.
The bound means that the limit $L(\sigma) = \lim_{n \to \infty} \abs{\operatorname{Av}_n(\sigma)}^{1/n}$ is finite; Arratia showed that this limit exists.
The number $L(\sigma)$ is the Stanley–Wilf limit of $\sigma$.

Example: for $\sigma = 123$, $\abs{\operatorname{Av}_n(123)}$ is the [[Catalan number|0YWZJEABB2]] $C_n \le 4^n$, so $c_{123} = 4$ works and $L(123) = 4$.

Without a forbidden pattern the statement fails, since there are $n!$ permutations of $\set{1, \ldots, n}$, and $n!$ grows faster than $c^n$ for each constant $c$.

## Explanations

### L1 human

Forbidding a single pattern is a strong restriction on a long permutation.
The theorem makes this precise: the number of permutations that avoid a fixed pattern grows only exponentially in $n$.
Without restriction there are $n!$ permutations, which grow much faster.

### L2 human

For patterns of length $3$ the counts are Catalan numbers, but for longer patterns exact formulas are rare.
The theorem says that every pattern class has finite exponential growth rate, the Stanley–Wilf limit.
The proof by Marcus and Tardos is short and goes through extremal problems for $0$-$1$ matrices.
