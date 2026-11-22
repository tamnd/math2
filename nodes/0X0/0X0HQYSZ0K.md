---
tag: 0X0HQYSZ0K
kind: concept
name: Determinant of a linear map
msc: [15A04, 15A15]
topics: [DTBK11SR77]
audience: ug2
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Determinant of an endomorphism
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: History
---

## Summary

A linear map from a space to itself has a determinant of its own, a single number that does not depend on the coordinates we use to write the map down.
It tells whether the map can be undone, and over the real numbers it tells by what factor the map scales volume.
Let $V$ be a vector space of finite dimension $n$ over a field $F$, and let $T \colon V \to V$ be an endomorphism.
Choose a basis $B$ of $V$ and write the matrix $[T]_B$ of $T$, with $B$ used for both the domain and the codomain.
The determinant of $T$ is
$$\det T = \det [T]_B,$$
the [[determinant|00KDZRW4C0]] of that matrix, and the [[formal definition|03F5KP94K0]] states this with the convention $\det T = 1$ for $V = 0$.
The [[invariance theorem|0KMN32XGPF]] shows that every basis gives the same value, so $\det T$ belongs to $T$ and not to $B$.

## Motivation

Many linear maps come without a preferred basis.
Differentiation acts on polynomials, the transpose acts on matrices, and a rotation of space has no favorite axes.
We still want to ask of such a map whether it is invertible, and whether it keeps or reverses orientation.
A matrix answers these questions, but a matrix depends on a basis, so we need a number that every basis agrees on.

The determinant is such a number.
A change of basis replaces $[T]_B$ by a [[similar matrix|0E89HQATM8]] $P^{-1} [T]_B P$, and the factors $\det P^{-1}$ and $\det P$ cancel.
So we may compute $\det T$ in whatever basis makes the matrix simplest, often a diagonal or triangular one.
The idea returns in the study of eigenvalues, where $\det T$ is the constant term of the [[characteristic polynomial|0J5EMJRRFM]] up to sign, and in geometry, where $\lvert \det T \rvert$ is the [[volume scaling factor|RC5BTSG8T2]] of a real map.

## Notation

We write $\det T$ or $\det(T)$, and $[T]_B$ for the [[matrix of $T$|0YQSGNYE3K]] in the basis $B$, whose column $j$ holds the coordinates of $T(b_j)$.
Some books write $|T|$, but that symbol also suggests a norm, so we avoid it.
In Mathlib the determinant of a linear map is `LinearMap.det`.

## Remarks

### A first computation

Take $T(x, y) = (x + y, 2y)$ on $\mathbb{R}^2$.
In the standard basis the columns are $T(1, 0) = (1, 0)$ and $T(0, 1) = (1, 2)$, so
$$\det T = \det \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} = 1 \cdot 2 - 1 \cdot 0 = 2.$$
Now use the basis $b_1 = (1, 0)$ and $b_2 = (1, 1)$.
Then $T(b_1) = b_1$ and $T(b_2) = (2, 2) = 2 b_2$, so the matrix in this basis is $\operatorname{diag}(1, 2)$.
Its determinant is $1 \cdot 2 = 2$ again, as the invariance theorem promises.
The second basis was better: it made the matrix diagonal, and the determinant could be read off at once.

### More examples

For the identity, $\det \operatorname{id}_V = 1$, and for a scalar map $\det(c \operatorname{id}_V) = c^n$, because the matrix is $c I_n$ in every basis.
The rotation of $\mathbb{R}^2$ by an angle $\theta$ has the [[rotation matrix|HNY4CPEEJA]] with columns $(\cos \theta, \sin \theta)$ and $(-\sin \theta, \cos \theta)$, so its determinant is $\cos^2 \theta + \sin^2 \theta = 1$.
On polynomials of degree at most $2$, the substitution $p(x) \mapsto p(2x)$ has determinant $8$, as [[the substitution example|GXDM4QPRN5]] shows in two bases.
On the $2 \times 2$ matrices, the transpose map $X \mapsto X^{\mathsf{T}}$ has determinant $-1$, as [[the transpose example|STX4PZKC69]] works out.

### What it is not

A linear map $\mathbb{R}^2 \to \mathbb{R}^3$ has no determinant, because it is not an endomorphism and all its matrices are $3 \times 2$; [[the map into space|WYHE1FWPHN]] checks this.
A map $V \to W$ between two different spaces of the same dimension has square matrices, but their determinants depend on the two bases, so no single number belongs to the map.
The identity of an infinite-dimensional space has no determinant in this sense either, since it has no finite matrix.

### The rules you can use

The rules for matrices carry over, since $[S \circ T]_B = [S]_B [T]_B$.
By [[multiplicativity|04CPJ6AF00]], $\det(S \circ T) = \det S \cdot \det T$.
So $T$ is invertible exactly when $\det T \ne 0$, and then $\det(T^{-1}) = (\det T)^{-1}$.
Over an algebraic closure of $F$, $\det T$ is the [[product of the eigenvalues|0C2F40MEBC]], counted with algebraic multiplicity.
With $\chi_T(x) = \det(x \operatorname{id}_V - T)$, we get $\chi_T(0) = \det(-T) = (-1)^n \det T$.
The dual map $T^*$ has the same determinant, because its matrix in the dual basis is the [[transpose|0W809K6AW0]] of $[T]_B$.

### Watch out

The matrix must use one basis for both the domain and the codomain.
Take the identity of $\mathbb{R}^2$, with the basis $e_1, e_2$ on the domain and $2e_1, e_2$ on the codomain.
Since $e_1 = \tfrac{1}{2}(2 e_1)$, that matrix is $\operatorname{diag}(\tfrac{1}{2}, 1)$, with determinant $\tfrac{1}{2}$, while $\det \operatorname{id} = 1$.

A second trap is the scalar rule.
The map $-\operatorname{id}$ on $\mathbb{R}^2$ has determinant $(-1)^2 = 1$, not $-1$, because the rule is $\det(cT) = c^n \det T$.

### History

Determinants were studied as expressions attached to systems of linear equations long before matrices were introduced.
So the number came first, and the reading of it as an invariant of a linear map, free of coordinates, is the later point of view.

### Try it

First, let $D$ be differentiation on the polynomials of degree at most $2$, and find $\det D$.
In the basis $1, x, x^2$ the columns are $D(1) = 0$, $D(x) = 1$ and $D(x^2) = 2x$, so the matrix is strictly upper triangular and $\det D = 0$, which fits the fact that $D$ kills the constants.

Second, find the determinant of $T(x, y, z) = (2x, 2y, 2z)$ on $\mathbb{R}^3$.
This is $2 \operatorname{id}$, so $\det T = 2^3 = 8$.

## Explanations

### L1 human

A linear map moves the vectors of a space around inside the same space.
To find its determinant, choose a basis, write the matrix of the map, and take the determinant of the matrix.
A different basis gives a different matrix, but always the same determinant, so the number belongs to the map.
For the map that doubles every vector of the plane, every basis gives $2 \cdot 2 = 4$, because areas grow by a factor of $4$.
The map can be undone exactly when this number is not zero.

### L2 human

Here is a typical use: is the map $T(p) = p + p'$ on the polynomials of degree at most $2$ invertible?
Use the basis $1, x, x^2$ and compute the images:
$$T(1) = 1, \qquad T(x) = x + 1, \qquad T(x^2) = x^2 + 2x.$$
Their coordinates are the columns of the matrix:
$$[T] = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix}.$$
The matrix is [[upper triangular|0K1KKMFHYH]], so $\det T = 1 \cdot 1 \cdot 1 = 1$, and $T$ is invertible.
In fact $T^{-1}(p) = p - p' + p''$.
Check: $T(p - p' + p'') = p - p' + p'' + p' - p'' + p''' = p + p'''$, and $p''' = 0$ for degree at most $2$.
One small matrix decided invertibility for a map on a space of functions, and that is the typical use of the determinant of a map.

### L3 human

Without a basis, the top [[exterior power|0MDMZ965VE]] $\Lambda^n V$ is a line, so the induced map $\Lambda^n T$ is multiplication by a scalar, and that scalar is $\det T$.
In symbols, $T v_1 \wedge \dots \wedge T v_n = \det T \cdot v_1 \wedge \dots \wedge v_n$, and multiplicativity becomes the functoriality $\Lambda^n (S \circ T) = \Lambda^n S \circ \Lambda^n T$.
The same construction works for a free module of finite rank over a commutative ring, and Mathlib's `LinearMap.det` gives the value $1$ when the module has no finite basis.
The map $\det \colon \operatorname{GL}(V) \to F^{\times}$ is a group homomorphism whose kernel is the [[special linear group|0V9PMN0RBH]].
Over $\mathbb{R}$ the sign of $\det T$ decides whether $T$ keeps the [[orientation|0QJJAQ6ZYZ]] of $V$, and for a smooth map the [[Jacobian determinant|0ZCSMYHTBP]] is the determinant of its derivative at each point.
