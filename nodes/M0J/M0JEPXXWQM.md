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

Let $A = \begin{pmatrix} 0 & 1 & 2 & 3 \\ -1 & 0 & 4 & 5 \\ -2 & -4 & 0 & 6 \\ -3 & -5 & -6 & 0 \end{pmatrix}$ over $\mathbb{Z}$.

1. The perfect matchings of $\{1, 2, 3, 4\}$ are $\{12, 34\}$, $\{13, 24\}$ and $\{14, 23\}$, with signs $+1$, $-1$, $+1$.
2. So the [[definition|C9JJD2AVJR]] gives $\operatorname{pf}(A) = a_{12} a_{34} - a_{13} a_{24} + a_{14} a_{23} = 6 - 10 + 12 = 8$.
3. By the [[theorem|473MBZST4D]], $\det A = 8^2 = 64$.
4. Check by the [[Laplace expansion|0C08BQ3M05]] along row 1: $\det A = 1 \cdot C_{12} + 2 \cdot C_{13} + 3 \cdot C_{14}$.
5. $C_{12} = -\det \begin{pmatrix} -1 & 4 & 5 \\ -2 & 0 & 6 \\ -3 & -6 & 0 \end{pmatrix} = -(-48) = 48$.
6. $C_{13} = \det \begin{pmatrix} -1 & 0 & 5 \\ -2 & -4 & 6 \\ -3 & -5 & 0 \end{pmatrix} = -40$.
7. $C_{14} = -\det \begin{pmatrix} -1 & 0 & 4 \\ -2 & -4 & 0 \\ -3 & -5 & -6 \end{pmatrix} = -(-32) = 32$.
8. So $\det A = 48 - 80 + 96 = 64$, which agrees with step 3.

## Remarks

The cofactors are $C_{12} = a_{34} P$, $C_{13} = -a_{24} P$ and $C_{14} = a_{23} P$ with $P = 8$: indeed $48 = 6 \cdot 8$, $-40 = -5 \cdot 8$ and $32 = 4 \cdot 8$.
This is the pattern of the proof for size $4$.
The Pfaffian has $3$ terms, while the Leibniz formula for $\det A$ has $24$.

## Explanations

### L1 human

The Pfaffian of a $4 \times 4$ alternating matrix has three terms, one for each way to pair up four indices.
Here it is $8$, so the determinant is $64$.

### L2 human

The Laplace expansion confirms $64$ with three $3 \times 3$ determinants.
A trap: the middle term of the Pfaffian, for the pairing $\{13, 24\}$, has a minus sign.
