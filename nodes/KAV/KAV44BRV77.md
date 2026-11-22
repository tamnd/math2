---
tag: KAV44BRV77
kind: statement
role: theorem
name: Invariant subspaces of dimension 1 or 2 for real operators
aliases: [real-operators-have-an-invariant-subspace-of-dimension-1-or-2]
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
about: [0ACX5QT8TE, 0BQAA2BK3Q]
uses: [0ACX5QT8TE, 0ZND7NQ970]
sources:
  - book: isbn:9783031410253
    locator: Chapter 5
  - url: https://linear.axler.net/
    locator: Chapter 5
---

## Statement

A real linear map may have no eigenvector, but it always maps some line or some plane into itself, and in odd dimension it always has a real eigenvalue.

Let $V$ be a finite-dimensional real vector space with $V \ne 0$, and let $T \colon V \to V$ be a linear map.

1. $T$ has an [[invariant subspace|0ACX5QT8TE]] $U$ with $\dim U = 1$ or $\dim U = 2$.
2. If $\dim V$ is odd, then $T$ has a real [[eigenvalue|0BQAA2BK3Q]], so $T$ has an invariant subspace of dimension $1$.

The same holds for every real $n \times n$ matrix with $n \ge 1$, acting on $\mathbb{R}^n$.

## Remarks

### Where it fits

Over $\mathbb{C}$, the [[existence of an eigenvalue|08CJB2NQ92]] gives an invariant line for every operator.
Over $\mathbb{R}$ that fails, and the theorem says how badly it can fail: at worst we need a plane.
The reason is that a real polynomial splits into real factors of degree $1$ and $2$, and the [[proof by factoring a real polynomial|XTN1H33835]] turns each kind of factor into an invariant subspace of that dimension.

### Why each hypothesis is needed

A plane can be necessary.
The [[rotation of the plane by an angle that is not a multiple of pi|5AE98D7959]] moves every line through the origin, so its only invariant subspaces are $0$ and $\mathbb{R}^2$.

Part 2 needs odd dimension.
The rotation by $90$ degrees on $\mathbb{R}^2$ has the characteristic polynomial $t^2 + 1$ and no real eigenvalue.
The block diagonal matrix with two such blocks acts on $\mathbb{R}^4$ with the characteristic polynomial $(t^2 + 1)^2$, so it has no real eigenvalue either.

The space must be finite-dimensional.
The right shift $(x_1, x_2, \dots) \mapsto (0, x_1, x_2, \dots)$ on real sequences has no eigenvalue, as the [[shift operators|HBVWZ0FXWC]] show.
It has no invariant plane either.
For $w \ne 0$, the first nonzero entries of $w$, $Tw$ and $T^2 w$ sit in three different places, so these three vectors are independent.
An invariant subspace that contains $w$ also contains $Tw$ and $T^2 w$, so it has dimension at least $3$.

### What it gives you

The theorem starts inductions for real matrices in the way that eigenvectors start them for complex matrices.
Repeating it on a complement gives the real Schur form: every real square matrix is orthogonally similar to a block upper triangular matrix with diagonal blocks of size $1$ or $2$.

In dimension $3$ the characteristic polynomial has odd degree, so every real $3 \times 3$ matrix has a real eigenvector.
For a rotation $R$ of $\mathbb{R}^3$ (orthogonal with $\det R = 1$) one step more gives an axis.
The real eigenvalues of $R$ are $\pm 1$, and the complex ones come in pairs $\mu, \bar\mu$ with $\mu \bar\mu = 1$.
Since the product of the three eigenvalues is $\det R = 1$, at least one of them equals $1$, and its eigenvector spans a fixed axis.

### The converse

An invariant plane need not contain an eigenvector.
For the rotation of $\mathbb{R}^2$ by $90$ degrees, the plane $\mathbb{R}^2$ itself is invariant, but there is no real eigenvector at all.
So part 1 cannot be improved to "an invariant line" without the odd dimension of part 2.

### Generalizations

Over a general field $F$, the same proof gives an invariant subspace of dimension at most $d$, where $d$ is the degree of an irreducible factor of a polynomial that kills a nonzero vector.
Over a real closed field the statement holds as it stands.
Such a field shares the two facts that the proof uses: polynomials split into factors of degree $1$ and $2$, and a polynomial of odd degree has a root.

## History

The approach without determinants, through a polynomial that kills one vector, is the one that Axler presents in "Linear Algebra Done Right".
The odd-dimensional case is the older observation that a real polynomial of odd degree has a real root, applied to the characteristic polynomial.

## Explanations

### L1 human

A real matrix need not have a real eigenvector: a quarter turn of the plane moves every line.
But some line or some plane is always mapped into itself.
On an invariant plane without eigenvectors, the matrix acts like a rotation combined with a stretch.
In three dimensions you never need the plane, because a polynomial of degree $3$ always has a real root.
That is why every motion of a rigid body that turns it about a fixed point has an axis.

### L2 human

Here is a typical search for an invariant plane: take
$$A = \begin{pmatrix} 0 & 0 & -1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$$
on $\mathbb{R}^3$, and follow the vector $e_1$.
The columns of $A$ give $A e_1 = e_2$, $A e_2 = e_3$ and $A e_3 = -e_1$, so $A^3 e_1 = -e_1$ and $p(x) = x^3 + 1$ kills $e_1$.
Over $\mathbb{R}$ this factors as
$$x^3 + 1 = (x + 1)(x^2 - x + 1),$$
and the quadratic factor has discriminant $1 - 4 = -3 < 0$.
Put $w = (A + I)e_1 = (1, 1, 0)^{\mathsf{T}}$; then $(A^2 - A + I)w = (A^3 + I)e_1 = 0$.
So $A^2 w = Aw - w$, and the plane $U = \operatorname{span}\{w, Aw\}$ with $Aw = (0, 1, 1)^{\mathsf{T}}$ is invariant.
Check: $A(Aw) = (-1, 0, 1)^{\mathsf{T}}$, and $Aw - w = (0, 1, 1)^{\mathsf{T}} - (1, 1, 0)^{\mathsf{T}} = (-1, 0, 1)^{\mathsf{T}}$.
The linear factor $x + 1$ gives the real eigenvalue $-1$ that part 2 promises: $v = (1, -1, 1)^{\mathsf{T}}$ has $Av = (-1, 1, -1)^{\mathsf{T}} = -v$.
Watch out: the invariant plane came from a factor of a polynomial, not from an eigenvector, and a real operator can have many invariant planes.

### L3 human

Make $V$ into a module over $\mathbb{R}[x]$, with $x$ acting as $T$.
The theorem says that a nonzero finite-dimensional module of this kind has a simple submodule.
A simple $\mathbb{R}[x]$-module is $\mathbb{R}[x]/(q)$ with $q$ irreducible, so its dimension is $\deg q$, which is $1$ or $2$.
Complexification gives the same picture: an eigenvalue $a + ib$ with $b \ne 0$ of the complex extension of $T$ has an eigenvector $u + iw$, and $u, w$ span a real invariant plane.
The later sub-area on diagonalization and invariant subspaces uses this to build the real canonical forms.
