---
tag: ~be9e3bea
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

Let $n \ge 1$, let $A$ be a real $n \times n$ matrix, and let $\lambda$ be [[Lebesgue measure|2Z2QVWZ262]] on $\mathbb{R}^n$.

1. For every Borel set $S \subseteq \mathbb{R}^n$, the image $A(S)$ is Lebesgue measurable, and
$$\lambda(A(S)) = \lvert \det A \rvert \, \lambda(S),$$
with the [[determinant|0C3CFHDN6R]] $\det A$ and the convention $0 \cdot \infty = 0$.
2. In particular, let $v_1, \dots, v_n$ be the columns of $A$. Then the parallelotope $P = \{ t_1 v_1 + \dots + t_n v_n : 0 \le t_i \le 1 \}$ has volume $\lambda(P) = \lvert \det A \rvert$.

## Remarks

### Why each hypothesis is needed

- The matrix must be square: a $3 \times 2$ matrix maps $\mathbb{R}^2$ into a plane of $\mathbb{R}^3$, and $\lambda^3$ of every such image is $0$.
- The field must be $\mathbb{R}$, since Lebesgue measure lives on $\mathbb{R}^n$; on $\mathbb{C}^n = \mathbb{R}^{2n}$ the factor is $\lvert \det A \rvert^2$.
- Borel sets keep the proof short; the formula also holds for every Lebesgue measurable $S$, because such an $S$ differs from a Borel set by a null set.
- The absolute value is needed: $\operatorname{diag}(-1, 1)$ has determinant $-1$, and it maps the unit square to a square of area $1$.

### Consequences

- In $\mathbb{R}^2$, the parallelogram spanned by $(a, c)$ and $(b, d)$ has area $\lvert ad - bc \rvert$.
- The tetrahedron with vertices $0, v_1, v_2, v_3$ in $\mathbb{R}^3$ has volume $\lvert \det(v_1, v_2, v_3) \rvert / 6$.
- An invertible $A$ with $\lvert \det A \rvert = 1$, for example an orthogonal matrix, keeps every volume.
- So $\det A$ is a *signed volume*: its absolute value is the volume of $P$, and its sign tells whether $v_1, \dots, v_n$ has the [[orientation|0QJJAQ6ZYZ]] of the standard basis.
- The statement is the linear case of the [[change of variables formula|00N5FHP1CV]], where $\lvert \det A \rvert$ becomes the absolute value of the Jacobian determinant.

### Converse

A linear map that keeps all volumes has $\lvert \det A \rvert = 1$, by part 2.
It need not be orthogonal: the shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ keeps areas but changes lengths.

### Generalizations

- For $k \le n$ vectors in $\mathbb{R}^n$ with $n \times k$ matrix $A$, the $k$-dimensional volume of their parallelotope is $\sqrt{\det(A^T A)}$; see the [[Cauchy-Binet formula|08WE2W7DYS]].
- For a diffeomorphism $G$, $\lambda(G(E)) = \int_E \lvert \det DG(x) \rvert \, dx$, the [[change of variables formula in terms of Lebesgue measure|F9TB015RGN]].

## Explanations

### L1 human

A square matrix sends the unit cube to a slanted box spanned by its columns.
The volume of this box is the absolute value of the determinant.
Every other region has its volume multiplied by the same factor.
The sign of the determinant tells whether the matrix also flips space like a mirror.

### L2 human

Take $v_1 = (3, 1)$ and $v_2 = (1, 2)$ in $\mathbb{R}^2$.

1. The theorem gives the area $\lvert 3 \cdot 2 - 1 \cdot 1 \rvert = 5$ for their parallelogram.
2. Check with lengths and angles: area$^2 = \lvert v_1 \rvert^2 \lvert v_2 \rvert^2 - (v_1 \cdot v_2)^2 = 10 \cdot 5 - 25 = 25$, so the area is $5$.
3. The disc of radius $1$ goes to an ellipse of area $5 \pi$ under the matrix with these columns.

The typical use is to compute areas and volumes of parallelograms, parallelotopes and their linear images.
A trap: a negative determinant does not mean a negative volume; the volume is $\lvert \det A \rvert$.

### L3 human

The map $S \mapsto \lambda(A(S))$ is a translation-invariant Radon measure, so it is a constant multiple of $\lambda$.
The constant is a homomorphism $\mathrm{GL}_n(\mathbb{R}) \to (0, \infty)$, and it equals $\lvert \det A \rvert$.
For a general locally compact group, the same construction defines the modular function.
