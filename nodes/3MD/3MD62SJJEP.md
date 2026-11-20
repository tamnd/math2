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

Let $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
Both are [[symmetric|0N28QN4CYA]].

1. $AB = \begin{pmatrix} 1 \cdot 0 + 0 \cdot 1 & 1 \cdot 1 + 0 \cdot 0 \\ 0 \cdot 0 + 0 \cdot 1 & 0 \cdot 1 + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.
2. $BA = \begin{pmatrix} 0 \cdot 1 + 1 \cdot 0 & 0 \cdot 0 + 1 \cdot 0 \\ 1 \cdot 1 + 0 \cdot 0 & 1 \cdot 0 + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$.
3. $AB$ has entry $1$ at $(1, 2)$ and $0$ at $(2, 1)$, so $AB$ is not symmetric.
4. Also $(AB)^{\mathsf{T}} = BA$, as the [[theorem|YX9Z3E9SGN]] predicts, and $AB \neq BA$.

## Remarks

$AB + BA = B$ is symmetric and $AB - BA = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ is [[skew-symmetric|0PBY4E9GQF]].
So the symmetric matrices are closed under $A \circ B = (AB + BA)/2$ but not under the matrix product.

## Explanations

### L1 human

Here two mirror-image matrices give a product that is not a mirror image.
The cause is that $AB$ and $BA$ are different.

### L2 human

$A$ projects onto the first axis and $B$ exchanges the axes.
Exchanging and then projecting is not the same as projecting and then exchanging, and the failure of symmetry measures this.
