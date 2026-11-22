---
tag: V8KKHKXXB3
kind: statement
role: theorem
name: Classification of alternating bilinear forms
aliases: [classification-of-alternating-forms, symplectic-basis-theorem]
msc: ["15A63", "15A21"]
topics: [DYAK7YMK7B]
audience: ug1
about: [0DGDS5XY84]
uses: [08ZQAKBKHF, 0P24YW565F, NZJDNC6EP6, D3E2Y85S6H, 0SPYAGE7T0, 0KAN330PAH]
sources:
  - url: https://en.wikipedia.org/wiki/Symplectic_vector_space
    locator: Standard symplectic space
  - book: isbn:9780387728285
    locator: Chapter 11
  - book: isbn:9780135367971
    locator: Chapter 10
---

## Statement

Every alternating form on a finite-dimensional space looks the same in a good basis: a row of $2 \times 2$ blocks $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ followed by zeros, so its rank is the only invariant.

Let $V$ be a vector space of finite dimension $n$ over a field $F$ of any characteristic, and let $B$ be an [[alternating bilinear form|08ZQAKBKHF]] on $V$.
Let $J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$.

1. (Symplectic basis.) There are an integer $m \geq 0$ and a basis $(u_1, v_1, \dots, u_m, v_m, w_1, \dots, w_k)$ of $V$, with $2m + k = n$, such that $B(u_i, v_i) = 1$ and $B(v_i, u_i) = -1$ for each $i$, and $B$ is zero on every other ordered pair of basis vectors.
2. In this basis the [[matrix|0P24YW565F]] of $B$ is the block diagonal matrix $J \oplus \dots \oplus J \oplus 0_k$, with $m$ blocks $J$.
3. The rank of $B$ is $2m$, so it is even, and $(w_1, \dots, w_k)$ is a basis of the radical of $B$.
4. Two alternating $n \times n$ matrices over $F$ are [[congruent|NZJDNC6EP6]] if and only if they have the same rank.
5. If $B$ is [[nondegenerate|0KAN330PAH]], then $n$ is even.
6. The determinant of an alternating matrix over $F$ is a square in $F$.

The [[proof|388BWRRP7H]] splits off one plane with the matrix $J$ at a time, by induction on $n$.

## Remarks

### A first case

Take the form $B(x, y) = x^{\mathsf{T}} A y$ on $\mathbb{Q}^2$ with $A = \begin{pmatrix} 0 & 2 \\ -2 & 0 \end{pmatrix}$.
It is alternating, since $B(x, x) = 2x_1 x_2 - 2x_2 x_1 = 0$.
Keep $u_1 = e_1$ and halve the second vector, $v_1 = \tfrac{1}{2} e_2$, so that $B(u_1, v_1) = \tfrac{1}{2} \cdot 2 = 1$.
The matrix $P$ with columns $u_1, v_1$ gives
$$P^{\mathsf{T}} A P = \begin{pmatrix} 1 & 0 \\ 0 & \tfrac{1}{2} \end{pmatrix} \begin{pmatrix} 0 & 2 \\ -2 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & \tfrac{1}{2} \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = J.$$
Check: $\det A = 4 = 2^2$ is a square, as part 6 says.
A larger case, the [[symplectic basis of a 4 by 4 alternating matrix|C8S4RH68S0]], runs the same steps twice.

### Why each hypothesis is needed

The form must be alternating, and skew-symmetry is not enough.
Over $\mathbb{F}_2$ we have $-1 = 1$, so the $1 \times 1$ matrix $(1)$ is skew-symmetric, but it has the odd rank $1$.
The [[skew-symmetric form over the field with two elements|1V7NMPCSK9]] shows the same failure in dimension $2$.
Outside characteristic $2$ the two notions agree, by the [[relation between alternating and skew-symmetric forms|SX9CD5NEPD]].

The scalars must form a field, because the proof divides by $B(u, z)$.
Over the ring $\mathbb{Z}$ the form with matrix $2J$ is not congruent to $J$.
An integer change of basis has $\det P = \pm 1$, so it gives $\det(P^{\mathsf{T}} (2J) P) = 4$, never $\det J = 1$.

Finite dimension is needed for the rank and for the induction on $n$.

### What it gives you

The theorem says that every [[symplectic vector space|PQ7JJY0VPH]] has even dimension $2m$.
After a reordering to $(u_1, \dots, u_m, v_1, \dots, v_m)$, its form has the matrix $\begin{pmatrix} 0 & I_m \\ -I_m & 0 \end{pmatrix}$.
So two nondegenerate alternating forms on spaces of the same dimension are isometric, and there is only one symplectic space of each even dimension, up to isomorphism.
An alternating matrix of odd size has determinant $0$ in every characteristic, because its rank is even and so smaller than its size.
The square root in part 6 is a polynomial in the entries, the [[Pfaffian|NH5HWBPWS9]], by [[the theorem on the Pfaffian|473MBZST4D]].

### The converse

Parts 5 and 6 do not reverse.
The zero form on $F^2$ lives in even dimension, but it is degenerate.
The identity matrix $I_2$ has the square determinant $1$, but it is not alternating.
Part 4 is already an equivalence: congruent matrices have the same rank, and matrices of the same rank are congruent.

### Generalizations

Over a principal ideal domain, an alternating matrix is congruent to a block sum of matrices $d_i J$ with $d_1 \mid d_2 \mid \cdots$, followed by zeros.
This is a symplectic version of the Smith normal form, and the case $2J$ over $\mathbb{Z}$ above shows why the $d_i$ appear.
Symmetric forms behave very differently: their classification depends on the field, as the theory of [[quadratic forms|0RBQS1JJCR]] shows.

### Watch out

The classification of alternating forms does not depend on the field, while the classification of symmetric forms does.
Over $\mathbb{Q}$ the symmetric forms $x_1 y_1 + x_2 y_2$ and $x_1 y_1 + 2 x_2 y_2$ both have rank $2$, but they are not congruent.
Do not carry the rule "rank decides everything" from alternating forms to symmetric ones.

### Try it

First, find the rank of the alternating form with matrix $\begin{pmatrix} 0 & 1 & 1 \\ -1 & 0 & 1 \\ -1 & -1 & 0 \end{pmatrix}$ over $\mathbb{Q}$.
The rank is even and at most $3$, and the matrix is not zero, so the rank is $2$.

Second, is $\begin{pmatrix} 0 & 3 \\ -3 & 0 \end{pmatrix}$ congruent to $J$ over $\mathbb{Q}$?
Yes, since both are alternating of rank $2$; the matrix $P = \operatorname{diag}(1, \tfrac{1}{3})$ does it.

## Explanations

### L1 human

An alternating form gives zero for a vector paired with itself, like a signed area.
The theorem says that every such form is built from the same brick.
The brick is a pair of vectors $u, v$ with value $1$ in one order and $-1$ in the other.
A space is a stack of these bricks, plus some vectors that pair to zero with everything.
So you only need to count the bricks, and twice that number is the rank.

### L2 human

Here is a typical use: decide whether two alternating matrices are congruent without finding $P$.
Take $A_1 = \begin{pmatrix} 0 & 1 & 2 \\ -1 & 0 & 3 \\ -2 & -3 & 0 \end{pmatrix}$ and $A_2 = \begin{pmatrix} 0 & 5 & 0 \\ -5 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$ over $\mathbb{Q}$.
Both are alternating, since each is minus its transpose with zero diagonal.
Both have rank $2$: they are not zero, and an alternating $3 \times 3$ matrix has even rank below $3$.
By part 4 they are congruent, and both are congruent to $J \oplus 0_1$.
Check for $A_1$: the vector $w = (3, -2, 1)$ satisfies
$$A_1 w = (0 - 2 + 2, -3 + 0 + 3, -6 + 6 + 0) = (0, 0, 0),$$
so $w$ spans the radical, which has dimension $3 - 2 = 1$.
The rank is the whole answer, which is why it is the first thing to compute for an alternating form.

### L3 human

The theorem is the linear version of the theorem of Darboux in symplectic geometry, which gives local coordinates in which a closed nondegenerate $2$-form has constant standard coefficients.
For nondegenerate forms, part 4 says that $\operatorname{GL}_{2m}(F)$ acts on them by $A \mapsto P^{\mathsf{T}} A P$ with one single orbit.
The stabilizer of $J \oplus \dots \oplus J$ is the [[symplectic group|X12FS2JAP0]].
The Pfaffian is a relative invariant of this action: $\operatorname{pf}(P^{\mathsf{T}} A P) = \det P \cdot \operatorname{pf}(A)$.
The same splitting by hyperbolic planes, done for symmetric forms in characteristic not $2$, gives the [[Witt decomposition|BPMRSPB6GD]], and there the anisotropic part need not vanish.
