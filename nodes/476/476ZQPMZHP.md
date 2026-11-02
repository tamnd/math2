---
tag: 476ZQPMZHP
kind: statement
role: proposition
name: Clenshaw algorithm
msc: [65D20, 33C45]
uses: [0FYX44GP92, M6EAR1JHPP, FYBQ3Z52Z7]
about: [0FYX44GP92]
sources:
  - url: https://en.wikipedia.org/wiki/Clenshaw_algorithm
same_as:
  wikidata: Q1067155
  wikipedia: Clenshaw algorithm
---

## Statement

Let $n \ge 1$, let $x$ be a fixed point, and let $\phi_0(x), \ldots, \phi_n(x)$ be numbers that satisfy the three-term [[recurrence|0FYX44GP92]]
$$\phi_{k+1}(x) = \alpha_k(x)\, \phi_k(x) + \beta_k(x)\, \phi_{k-1}(x), \qquad 1 \le k \le n-1,$$
for given coefficients $\alpha_k(x)$ and $\beta_k(x)$.
Let $a_0, \ldots, a_n$ be numbers and $S(x) = \sum_{k=0}^{n} a_k \phi_k(x)$.
Set $b_{n+1} = b_{n+2} = 0$ and, for $k = n, n-1, \ldots, 1$,
$$b_k = a_k + \alpha_k(x)\, b_{k+1} + \beta_{k+1}(x)\, b_{k+2},$$
where $\alpha_n(x)$, $\beta_n(x)$ and $\beta_{n+1}(x)$ may be given any values in these formulas, since they multiply $b_{n+1} = 0$ or $b_{n+2} = 0$.
Then
$$S(x) = a_0\, \phi_0(x) + b_1\, \phi_1(x) + \beta_1(x)\, b_2\, \phi_0(x).$$

## Remarks

Write $a_k = b_k - \alpha_k b_{k+1} - \beta_{k+1} b_{k+2}$ for $1 \le k \le n$ and substitute in $\sum_{k \ge 1} a_k \phi_k$.
After collecting terms, the coefficient of $b_j$ for $j \ge 3$ is $\phi_j - \alpha_{j-1}\phi_{j-1} - \beta_{j-1}\phi_{j-2} = 0$, and the coefficient of $b_2$ is $\phi_2 - \alpha_1 \phi_1 = \beta_1 \phi_0$; only the terms in the formula remain.
For the [[Chebyshev polynomials|M6EAR1JHPP]] $T_k$ one has $\phi_0 = 1$, $\phi_1 = x$, $\alpha_k = 2x$ and $\beta_k = -1$, so $\sum_{k=0}^n a_k T_k(x) = a_0 + x b_1 - b_2$.
Check with $n = 2$: $b_2 = a_2$, $b_1 = a_1 + 2x a_2$, and $a_0 + x(a_1 + 2x a_2) - a_2 = a_0 + a_1 x + a_2(2x^2 - 1)$, which is $a_0 T_0 + a_1 T_1 + a_2 T_2$.
For the monomials $\phi_k = x^k$, with $\alpha_k = x$ and $\beta_k = 0$, the algorithm is [[Horner's method|FYBQ3Z52Z7]].
The cost is $O(n)$ operations, and the values $\phi_k(x)$ for $k \ge 2$ are never formed.

## Explanations

### L1 human

Many useful functions are sums of special polynomials, such as Chebyshev or Legendre polynomials, each defined by a recurrence from the two before.
Computing every polynomial value and then adding is possible, but Clenshaw found a shorter route.
It runs a similar recurrence backwards, starting from the last coefficient, and reads off the sum at the end.
It plays for these families the role that Horner's rule plays for ordinary polynomials.

### L2 human

The algorithm is the standard way to evaluate a truncated Chebyshev series, for instance in function libraries and in Chebyshev spectral methods.
It works for any family defined by a three-term recurrence, so for all classical orthogonal polynomials and also for some special functions such as Bessel functions.
The backward recurrence is the transpose of the forward one, which explains why only $b_1$ and $b_2$ appear in the result.
Its rounding error behaviour is good for Chebyshev series on $[-1, 1]$, though near the endpoints $\pm 1$ the errors can be amplified.
