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

Let $V = M_2(\R)$ be the [[space of $2 \times 2$ real matrices|0RE6X3BGPN]], and let $\det \colon V \to \R$ be the [[determinant|00KDZRW4C0]], $\det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$.
We show that $\det$ is not a [[linear form|0RT96J4D3H]] on $V$.

1. Homogeneity fails. Let $I$ be the identity matrix. Then $\det(2I) = 2 \cdot 2 - 0 \cdot 0 = 4$.
2. A linear form $f$ satisfies $f(2I) = 2 f(I)$. Here $2 \det I = 2 \cdot 1 = 2 \ne 4$.
3. Additivity fails. Let $E_{11} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $E_{22} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$.
4. Then $\det E_{11} = 1 \cdot 0 - 0 \cdot 0 = 0$ and $\det E_{22} = 0 \cdot 1 - 0 \cdot 0 = 0$.
5. But $E_{11} + E_{22} = I$, and $\det I = 1 \ne 0 + 0$.
6. So $\det$ satisfies neither condition of a linear form.

## Remarks

- The determinant is linear in each column when the other column is fixed. This property is multilinearity, and it is weaker than linearity in the whole matrix.
- On $1 \times 1$ matrices, $\det(a) = a$, so the determinant is a linear form there. It fails to be linear for every size $n \ge 2$, since $\det(2I_n) = 2^n \ne 2$.
- The [[trace|0XC1RDBY7A]] is a linear form on $M_2(\R)$, and it is often compared with the determinant: both are coefficients of the characteristic polynomial.

## Explanations

### L1 human

The determinant of a $2 \times 2$ matrix is a single number, but it does not behave like a linear form.
If every entry is doubled, the determinant becomes four times as large, not twice as large.
Two matrices with determinant $0$ can add up to the identity matrix, which has determinant $1$.

### L2 human

To show that a map to the scalars is not a linear form, one failed instance is enough.

1. Test the scaling rule on a simple input: $\det(2I) = 4$, while linearity would give $2$.
2. Test the sum rule on two simple inputs: $\det(E_{11} + E_{22}) = 1$, while linearity would give $0$.

The typical use of this example is a warning: "linear in each row" and "linear" are different properties.
A trap: the formula $\det(A + B) = \det A + \det B$ is false, and students sometimes use it in proofs.
