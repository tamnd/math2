---
tag: 1MN49GY0GV
kind: example
name: The basic Weyr matrix of structure (2, 2)
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: research
instance_of: [9XEA4VR8WP]
uses: [9XEA4VR8WP, 0PBFS92AJP, 8G3X8MPG7E]
sources:
  - url: https://en.wikipedia.org/wiki/Weyr_canonical_form
    locator: Definitions
  - book: isbn:9780199793730
---

## Example

Let $W = \begin{pmatrix} 0 & I_2 \\ 0 & 0 \end{pmatrix} = E_{13} + E_{24}$, a $4 \times 4$ matrix over a field $F$ cut into blocks of sizes $2, 2$.

1. Diagonal blocks. $W_{11} = W_{22} = 0 \cdot I_2$.
2. Superdiagonal block. $W_{12} = I_2$, the identity with no zero rows below, since $n_1 = n_2 = 2$.
3. There are no other blocks above the diagonal, and $W_{21} = 0$. So $W$ is a basic Weyr matrix with eigenvalue $0$ and structure $(2, 2)$.
4. Powers. $W e_3 = e_1$, $W e_4 = e_2$, $W e_1 = W e_2 = 0$, so $W^2 = 0$. $\dim \ker W = 2$ and $\dim \ker W^2 = 4$, with jumps $2, 2$.
5. Jordan form. The chains $e_3 \mapsto e_1 \mapsto 0$ and $e_4 \mapsto e_2 \mapsto 0$ give $W \sim J_2(0) \oplus J_2(0)$.
6. Centralizer. Write $X = \begin{pmatrix} P & Q \\ R & S \end{pmatrix}$ in $2 \times 2$ blocks. Then $WX = \begin{pmatrix} R & S \\ 0 & 0 \end{pmatrix}$ and $XW = \begin{pmatrix} 0 & P \\ 0 & R \end{pmatrix}$.
7. So $XW = WX$ if and only if $R = 0$ and $S = P$. The centralizer is the set of $\begin{pmatrix} P & Q \\ 0 & P \end{pmatrix}$, block upper triangular of dimension $8 = 2^2 + 2^2$.

## Remarks

In the Jordan basis, the matrix is $J_2(0) \oplus J_2(0) = E_{12} + E_{34}$, and $E_{31} + E_{42}$ commutes with it; this matrix is below the block diagonal for the blocks $\{1, 2\}$, $\{3, 4\}$.
The centralizer of $W$ is isomorphic to the algebra $M_2(F[t]/(t^2))$ of $2 \times 2$ matrices over the dual numbers, through $P + tQ$.

## Explanations

### L1 human

This matrix moves the last two basis vectors onto the first two, and kills the first two.
Every matrix that commutes with it has the same $2 \times 2$ block twice on the diagonal and zero in the lower left corner.

### L2 human

The block computation in step 6 needs only the rule for multiplying $2 \times 2$ block matrices.
The answer shows the general pattern of the Weyr form: commuting matrices are block upper triangular, and the later diagonal blocks repeat the corners of the earlier ones.
