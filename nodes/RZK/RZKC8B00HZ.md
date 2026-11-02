---
tag: RZKC8B00HZ
kind: statement
role: proposition
name: An infinite product converges iff its series of logarithms converges
msc: [40A20]
uses: [H1Z2TKY3EQ, 0044CPHJBV, 0CVVKY7GY2, 0HW7BNHHGF]
about: [PCYRWA7SYB]
sources:
  - url: https://en.wikipedia.org/wiki/Infinite_product
---

## Statement

Let $(a_n)_{n \ge 1}$ be a sequence of positive real numbers.
Then the infinite product $\prod_{n=1}^{\infty} a_n$ [[converges|H1Z2TKY3EQ]] if and only if the series $\sum_{n=1}^{\infty} \ln a_n$ [[converges|0CVVKY7GY2]], where $\ln$ is the [[natural logarithm|0044CPHJBV]].
In that case
$$\prod_{n=1}^{\infty} a_n = \exp\left( \sum_{n=1}^{\infty} \ln a_n \right).$$

## Remarks

The partial products and the partial sums are linked by $\prod_{n \le N} a_n = \exp\left(\sum_{n \le N} \ln a_n\right)$.
The map $\exp$ is a continuous bijection from $\R$ onto $(0, \infty)$, with continuous inverse $\ln$.
So the partial products tend to a positive limit exactly when the partial sums tend to a real limit.
The nonzero condition in the definition of convergence is what makes this work: partial sums tending to $-\infty$ correspond to products diverging to $0$.
A consequence: if $u_n \ge 0$, then $\prod (1 + u_n)$ converges if and only if $\sum u_n$ converges.
Indeed, if $u_n \to 0$ then $\ln(1 + u_n) / u_n \to 1$, and the [[limit comparison test|0HW7BNHHGF]] applies; if $u_n \not\to 0$, both diverge.
Example: $\prod (1 + 1/n^2)$ converges and $\prod (1 + 1/n)$ diverges.

## Explanations

### L1 human

Taking logarithms turns products into sums.
So an infinite product of positive numbers behaves exactly like the infinite series of their logarithms.
This lets the convergence tests for series decide convergence of products.

### L2 human

The statement reduces the theory of products of positive numbers to the theory of series.
Its most used form is the criterion for $\prod (1 + u_n)$ with $u_n \ge 0$, which compares the product with $\sum u_n$.
For complex factors one uses a branch of the logarithm near $1$, and absolute convergence of $\sum (a_n - 1)$ gives convergence of the product.
