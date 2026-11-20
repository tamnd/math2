---
tag: VFFVMRTVRZ
kind: example
name: The signed area form on the plane
msc: ["15A15", "15A69"]
topics: [DTBK11SR77]
audience: ug1
instance_of: [0K6CH0MT0F]
uses: [0MSWYWHYF5, 0SDMPMCN43, 1C8RRWHD45]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Parallelogram area
---

## Example

Let $\omega \colon \mathbb{R}^2 \times \mathbb{R}^2 \to \mathbb{R}$ be $\omega(u, v) = u_1 v_2 - u_2 v_1$.

1. Linearity in $u$: for fixed $v$, $\omega(u, v) = v_2 u_1 - v_1 u_2$ is a linear combination of $u_1$ and $u_2$. So $\omega(su + tu', v) = s\,\omega(u, v) + t\,\omega(u', v)$.
2. Linearity in $v$: for fixed $u$, $\omega(u, v) = u_1 v_2 - u_2 v_1$ is a linear combination of $v_1$ and $v_2$.
3. So $\omega$ is [[bilinear|0SDMPMCN43]].
4. Alternating: $\omega(u, u) = u_1 u_2 - u_2 u_1 = 0$ for each $u$.
5. So $\omega$ is an [[alternating multilinear map|0MSWYWHYF5]].
6. Normalization: $\omega(e_1, e_2) = 1 \cdot 1 - 0 \cdot 0 = 1$.
7. Numerical check: for $u = (2, 1)$ and $v = (1, 3)$, $\omega(u, v) = 6 - 1 = 5$, and $\omega(v, u) = 1 - 6 = -5$.

## Remarks

By the [[existence and uniqueness theorem|1C8RRWHD45]], $\omega(u, v) = \det \begin{pmatrix} u_1 & u_2 \\ v_1 & v_2 \end{pmatrix}$, since both are alternating, bilinear and $1$ on $(e_1, e_2)$.
The number $\abs{\omega(u, v)}$ is the area of the parallelogram with sides $u$ and $v$; for $u = (2, 1)$, $v = (1, 3)$ the area is $5$.
Each alternating bilinear form on $\mathbb{R}^2$ is $c\,\omega$ for $c = \omega'(e_1, e_2)$; for example $\omega'(u, v) = 3u_1 v_2 - 3u_2 v_1$ is $3\omega$.

## Explanations

### L1 human

The signed area of two arrows in the plane is a single number.
It doubles when one arrow doubles, and it is zero when the two arrows point the same way.
For the arrows $(2, 1)$ and $(1, 3)$ it is $2 \cdot 3 - 1 \cdot 1 = 5$.

### L2 human

The sign of $\omega(u, v)$ tells the turning direction from $u$ to $v$: positive for a counterclockwise turn of less than a half turn.
A trap: $\omega$ is not linear as a map on $\mathbb{R}^4$; for instance $\omega(2u, 2v) = 4\,\omega(u, v)$.
