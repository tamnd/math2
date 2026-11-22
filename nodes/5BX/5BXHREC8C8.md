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

The familiar moves of plane geometry that keep the origin fixed, such as turning, flipping, slanting and stretching, are all linear maps, and each one is a $2 \times 2$ matrix.
Each map below has the form $x \mapsto Ax$ on $\R^2$, so it is a [[linear map|0RJF668P1T]] by the [[theorem on matrix transformations|W6KB0J3SZZ]].
The columns of $A$ are the images of $e_1 = (1, 0)$ and $e_2 = (0, 1)$.
For each map we compute the images of $e_1$, $e_2$ and $(1, 1)$, and we describe the image of the unit square with corners $(0, 0)$, $(1, 0)$, $(0, 1)$ and $(1, 1)$.

Rotations come first.
The rotation by an angle $\theta$ about the origin turns $e_1$ to $(\cos\theta, \sin\theta)$ and $e_2$ to $(-\sin\theta, \cos\theta)$, so
$$A_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}.$$
For a right angle, $\theta = \pi/2$ gives $\cos\theta = 0$ and $\sin\theta = 1$, so $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.
Then $e_1 \mapsto (0, 1)$, $e_2 \mapsto (-1, 0)$ and $(1, 1) \mapsto (-1, 1)$, and the image is the unit square turned a quarter turn, with area $1$.

Two reflections come next.
The reflection in the $x$-axis has $A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$, so $e_1 \mapsto (1, 0)$, $e_2 \mapsto (0, -1)$ and $(1, 1) \mapsto (1, -1)$.
Its image of the square is the square below the $x$-axis with corners $(0, 0)$, $(1, 0)$, $(0, -1)$ and $(1, -1)$, again of area $1$.
The reflection in the line $y = x$ has $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, so $e_1 \mapsto (0, 1)$, $e_2 \mapsto (1, 0)$ and $(1, 1) \mapsto (1, 1)$.
The image is the unit square itself, but the corners $(1, 0)$ and $(0, 1)$ change places.

The projection onto the $x$-axis has $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$.
It sends $e_1 \mapsto (1, 0)$, $e_2 \mapsto (0, 0)$ and $(1, 1) \mapsto (1, 0)$, so the square collapses to the segment from $(0, 0)$ to $(1, 0)$, of area $0$.

The horizontal shear has $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.
It sends $e_1 \mapsto (1, 0)$, $e_2 \mapsto (1, 1)$ and $(1, 1) \mapsto (2, 1)$.
The image is the parallelogram with corners $(0, 0)$, $(1, 0)$, $(2, 1)$ and $(1, 1)$, with base $1$ and height $1$, so its area is $1$.

The scaling with factors $2$ and $3$ has $A = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$.
It sends $e_1 \mapsto (2, 0)$, $e_2 \mapsto (0, 3)$ and $(1, 1) \mapsto (2, 3)$, so the image is the rectangle $[0, 2] \times [0, 3]$, of area $6$.

In every case the image of the square is the parallelogram with sides $A e_1$ and $A e_2$.
The reason is linearity: a point $s e_1 + t e_2$ of the square, with $0 \le s, t \le 1$, goes to $s\,Ae_1 + t\,Ae_2$.

## Remarks

### What the areas say

The areas of the images are $1$ for the rotations, $1$ for both reflections, $0$ for the projection, $1$ for the shear and $6$ for the scaling.
These are the absolute values of the [[determinants|00KDZRW4C0]]: for example $\det \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = 1 \cdot 1 - 1 \cdot 0 = 1$ and $\det \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = 0 - 1 = -1$.
This is the meaning of the [[determinant as a signed volume|04X3PR72VJ]].
The two reflections have determinant $-1$, and the sign records that they reverse the order of the corners around the square.

### Which maps can be undone

The projection is the only map in the list that is not invertible.
It loses the second coordinate: its [[kernel|0S23E6YE83]] is the $y$-axis, and its [[image|0WSFKKT6FF]] is the $x$-axis.
Every other map can be undone by another map in the same family, such as the rotation by $-\theta$, the same reflection again, the shear with $-1$ in place of $1$, or the scaling with factors $\tfrac{1}{2}$ and $\tfrac{1}{3}$.

### What is not linear

A [[rotation|0HFREYRSZP]] is a linear map only when its center is the origin.
The quarter turn about the point $(1, 0)$ fixes $(1, 0)$ and sends the origin to $(1, -1)$, so it moves $0$ and is not linear.
A [[translation|DTCM6N02A9]] fails for the same reason.
Related pages treat [[reflections|06BRDF3F0E]], [[projections|033DA1WE8Y]] and [[homotheties|0ZG1PNEP35]], the scalings with equal factors.

## Explanations

### L1 human

A linear map of the plane is fixed by where it sends the two unit arrows $(1, 0)$ and $(0, 1)$.
The unit square then goes to the parallelogram built on the two new arrows.
Rotations turn the square, reflections flip it, shears slant it, scalings stretch it and projections flatten it.
For example, the scaling by $2$ and $3$ turns the square into a $2$ by $3$ rectangle of area $6$.

### L2 human

The image of the unit square is a quick picture of any $2 \times 2$ matrix.
Take $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$, read its two columns $(2, 1)$ and $(1, 1)$, draw them as arrows from the origin, and complete the parallelogram.
The fourth corner is $(2, 1) + (1, 1) = (3, 2)$, which is $A(1, 1)$.
The area is $|2 \cdot 1 - 1 \cdot 1| = 1$, so this map changes no areas, although it changes shapes.
The method shows at a glance whether a map flattens the plane: it does exactly when the two columns lie on one line.
Watch out: not every geometric motion is linear, since translations and rotations about points other than the origin move $0$.
