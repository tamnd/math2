---
tag: REB4ZHN28T
kind: example
name: Linear algebra in computer graphics
msc: ["15A04", "68U05", "51N15"]
topics: [K0FNC6CWZN]
audience: ug1
instance_of: [0JF0TVYGWT]
illustrates: [00BKRZKMSS, FS9FRJ17D2]
uses: [032Q9FB8MT, 00BKRZKMSS, HNY4CPEEJA, DTCM6N02A9, FS9FRJ17D2, YHKSDF59HK]
sources:
  - book: isbn:9780321982384
    locator: Section 2.7
  - url: https://en.wikipedia.org/wiki/Transformation_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Homogeneous_coordinates
    locator: lead section
---

## Example

In a video game, a car on the screen is a list of corner points, and the game redraws it many times each second as the car turns and moves.
Each redraw must turn, stretch or move every point and then show a 3D scene on a flat screen.
Matrices do all of this, and a chain of steps becomes one product of matrices.
We work out the three basic tools: matrices for linear maps, homogeneous coordinates for translations, and a projection from space to the screen.

**Part 1: linear maps of the plane.**

1. The shear $S = \begin{pmatrix} 1 & 0.5 \\ 0 & 1 \end{pmatrix}$ sends $(1, 1)$ to $(1.5, 1)$ and $(0, 1)$ to $(0.5, 1)$.
   It slants the unit square to the right and keeps its area, since $\det S = 1$.
2. The scaling $K = \operatorname{diag}(2, 0.5)$ doubles widths and halves heights.
3. The [[composition|00BKRZKMSS]] "first shear, then scale" has the matrix $K S = \begin{pmatrix} 2 & 1 \\ 0 & 0.5 \end{pmatrix}$, by [[matrix multiplication|032Q9FB8MT]].
4. The other order gives $S K = \begin{pmatrix} 2 & 0.25 \\ 0 & 0.5 \end{pmatrix} \ne K S$, so the order matters.

**Part 2: translations by homogeneous coordinates.**

1. The translation $p \mapsto p + (3, 1)$ moves the origin, so it is [[not a linear map of the plane|DTCM6N02A9]], and no $2 \times 2$ matrix gives it.
2. In [[homogeneous coordinates|FS9FRJ17D2]], the point $(x, y)$ is the vector $(x, y, 1)$.
   Then the translation is the $3 \times 3$ matrix $T = \begin{pmatrix} 1 & 0 & 3 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$, since $T (x, y, 1)^{\mathsf T} = (x + 3, y + 1, 1)^{\mathsf T}$.
3. The [[rotation matrix|HNY4CPEEJA]] by $90^\circ$ about the origin becomes $R = \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$.
4. "First rotate, then translate" is $T R = \begin{pmatrix} 0 & -1 & 3 \\ 1 & 0 & 1 \\ 0 & 0 & 1 \end{pmatrix}$.
   It sends $(1, 0)$ to $(3, 2)$.
5. "First translate, then rotate" is $R T = \begin{pmatrix} 0 & -1 & -1 \\ 1 & 0 & 3 \\ 0 & 0 & 1 \end{pmatrix}$.
   It sends $(1, 0)$ to $(-1, 4)$.
6. The matrix applied first stands on the right, next to the vector, and the two orders give different pictures.
7. Rotation by $90^\circ$ about the point $c = (1, 1)$ is "move $c$ to the origin, rotate, move back".
   Its matrix is
$$T_{c} R\, T_{-c} = \begin{pmatrix} 0 & -1 & 2 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$
   Check: this matrix fixes $(1, 1)$, since $(-1 + 2, 1 + 0) = (1, 1)$.
   It sends $(2, 1)$ to $(1, 2)$, which is a quarter turn about $c$.
8. The triangle with the corners $(0, 0)$, $(2, 0)$, $(0, 1)$ goes under $T R$ to the triangle with the corners $(3, 1)$, $(3, 3)$, $(2, 1)$.
   To get all three corners at once, multiply $T R$ by the $3 \times 3$ matrix whose columns are the three corners.

**Part 3: perspective projection.**

1. A camera at the origin looks along the positive $z$-axis, with the screen in the plane $z = d$.
   A point $(x, y, z)$ with $z > 0$ appears at $(d x / z, d y / z)$, where the ray from the camera meets the screen.
2. This [[perspective projection|YHKSDF59HK]] divides by $z$, so it is not linear in $(x, y, z)$.
3. In homogeneous coordinates it is linear.
   The matrix $P = \begin{pmatrix} d & 0 & 0 & 0 \\ 0 & d & 0 & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix}$ sends $(x, y, z, 1)$ to $(d x, d y, z)$.
   Division by the last entry then gives the screen point $(d x / z, d y / z)$.
4. With $d = 1$, the point $(2, 1, 4)$ goes to $(2, 1, 4)$ and then to $(0.5, 0.25)$.
5. The point $(4, 2, 8)$ lies on the same ray and has the same image $(0.5, 0.25)$.
   So $P$ is not injective, and depth is lost.
6. The point $(2, 1, 2)$ is closer to the camera and appears at $(1, 0.5)$, farther from the center of the screen.
   This is why near objects look larger.
7. Rotations and translations of space are $4 \times 4$ matrices in homogeneous coordinates, so the whole path from a model to the screen is one product of matrices.

## Remarks

### What the example shows

Graphics software works with $3 \times 3$ matrices for the plane and $4 \times 4$ matrices for space.
Every affine map and every perspective projection becomes one matrix, and a chain of steps becomes one product.
For a model with a million points, the program multiplies the matrices of the chain once and then applies the product to each point.

### Watch out: the order of the factors

The order of the factors is the main source of errors.
Change the translation vector $t = (3, 1)$ in part 2 to $(0, 0)$: then $T = I$, and the two orders agree.
For every other $t$ they differ.
The reason is that the last column of $T R$ is $(t, 1)$, the last column of $R T$ is $(R t, 1)$, and a quarter turn fixes no vector except $0$.
In space, even two rotations about different axes [[do not commute|F1KZ5GE4TC]].

### Inverses

Homogeneous coordinates also make the inverse of a translation a matrix: $T^{-1}$ has the entries $-3$ and $-1$ in its last column.
The last row $(0, 0, 1)$ of an affine matrix stays the same under products and inverses.
The inverse of a product reverses the order, so $(T R)^{-1} = R^{-1} T^{-1}$.

### Try it

First, find the matrix that scales by $2$ about the point $(1, 0)$.
It is $T_{c} \operatorname{diag}(2, 2, 1)\, T_{-c}$ with $c = (1, 0)$, which is $\begin{pmatrix} 2 & 0 & -1 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$.
Check: it fixes $(1, 0)$, since $2 - 1 = 1$, and it sends $(2, 0)$ to $(3, 0)$.

Second, check that $R^{-1} T^{-1}$ sends $(3, 2)$ back to $(1, 0)$.
First $T^{-1}$ gives $(0, 1)$, and then the rotation by $-90^\circ$ gives $(1, 0)$.

## Explanations

### L1 human

A computer picture is made of many points, and each point is a pair or triple of numbers.
To turn, stretch or move the picture, the computer multiplies every point by a small table of numbers, a matrix.
For example, a turn by a quarter circle sends the point $(1, 0)$ to $(0, 1)$.
A trick with one extra coordinate equal to $1$ also handles moves of the whole picture.
A turn followed by a move gives a different result from a move followed by a turn.

### L2 human

To build a graphics transformation, do these steps.

1. Write each step as a matrix in homogeneous coordinates, with rotations and scalings in the upper left block and translations in the last column.
2. Multiply the matrices in the reverse order of the steps, so that the first step stands on the right.
3. Apply the product to the points, and divide by the last coordinate if a projection is part of the chain.

For example, to rotate by $90^\circ$ about $(1, 1)$, the chain is $T_{-c}$, then $R$, then $T_c$.
So the matrix is $T_c R T_{-c}$, as in part 2.

The typical use is a scene graph, where each object carries its own matrix relative to its parent.
The trap is the order of the product, because writing the steps from left to right in the order they happen gives the wrong matrix.

### L3 human

The $3 \times 3$ matrices with last row $(0, 0, 1)$ form the affine group of the plane, a semidirect product of the translations and the general linear group.
Homogeneous coordinates identify the plane with the affine chart $z = 1$ of the projective plane, and projective maps act there as $3 \times 3$ invertible matrices up to scale.
A perspective projection is a linear map in these coordinates followed by the passage to the chart, and this explains why it maps lines to lines.
Rotations in space are often stored as unit quaternions, which compose smoothly and avoid the loss of a degree of freedom that Euler angles can suffer.
