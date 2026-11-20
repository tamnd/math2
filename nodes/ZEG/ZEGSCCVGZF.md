---
tag: ZEGSCCVGZF
kind: example
name: Quadratic forms over F₂ that do not come from a symmetric bilinear form
msc: [15A63, "11E04", 11T99]
topics: [6TSCEW8QMK]
audience: ug2
instance_of: [0RBQS1JJCR]
illustrates: [VN9AG8JKYT]
uses: [0HZNE5QZDJ, 0744CN4MDA, 0HYFWKKY3C, 0ZXZ82FTX2]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Symmetric_bilinear_form
    locator: lead section
---

## Example

Let $F = \F_2$, the [[field with two elements|0ZXZ82FTX2]], where $1 + 1 = 0$.
We show that both directions of [[the correspondence theorem|VN9AG8JKYT]] fail.

**The form $xy$ on $\F_2^2$.**

1. $Q(x, y) = xy$ is a [[quadratic form|0HZNE5QZDJ]]. Its [[polar form|0HYFWKKY3C]] is $b_Q(u, v) = x y' + x' y$, which is bilinear.
2. Let $B$ be any [[symmetric bilinear form|0744CN4MDA]] on $\F_2^2$, and let $v = (x, y)$, $w = (x', y')$.
3. Then $B(v + w, v + w) = B(v, v) + 2B(v, w) + B(w, w) = B(v, v) + B(w, w)$, since $2 = 0$.
4. So $v \mapsto B(v, v)$ is additive for every symmetric bilinear form $B$.
5. For $Q$: $Q(1, 1) = 1$, but $Q(1, 0) + Q(0, 1) = 0 + 0 = 0$. So $Q$ is not additive.
6. By steps 4 and 5, $Q$ is not $B(v, v)$ for any symmetric bilinear form $B$. The map $B \mapsto Q_B$ is not onto.

**The form $x^2$ on $\F_2$.**

7. $Q(x) = x^2$ has polar form $b_Q(u, v) = (u + v)^2 - u^2 - v^2 = 2uv = 0$.
8. The zero form also has polar form $0$, but $Q(1) = 1 \ne 0$. So $Q$ is not determined by its polar form.
9. Since $x^2 = x$ for $x \in \F_2$, this $Q$ is also a linear map. The symmetric bilinear form $B(u, v) = uv$ gives $B(v, v) = Q(v)$, but $B$ is not $\frac12 b_Q$, because $\frac12$ does not exist.

## Remarks

The two forms are the smallest cases where characteristic $2$ breaks the theorem.
In step 1, the polar form of $xy$ has the matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, with zero diagonal, as for every polar form in characteristic $2$.
No symmetric matrix $A$ over $\F_2$ gives $x^T A x = xy$, since $x^T A x = a_{11} x^2 + a_{22} y^2$ there.
The upper triangular matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ does give $xy$.
Over $\F_2$ there are $8$ quadratic forms in two variables, $ax^2 + bxy + cy^2$, but only $4$ of them are of the form $B(v, v)$.

## Explanations

### L1 human

In $\F_2$ we have $1 + 1 = 0$, so we cannot divide by $2$.
The usual formula $B = \frac12 (Q(u + v) - Q(u) - Q(v))$ then has no meaning.
The form $xy$ shows the failure with numbers: $Q(1, 1) = 1$, while the two other values are $0$.

### L2 human

This example matters in coding theory and in the theory of finite groups, where forms over $\F_2$ are common.
A trap: in characteristic $2$, do not replace a quadratic form by a symmetric matrix.
Write it as $\sum_{i \le j} c_{ij} x_i x_j$, or by an upper triangular matrix, and keep its polar form as a separate object.
