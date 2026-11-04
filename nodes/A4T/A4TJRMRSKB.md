---
tag: A4TJRMRSKB
kind: proof
name: Proof of Liouville's formula
msc: [34A30]
proves: 09PS3S0EF6
uses: [016PE4VZ8Q, 0K4VQB7HWR, 07PTPSZPME, 0V9A43H7WV, 0M0TKFRX2A, 0NC2A3HWGT, 0RXX2PT1MQ, 0EX9GFJ0B3, 003QDZ4T16, 0E8HNVBCSP]
sources:
  - url: https://en.wikipedia.org/wiki/Liouville%27s_formula
    locator: Proof of Liouville's formula
---

## Proof

We show that $w = \det \Phi$ satisfies $w' = (\tr A)\, w$ and then solve this equation.

1. Write $\Phi = (\varphi_{ij})$ and $A = (A_{ij})$. Each $\varphi_{ij}$ is differentiable on $I$. By the [[Leibniz formula|016PE4VZ8Q]], $\det \Phi = \sum_{\sigma} \operatorname{sgn}(\sigma) \prod_{i=1}^{n} \varphi_{i, \sigma(i)}$, summed over all permutations $\sigma$.
2. By induction on the number of factors, the [[product rule|0V9A43H7WV]] gives $(f_1 \cdots f_n)' = \sum_{k} f_1 \cdots f_k' \cdots f_n$ for differentiable $f_1, \dots, f_n$.
3. With [[linearity of differentiation|0M0TKFRX2A]], $(\det \Phi)' = \sum_{k=1}^{n} \det \Phi_k$. Here $\Phi_k$ is $\Phi$ with row $k$ replaced by row $k$ of $\Phi'$.
4. From $\Phi' = A \Phi$, row $k$ of $\Phi'$ has entries $\varphi_{kj}' = \sum_{l} A_{kl} \varphi_{lj}$. So it is $\sum_l A_{kl}$ times row $l$ of $\Phi$.
5. Each term of the Leibniz formula contains exactly one entry of row $k$. So the determinant is linear in row $k$, and $\det \Phi_k = \sum_l A_{kl} \det \Phi_{k, l}$. Here $\Phi_{k, l}$ is $\Phi$ with row $k$ replaced by row $l$ of $\Phi$.
6. For $l \ne k$, the matrix $\Phi_{k, l}$ has two equal rows, so [[its determinant is $0$|0K4VQB7HWR]]. For $l = k$, $\Phi_{k, k} = \Phi$. Hence $\det \Phi_k = A_{kk} \det \Phi$.
7. Summing over $k$ and using the definition of the [[trace|07PTPSZPME]], $w' = (\tr A)\, w$ on $I$, where $w = \det \Phi$.
8. The function $\tr A$ is continuous, as a sum of continuous entries. Let $T(t) = \int_{t_0}^{t} \tr A(s)\, ds$. By [[the antiderivative theorem|0NC2A3HWGT]], $T' = \tr A$, and $T(t_0) = 0$.
9. Let $g = w\, e^{-T}$. By the product rule, the [[chain rule|0RXX2PT1MQ]] and [[the derivative of the exponential|0EX9GFJ0B3]], $g' = (\tr A)\, w\, e^{-T} - w\, (\tr A)\, e^{-T} = 0$.
10. So [[$g$ is constant|003QDZ4T16]] on $I$, and $g(t) = g(t_0) = \det \Phi(t_0)$.
11. By the [[exponential of a sum|0E8HNVBCSP]], $e^{T(t)} e^{-T(t)} = 1$. Multiplying $g(t)$ by $e^{T(t)}$ gives $\det \Phi(t) = \det \Phi(t_0) \exp\left(\int_{t_0}^{t} \tr A(s)\, ds\right)$.

## Idea

Differentiating a determinant row by row gives a sum of $n$ determinants. In the $k$-th one, the new row $k$ is a combination of the rows of $\Phi$, and only the multiple $A_{kk}$ of row $k$ survives. So $\det \Phi$ solves a scalar linear equation with coefficient $\tr A$, whose solutions are exponentials.
