---
tag: N9ZCXH6HV1
kind: definition
name: Lebesgue constant
msc: [41A05, 65D05, 41A10]
defines: 7V7KWNK9HN
uses: [237KR6FRCK, DA3CQJ5MJ6, 06EKW1AKXF]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue_constant
---

## Definition

Let $a < b$, let $n \ge 0$, and let $x_0 < x_1 < \cdots < x_n$ be points of $[a, b]$.
Let $\ell_0, \dots, \ell_n$ be the [[Lagrange basis polynomials|DA3CQJ5MJ6]] of these nodes, so that $\ell_j(x_i) = 1$ if $i = j$ and $0$ otherwise.
The *Lebesgue function* of the nodes is $\lambda_n(x) = \sum_{j=0}^{n} \abs{\ell_j(x)}$.
The *Lebesgue constant* of the nodes is
$$\Lambda_n = \max_{a \le x \le b} \lambda_n(x).$$

## Remarks

Let $I_n \colon C[a, b] \to C[a, b]$ send $f$ to its [[Lagrange interpolation|237KR6FRCK]] polynomial $\sum_j f(x_j) \ell_j$.
With the uniform norm, $\Lambda_n$ is the [[operator norm|06EKW1AKXF]] of $I_n$.

Example: nodes $-1, 0, 1$ in $[-1, 1]$.
Here $\ell_0 = x(x - 1)/2$, $\ell_1 = 1 - x^2$ and $\ell_2 = x(x + 1)/2$.
For $0 \le x \le 1$ this gives $\lambda_2(x) = 1 + x - x^2$, and by symmetry $\Lambda_2 = \lambda_2(1/2) = 5/4$.

Non-example: the number $\max_x \abs{\sum_j \ell_j(x)}$ is not the Lebesgue constant; it always equals $1$, because $\sum_j \ell_j = 1$.
The absolute values must be taken term by term.

Always $\Lambda_n \ge 1$.
For equally spaced nodes $\Lambda_n$ grows like $2^{n+1} / (e \, n \log n)$.
For Chebyshev nodes $\Lambda_n = \frac{2}{\pi} \log n + O(1)$, and no choice of nodes does better than $\frac{2}{\pi} \log n - C$ for an absolute constant $C$.
