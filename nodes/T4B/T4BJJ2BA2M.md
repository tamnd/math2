---
tag: T4BJJ2BA2M
kind: proof
name: Proof of Jacobi's formula by the product rule and Laplace expansion
msc: ["15A15"]
topics: [DTBK11SR77]
audience: grad
proves: 357FEAZ0Q4
methods: [0NTF6DMVAP]
uses: [016PE4VZ8Q, 0V9A43H7WV, 0C08BQ3M05, 0W2QAVJQ1W, 0GMPYM0NSR, 0528HKWZ1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi%27s_formula
---

## Proof

We differentiate the Leibniz formula term by term, and we recognize the result as a sum of Laplace expansions, one for each row.

1. Write $A(t) = (a_{ij}(t))$.
   Each entry $a_{ij}$ is differentiable, because $A$ is differentiable.
   For $\mathbb{K} = \mathbb{C}$ we use the product rule for complex-valued functions of a real variable, which has the same proof as for real values.
2. By the [[Leibniz formula|016PE4VZ8Q]],
$$\det A(t) = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) \prod_{i=1}^{n} a_{i \sigma(i)}(t).$$
3. By the [[product rule|0V9A43H7WV]] and induction on the number of factors, each product in step 2 is differentiable, with
$$\frac{d}{dt} \prod_{i=1}^{n} a_{i \sigma(i)} = \sum_{k=1}^{n} a'_{k \sigma(k)} \prod_{i \ne k} a_{i \sigma(i)}.$$
4. A finite sum of differentiable functions is differentiable, so $\det A(t)$ is differentiable.
   Its derivative is the sum of the derivatives of step 3, and we exchange the two finite sums:
$$\frac{d}{dt} \det A = \sum_{k=1}^{n} \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma)\, a'_{k \sigma(k)} \prod_{i \ne k} a_{i \sigma(i)}.$$
5. Let $A_k$ be the matrix $A$ with row $k$ replaced by row $k$ of $A'$.
   The inner sum in step 4 is the Leibniz formula for $A_k$, so it equals $\det A_k$.
6. Let $C_{kj}$ be the [[cofactors|0W2QAVJQ1W]] of $A$.
   A cofactor in row $k$ deletes row $k$, and $A_k$ agrees with $A$ outside row $k$, so the cofactors of $A_k$ in row $k$ are also $C_{kj}$.
7. By the [[Laplace expansion|0C08BQ3M05]] of $A_k$ along row $k$,
$$\det A_k = \sum_{j=1}^{n} a'_{kj}\, C_{kj}.$$
8. By steps 4 to 7,
$$\frac{d}{dt} \det A = \sum_{k=1}^{n} \sum_{j=1}^{n} C_{kj}\, a'_{kj}.$$
9. By the definition of the [[adjugate|0GMPYM0NSR]], $\operatorname{adj}(A)_{jk} = C_{kj}$.
   So the diagonal entry $j$ of $\operatorname{adj}(A) A'$ is
$$\big(\operatorname{adj}(A) A'\big)_{jj} = \sum_{k=1}^{n} \operatorname{adj}(A)_{jk}\, a'_{kj} = \sum_{k=1}^{n} C_{kj}\, a'_{kj}.$$
10. Summing over $j$ gives $\operatorname{tr}(\operatorname{adj}(A) A') = \sum_{j} \sum_{k} C_{kj}\, a'_{kj}$, which is the double sum of step 8.
    This proves the formula with the adjugate.
11. If $A(t)$ is invertible, the [[adjugate identity|0528HKWZ1Z]] gives $\operatorname{adj}(A) = \det(A)\, A^{-1}$.
    The trace is linear, so $\operatorname{tr}(\operatorname{adj}(A) A') = \det A \cdot \operatorname{tr}(A^{-1} A')$, which is the second form of the formula.

## Idea

The determinant is a sum of products, and each product takes one entry from each row.
The product rule differentiates one factor at a time, so the derivative splits into $n$ pieces, one for each row.
The piece for row $k$ is the determinant of $A$ with row $k$ replaced by its derivative.
Expanding that determinant along row $k$ gives the cofactors of $A$, and the cofactors assemble into the adjugate, which turns the double sum into a trace.

## Variants

A second proof starts at the identity.
By the Leibniz formula, the only term of $\det(I + \varepsilon X)$ that contributes to first order in $\varepsilon$ is the diagonal product, so
$$\det(I + \varepsilon X) = 1 + \varepsilon \operatorname{tr} X + O(\varepsilon^2).$$
For invertible $A$, multiplicativity gives $\det(A + \varepsilon X) = \det A \cdot \det(I + \varepsilon A^{-1} X)$, so the derivative of $\det$ at $A$ in the direction $X$ is $\det A \cdot \operatorname{tr}(A^{-1} X)$.
Both sides of the adjugate form are polynomials in the entries of $A$ and $X$, and the invertible matrices are dense, so the adjugate form holds for all $A$.
For $n = 1$ the formula reads $a' = \operatorname{tr}\big((1)(a')\big)$, with the convention that the adjugate of a $1 \times 1$ matrix is $(1)$.
