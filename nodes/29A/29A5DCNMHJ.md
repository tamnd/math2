---
tag: 29A5DCNMHJ
kind: example
name: The derivative on quadratic polynomials
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
instance_of: [0J7H0YBFDJ, 063D5Z2C70]
uses: [0PTF1PTJK0, 0RJF668P1T, 0YQSGNYE3K]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Examples
  - book: isbn:9783031410253
    locator: Chapter 3
---

## Example

Differentiation lowers the degree, so it maps the quadratics into themselves, and three derivatives kill every quadratic.
Let $P_2$ be the space of real polynomials of degree at most $2$, and let $D \colon P_2 \to P_2$ be the derivative,
$$D(a + bx + cx^2) = b + 2cx.$$

1. The map $D$ is [[linear|0RJF668P1T]], since the derivative of a sum is the sum of the derivatives and $(kp)' = k\,p'$.
2. The derivative of a polynomial of degree at most $2$ has degree at most $1$, so $D$ maps $P_2$ into $P_2$, and $D$ is an [[endomorphism|0PTF1PTJK0]].
3. We have $D^2(a + bx + cx^2) = D(b + 2cx) = 2c$.
4. Then $D^3(a + bx + cx^2) = D(2c) = 0$, so $D^3 = 0$, while $D^2 \ne 0$, since $D^2(x^2) = 2$.
5. In the basis $(1, x, x^2)$, the [[matrix|0YQSGNYE3K]] of $D$ is $N = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}$, and $N^3 = 0$.

Check: $D(1 + 3x + 5x^2) = 3 + 10x$, then $D(3 + 10x) = 10$, then $D(10) = 0$.

## Remarks

The map $D$ is neither injective nor surjective: $D(1) = 0$, and $x^2$ is not the derivative of any element of $P_2$.
This agrees with the theorem that the two properties are equivalent for endomorphisms in finite dimension.
Since some power of it is $0$, the map $D$ is a [[nilpotent endomorphism|063D5Z2C70]].

If we change the degree bound to $n$, the derivative on $P_n$ satisfies $D^{n+1} = 0$ and $D^n \ne 0$.
If we change the field to one of characteristic $2$, then $D(a + bx + cx^2) = b$, since $2c = 0$, and $D^2 = 0$ already.

## Explanations

### L1 human

Differentiating a quadratic polynomial gives a polynomial of lower degree.
So the derivative maps the quadratics into themselves.
Three derivatives kill each quadratic, so $D^3 = 0$.

### L2 human

In the basis $(1, x, x^2)$ the derivative becomes a strictly upper triangular matrix.
Its powers move the nonzero entries further from the diagonal until they vanish.
Watch out: if $D$ is treated as a map $P_2 \to P_1$, it is not an endomorphism, and $D^2$ is not defined.
