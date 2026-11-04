---
tag: 3BSGWCX46W
kind: proof
name: Proof of the formula for the derivative of a polynomial
msc: [26A24]
proves: 0MH1WK89PP
uses: [0JZGW75C5Z, 0M0TKFRX2A, 0F1WR9C83K, 0GBZDAFPX8, 0A61B60B5R]
sources:
  - url: https://en.wikipedia.org/wiki/Linearity_of_differentiation
    locator: Statement and derivation
---

## Proof

We argue by induction on $n$, the largest index of the coefficients.

1. Base case $n = 0$. Then $p(x) = a_0$ is constant. For $h \ne 0$, its difference quotient at $x$ is $\frac{a_0 - a_0}{h} = 0$.
2. A function that is constantly $0$ near $0$ has limit $0$ at $0$, by the [[epsilon-delta form of limits|0GBZDAFPX8]]. So $p$ has [[derivative|0F1WR9C83K]] $0$ at every $x$.
3. The claimed formula for $n = 0$ is the empty sum $\sum_{k=1}^{0} k a_k x^{k-1} = 0$. So the base case holds.
4. Induction step. Assume the claim for all polynomials $\sum_{k=0}^{n} a_k x^k$, for some $n \ge 0$. Let $p(x) = \sum_{k=0}^{n+1} a_k x^k$.
5. Write $p = r + a_{n+1} s$, where $r(x) = \sum_{k=0}^{n} a_k x^k$ and $s(x) = x^{n+1}$.
6. By the induction hypothesis, $r$ is [[differentiable|0A61B60B5R]] on $\R$ with $r'(x) = \sum_{k=1}^{n} k a_k x^{k-1}$.
7. By the [[power rule|0JZGW75C5Z]] with exponent $n + 1 \ge 1$, $s$ is differentiable on $\R$ with $s'(x) = (n + 1) x^{n}$.
8. By the [[linearity of differentiation|0M0TKFRX2A]] with coefficients $1$ and $a_{n+1}$, $p$ is differentiable at every $x$, and
$$p'(x) = \sum_{k=1}^{n} k a_k x^{k-1} + (n + 1) a_{n+1} x^{n} = \sum_{k=1}^{n+1} k a_k x^{k-1}.$$
9. This is the claim for $n + 1$. By induction, it holds for every $n$.

## Idea

A polynomial is built by adding one term $a_k x^k$ at a time. The power rule differentiates each term, and linearity lets us differentiate the sum term by term.
