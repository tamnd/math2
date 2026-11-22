---
tag: DT0H0YQ4H7
kind: example
name: The scalar triple product as an alternating trilinear form
msc: ["15A15", "15A69"]
topics: [DTBK11SR77]
audience: ug1
instance_of: [0K6CH0MT0F]
uses: [059Q2XWJDC, 0SEDGXG9S3, 05HQYM0R4G, 0MSWYWHYF5, 1C8RRWHD45]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Dimension 3 and higher
---

## Example

Let $t \colon (\mathbb{R}^3)^3 \to \mathbb{R}$ be the [[scalar triple product|059Q2XWJDC]] $t(u, v, w) = u \cdot (v \times w)$, where the [[cross product|0SEDGXG9S3]] is
$$v \times w = (v_2 w_3 - v_3 w_2,\ v_3 w_1 - v_1 w_3,\ v_1 w_2 - v_2 w_1).$$
We check that $t$ is an alternating trilinear form with $t(e_1, e_2, e_3) = 1$.

1. Trilinear.
   Each coordinate of $v \times w$ is a sum of products of one coordinate of $v$ and one coordinate of $w$, so the cross product is bilinear in $(v, w)$.
   The [[dot product|05HQYM0R4G]] is bilinear too, so $t$ is linear in each of $u$, $v$ and $w$.
2. Equal second and third arguments.
   Each coordinate of $v \times v$ has the form $v_2 v_3 - v_3 v_2 = 0$, so $v \times v = 0$ and $t(u, v, v) = 0$.
3. Equal first and second arguments.
   Write out the product:
$$u \cdot (u \times w) = u_1(u_2 w_3 - u_3 w_2) + u_2(u_3 w_1 - u_1 w_3) + u_3(u_1 w_2 - u_2 w_1).$$
4. The six products in step 3 cancel in pairs: $u_1 u_2 w_3$ with $-u_2 u_1 w_3$, $-u_1 u_3 w_2$ with $u_3 u_1 w_2$, and $u_2 u_3 w_1$ with $-u_3 u_2 w_1$.
   So $t(u, u, w) = 0$.
5. Equal first and third arguments.
   Exchanging $v$ and $w$ in the cross product changes its sign, so $t(u, v, u) = -t(u, u, v)$, and this is $0$ by step 4.
6. By steps 1 to 5, $t$ is [[alternating|0MSWYWHYF5]].
7. Normalization: $e_2 \times e_3 = (1 \cdot 1 - 0 \cdot 0,\ 0,\ 0) = e_1$, so $t(e_1, e_2, e_3) = e_1 \cdot e_1 = 1$.
8. A numerical check: for $u = (1, 0, 2)$, $v = (0, 1, 1)$ and $w = (1, 1, 0)$,
$$v \times w = (0 - 1,\ 1 - 0,\ 0 - 1) = (-1, 1, -1), \qquad t(u, v, w) = -1 + 0 - 2 = -3.$$

## Remarks

By the [[existence and uniqueness theorem|1C8RRWHD45]], $t(u, v, w)$ is the determinant of the matrix with rows $u$, $v$ and $w$, because both are alternating, trilinear and $1$ on the standard basis.
For the vectors of step 8, the rule of Sarrus confirms the value:
$$\det \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \end{pmatrix} = (0 + 0 + 0) - (2 + 1 + 0) = -3.$$
The absolute value $3$ is the volume of the parallelepiped with edges $u$, $v$ and $w$, and the negative sign says that $(u, v, w)$ is a left-handed triple.

Change $w$ to $u + v = (1, 1, 3)$.
Then $w$ lies in the plane of $u$ and $v$, the box is flat, and $t(u, v, u + v) = t(u, v, u) + t(u, v, v) = 0$ by linearity in the third argument and steps 2 and 5.

## Explanations

### L1 human

Three arrows in space span a slanted box.
The triple product gives the volume of this box, with a sign that says whether the three arrows are arranged like the thumb, index finger and middle finger of the right hand.
It is zero when two arrows are equal, because then the box is flat.
For the three arrows of step 8 the box has volume $3$.

### L2 human

To show that a formula in three vectors is a determinant, check linearity in each vector, zero on each pair of equal vectors, and the value $1$ on $e_1, e_2, e_3$.
Watch out: an alternating map must vanish for all three pairs of positions, not just one.
Here the pair of positions $2, 3$ came from $v \times v = 0$, the pair $1, 2$ needed a computation, and the pair $1, 3$ followed from the first two by a sign change.
