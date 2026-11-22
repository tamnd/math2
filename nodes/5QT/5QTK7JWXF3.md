---
tag: 5QTK7JWXF3
kind: statement
role: theorem
name: Block inverse formula with the Schur complement
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: ug2
about: [6HWFBXYPZP]
uses: [CA1J41NWGS, 01AXG9KZQF, 0TWTS88TWN, 0EB9N0S33C]
sources:
  - url: https://en.wikipedia.org/wiki/Schur_complement
    locator: Background
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Blockwise inversion
  - book: isbn:9780521548236
    locator: Section 0.7
---

## Statement

A block matrix with an invertible corner block factors as a block LDU product, and its inverse is built from the inverses of the corner block and of its Schur complement.
Let $F$ be a field, and let $M = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$ be a [[block matrix|01AXG9KZQF]] over $F$ with $A$ of size $p \times p$ and $D$ of size $q \times q$.
Let $A$ be [[invertible|0EB9N0S33C]], and let $S = M/A = D - CA^{-1}B$ be the [[Schur complement|CA1J41NWGS]] of $A$ in $M$.

1. (Block LDU factorization.)
$$M = \begin{pmatrix} I_p & 0 \\ CA^{-1} & I_q \end{pmatrix} \begin{pmatrix} A & 0 \\ 0 & S \end{pmatrix} \begin{pmatrix} I_p & A^{-1}B \\ 0 & I_q \end{pmatrix}.$$
2. $M$ is invertible if and only if $S$ is invertible.
3. If $S$ is invertible, then
$$M^{-1} = \begin{pmatrix} A^{-1} + A^{-1} B S^{-1} C A^{-1} & -A^{-1} B S^{-1} \\ -S^{-1} C A^{-1} & S^{-1} \end{pmatrix}.$$
4. In the same way, let $D$ be invertible and let $T = M/D = A - BD^{-1}C$. Then $M$ is invertible if and only if $T$ is invertible, and in that case
$$M^{-1} = \begin{pmatrix} T^{-1} & -T^{-1} B D^{-1} \\ -D^{-1} C T^{-1} & D^{-1} + D^{-1} C T^{-1} B D^{-1} \end{pmatrix}.$$

## Remarks

### The theorem at work

For $p = q = 1$ and $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with $a \ne 0$, the complement is $S = d - cb/a = (ad - bc)/a$.
The four blocks of part 3 are then
$$S^{-1} = \frac{a}{ad - bc}, \qquad \frac{1}{a} + \frac{1}{a}\, b\, S^{-1}\, c\, \frac{1}{a} = \frac{1}{a} + \frac{bc}{a(ad - bc)} = \frac{d}{ad - bc}, \qquad -\frac{b}{ad - bc}, \qquad -\frac{c}{ad - bc}.$$
This is the [[formula for the inverse of a $2 \times 2$ matrix|8XWC7RKNN1]].
The [[worked $3 \times 3$ example|DAYPSS15ET]] uses a $2 \times 2$ block $A$.

### Why the hypotheses are needed

The formula needs $A^{-1}$.
For the [[exchange matrix|D31650AJ43]] $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ with $A = (0)$, the matrix $M$ is invertible, but parts 1 and 3 do not apply, and part 4 does not apply either, since $D = (0)$.
Part 3 needs $S$ invertible.
For $M = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ and $A = (1)$, we get $S = 1 - 1 \cdot 1 \cdot 1 = 0$, and $M$ is singular, as part 2 predicts.
The blocks $A$ and $D$ must be square, so that $A^{-1}$ and $S^{-1}$ make sense, while $B$ and $C$ can be rectangular.

### What it gives you

Comparing the two formulas for $M^{-1}$ when $A$, $D$, $S$ and $T$ are invertible gives $T^{-1} = A^{-1} + A^{-1} B S^{-1} C A^{-1}$, which is the [[Woodbury formula|MDZDEFE53C]] for $(A - BD^{-1}C)^{-1}$.
The lower right block of $M^{-1}$ is $S^{-1}$, so the inverse of a Schur complement is a block of an inverse.
With [[determinants|0KA7A4ENVJ]], part 1 gives $\det M = \det A \det S$.
For $p = n - 1$ and $q = 1$, the number $S$ is the last pivot of the [[LU decomposition|0RKG5YW66Y]].

### Generalizations

The formulas hold for matrices over any ring when $A$ and $S$ are units, because the proof only multiplies blocks.
The quotient formula $M/A = (M/E)/(A/E)$ of Crabtree and Haynsworth holds when $E$ is an invertible leading block of $A$.
If $M$ is invertible but $A$ is singular, part 4 may still apply with an invertible $D$, and for singular blocks generalized inverses give a version of the formula, which belongs to matrix theory.

## Explanations

### L1 human

To invert a matrix made of four blocks, invert the upper left block first.
Then form the Schur complement and invert it too.
The four blocks of the inverse are built from these two inverses.

### L2 human

Compute in this order: $A^{-1}$, then $A^{-1}B$ and $CA^{-1}$, then $S = D - C(A^{-1}B)$, then $S^{-1}$.
Every block of $M^{-1}$ is a product of these pieces, so nothing is computed twice.
A trap: the upper left block of $M^{-1}$ is in general not $A^{-1}$; it has the correction term $A^{-1} B S^{-1} C A^{-1}$, which vanishes for example when $B = 0$ or $C = 0$.

### L3 human

Part 1 says that $M$ is in the double coset of $\operatorname{diag}(A, S)$ for the unipotent block triangular groups.
The formula is the block version of $LDU$, and it is the starting point of recursive inversion algorithms, such as the one Strassen gave with his fast multiplication.
Iterating over a chain of leading blocks recovers the [[existence of the LU decomposition|3PPBWG0B96]].
