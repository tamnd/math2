---
tag: M0JEPXXWQM
kind: example
name: Pfaffian of a 4 × 4 alternating integer matrix
msc: ["15A15"]
topics: [DTBK11SR77]
audience: grad
instance_of: [NH5HWBPWS9]
uses: [C9JJD2AVJR, 473MBZST4D, 0C08BQ3M05]
sources:
  - url: https://en.wikipedia.org/wiki/Pfaffian
---

## Example

Let
$$A = \begin{pmatrix} 0 & 1 & 2 & 3 \\ -1 & 0 & 4 & 5 \\ -2 & -4 & 0 & 6 \\ -3 & -5 & -6 & 0 \end{pmatrix}$$
over $\mathbb{Z}$.
It is alternating, since its diagonal is $0$ and each entry below the diagonal is the negative of its mirror entry.
We compute its [[Pfaffian|NH5HWBPWS9]] and check the square rule by computing $\det A$ independently.

1. The perfect matchings of $\{1, 2, 3, 4\}$ are $\{12, 34\}$, $\{13, 24\}$ and $\{14, 23\}$, with signs $+1$, $-1$ and $+1$.
2. So the [[definition|C9JJD2AVJR]] gives
$$\operatorname{pf}(A) = a_{12} a_{34} - a_{13} a_{24} + a_{14} a_{23} = 1 \cdot 6 - 2 \cdot 5 + 3 \cdot 4 = 8.$$
3. By the [[square rule|473MBZST4D]], $\det A$ should be $8^2 = 64$.
4. We check this by the [[Laplace expansion|0C08BQ3M05]] along row 1.
   Its first entry is $0$, so
$$\det A = 1 \cdot C_{12} + 2 \cdot C_{13} + 3 \cdot C_{14},$$
   where $C_{1j}$ is $(-1)^{1+j}$ times the determinant of $A$ without row 1 and column $j$.
5. Delete column 2 and expand along the first row of the minor:
$$\det \begin{pmatrix} -1 & 4 & 5 \\ -2 & 0 & 6 \\ -3 & -6 & 0 \end{pmatrix} = -1 \cdot 36 - 4 \cdot 18 + 5 \cdot 12 = -48,$$
   so $C_{12} = -(-48) = 48$.
6. Delete column 3:
$$\det \begin{pmatrix} -1 & 0 & 5 \\ -2 & -4 & 6 \\ -3 & -5 & 0 \end{pmatrix} = -1 \cdot 30 - 0 + 5 \cdot (-2) = -40,$$
   so $C_{13} = -40$.
7. Delete column 4:
$$\det \begin{pmatrix} -1 & 0 & 4 \\ -2 & -4 & 0 \\ -3 & -5 & -6 \end{pmatrix} = -1 \cdot 24 - 0 + 4 \cdot (-2) = -32,$$
   so $C_{14} = -(-32) = 32$.
8. Hence
$$\det A = 1 \cdot 48 + 2 \cdot (-40) + 3 \cdot 32 = 48 - 80 + 96 = 64,$$
   which agrees with step 3.

## Remarks

The cofactors are not random: $C_{12} = 48 = a_{34} \cdot 8$, $C_{13} = -40 = -a_{24} \cdot 8$ and $C_{14} = 32 = a_{23} \cdot 8$.
Each cofactor in row 1 is the Pfaffian times the entry of the complementary pair, with the sign of the Pfaffian formula.
So the Laplace expansion rebuilds the Pfaffian a second time, and the [[proof for sizes 2 and 4|5G56J9G502]] follows exactly this pattern.

The Pfaffian needed $3$ products of $2$ entries, while the Leibniz formula for $\det A$ has $24$ products of $4$ entries.
If we change one entry, say $a_{34} = 6$ to $a_{34} = 1$ with $a_{43} = -1$, the Pfaffian becomes $1 - 10 + 12 = 3$, and the determinant becomes $9$.
If we make $a_{34} = -2$, the Pfaffian becomes $-2 - 10 + 12 = 0$, and the matrix is singular.

## Explanations

### L1 human

The Pfaffian of a $4 \times 4$ alternating matrix has three terms, one for each way to pair up four indices.
Here the three terms are $6$, $-10$ and $12$, so the Pfaffian is $8$.
The determinant is then $64$, which we confirm with a longer computation.

### L2 human

The Laplace expansion confirms $64$ with three $3 \times 3$ determinants, so the Pfaffian saved most of the work.
The integer entries also show a fact that is not visible from the determinant formula: the determinant of an alternating integer matrix of even size is a perfect square.
Watch out: the middle term, for the pairing $\{13, 24\}$, has a minus sign, and forgetting it here would give $28$ instead of $8$.
