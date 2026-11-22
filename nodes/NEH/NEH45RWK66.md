---
tag: NEH45RWK66
kind: example
name: Two matrices of different rank are not equivalent
msc: ["15A21"]
topics: [P8J6QR66TJ]
audience: ug1
not_instance_of:
  - target: 0CMHSGTWXB
    note: diag(1, 0) has rank 1 and the identity I_2 has rank 2, and invertible factors do not change the rank
uses: [0P21AVFFSP, 02FDWY55AS, 0EWQEYRVA8, 0S4WTRE9GG]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_equivalence
---

## Example

Two diagonal matrices that differ in a single entry can fail to be equivalent, because that entry changes the rank.
Let $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $B = I_2$ over $\mathbb{Q}$.

1. The column space of $A$ is spanned by $e_1$, so $\operatorname{rank} A = 1$, by the [[definition of rank|0EWQEYRVA8]].
2. The column space of $B$ is $\mathbb{Q}^2$, so $\operatorname{rank} B = 2$.
3. Suppose that $B = PAQ$ with invertible $P$ and $Q$.
4. By the [[rank of a product|02FDWY55AS]], $\operatorname{rank}(PAQ) \le \operatorname{rank} A = 1$.
5. This contradicts $\operatorname{rank} B = 2$. So $A$ and $B$ are not [[equivalent|0P21AVFFSP]].

A second argument avoids rank.
If $B = PAQ$, then $A = P^{-1} B Q^{-1}$ is invertible as a [[product of invertible matrices|0S4WTRE9GG]].
But $A e_2 = 0$ with $e_2 \ne 0$, so $A$ is not invertible, which is again a contradiction.

## Remarks

### What equivalence sees

The two matrices have the same size, are both diagonal, and agree in the entry $(1, 1)$.
None of this matters, because equivalence sees only the rank.
For $2 \times 2$ matrices there are exactly three classes, of rank $0$, $1$ and $2$.

### Watch out

One cannot "scale the second row of $A$ up to $1$", because the scaling factor would have to turn $0$ into $1$, and no multiplication does this.
Adding a multiple of row 1 to row 2 does not help either: it gives $\begin{pmatrix} 1 & 0 \\ c & 0 \end{pmatrix}$, whose second column is still zero, so the rank is still $1$.

## Explanations

### L1 human

Row and column operations never change the rank.
The first matrix has rank $1$ and the identity has rank $2$.
So no sequence of such operations turns one into the other.

### L2 human

To show that two matrices of the same size are not equivalent, it is enough to compute their ranks and find that they differ.
To show that they are equivalent, equal ranks are enough too, by the rank normal form theorem.
