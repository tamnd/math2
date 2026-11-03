---
tag: 4HJT57DSKX
kind: definition
name: Lambda-ring
msc: ["19L20", "13D15", "19E08"]
defines: E2KA3XP47F
uses: [0310REJJY8, 0X5QVCF06N, 0SDC934R52]
sources:
  - url: https://en.wikipedia.org/wiki/Λ-ring
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] with $1$, and let $\lambda^n \colon R \to R$ for $n \ge 0$ be maps.
Write $\lambda_t(x) = \sum_{n \ge 0} \lambda^n(x) t^n \in R[\![t]\!]$.
The pair $(R, (\lambda^n))$ is a *lambda-ring* if for all $x, y \in R$ and $m, n \ge 1$:

1. $\lambda^0(x) = 1$ and $\lambda^1(x) = x$.
2. $\lambda_t(x + y) = \lambda_t(x) \lambda_t(y)$, that is, $\lambda^n(x + y) = \sum_{i=0}^{n} \lambda^i(x) \lambda^{n-i}(y)$.
3. $\lambda_t(1) = 1 + t$.
4. $\lambda^n(xy) = P_n(\lambda^1(x), \ldots, \lambda^n(x), \lambda^1(y), \ldots, \lambda^n(y))$.
5. $\lambda^m(\lambda^n(x)) = P_{m,n}(\lambda^1(x), \ldots, \lambda^{mn}(x))$.

Here $P_n$ and $P_{m,n}$ are the universal polynomials with integer coefficients defined as follows.
Take variables $\xi_1, \ldots, \xi_N$ and $\eta_1, \ldots, \eta_N$ with $N$ large, and let $e_k$ be the [[elementary symmetric polynomials|0X5QVCF06N]].
Then $P_n(e_1(\xi), \ldots, e_n(\xi), e_1(\eta), \ldots, e_n(\eta))$ is the coefficient of $t^n$ in $\prod_{i,j} (1 + \xi_i \eta_j t)$.
And $P_{m,n}(e_1(\xi), \ldots, e_{mn}(\xi))$ is the coefficient of $t^m$ in $\prod_{i_1 < \cdots < i_n} (1 + \xi_{i_1} \cdots \xi_{i_n} t)$.

A ring with maps satisfying only clauses 1 and 2 is a *pre-lambda-ring*.

## Remarks

Example: $\Z$ with $\lambda^n(k) = \binom{k}{n}$ is a lambda-ring.
Clause 2 is Vandermonde's identity $\binom{k + l}{n} = \sum_i \binom{k}{i} \binom{l}{n-i}$, and $\lambda_t(k) = (1 + t)^k$.

Example: for a scheme $X$, the K-group $K_0(X)$ of vector bundles with $\lambda^n[E] = [\Lambda^n E]$ is a lambda-ring.
The same holds for the representation ring of a group, with exterior powers of representations.

Non-example: $\Z$ with $\lambda^0 = 1$, $\lambda^1 = \id$ and $\lambda^n = 0$ for $n \ge 2$ fails clause 2.
Indeed clause 2 would force $\lambda^2(1 + 1) = \lambda^1(1) \lambda^1(1) = 1$, not $0$.

An element $x$ with $\lambda_t(x) = 1 + xt$ is a *line element*; the class of a line bundle is one.
Clauses 4 and 5 say that the $\lambda^n$ behave on products and composites as they do on sums of line elements, by the splitting principle.
Some authors call a pre-lambda-ring a lambda-ring, and a lambda-ring in the sense above a *special* lambda-ring.
