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

Over a field $F$, let
$$W = \begin{pmatrix} 0 & I_2 \\ 0 & 0 \end{pmatrix} = E_{13} + E_{24} = \begin{pmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix},$$
cut into blocks of sizes $2, 2$.
We check that $W$ is a [[basic Weyr matrix|9XEA4VR8WP]] with eigenvalue $0$ and structure $(2, 2)$, and we find the matrices that commute with it.

1. The diagonal blocks are $W_{11} = W_{22} = 0 \cdot I_2$, as the definition asks for $\lambda = 0$.
2. The block $W_{12}$ has size $n_1 \times n_2 = 2 \times 2$, so the definition asks for $I_2$ with no zero rows below, and $W_{12} = I_2$.
3. The only other block is $W_{21} = 0$, so $W$ is a basic Weyr matrix of structure $(2, 2)$.
4. On the standard basis, $W e_1 = W e_2 = 0$, $W e_3 = e_1$ and $W e_4 = e_2$. So $W^2 = 0$, and the kernels of $W$ and $W^2$ have dimensions $2$ and $4$, with jumps $2, 2$.
5. The chains $e_3 \mapsto e_1 \mapsto 0$ and $e_4 \mapsto e_2 \mapsto 0$ have length $2$, so $W$ is similar to the [[Jordan matrix|0PBFS92AJP]] $J_2(0) \oplus J_2(0)$.
6. Write a $4 \times 4$ matrix as $X = \begin{pmatrix} P & Q \\ R & S \end{pmatrix}$ in $2 \times 2$ blocks, and multiply in both orders:
$$W X = \begin{pmatrix} R & S \\ 0 & 0 \end{pmatrix}, \qquad X W = \begin{pmatrix} 0 & P \\ 0 & R \end{pmatrix}.$$
7. Comparing blocks, $XW = WX$ holds exactly when $R = 0$ and $S = P$. So the [[commuting matrices|8G3X8MPG7E]] are the matrices $\begin{pmatrix} P & Q \\ 0 & P \end{pmatrix}$ with $P, Q \in M_2(F)$, a space of dimension $8 = 2^2 + 2^2$.

## Remarks

The centralizer is block upper triangular, as the Weyr form promises, and its second diagonal block repeats the first.
In the Jordan basis the same map is $J_2(0) \oplus J_2(0) = E_{12} + E_{34}$, and there the commuting matrix $E_{31} + E_{42}$ sits below the block diagonal; the [[Jordan matrix of the same map|Y64E6EXGY5]] checks this.

The answer has an algebraic reading.
The map $P + tQ \mapsto \begin{pmatrix} P & Q \\ 0 & P \end{pmatrix}$ identifies the centralizer with $M_2(F[t]/(t^2))$, the $2 \times 2$ matrices over the ring in which $t^2 = 0$.
Check: the product of two such block matrices has diagonal $PP'$ and corner $PQ' + QP'$, which is the product $(P + tQ)(P' + tQ')$ with the $t^2$ term dropped.

If the structure changes to $(2, 1, 1)$, the [[basic Weyr matrix of that structure|H568T13KR4]] has a centralizer of dimension $6$, again block upper triangular.

## Explanations

### L1 human

The matrix $W$ moves the third and fourth basis vectors onto the first and second, and it sends the first two to zero.
So it is two copies of the same two-step ladder, set side by side.
Every matrix that commutes with $W$ has the same $2 \times 2$ block twice on the diagonal and zero in the lower left corner.

### L2 human

The whole computation is block multiplication of $2 \times 2$ block matrices, so you can do it without writing sixteen entries.
The result shows the general pattern of the Weyr form: commuting matrices are block upper triangular, and each diagonal block is a corner of the one before it.
Here the corner is the whole block, because the two groups have the same size.
Watch out: the block $W_{12}$ is $I_2$ here only because $n_1 = n_2$; for unequal sizes it has zero rows at the bottom.
