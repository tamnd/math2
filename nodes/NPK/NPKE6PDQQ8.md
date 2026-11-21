---
tag: NPKE6PDQQ8
kind: example
name: The conjugate transpose of a 2 × 2 matrix and of a product
msc: ["15A99", "15B57"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [0DXKE10PHF]
uses: [0EX045E2BP, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugate_transpose
    locator: Properties
---

## Example

We check the product rule $(AB)^* = B^* A^*$ and the scalar rule $(cA)^* = \overline{c} A^*$ on two complex matrices.
Let
$$A = \begin{pmatrix} 1 & i \\ 0 & 2 \end{pmatrix}, \qquad B = \begin{pmatrix} i & 1 \\ 1 & 0 \end{pmatrix}.$$

1. By the [[definition|0EX045E2BP]], swap the off-diagonal positions and conjugate every entry:
$$A^* = \begin{pmatrix} 1 & 0 \\ -i & 2 \end{pmatrix}, \qquad B^* = \begin{pmatrix} -i & 1 \\ 1 & 0 \end{pmatrix}.$$
2. Multiply $A$ by $B$, row times column:
$$AB = \begin{pmatrix} 1 \cdot i + i \cdot 1 & 1 \cdot 1 + i \cdot 0 \\ 0 \cdot i + 2 \cdot 1 & 0 \cdot 1 + 2 \cdot 0 \end{pmatrix} = \begin{pmatrix} 2i & 1 \\ 2 & 0 \end{pmatrix}.$$
3. Take the conjugate transpose of the product:
$$(AB)^* = \begin{pmatrix} -2i & 2 \\ 1 & 0 \end{pmatrix}.$$
4. Multiply the factors in the reversed order:
$$B^* A^* = \begin{pmatrix} (-i) \cdot 1 + 1 \cdot (-i) & (-i) \cdot 0 + 1 \cdot 2 \\ 1 \cdot 1 + 0 \cdot (-i) & 1 \cdot 0 + 0 \cdot 2 \end{pmatrix} = \begin{pmatrix} -2i & 2 \\ 1 & 0 \end{pmatrix}.$$
This is the matrix of step 3.
5. Now scale $A$ by $i$ and take the conjugate transpose:
$$iA = \begin{pmatrix} i & -1 \\ 0 & 2i \end{pmatrix}, \qquad (iA)^* = \begin{pmatrix} -i & 0 \\ -1 & -2i \end{pmatrix}.$$
Since $-i A^* = \begin{pmatrix} -i & 0 \\ -1 & -2i \end{pmatrix}$, we get $(iA)^* = -i A^* = \overline{i}\, A^*$, and not $i A^*$.

## Remarks

Step 4 checks the reversed order in one case.
The other order fails here: $A^* B^* = \begin{pmatrix} -i & 1 \\ 1 & -i \end{pmatrix}$, which is not $(AB)^*$.
Step 5 shows that a scalar comes out conjugated, so $A \mapsto A^*$ is not a linear map of complex vector spaces.
If $c$ is real, then $\overline{c} = c$, and the scalar rule looks like the rule for the [[transpose|09DXWYRD43]].

## Explanations

### L1 human

Each entry moves to its mirror position across the main diagonal, and its imaginary part changes sign.
For products the order turns around, just as when you take off socks and shoes: what went on last comes off first.

### L2 human

The product rule rests on one identity of complex numbers, $\overline{zw} = \overline{z}\, \overline{w}$.
The entry $(i, j)$ of $(AB)^*$ is $\overline{\sum_k a_{jk} b_{ki}} = \sum_k \overline{b_{ki}}\, \overline{a_{jk}}$, which is the entry $(i, j)$ of $B^* A^*$.
Watch out: with entries from a noncommutative ring, such as the quaternions, the order of the factors $\overline{b_{ki}}\, \overline{a_{jk}}$ matters, and there one needs $\overline{zw} = \overline{w}\, \overline{z}$.
