---
tag: RC5BTSG8T2
kind: statement
role: theorem
name: Determinant as volume scaling factor
msc: ["15A15", "28A75"]
topics: [DTBK11SR77]
audience: ug2
uses: [0C3CFHDN6R, 2Z2QVWZ262]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Signed volume of a parallelotope
---

## Statement

A real square matrix multiplies every volume by the same factor, and that factor is the absolute value of its determinant.
Let $n \ge 1$, let $A$ be a real $n \times n$ matrix, viewed as the linear map $x \mapsto Ax$ of $\mathbb{R}^n$, and let $\lambda$ be [[Lebesgue measure|2Z2QVWZ262]] on $\mathbb{R}^n$.

1. For every Borel set $S \subseteq \mathbb{R}^n$, the image $A(S)$ is Lebesgue measurable, and
$$\lambda(A(S)) = \lvert \det A \rvert \, \lambda(S),$$
   with the [[determinant|0C3CFHDN6R]] $\det A$ and the convention $0 \cdot \infty = 0$.
2. In particular, let $v_1, \dots, v_n$ be the columns of $A$.
   The parallelotope $P = \{ t_1 v_1 + \dots + t_n v_n : 0 \le t_i \le 1 \}$, which is the image of the unit cube $[0, 1]^n$, has volume $\lambda(P) = \lvert \det A \rvert$.

## Remarks

### The unit square and its image

Take $A$ with the columns $v_1 = (3, 1)$ and $v_2 = (1, 2)$.
It sends the unit square to the parallelogram with the sides $v_1$ and $v_2$, and part 2 gives its area:
$$\lvert \det A \rvert = \lvert 3 \cdot 2 - 1 \cdot 1 \rvert = 5.$$
Check with lengths and the dot product: the squared area is $\lVert v_1 \rVert^2 \lVert v_2 \rVert^2 - (v_1 \cdot v_2)^2 = 10 \cdot 5 - 5^2 = 25$, so the area is $5$.
Part 1 says more: every region is scaled by the same factor.
The unit disc, of area $\pi$, goes to an ellipse of area $5\pi$.

### The sign is the orientation

The determinant itself is a *signed volume*: its absolute value is the volume of $P$, and its sign records the [[orientation|0QJJAQ6ZYZ]] of the columns.
When $\det A > 0$, the columns $v_1, \dots, v_n$ have the orientation of the standard basis, and $A$ keeps orientation.
When $\det A < 0$, the map turns space over, like a mirror.
For example, $\operatorname{diag}(-1, 1)$ has determinant $-1$ and reflects the plane in the vertical axis, yet it sends the unit square to a square of area $1$.
In the plane, $\det A > 0$ means that the turn from $v_1$ to $v_2$ is counterclockwise, as for $(3, 1)$ and $(1, 2)$.

### Areas and volumes of parallelotopes

In $\mathbb{R}^2$ the parallelogram spanned by $(a, c)$ and $(b, d)$ has area $\lvert ad - bc \rvert$, and the triangle on the same two sides has half that area.
For the triangle with corners $(1, 1)$, $(4, 2)$ and $(2, 4)$, the sides from $(1, 1)$ are $(3, 1)$ and $(1, 3)$, so its area is $\tfrac{1}{2} \lvert 9 - 1 \rvert = 4$.

In $\mathbb{R}^3$ the [[parallelepiped|0SQV2VJTGY]] on $(1, 0, 0)$, $(1, 2, 0)$ and $(0, 1, 3)$ has volume
$$\left\lvert \det \begin{pmatrix} 1 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 3 \end{pmatrix} \right\rvert = 1 \cdot 2 \cdot 3 = 6,$$
because the matrix is upper triangular.
The tetrahedron with the corners $0, v_1, v_2, v_3$ has volume $\lvert \det(v_1, v_2, v_3) \rvert / 6$, so the tetrahedron on the three standard basis vectors has volume $\tfrac{1}{6}$.

### Why each hypothesis is needed

The matrix must be square.
A $3 \times 2$ matrix maps $\mathbb{R}^2$ into a plane of $\mathbb{R}^3$, and every subset of a plane has $3$-dimensional measure $0$, so no factor relates the two measures in a useful way.

The scalars must be real, because Lebesgue measure lives on $\mathbb{R}^n$.
A complex matrix acts on $\mathbb{C}^n = \mathbb{R}^{2n}$, and there the factor is $\lvert \det A \rvert^2$; for $A = (i)$ on $\mathbb{C}$, a rotation by a right angle, the factor is $\lvert i \rvert^2 = 1$.

The absolute value is needed, because a volume is never negative while $\det \operatorname{diag}(-1, 1) = -1$.
Borel sets keep the proof short, and the formula also holds for every Lebesgue measurable $S$, because such a set differs from a Borel set by a null set.

### The converse

A linear map that keeps all volumes has $\lvert \det A \rvert = 1$, by part 2 applied to the unit cube.
It need not keep lengths.
The shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has determinant $1$ and keeps every area, but it sends $(0, 1)$ to $(1, 1)$, of length $\sqrt{2}$.

### Generalizations

For $k \le n$ vectors in $\mathbb{R}^n$ with the $n \times k$ matrix $A$, the $k$-dimensional volume of their parallelotope is $\sqrt{\det(A^{\mathsf{T}} A)}$, and the [[Cauchy-Binet formula|08WE2W7DYS]] expands $\det(A^{\mathsf{T}} A)$ as a sum of squares of $k \times k$ minors.
The theorem is the linear case of the [[change of variables formula|00N5FHP1CV]].
For a diffeomorphism $G$, the [[change of variables formula for Lebesgue measure|F9TB015RGN]] reads $\lambda(G(E)) = \int_E \lvert \det DG(x) \rvert \, dx$, with the Jacobian determinant in place of $\det A$.

## Explanations

### L1 human

A square matrix sends the unit cube to a slanted box whose edges are the columns of the matrix.
The volume of this box is the absolute value of the determinant.
Every other region has its volume multiplied by the same factor.
For example, the matrix that doubles the $x$ direction and triples the $y$ direction has determinant $6$, and it turns a square of area $1$ into a rectangle of area $6$.
The sign of the determinant tells whether the matrix also flips space like a mirror.

### L2 human

Here is a typical use: find the area of the ellipse $\frac{x^2}{4} + \frac{y^2}{9} \le 1$.
The matrix $A = \operatorname{diag}(2, 3)$ sends the unit disc onto this ellipse, because $(u, v)$ with $u^2 + v^2 \le 1$ goes to $(x, y) = (2u, 3v)$ with $\frac{x^2}{4} + \frac{y^2}{9} = u^2 + v^2 \le 1$.
Part 1 gives the area:
$$\lambda(A(\text{disc})) = \lvert \det A \rvert \cdot \pi = 6\pi.$$
In general, the ellipse with semi-axes $a$ and $b$ has area $\pi a b$.
The method works for any region that is a linear image of a region whose volume we know.
Watch out: a negative determinant does not mean a negative volume, because the volume is $\lvert \det A \rvert$, and the sign only carries the orientation.

### L3 human

The map $S \mapsto \lambda(A(S))$ is a translation-invariant Radon measure, so it is a constant multiple of $\lambda$ by the uniqueness of Haar measure.
The constant is a homomorphism $\mathrm{GL}_n(\mathbb{R}) \to (0, \infty)$, and the [[proof|QZE2CYP536]] shows that it equals $\lvert \det A \rvert$.
For an automorphism of any locally compact group, the same construction defines its modulus, the factor by which it scales Haar measure.
The [[Jacobian determinant|0ZCSMYHTBP]] of a smooth map carries the same idea to curved coordinates and to manifolds, where it measures the local scaling of volume at each point.
