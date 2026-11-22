---
tag: VRD3P83FH7
kind: example
name: Matrices of different sizes cannot be added
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
not_instance_of:
  - target: 0Y7H3SAVA1
    note: a 2 by 2 matrix and a 2 by 3 matrix have no common set of positions, so their sum is not defined
uses: [0BVXADM10P]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_addition
    locator: Entrywise sum
---

## Example

Matrix addition pairs up entries by position, so it breaks down as soon as one matrix has a position that the other lacks.
Let
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \qquad C = \begin{pmatrix} 1 & 0 & 5 \\ 2 & 1 & 0 \end{pmatrix}.$$

1. The [[definition of the sum|0BVXADM10P]] asks that $A$ and $C$ have the same size.
2. The size of $A$ is $2 \times 2$, and the size of $C$ is $2 \times 3$, so the condition fails.
3. The position $(1, 3)$ has the entry $c_{13} = 5$, but $A$ has no entry $a_{13}$.
4. So the entry $(A + C)_{13} = a_{13} + c_{13}$ has no meaning, and $A + C$ is not defined.
5. Padding $A$ with a zero column does produce a sum,
$$\begin{pmatrix} 1 & 2 & 0 \\ 3 & 4 & 0 \end{pmatrix} + C = \begin{pmatrix} 2 & 2 & 5 \\ 5 & 5 & 0 \end{pmatrix},$$
but this is the sum of a new matrix and $C$, and the choice of where to put the zeros was ours.

## Remarks

Step 5 shows why no padding rule is built into the definition.
Putting the zero column first instead gives
$$\begin{pmatrix} 0 & 1 & 2 \\ 0 & 3 & 4 \end{pmatrix} + C = \begin{pmatrix} 1 & 1 & 7 \\ 2 & 4 & 4 \end{pmatrix},$$
a different answer, so "padding" does not give a well defined sum.

Some software extends the sum by broadcasting, for example adding a $2 \times 1$ column to each column of a $2 \times 3$ matrix.
Broadcasting is a convention of the software, and it is not matrix addition.

If $A$ is replaced by any $2 \times 3$ matrix, the sum is defined again, for example
$$\begin{pmatrix} 1 & 2 & 0 \\ 3 & 4 & 1 \end{pmatrix} + C = \begin{pmatrix} 2 & 2 & 5 \\ 5 & 5 & 1 \end{pmatrix}.$$

## Explanations

### L1 human

We can add two tables only if they have the same shape.
Here one table has two columns and the other has three.
The third column of the second table has nothing to be added to.

### L2 human

The sum is defined on each set $M_{m \times n}(R)$ separately, and there is no addition between two of these sets.
In terms of linear maps, $A$ describes a map $F^2 \to F^2$ and $C$ a map $F^3 \to F^2$, and two maps with different domains cannot be added.
The trap is to pad with zeros and call the result $A + C$.
