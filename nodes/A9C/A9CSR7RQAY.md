---
tag: A9CSR7RQAY
kind: definition
name: Banach limit
msc: [40H05, 46B45]
defines: SYF2ND6J97
uses: [08P6T2WH6R, 0T3RZQXDYD, 033RZ32T4Q, QB5AE3VYZZ]
sources:
  - url: https://en.wikipedia.org/wiki/Banach_limit
---

## Definition

Let $\ell^\infty$ be the vector space of bounded real sequences $x = (x_n)_{n \ge 1}$, as in the [[spaces ℓ^p|08P6T2WH6R]].
Let $S \colon \ell^\infty \to \ell^\infty$ be the shift, $S(x_1, x_2, x_3, \dots) = (x_2, x_3, \dots)$, and let $\mathbf{1} = (1, 1, 1, \dots)$.
A *Banach limit* is a linear map $\varphi \colon \ell^\infty \to \R$ such that:

1. $\varphi(x) \ge 0$ for every $x$ with $x_n \ge 0$ for all $n$.
2. $\varphi(Sx) = \varphi(x)$ for every $x \in \ell^\infty$.
3. $\varphi(\mathbf{1}) = 1$.

## Remarks

Every Banach limit satisfies $\liminf_n x_n \le \varphi(x) \le \limsup_n x_n$.
Check of the left inequality: if $x_n \ge c$ for all $n \ge N$, then $S^N x - c \mathbf{1}$ has nonnegative terms, so $\varphi(x) = \varphi(S^N x) \ge c$.
Hence $\varphi(x) = \lim_n x_n$ for every convergent $x$, and $\abs{\varphi(x)} \le \sup_n \abs{x_n}$, so $\varphi$ is continuous of norm $1$.
Banach limits exist by the [[Hahn–Banach theorem|QB5AE3VYZZ]], applied to the sublinear functional $p(x) = \limsup_{m} \frac{1}{m} \sum_{k=1}^{m} x_k$ or a similar one.

Non-example: $\varphi(x) = \limsup_n x_n$ satisfies clauses 1, 2 and 3, but it is not linear.
For $x = (1, 0, 1, 0, \dots)$ and $y = Sx$ one has $\varphi(x) + \varphi(y) = 2$ but $\varphi(x + y) = \varphi(\mathbf{1}) = 1$.

Non-example: $\varphi(x) = x_1$ is linear and positive with $\varphi(\mathbf{1}) = 1$, but it fails clause 2.
