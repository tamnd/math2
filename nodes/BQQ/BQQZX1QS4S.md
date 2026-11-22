---
tag: BQQZX1QS4S
kind: example
name: The determinant as a quadratic form on 2 × 2 matrices
msc: ["15A63", "15A15"]
topics: [6TSCEW8QMK]
audience: ug1
instance_of: [0RBQS1JJCR, 0HYFWKKY3C]
uses: [0HZNE5QZDJ, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Definitions
---

## Example

Let $V$ be the real vector space of $2 \times 2$ real matrices, which has dimension $4$.
Define $Q \colon V \to \mathbb{R}$ by the [[determinant|00KDZRW4C0]]:
$$Q\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc.$$
We check that $Q$ is a [[quadratic form|0HZNE5QZDJ]], find its matrix, and put it in diagonal form.

1. Scaling. Every entry of $tM$ carries a factor $t$, so $Q(tM) = (ta)(td) - (tb)(tc) = t^2 (ad - bc) = t^2 Q(M)$ for every $t \in \mathbb{R}$.
2. Polar form. Let $M'$ have entries $a', b', c', d'$. Expand $(a + a')(d + d') - (b + b')(c + c')$ and remove $Q(M)$ and $Q(M')$:
$$Q(M + M') - Q(M) - Q(M') = ad' + a'd - bc' - b'c.$$
3. Bilinearity. Each term of step 2 is one entry of $M$ times one entry of $M'$, so the polar form is linear in $M$ and in $M'$. So $Q$ is a quadratic form.
4. Matrix. In the coordinates $(a, b, c, d)$ the form is $ad - bc$, with two cross terms and no squares. Its symmetric matrix has $\tfrac{1}{2}$ at the positions $(1, 4)$ and $(4, 1)$, $-\tfrac{1}{2}$ at the positions $(2, 3)$ and $(3, 2)$, and $0$ elsewhere.
5. Diagonal form. Put $a = s + t$, $d = s - t$, $b = u + w$ and $c = u - w$. This change of variables is invertible, since $s = (a + d)/2$, $t = (a - d)/2$, $u = (b + c)/2$ and $w = (b - c)/2$. Then
$$ad - bc = (s + t)(s - t) - (u + w)(u - w) = s^2 - t^2 - u^2 + w^2.$$

## Remarks

The determinant is not linear, but on $2 \times 2$ matrices it is a quadratic form.
Step 5 gives two positive and two negative squares, so its [[signature|07EZA80NEH]] is $(2, 2, 0)$.
The polar form of step 2 is exactly the mixed term in $\det(M + M') = \det M + \det M' + (ad' + a'd - bc' - b'c)$.
So $\det(M + M')$ differs from $\det M + \det M'$ by the polar form, and that is the usual way to see that the determinant is not additive.

The matrices with $Q(M) = 0$ are the singular matrices.
They form a cone through $0$, because $Q(tM) = t^2 Q(M)$, but not a subspace: $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ are singular, while their sum $I_2$ is not.
For $n \times n$ matrices with $n \ge 3$, the determinant is homogeneous of degree $n$, so it fails condition 1 and is not a quadratic form.

## Explanations

### L1 human

The determinant $ad - bc$ of a $2 \times 2$ table is built from products of two entries.
If you multiply every entry by $t$, each product picks up $t^2$.
For example, $\det \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = 4 - 6 = -2$, and $\det \begin{pmatrix} 2 & 4 \\ 6 & 8 \end{pmatrix} = 16 - 24 = -8 = 4 \cdot (-2)$.

### L2 human

Here is a use in geometry: the matrices with determinant $1$ form the group $\mathrm{SL}_2(\mathbb{R})$.
In the coordinates of step 5 this set is the quadric $s^2 + w^2 - t^2 - u^2 = 1$ in $\mathbb{R}^4$.
For example, the rotation by a right angle, $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, has $s = 0$, $t = 0$, $u = 0$ and $w = -1$, and $w^2 = 1$.
Watch out: the inverse change of variables in step 5 divides by $2$, so the diagonal form is not available over a field of characteristic $2$.
