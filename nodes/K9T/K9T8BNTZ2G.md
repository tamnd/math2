---
tag: K9T8BNTZ2G
kind: example
name: The permanent is multilinear but not a determinant
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
instance_of: [X9B1XETBPF]
not_instance_of:
  - target: 00KDZRW4C0
    note: the 2 × 2 permanent ad + bc is multilinear in the rows with value 1 on the identity, but it is 2 on a matrix with two equal rows, so it is not alternating
uses: [R582CKDHF4, 0MSWYWHYF5, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: As an alternating multilinear form
---

## Example

Let $p \colon M_2(\mathbb{R}) \to \mathbb{R}$ be the $2 \times 2$ [[permanent|R582CKDHF4]],
$$p \begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad + bc.$$
It has the same two products as the determinant $ad - bc$, but with a plus sign.
We check the three properties of the [[definition of the determinant|0C3CFHDN6R]] one by one.

1. Linear in row $1$.
   For fixed $(c, d)$, the value $p = d \cdot a + c \cdot b$ is a linear function of $(a, b)$.
2. Linear in row $2$.
   For fixed $(a, b)$, the value $p = a \cdot d + b \cdot c$ is a linear function of $(c, d)$.
3. Value $1$ on the identity.
   We have $p(I_2) = 1 \cdot 1 + 0 \cdot 0 = 1$.
4. Zero on equal rows.
   This fails, because
$$p \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = 1 \cdot 1 + 1 \cdot 1 = 2 \ne 0.$$

So $p$ satisfies properties 1 and 3 but not property 2, and $p$ is not the [[determinant|00KDZRW4C0]].
For the same matrix the determinant is $1 - 1 = 0$, as property 2 demands.

## Remarks

The example shows that the alternating property cannot be dropped from the definition.
Linearity in each row and the value on $I_2$ alone allow more than one function, and the permanent is a second one.

The permanent also ignores the order of the rows.
Swap the two rows:
$$p \begin{pmatrix} c & d \\ a & b \end{pmatrix} = cb + da = p \begin{pmatrix} a & b \\ c & d \end{pmatrix}.$$
A determinant changes sign under the same swap, and that sign change is exactly what the alternating property forces.

Change the ring and the picture changes.
Over a field of characteristic $2$, we have $+1 = -1$, so $ad + bc = ad - bc$ and the permanent equals the determinant.
There, $2 = 0$, and the matrix of ones gives $p = 0$ as well.

## Explanations

### L1 human

The permanent looks almost like the determinant, but it adds the two diagonal products instead of subtracting them.
For a table with two equal rows, such as rows $(1, 1)$ and $(1, 1)$, it gives $2$ and not $0$.
So it breaks one of the three rules that define the determinant.

### L2 human

The $n \times n$ permanent is the Leibniz sum with every sign replaced by $+$.
For a matrix of zeros and ones, it counts the ways to choose one $1$ in each row with no two in the same column.
For example, the permanent of the $3 \times 3$ matrix of ones is $3! = 6$, while its determinant is $0$.
Row reduction does not help, because adding a multiple of one row to another changes the permanent, and no fast general method for the permanent is known.
Watch out: if you forget the signs in a Laplace expansion, you compute the permanent and not the determinant.
