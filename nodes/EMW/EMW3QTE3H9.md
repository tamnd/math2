---
tag: EMW3QTE3H9
kind: statement
role: proposition
name: Normal operators have equal norms for T and its adjoint
aliases: [normal-iff-norm-of-tv-equals-norm-of-adjoint-v]
msc: ["15A04", "47B15"]
topics: [3YM9EK6VMB]
audience: ug1
about: [0C8BR8XRTR]
uses: [0ENZN5G4CV, 0ST8QF9T3T, TPP76FP659, WAYMK9GR5S]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_operator
    locator: Properties
  - book: isbn:9783031410253
    locator: Chapter 7
  - book: isbn:9780134860244
    locator: Section 6.4
---

## Statement

An operator is normal exactly when it and its adjoint stretch every vector by the same amount, and then the two share their eigenvectors.

Let $V$ be a finite-dimensional inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $T \colon V \to V$ be a linear operator with [[adjoint|0ST8QF9T3T]] $T^*$.

1. $T$ is [[normal|0ENZN5G4CV]] if and only if $\norm{Tv} = \norm{T^* v}$ for every $v \in V$.
2. If $T$ is normal, then $\ker T = \ker T^*$.
3. If $T$ is normal and $\lambda \in \mathbb{K}$, then $T - \lambda I$ is normal, and for every $v \in V$
$$Tv = \lambda v \iff T^* v = \overline{\lambda} v.$$

So a normal operator and its adjoint have the same eigenvectors, with conjugate eigenvalues.

## Remarks

### A first check

Take the quarter turn $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ on $\mathbb{R}^2$, with $R^* = R^{\mathsf{T}} = -R$.
For $v = (x, y)$ we get $Rv = (-y, x)$ and $R^* v = (y, -x)$, and both have length $\sqrt{x^2 + y^2}$.
So part 1 confirms that $R$ is normal.
Over $\mathbb{C}$, part 3 says that the eigenvector $(1, -i)$ of $R$ for $i$ is an eigenvector of $R^* = -R$ for $\overline{i} = -i$, and indeed $-R(1, -i) = -i(1, -i)$.

### Why normality is needed

Parts 2 and 3 fail without normality.
For $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ on $\mathbb{R}^2$, the kernel of $N$ is spanned by $e_1$, while the kernel of $N^{\mathsf{T}}$ is spanned by $e_2$.
For [[the shear|BF9MKKHH4Z]] $S = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, the vector $e_1$ is an eigenvector of $S$, but $S^{\mathsf{T}} e_1 = (1, 1)$ is not a multiple of $e_1$.
Finite dimension is only used to make sure that $T^*$ exists.

### What it gives you

Part 3 is the step that makes the spectral theory of normal operators work.
It gives [[the orthogonality of eigenspaces|0JHGAV9H25]]: if $Tv = \lambda v$ and $Tw = \mu w$ with $\lambda \ne \mu$, then $\lambda \ip{v}{w} = \ip{Tv}{w} = \ip{v}{T^* w} = \ip{v}{\overline{\mu} w} = \mu \ip{v}{w}$, so $\ip{v}{w} = 0$.
It also shows that an eigenspace $E$ of $T$ is invariant under $T^*$, so its orthogonal complement $E^\perp$ is invariant under $T$, which is the key step in the deflation proof of [[the complex spectral theorem|04CW1P44VD]].

Part 2 gives an orthogonal splitting of the space.
By [[the kernel and image of the adjoint|YPP8XT6B7Y]], $\im T = (\ker T^*)^\perp$, and part 2 turns this into $\im T = (\ker T)^\perp$.
So a normal operator has $V = \ker T \oplus \im T$ with the two parts orthogonal.

### The converse

Part 1 is already an equivalence.
Part 2 has no converse.
The shear $S$ is invertible, so $\ker S = \ker S^{\mathsf{T}} = 0$, but $S$ is not normal.
Part 3 has a partial converse over $\mathbb{C}$: if $V$ has a basis of common eigenvectors of $T$ and $T^*$, then $T$ and $T^*$ are both diagonal in that basis, so they commute.

### Generalizations

Parts 1 to 3 hold for bounded operators on a Hilbert space, with the same proof.
An operator with $\norm{T^* v} \leq \norm{Tv}$ for all $v$ is called [[hyponormal|35XKRHEC3Q]], and in finite dimension every hyponormal operator is normal.

## Explanations

### L1 human

A normal operator and its adjoint stretch each vector by the same amount.
They can turn the vector in different ways, but the two results have the same length.
For a quarter turn of the plane, the operator turns left and its adjoint turns right, and both keep every length.

### L2 human

Here is how the norm test catches a matrix that is not normal.
Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ on $\mathbb{R}^2$ with the dot product, so $A^* = A^{\mathsf{T}} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$.
For $v = e_1$ we get
$$\norm{A e_1} = \norm{(1, 0)} = 1, \qquad \norm{A^{\mathsf{T}} e_1} = \norm{(1, 1)} = \sqrt{2}.$$
One vector with different norms is enough, so $A$ is not normal by part 1.
Check: $A A^{\mathsf{T}} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ and $A^{\mathsf{T}} A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$ differ.
The typical use of part 3 is inside proofs, to turn an eigenvector of $T$ into an eigenvector of $T^*$.
Watch out: the eigenvalue changes to its conjugate, so for $T^*$ it is $\overline{\lambda}$ and not $\lambda$.

### L3 human

The proof rests on the identity
$$\norm{Tv}^2 - \norm{T^* v}^2 = \ip{(T^* T - T T^*) v}{v},$$
which says that part 1 is a statement about the self-adjoint operator $T^* T - T T^*$ and its quadratic form.
A self-adjoint operator is $0$ exactly when its quadratic form is $0$, and that is the whole proof.
In operator theory the size of $T^* T - T T^*$ measures how far $T$ is from normal, and the same identity is the start of the theory of hyponormal and subnormal operators.
