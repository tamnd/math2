---
tag: DWKSAB7V4T
kind: example
name: The ring of 2 × 2 matrices over the field with two elements
msc: ["16S50", "15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [AB2MD5CD13]
uses: [0FHVPRAE60, 076JGP6R3T, 0F6ES3BRYP]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_ring
    locator: Examples
  - url: https://en.wikipedia.org/wiki/GF(2)
    locator: lead section
---

## Example

Let $\mathbb{F}_2 = \{0, 1\}$ be the field with two elements, where $1 + 1 = 0$.
We look at the [[matrix ring|0FHVPRAE60]] $M_2(\mathbb{F}_2)$.

1. A matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ has 4 entries, each $0$ or $1$. So $M_2(\mathbb{F}_2)$ has $2^4 = 16$ elements.
2. It is not commutative: $E_{12} E_{21} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, but $E_{21} E_{12} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$.
3. Let $J = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$. Then $J^2 = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix} = 0$ in $\mathbb{F}_2$, since $2 = 0$.
4. So the four matrices $0$, $E_{12}$, $E_{21}$ and $J$ all have square $0$.
5. Every matrix $A$ satisfies $A + A = 0$, because $2 = 0$ in $\mathbb{F}_2$. So the ring has [[characteristic|0F6ES3BRYP]] $2$.
6. The matrix $P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has $P^2 = I$, and $P \neq I$; also $P = I + J$.

## Remarks

The invertible elements are the six matrices with $ad - bc = 1$ in $\mathbb{F}_2$; they form a group isomorphic to the symmetric group $S_3$.
A finite ring this small already shows the main features of matrix rings: non-commutativity, zero divisors and nonzero nilpotents.

## Explanations

### L1 human

With only the numbers $0$ and $1$, there are exactly 16 matrices of size $2 \times 2$.
They can be added and multiplied with the rule $1 + 1 = 0$.
Even here, $AB$ and $BA$ can differ.

### L2 human

Step 3 shows a nilpotent matrix with no zero entry, which cannot happen for $2 \times 2$ real matrices with all entries equal to $1$.
The field matters: over $\mathbb{R}$, the same $J$ satisfies $J^2 = 2J$.
