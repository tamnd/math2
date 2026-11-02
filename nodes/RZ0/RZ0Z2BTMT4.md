---
tag: RZ0Z2BTMT4
kind: definition
name: Infinite product
msc: [40A20]
defines: JYV1Y8XX16
uses: [0QE8STGJH2, 09FTAET5Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Infinite_product
---

## Definition

Let $(a_n)_{n \ge 1}$ be a [[sequence|0QE8STGJH2]] of [[complex numbers|09FTAET5Z4]].
The infinite product with factors $a_n$ is the sequence $(p_N)_{N \ge 1}$ of partial products
$$p_N = a_1 a_2 \cdots a_N = \prod_{n=1}^{N} a_n.$$
It is written $\prod_{n=1}^{\infty} a_n$.

## Remarks

The symbol $\prod_{n=1}^{\infty} a_n$ also denotes the value of the product when the product [[converges|PCYRWA7SYB]].
Example: for $a_n = 1 - 1/(n+1)^2$ the partial products are $p_N = \prod_{n=2}^{N+1} \frac{(n-1)(n+1)}{n^2} = \frac{N+2}{2(N+1)}$, by telescoping.
So $p_N \to \tfrac12$ and the product converges with value $\tfrac12$.
Non-example of convergence: for $a_n = 1 - 1/(n+1)$ the partial products are $p_N = 1/(N+1) \to 0$.
By convention this product does not converge but diverges to $0$, since a limit $0$ reached by nonzero factors is excluded in the definition of convergence.
A product can start at another index, such as $\prod_{n=2}^{\infty} (1 - 1/n^2)$.

## Explanations

### L1 human

An infinite product is the list of products of the first $N$ factors, for $N = 1, 2, 3, \ldots$.
