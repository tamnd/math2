---
tag: QM8XZDS9TK
kind: example
name: The dual of a matrix map acts on rows by right multiplication
msc: ["15A04"]
topics: [9K7FFF26QR]
audience: ug1
instance_of: [0AZ5ARP287]
uses: [0C2TQMW5A1, 0PDVQEP0ZC, 032Q9FB8MT, EGJXHX96R9, 0W809K6AW0]
sources:
  - url: https://en.wikipedia.org/wiki/Transpose_of_a_linear_map
    locator: Representation as a matrix
  - book: isbn:9780134860244
    locator: Section 2.6
---

## Example

Let $F$ be a field, let $A$ be an $m \times n$ matrix over $F$, and let $f \colon F^n \to F^m$ be $f(x) = Ax$, the [[matrix-vector product|0PDVQEP0ZC]].
Identify each form on $F^k$ with a row of length $k$, as in the example on [[row vectors as linear forms|EGJXHX96R9]].
We show that the [[dual map|0C2TQMW5A1]] $f^*$ sends a row $y$ of length $m$ to the row $yA$ of length $n$.

1. Let $y = (y_1, \dots, y_m)$, the form $z \mapsto yz$ on $F^m$.
2. By definition, $f^*(y)$ is the form $x \mapsto y(f(x)) = y(Ax)$ on $F^n$.
3. By associativity of [[matrix multiplication|032Q9FB8MT]], $y(Ax) = (yA)x$.
4. So $f^*(y)$ is the form given by the row $yA$.
5. Written as columns, $(yA)^{\mathsf{T}} = A^{\mathsf{T}} y^{\mathsf{T}}$. So, in the standard dual bases, $f^*$ has the matrix $A^{\mathsf{T}}$, the [[transpose|0W809K6AW0]] of $A$.

A numerical check with $m = n = 2$:

6. Let $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $y = (1, -1)$, the form $z_1 - z_2$.
7. Then $yA = (1 - 3,\ 2 - 4) = (-2, -2)$, so $f^*(y)$ is the form $-2x_1 - 2x_2$.
8. Direct check at $x = (1, 1)^{\mathsf{T}}$: $Ax = (3, 7)^{\mathsf{T}}$, and $y(Ax) = 3 - 7 = -4$. Also $(yA)x = -2 - 2 = -4$.
9. In columns: $A^{\mathsf{T}} (1, -1)^{\mathsf{T}} = (1 - 3,\ 2 - 4)^{\mathsf{T}} = (-2, -2)^{\mathsf{T}}$, the same coefficients.

## Remarks

- The map $f$ multiplies columns by $A$ on the left; the dual map multiplies rows by $A$ on the right. This is the cleanest way to see why the matrix of $f^*$ is $A^{\mathsf{T}}$.
- The rows of $A$ are $f^*(e_1^*), \dots, f^*(e_m^*)$, the pullbacks of the coordinate forms of $F^m$. So the image of $f^*$ is the row space of $A$.

## Explanations

### L1 human

A matrix $A$ turns a column $x$ into the column $Ax$.
A row $y$ measures columns: it turns $z$ into the number $yz$.
Measuring $Ax$ with $y$ is the same as measuring $x$ with the new row $yA$.
So the dual map turns the row $y$ into the row $yA$.

### L2 human

To compute $f^*$ on a form, multiply its row by $A$ from the right.

1. Write the form on $F^m$ as a row $y$.
2. Compute $yA$.
3. Read $yA$ as a form on $F^n$.

The typical use is to read the rows of $A$ as pulled back coordinate forms, which links the row space to the dual map.
A trap: multiplying $Ay$ instead of $yA$ is not even defined when $y$ is a row.
