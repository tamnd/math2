---
tag: AA0NDX7JXV
kind: example
name: The determinant is not a linear form
msc: ["15A04", "15A15"]
topics: [9K7FFF26QR]
audience: ug1
not_instance_of:
  - target: 07YQ1C78G0
    note: the determinant on 2 × 2 matrices is neither additive nor homogeneous, since det(2I) = 4 and det(E11) + det(E22) = 0 differs from det(I) = 1
uses: [0RT96J4D3H, 00KDZRW4C0, 0RE6X3BGPN]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_form
    locator: Non-example
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: lead section
---

## Example

Let $V = M_2(\mathbb{R})$ be the [[space of $2 \times 2$ real matrices|0RE6X3BGPN]], and let $\det \colon V \to \mathbb{R}$ be the [[determinant|00KDZRW4C0]],
$$\det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc.$$
The determinant returns one number for each matrix, but it is not a [[linear form|0RT96J4D3H]] on $V$.
Both conditions of a linear form fail, and one small case is enough for each.

Homogeneity fails.
Let $I$ be the identity matrix, so $\det I = 1$.
Doubling $I$ doubles both diagonal entries:
$$\det(2I) = 2 \cdot 2 - 0 \cdot 0 = 4.$$
A linear form $f$ would give $f(2I) = 2 f(I)$, and here $2 \det I = 2 \ne 4$.

Additivity fails.
Let $E_{11} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $E_{22} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$.
Each has a zero on the diagonal, so
$$\det E_{11} = 1 \cdot 0 - 0 \cdot 0 = 0, \qquad \det E_{22} = 0 \cdot 1 - 0 \cdot 0 = 0.$$
But $E_{11} + E_{22} = I$, and $\det I = 1 \ne 0 + 0$.

## Remarks

The determinant is linear in each column when the other column is held fixed.
This property is called multilinearity, and it is weaker than linearity in the whole matrix: doubling the matrix doubles both columns, so the determinant is multiplied by $2 \cdot 2 = 4$.

The size of the matrix matters.
On $1 \times 1$ matrices $\det(a) = a$, so there the determinant is a linear form.
For every size $n \ge 2$ it fails, since $\det(2 I_n) = 2^n$, while linearity would give $2$.

The [[trace|0XC1RDBY7A]] is a linear form on $M_2(\mathbb{R})$, and it makes a good contrast.
Both numbers appear in the characteristic polynomial $t^2 - (\tr A) \, t + \det A$ of a $2 \times 2$ matrix, but only the trace is linear.

## Explanations

### L1 human

The determinant of a $2 \times 2$ matrix is a single number, but it does not behave like a linear form.
If you double every entry, the determinant becomes four times as large, not twice as large.
Also, two matrices with determinant $0$ can add up to the identity matrix, which has determinant $1$.

### L2 human

To show that a map to the scalars is not a linear form, one failing case is enough, and the best test cases are the simplest matrices.
Try the scaling rule on $I$: $\det(2I) = 4$, while linearity would give $2$.
Try the sum rule on $E_{11}$ and $E_{22}$: $\det(E_{11} + E_{22}) = 1$, while linearity would give $0$.
The typical use of this example is as a warning that "linear in each column" and "linear" are different properties.
Watch out: the formula $\det(A + B) = \det A + \det B$ is false, and it is a common slip in proofs.
