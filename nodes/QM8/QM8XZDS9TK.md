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
As in the example on [[row vectors as linear forms|EGJXHX96R9]], we identify each linear form on $F^k$ with a row of length $k$, which acts on a column $z$ by $z \mapsto yz$.
We show that the [[dual map|0C2TQMW5A1]] $f^*$ sends a row $y$ of length $m$ to the row $yA$ of length $n$.

1. Let $y = (y_1, \dots, y_m)$, viewed as the form $z \mapsto yz$ on $F^m$.
2. By the definition of the dual map, $f^*(y)$ is the form $x \mapsto y(f(x)) = y(Ax)$ on $F^n$.
3. [[Matrix multiplication|032Q9FB8MT]] is associative, so $y(Ax) = (yA)x$ for every column $x$.
4. So $f^*(y)$ is the form given by the row $yA$.
5. If we write forms as columns instead, the column of $f^*(y)$ is $(yA)^{\mathsf{T}} = A^{\mathsf{T}} y^{\mathsf{T}}$. So in the dual bases of the standard bases, $f^*$ has the matrix $A^{\mathsf{T}}$, the [[transpose|0W809K6AW0]] of $A$.

Now a check with numbers, for $m = n = 2$.
Let $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $y = (1, -1)$, the form $z_1 - z_2$.
Multiply the row by $A$ from the right:
$$yA = \begin{pmatrix} 1 \cdot 1 - 1 \cdot 3 & 1 \cdot 2 - 1 \cdot 4 \end{pmatrix} = \begin{pmatrix} -2 & -2 \end{pmatrix}.$$
So $f^*(y)$ is the form $-2x_1 - 2x_2$.
Check at $x = (1, 1)^{\mathsf{T}}$: here $Ax = (3, 7)^{\mathsf{T}}$, so $y(Ax) = 3 - 7 = -4$, and also $(yA)x = -2 - 2 = -4$.
In columns, $A^{\mathsf{T}} (1, -1)^{\mathsf{T}} = (1 - 3, \, 2 - 4)^{\mathsf{T}} = (-2, -2)^{\mathsf{T}}$, which has the same entries.

## Remarks

The example shows the cleanest reason why the transpose appears.
The map $f$ multiplies columns by $A$ from the left, and the dual map multiplies rows by $A$ from the right.
Turning rows into columns turns right multiplication by $A$ into left multiplication by $A^{\mathsf{T}}$.

It also shows where the rows of $A$ come from.
Take $y = e_i^*$, the row with $1$ in place $i$ and $0$ elsewhere, which reads off coordinate $i$ of $F^m$.
Then $e_i^* A$ is row $i$ of $A$, so the rows of $A$ are the pullbacks $f^*(e_1^*), \dots, f^*(e_m^*)$.
Since these forms span $(F^m)^*$, the image of $f^*$ is the row space of $A$, which is the start of the [[proof by duality|7DQXA4AY1D]] that row rank equals column rank.

If $A$ is not square, the sizes change but nothing else.
For a $1 \times n$ matrix $A = a$, the map $f$ is itself the form $x \mapsto ax$, and $f^*$ sends the form $s \mapsto cs$ on $F$ to the row $ca$.

## Explanations

### L1 human

A matrix $A$ turns a column $x$ into the column $Ax$.
A row $y$ measures columns: it turns a column $z$ into the number $yz$.
Measuring $Ax$ with $y$ gives the same number as measuring $x$ with the new row $yA$.
So the dual map turns the row $y$ into the row $yA$.
For $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, the row $(1, 0)$ becomes $(1, 2)$, the first row of $A$.

### L2 human

Here is a typical use: write a pulled back equation without any substitution.
Let $A = \begin{pmatrix} 2 & 0 & 1 \\ 1 & 3 & -1 \end{pmatrix}$, so $f \colon F^3 \to F^2$, and let the form on $F^2$ be $y = (1, 2)$, that is, $z_1 + 2z_2$.
Then
$$yA = \begin{pmatrix} 2 + 2 & 0 + 6 & 1 - 2 \end{pmatrix} = \begin{pmatrix} 4 & 6 & -1 \end{pmatrix},$$
so the pulled back form is $4x_1 + 6x_2 - x_3$.
Check at $x = (1, 0, 0)^{\mathsf{T}}$: $Ax = (2, 1)^{\mathsf{T}}$ and $2 + 2 \cdot 1 = 4$, the first entry of $yA$.
Watch out: the product $Ay$ is not defined here, since $y$ is a row; the dual map always multiplies from the right.
