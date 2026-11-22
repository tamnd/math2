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

Let $\omega \colon \mathbb{R}^2 \times \mathbb{R}^2 \to \mathbb{R}$ be the map $\omega(u, v) = u_1 v_2 - u_2 v_1$.
We check that $\omega$ is an alternating bilinear form with $\omega(e_1, e_2) = 1$.

1. Linearity in $u$.
   For fixed $v$, the value $\omega(u, v) = v_2 u_1 - v_1 u_2$ is a fixed combination of $u_1$ and $u_2$, so
$$\omega(s u + t u', v) = s\, \omega(u, v) + t\, \omega(u', v)$$
   for all real $s, t$ and all $u, u'$.
2. Linearity in $v$.
   For fixed $u$, the value $\omega(u, v) = u_1 v_2 - u_2 v_1$ is a fixed combination of $v_1$ and $v_2$, so $\omega$ is linear in $v$ in the same way.
3. By steps 1 and 2, $\omega$ is [[bilinear|0SDMPMCN43]].
4. The alternating property.
   For every $u$,
$$\omega(u, u) = u_1 u_2 - u_2 u_1 = 0.$$
   So $\omega$ is an [[alternating multilinear map|0MSWYWHYF5]].
5. Normalization: $\omega(e_1, e_2) = 1 \cdot 1 - 0 \cdot 0 = 1$.
6. A numerical check: for $u = (2, 1)$ and $v = (1, 3)$,
$$\omega(u, v) = 2 \cdot 3 - 1 \cdot 1 = 5, \qquad \omega(v, u) = 1 \cdot 1 - 3 \cdot 2 = -5,$$
   so exchanging the arguments changes the sign, as it must for an alternating form.

## Remarks

Since $\omega$ is alternating, bilinear and $1$ on $(e_1, e_2)$, the [[existence and uniqueness theorem|1C8RRWHD45]] gives
$$\omega(u, v) = \det \begin{pmatrix} u_1 & u_2 \\ v_1 & v_2 \end{pmatrix}.$$
The number $\lvert \omega(u, v) \rvert$ is the area of the parallelogram with sides $u$ and $v$.
For $u = (2, 1)$ and $v = (1, 3)$ that area is $5$.

The same theorem shows that $\omega$ is the only such form up to a factor.
Every alternating bilinear form $\omega'$ on $\mathbb{R}^2$ equals $c\, \omega$ with $c = \omega'(e_1, e_2)$.
For example, $\omega'(u, v) = 3 u_1 v_2 - 3 u_2 v_1$ is $3 \omega$.
On $\mathbb{R}^3$ this fails: the forms $u_1 v_2 - u_2 v_1$ and $u_1 v_3 - u_3 v_1$ are both alternating and bilinear, and neither is a multiple of the other.

## Explanations

### L1 human

The signed area of two arrows in the plane is a single number.
It doubles when one arrow doubles, and it is zero when the two arrows point along the same line.
For the arrows $(2, 1)$ and $(1, 3)$ it is $2 \cdot 3 - 1 \cdot 1 = 5$.
In the other order it is $-5$, because the sign tells which way you turn from the first arrow to the second.

### L2 human

The sign of $\omega(u, v)$ gives the direction of the turn from $u$ to $v$.
It is positive when the shorter turn from $u$ to $v$ is counterclockwise, as for $e_1$ and $e_2$, and negative when it is clockwise.
Watch out: $\omega$ is not a linear map on $\mathbb{R}^4$, even though its formula has no squares.
For example $\omega(2u, 2v) = 4\, \omega(u, v)$, and with $u = (2, 1)$ and $v = (1, 3)$ that is $20$, not $10$.
