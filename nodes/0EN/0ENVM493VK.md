---
tag: 0ENVM493VK
kind: statement
role: corollary
name: Inverse in terms of the adjugate
msc: [15A09]
uses: [0528HKWZ1Z, 0TWTS88TWN]
sources:
  - url: https://en.wikipedia.org/wiki/Adjugate_matrix
    locator: Important consequence
---

## Statement

Let $K$ be a commutative ring, let $n \ge 2$, and let $A$ be an $n \times n$ matrix over $K$ such that $\det A$ is a unit of $K$.
Then $A$ is [[invertible|0EB9N0S33C]], and
$$A^{-1} = (\det A)^{-1} \operatorname{adj}(A),$$
where $\operatorname{adj}(A)$ is the [[adjugate|07W9H8QF38]] of $A$.

## Remarks

The statement follows by dividing [[$A \operatorname{adj}(A) = \operatorname{adj}(A) A = \det(A) I_n$|0528HKWZ1Z]] by $\det A$.
For $n = 2$ and $ad - bc \ne 0$ over a field, $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.
For large $n$, row reduction computes the inverse much faster than this formula.

## Explanations

### L1 human

This formula gives every entry of the inverse as a quotient of two determinants.
It is useful for theory and for small matrices.
For $2 \times 2$ matrices, it is the formula that most students learn first.
