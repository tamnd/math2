---
tag: ZEGSCCVGZF
kind: example
name: Quadratic forms over F₂ that do not come from a symmetric bilinear form
msc: ["15A63", "11E04", "11T99"]
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

Let $F = \mathbb{F}_2$, the [[field with two elements|0ZXZ82FTX2]], in which $1 + 1 = 0$.
Two small forms show that both halves of [[the correspondence between quadratic forms and symmetric bilinear forms|VN9AG8JKYT]] fail in characteristic $2$.

The first form is $Q(x, y) = xy$ on $\mathbb{F}_2^2$.
It shows that a quadratic form need not come from a symmetric bilinear form.

1. $Q$ is a [[quadratic form|0HZNE5QZDJ]]: it scales as $Q(ax, ay) = a^2 xy$, and its [[polar form|0HYFWKKY3C]] $b_Q(u, v) = xy' + x'y$ for $u = (x, y)$ and $v = (x', y')$ is bilinear.
2. Let $B$ be any [[symmetric bilinear form|0744CN4MDA]] on $\mathbb{F}_2^2$. Expanding with bilinearity and symmetry gives
$$B(u + v, u + v) = B(u, u) + 2B(u, v) + B(v, v) = B(u, u) + B(v, v),$$
because $2 = 0$ in $\mathbb{F}_2$. So the map $v \mapsto B(v, v)$ is additive.
3. The form $Q$ is not additive, because $Q(1, 1) = 1$ while $Q(1, 0) + Q(0, 1) = 0 + 0 = 0$.
4. By steps 2 and 3, $Q(v) \ne B(v, v)$ for some $v$, whatever symmetric bilinear form $B$ we choose. So the map $B \mapsto (v \mapsto B(v, v))$ is not onto.

The second form is $Q(x) = x^2$ on $\mathbb{F}_2$.
It shows that a quadratic form is not determined by its polar form.

5. The polar form is $b_Q(u, v) = (u + v)^2 - u^2 - v^2 = 2uv = 0$.
6. The zero form also has polar form $0$, but $Q(1) = 1 \ne 0$. So two different quadratic forms have the same polar form.
7. The symmetric bilinear form $B(u, v) = uv$ does satisfy $B(v, v) = Q(v)$. But $B$ cannot be recovered as $\tfrac{1}{2} b_Q$, because $\tfrac{1}{2}$ does not exist in $\mathbb{F}_2$ and $b_Q = 0$.

## Remarks

The two forms are the smallest cases where characteristic $2$ breaks the correspondence.
Every polar form in characteristic $2$ has zero diagonal, since $b_Q(v, v) = 2Q(v) = 0$; for $xy$ the matrix of $b_Q$ is $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
No symmetric matrix $A$ over $\mathbb{F}_2$ gives $x^{\mathsf{T}} A x = xy$, because there $x^{\mathsf{T}} A x = a_{11} x^2 + 2a_{12} xy + a_{22} y^2 = a_{11} x^2 + a_{22} y^2$.
The upper triangular matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ does give $xy$.

A count makes the gap exact.
A quadratic form $ax^2 + bxy + cy^2$ on $\mathbb{F}_2^2$ is fixed by its values $a = Q(1, 0)$, $c = Q(0, 1)$ and $a + b + c = Q(1, 1)$, so there are $2^3 = 8$ of them.
By the remark above, only the $4$ forms with $b = 0$ have the shape $B(v, v)$.

## Explanations

### L1 human

In $\mathbb{F}_2$ we have $1 + 1 = 0$, so we cannot divide by $2$.
The usual recipe $B = \tfrac{1}{2}\bigl(Q(u + v) - Q(u) - Q(v)\bigr)$ then has no meaning.
The form $xy$ shows the failure with numbers: it is $1$ at $(1, 1)$, but $0$ at $(1, 0)$ and at $(0, 1)$, and every $B(v, v)$ would add these values.

### L2 human

Forms over $\mathbb{F}_2$ are common in coding theory and in the study of finite groups, so the trap is a real one.
In characteristic $2$, do not replace a quadratic form by a symmetric matrix.
Write it as $\sum_{i \le j} c_{ij} x_i x_j$, or with an upper triangular matrix, and keep its polar form as a separate object.
For example, $x^2 + xy + y^2$ and $xy$ on $\mathbb{F}_2^2$ have the same polar form $xy' + x'y$, but the first has no nonzero zero and the second has the zero $(1, 0)$.
