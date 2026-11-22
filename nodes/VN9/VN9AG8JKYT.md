---
tag: VN9AG8JKYT
kind: statement
role: theorem
name: Correspondence between quadratic forms and symmetric bilinear forms
msc: ["15A63", "11E04"]
topics: [6TSCEW8QMK]
audience: ug1
about: [0RBQS1JJCR, 0AXZNE5XNH, 0HYFWKKY3C]
uses: [0HZNE5QZDJ, 0744CN4MDA, 0HYFWKKY3C, 0P24YW565F]
proofs: [VQWHWZED07]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Symmetric_bilinear_form
    locator: lead section
  - book: isbn:9780387728285
---

## Statement

When $2$ is invertible, a quadratic form and a symmetric bilinear form are the same thing, and each quadratic form has exactly one symmetric matrix in each basis.
Let $F$ be a field whose characteristic is not $2$, and let $V$ be a finite-dimensional vector space over $F$ with basis $(e_1, \dots, e_n)$.

1. For each [[symmetric bilinear form|0744CN4MDA]] $B$ on $V$, the map $Q_B(v) = B(v, v)$ is a [[quadratic form|0HZNE5QZDJ]], and its [[polar form|0HYFWKKY3C]] is $2B$.
2. For each quadratic form $Q$ on $V$, the map $B_Q(u, v) = \tfrac{1}{2} \bigl( Q(u + v) - Q(u) - Q(v) \bigr)$ is a symmetric bilinear form with $B_Q(v, v) = Q(v)$.
3. The maps $B \mapsto Q_B$ and $Q \mapsto B_Q$ are inverse bijections between the symmetric bilinear forms on $V$ and the quadratic forms on $V$.
4. For each quadratic form $Q$ there is exactly one symmetric $n \times n$ matrix $A$ with $Q(\sum_i x_i e_i) = x^{\mathsf{T}} A x$ for all $x \in F^n$, namely the [[matrix|0P24YW565F]] of $B_Q$.

## Remarks

### A round trip with numbers

Start from $B(u, v) = 2u_1 v_1 + 3(u_1 v_2 + u_2 v_1)$ on $\mathbb{R}^2$, which is bilinear and symmetric.
Putting $u = v$ gives the quadratic form $Q_B(v) = 2v_1^2 + 6 v_1 v_2$.
Now go back and expand:
$$Q_B(u + v) - Q_B(u) - Q_B(v) = 4u_1 v_1 + 6(u_1 v_2 + u_2 v_1) = 2B(u, v).$$
Half of it is $B$ again, as part 3 promises, and the symmetric matrix of part 4 is $\begin{pmatrix} 2 & 3 \\ 3 & 0 \end{pmatrix}$.

### Why each hypothesis is needed

The characteristic must not be $2$.
Over $\mathbb{F}_2$, [[the form xy is B(v, v) for no symmetric bilinear form B|ZEGSCCVGZF]], so $B \mapsto Q_B$ is not onto.
In the same example, the form $x^2$ on $\mathbb{F}_2$ has polar form $0$, just like the zero form, so a quadratic form is not determined by its polar form.

In part 4 the matrix must be symmetric for uniqueness.
The matrices $\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ and $\begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$ both give $x^2 + xy$, and the symmetric one is $\begin{pmatrix} 1 & 1/2 \\ 1/2 & 0 \end{pmatrix}$.

### What it gives you

Every notion for symmetric bilinear forms passes to quadratic forms: the matrix, [[orthogonality|01TXN7ETH2]], [[nondegeneracy|01NHFZF2SK]], the rank, and [[congruence|WJWNYSQKK8]] of matrices.
So [[the diagonalization theorem|0Z3FEWZ8HA]] can be stated for symmetric matrices or for quadratic forms, with the same content.
Both maps are $F$-linear, so the quadratic forms on $V$ form a vector space of dimension $n(n + 1)/2$, the same as the symmetric $n \times n$ matrices.

### In characteristic 2

Part 1 still holds in characteristic $2$, but then the polar form $2B$ is zero, and parts 2 to 4 fail.
Every quadratic form is still $x^{\mathsf{T}} A x$ for an upper triangular matrix $A$, with $a_{ij} = c_{ij}$ for $i \le j$, but symmetric matrices are not enough and the polar form $b_Q$ is alternating.
The same proof works for modules over any commutative ring in which $2$ is a unit.

## Explanations

### L1 human

A symmetric bilinear form takes two vectors and gives a number.
If you put the same vector in both places, you get a quadratic form.
Outside characteristic $2$ you can go back with the formula $\tfrac{1}{2}\bigl(Q(u + v) - Q(u) - Q(v)\bigr)$.
For $Q(x, y) = x^2 + y^2$ this formula gives the dot product $xx' + yy'$.

### L2 human

Here is a typical use: decide whether two vectors are orthogonal for $Q(x, y) = x^2 + 4xy - y^2$.
Part 4 gives the matrix $A = \begin{pmatrix} 1 & 2 \\ 2 & -1 \end{pmatrix}$, so $B(u, v) = u^{\mathsf{T}} A v$.
For $u = (1, 0)$ and $v = (2, -1)$,
$$B(u, v) = \begin{pmatrix} 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 2 & -1 \end{pmatrix} \begin{pmatrix} 2 \\ -1 \end{pmatrix} = 1 \cdot 2 + 2 \cdot (-1) = 0,$$
so $u$ and $v$ are orthogonal for $Q$.
Check with the polar form: $Q(3, -1) - Q(1, 0) - Q(2, -1) = (9 - 12 - 1) - 1 - (4 - 8 - 1) = -4 - 1 + 5 = 0$.
Watch out: over $\mathbb{F}_2$ this method breaks down, which matters for codes and other forms over $\mathbb{F}_2$.

### L3 human

When $2$ is invertible, the construction gives an isomorphism between the category of symmetric bilinear spaces and the category of quadratic spaces, with the same isometries.
In characteristic $2$ the two theories separate, and quadratic forms carry more structure; for nondegenerate forms over $\mathbb{F}_2$ the Arf invariant takes the place that the discriminant has in odd characteristic.
This is why texts on algebraic groups and on coding theory often work with quadratic forms rather than with symmetric bilinear forms.
