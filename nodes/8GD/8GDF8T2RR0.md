---
tag: 8GDF8T2RR0
kind: proof
name: Proof of the second-order Taylor expansion
msc: ["26B12"]
proves: 0P30YYZN85
uses: [0J8T4K4YTE, 0PJXBR6QA3, 0NS2QYVC4Y, 0SCSQWXRA4, 0NNQY8WCW6, 0TCBZMEYGN, 0KXSK8TEEB]
sources:
  - url: https://en.wikipedia.org/wiki/Taylor%27s_theorem
    locator: Taylor's theorem for multivariate functions
---

## Proof

We take $k = 2$ in Taylor's theorem and rewrite the terms with matrices.

1. Let $U$, $f$ and $a$ be as in the statement. Write $\partial_i$ for the partial derivative in the direction $x_i$. Since $f$ is of [[class C^2|0TCBZMEYGN]], it is [[differentiable|0KXSK8TEEB]] at $a$, so $\nabla f(a)$ is defined.
2. By [[Taylor's theorem in several variables|0J8T4K4YTE]] with $k = 2$, we have $f(a + h) = \sum_{\abs{\alpha} \le 2} \frac{D^\alpha f(a)}{\alpha!} h^\alpha + R_2(h)$ with $R_2(h) / \norm{h}^2 \to 0$ as $h \to 0$.
3. It suffices to show that the sum in step 2 equals $f(a) + \nabla f(a) \cdot h + \tfrac{1}{2} h^{\mathsf{T}} H_f(a) h$. Then $R(h) = R_2(h)$ has the required limit.
4. The only [[multi-index|0PJXBR6QA3]] with $\abs{\alpha} = 0$ is $\alpha = 0$. Its term is $f(a)$.
5. The multi-indices with $\abs{\alpha} = 1$ are the $e_i$, with $e_i! = 1$ and $h^{e_i} = h_i$. Their terms add up to $\sum_i \partial_i f(a) h_i$. This is $\nabla f(a) \cdot h$, since the [[gradient|0NS2QYVC4Y]] is the vector of partial derivatives.
6. The multi-indices with $\abs{\alpha} = 2$ are $2 e_i$ for each $i$, and $e_i + e_j$ for each pair $i < j$.
7. For $\alpha = 2 e_i$ we have $\alpha! = 2$, so the term is $\tfrac{1}{2} \partial_i \partial_i f(a) \, h_i^2$. For $\alpha = e_i + e_j$ with $i < j$ we have $\alpha! = 1$, so the term is $\partial_i \partial_j f(a) \, h_i h_j$.
8. Let $H = H_f(a)$, the [[Hessian matrix|0SCSQWXRA4]], with entries $H_{ij} = \partial_i \partial_j f(a)$. By [[Schwarz's theorem|0NNQY8WCW6]], $H_{ij} = H_{ji}$.
9. Then $\tfrac{1}{2} h^{\mathsf{T}} H h = \tfrac{1}{2} \sum_{i, j} H_{ij} h_i h_j = \tfrac{1}{2} \sum_i H_{ii} h_i^2 + \tfrac{1}{2} \sum_{i < j} (H_{ij} + H_{ji}) h_i h_j$.
10. By step 8 the last sum is $\sum_{i < j} H_{ij} h_i h_j$. So $\tfrac{1}{2} h^{\mathsf{T}} H h$ equals the sum of the terms in step 7.
11. Steps 4, 5, 7 and 10 give the identity of step 3, which proves the expansion.

## Idea

The second-order expansion is the case $k = 2$ of Taylor's theorem. The only work is bookkeeping: the terms of order two in multi-index form match $\tfrac{1}{2} h^{\mathsf{T}} H h$, because the Hessian is symmetric and each mixed term appears twice in the matrix product.
