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

A matrix ring over a finite field is finite, so every one of its features can be checked by hand.
Let $\mathbb{F}_2 = \{0, 1\}$ be the field with two elements, where $1 + 1 = 0$, and look at the [[matrix ring|0FHVPRAE60]] $M_2(\mathbb{F}_2)$.

1. A matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ has $4$ entries, each $0$ or $1$. So $M_2(\mathbb{F}_2)$ has $2^4 = 16$ elements.
2. The ring is not commutative. With the matrix units $E_{12}$ and $E_{21}$,
$$E_{12} E_{21} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \qquad E_{21} E_{12} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}.$$
3. Let $J = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$. Each entry of $J^2$ is $1 \cdot 1 + 1 \cdot 1 = 1 + 1 = 0$, so $J^2 = 0$.
4. So the four matrices $0$, $E_{12}$, $E_{21}$ and $J$ all have square $0$, and the last three are nonzero zero divisors.
5. Every matrix $A$ satisfies $A + A = 0$, because $1 + 1 = 0$ in each entry. So the ring has [[characteristic|0F6ES3BRYP]] $2$.
6. The matrix $P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ satisfies $P^2 = I$ and $P \ne I$. Also $P = I + J$, so $P^2 = I + 2J + J^2 = I$ gives a second check, since $I$ and $J$ commute.

## Remarks

### Exactly four matrices with square zero

Step 4 lists all of them.
A $2 \times 2$ matrix $A$ over a field has $A^2 = 0$ exactly when its trace $a + d$ and its determinant $ad - bc$ are both $0$.
Over $\mathbb{F}_2$, trace $0$ means $a = d$, and then $a^2 = a$ turns the determinant condition into $a = bc$.
If $a = d = 0$, then $bc = 0$, which gives $0$, $E_{12}$ and $E_{21}$.
If $a = d = 1$, then $b = c = 1$, which gives $J$.

### The invertible matrices

A matrix is invertible exactly when $ad - bc = 1$ in $\mathbb{F}_2$.
Six of the $16$ matrices pass this test: $I$, $P$, and the four matrices
$$\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \quad \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}, \quad \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}, \quad \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}.$$
They form the group $GL_2(\mathbb{F}_2)$, which permutes the three nonzero vectors of $\mathbb{F}_2^2$ and is isomorphic to the symmetric group $S_3$.

### Try it

Find the inverse of $U = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ in $M_2(\mathbb{F}_2)$.
Answer: $U^2 = \begin{pmatrix} 1 & 1 + 1 \\ 0 & 1 \end{pmatrix} = I$, so $U$ is its own inverse.

## Explanations

### L1 human

With only the numbers $0$ and $1$, and the rule $1 + 1 = 0$, there are exactly $16$ matrices of size $2 \times 2$.
They can be added and multiplied like real matrices, using this rule.
Even in this small ring, $AB$ and $BA$ can differ, and a nonzero matrix can have square zero.

### L2 human

The typical use of this ring is as a small test case: a claim about matrix rings can be checked on all $16$ elements.
Step 3 shows how the field changes the answer.
Over $\mathbb{R}$ the same matrix $J$ has $J^2 = 2J \ne 0$, but over $\mathbb{F}_2$ the entry $2$ becomes $0$.
Watch out: a nilpotent matrix need not have any zero entry, as $J$ shows.
