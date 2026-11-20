---
tag: 5BXHREC8C8
kind: example
name: Linear transformations of the plane
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: school
instance_of: [0NRYHJPQG2]
uses: [0RJF668P1T, W6KB0J3SZZ, 0CCQV3884B, 0V7ZD6P7RK]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Transformation_matrix
    locator: Examples in 2 dimensions
  - book: isbn:9780321982384
    locator: Section 1.9
---

## Example

Each map below is a map $\R^2 \to \R^2$ of the form $x \mapsto Ax$ for a $2 \times 2$ matrix $A$.
So each map is a [[linear map|0RJF668P1T]], by the [[theorem on matrix transformations|W6KB0J3SZZ]].
The columns of $A$ are the images of $e_1 = (1, 0)$ and $e_2 = (0, 1)$.
The unit square has the corners $(0, 0)$, $(1, 0)$, $(0, 1)$ and $(1, 1)$.
For each map, we compute the images of $e_1$, $e_2$ and $(1, 1)$, and we describe the image of the unit square.

1. Rotation by a right angle. $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$. Then $e_1 \mapsto (0, 1)$, $e_2 \mapsto (-1, 0)$ and $(1, 1) \mapsto (-1, 1)$. The image is the unit square turned a quarter turn about the origin. Its area is $1$.
2. Rotation by an angle $\theta$. $A = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$. The columns are $e_1$ and $e_2$ turned by $\theta$. Item 1 is the case $\theta = \pi/2$, where $\cos\theta = 0$ and $\sin\theta = 1$.
3. Reflection in the $x$-axis. $A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$. Then $e_1 \mapsto (1, 0)$, $e_2 \mapsto (0, -1)$ and $(1, 1) \mapsto (1, -1)$. The image is the square below the $x$-axis with corners $(0, 0)$, $(1, 0)$, $(0, -1)$, $(1, -1)$. Its area is $1$.
4. Reflection in the line $y = x$. $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$. Then $e_1 \mapsto (0, 1)$, $e_2 \mapsto (1, 0)$ and $(1, 1) \mapsto (1, 1)$. The image is the unit square again, but the corners $(1, 0)$ and $(0, 1)$ change places.
5. Projection onto the $x$-axis. $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$. Then $e_1 \mapsto (1, 0)$, $e_2 \mapsto (0, 0)$ and $(1, 1) \mapsto (1, 0)$. The image is the segment from $(0, 0)$ to $(1, 0)$. Its area is $0$.
6. Horizontal shear. $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$. Then $e_1 \mapsto (1, 0)$, $e_2 \mapsto (1, 1)$ and $(1, 1) \mapsto (2, 1)$. The image is the parallelogram with corners $(0, 0)$, $(1, 0)$, $(2, 1)$, $(1, 1)$. Its base is $1$ and its height is $1$, so its area is $1$.
7. Scaling. $A = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$. Then $e_1 \mapsto (2, 0)$, $e_2 \mapsto (0, 3)$ and $(1, 1) \mapsto (2, 3)$. The image is the rectangle $[0, 2] \times [0, 3]$. Its area is $6$.

In each item, the image of the square is the parallelogram with sides $A e_1$ and $A e_2$.
The reason is that a point $s e_1 + t e_2$ of the square goes to $s\,Ae_1 + t\,Ae_2$, by linearity.

## Remarks

- The areas $1, 1, 1, 1, 0, 1, 6$ are the absolute values of the [[determinants|00KDZRW4C0]] of the matrices. This is the meaning of the [[determinant as a signed volume|04X3PR72VJ]].
- The two reflections have determinant $-1$; they reverse the order of the corners around the square.
- The projection is the only map in the list that is not invertible. Its kernel is the $y$-axis, and its image is the $x$-axis.
- A [[rotation|0HFREYRSZP]] is a linear map only when its centre is the origin. A rotation about another point moves $0$, so it is not linear.
- See also [[reflections|06BRDF3F0E]], [[projections|033DA1WE8Y]] and [[homotheties|0ZG1PNEP35]], which are the scalings with equal factors.

## Explanations

### L1 human

A linear map of the plane is fixed by where it sends the two unit arrows $(1, 0)$ and $(0, 1)$.
The unit square then goes to the parallelogram built on the two new arrows.
Rotations turn the square, reflections flip it, shears slant it, scalings stretch it and projections flatten it.

### L2 human

The image of the unit square is a quick picture of any $2 \times 2$ matrix.
Read the two columns, draw them as arrows from the origin and complete the parallelogram.
The area of the parallelogram is the factor by which the map changes all areas.
The trap is to think that every geometric motion is linear: translations and rotations about points other than the origin are not.
