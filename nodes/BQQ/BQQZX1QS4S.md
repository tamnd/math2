---
tag: BQQZX1QS4S
kind: example
name: The determinant as a quadratic form on 2 × 2 matrices
msc: [15A63, 15A15]
topics: [6TSCEW8QMK]
audience: ug1
instance_of: [0RBQS1JJCR, 0HYFWKKY3C]
uses: [0HZNE5QZDJ, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Definitions
---

## Example

Let $V$ be the real vector space of $2 \times 2$ real matrices, with dimension $4$.
Define $Q \colon V \to \R$ by the [[determinant|00KDZRW4C0]]:
$$Q\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc.$$

1. Homogeneity: $Q(tM) = (ta)(td) - (tb)(tc) = t^2 (ad - bc) = t^2 Q(M)$ for every $t \in \R$.
2. Polar form: let $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ and $M' = \begin{pmatrix} a' & b' \\ c' & d' \end{pmatrix}$. Expanding the products gives
$$Q(M + M') - Q(M) - Q(M') = ad' + a'd - bc' - b'c.$$
3. Each term is a product of one entry of $M$ and one entry of $M'$. So the polar form is linear in $M$ and in $M'$, and $Q$ is a [[quadratic form|0HZNE5QZDJ]].
4. In the coordinates $(a, b, c, d)$, the form is $ad - bc$. Its symmetric matrix has $\frac12$ in the positions $(1, 4)$ and $(4, 1)$, and $-\frac12$ in the positions $(2, 3)$ and $(3, 2)$.
5. A diagonal form: put $a = s + t$, $d = s - t$, $b = u + w$ and $c = u - w$. Then $ad - bc = s^2 - t^2 - u^2 + w^2$.
6. Check of step 5: $(s + t)(s - t) = s^2 - t^2$ and $(u + w)(u - w) = u^2 - w^2$. The difference is $s^2 - t^2 - u^2 + w^2$.

## Remarks

The determinant is not a linear map, but on $2 \times 2$ matrices it is a quadratic form.
By step 5, it has two positive and two negative squares, so its [[signature|07EZA80NEH]] is $(2, 2, 0)$.
The matrices with $Q(M) = 0$ are the singular matrices; they form a cone, not a subspace.
For $n \times n$ matrices with $n \ge 3$, the determinant is homogeneous of degree $n$, so it is not a quadratic form.
The same polar form $ad' + a'd - bc' - b'c$ appears as the mixed term in $\det(M + M')$.

## Explanations

### L1 human

The determinant $ad - bc$ of a $2 \times 2$ table is a sum of products of two entries.
If we multiply every entry by $t$, the determinant is multiplied by $t^2$.
For example, $\det \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = -2$, and $\det \begin{pmatrix} 2 & 4 \\ 6 & 8 \end{pmatrix} = 16 - 24 = -8 = 4 \cdot (-2)$.

### L2 human

The typical use of this example is in geometry: the matrices with determinant $1$ lie on the "unit sphere" of this form.
By step 5, that set is $s^2 + w^2 - t^2 - u^2 = 1$, a quadric in $\R^4$.
A trap: $\det(M + M') \ne \det M + \det M'$ in general.
The difference is exactly the polar form of step 2.
