---
tag: 3MD62SJJEP
kind: example
name: Two symmetric matrices whose product is not symmetric
msc: ["15A99", "15B57"]
topics: [Y1ESNQ2V52]
audience: ug1
not_instance_of:
  - target: 0VR671PHE5
    note: the product of the symmetric matrices E11 and (0, 1; 1, 0) is E12, which is not symmetric
illustrates: [YX9Z3E9SGN]
uses: [0N28QN4CYA, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_matrix
    locator: Properties
---

## Example

Let
$$A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \qquad B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$
over $\mathbb{R}$.
Both are [[symmetric|0N28QN4CYA]], and we show that their [[product|076JGP6R3T]] is not.

1. Multiply in the order $AB$:
$$AB = \begin{pmatrix} 1 \cdot 0 + 0 \cdot 1 & 1 \cdot 1 + 0 \cdot 0 \\ 0 \cdot 0 + 0 \cdot 1 & 0 \cdot 1 + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}.$$
2. The entry of $AB$ at $(1, 2)$ is $1$ and the entry at $(2, 1)$ is $0$, so $AB$ is not symmetric.
3. Multiply in the order $BA$:
$$BA = \begin{pmatrix} 0 \cdot 1 + 1 \cdot 0 & 0 \cdot 0 + 1 \cdot 0 \\ 1 \cdot 1 + 0 \cdot 0 & 1 \cdot 0 + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}.$$
4. So $AB \neq BA$, and $(AB)^{\mathsf{T}} = BA$, as the [[theorem on products of symmetric matrices|YX9Z3E9SGN]] predicts.

## Remarks

The failure comes from the order of the factors, and two combinations of the products repair it.
The sum $AB + BA = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = B$ is symmetric, and the difference $AB - BA = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ is [[skew-symmetric|0PBY4E9GQF]].
This holds for every pair of symmetric matrices, since $(AB + BA)^{\mathsf{T}} = BA + AB$ and $(AB - BA)^{\mathsf{T}} = BA - AB$.
So the symmetric matrices are closed under the product $(AB + BA)/2$, but not under the matrix product.

A small change gives commuting factors.
If we replace $B$ by $\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$, then $AB = BA = 0$, which is symmetric.

## Explanations

### L1 human

Here two matrices that look the same after a flip over the diagonal have a product that does not.
The reason is that $AB$ and $BA$ are different, and flipping $AB$ gives $BA$.

### L2 human

Read the two matrices as maps of the plane: $A$ projects onto the first axis, and $B$ exchanges the two axes.
Exchanging and then projecting, which is $AB$, sends $(0, 1)$ to $(1, 0)$ and $(1, 0)$ to $0$, while projecting and then exchanging, which is $BA$, does the opposite.
The lack of symmetry of $AB$ is exactly the difference $AB - BA$ between the two orders.
