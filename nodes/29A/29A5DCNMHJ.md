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

Let $P_2$ be the real polynomials of degree at most $2$, and let $D \colon P_2 \to P_2$ be the derivative:
$$D(a + bx + cx^2) = b + 2cx.$$

1. $D$ is [[linear|0RJF668P1T]]: the derivative of a sum is the sum of the derivatives, and $(kp)' = k\,p'$.
2. The derivative of a polynomial of degree at most $2$ has degree at most $1$. So $D$ maps $P_2$ into $P_2$, and $D$ is an [[endomorphism|0PTF1PTJK0]].
3. $D^2(a + bx + cx^2) = D(b + 2cx) = 2c$.
4. $D^3(a + bx + cx^2) = D(2c) = 0$. So $D^3 = 0$, while $D^2 \ne 0$, since $D^2(x^2) = 2$.
5. In the basis $(1, x, x^2)$, the [[matrix|0YQSGNYE3K]] of $D$ is $N = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}$, and $N^3 = 0$.
6. Numerical check: $D(1 + 3x + 5x^2) = 3 + 10x$, then $D(3 + 10x) = 10$, then $D(10) = 0$.

## Remarks

- $D$ is neither injective nor surjective: $D(1) = 0$, and $x^2$ is not a derivative of an element of $P_2$. This agrees with the theorem that the two properties are equivalent in finite dimension.
- $D$ is a [[nilpotent endomorphism|063D5Z2C70]]: some power of it is $0$.
- On $P_n$, the derivative satisfies $D^{n+1} = 0$ and $D^n \ne 0$.
- Over a field of characteristic $2$, $D(cx^2) = 2cx = 0$. Then $D^2 = 0$ already.

## Explanations

### L1 human

Differentiating a quadratic polynomial gives a polynomial of lower degree.
So the derivative maps the quadratics into themselves.
Three derivatives kill each quadratic, so $D^3 = 0$.

### L2 human

The derivative becomes a strictly upper triangular matrix in the basis $(1, x, x^2)$.
Its powers move the nonzero entries further from the diagonal until they vanish.
The trap is to treat $D$ as a map $P_2 \to P_1$; it is then not an endomorphism, and $D^2$ is not defined.
