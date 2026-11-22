---
tag: AW5RBMW7RK
kind: statement
role: theorem
name: A strictly upper triangular matrix is nilpotent
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
about: [0N4XY7Z3NN, 07BSPZPSMF]
uses: [0MKABWDRNC, 0419GJC84P]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Nilpotent_matrix
    locator: Examples
---

## Statement

A strictly upper triangular matrix of order $n$ becomes zero after at most $n$ multiplications by itself.
Let $R$ be a ring, let $n \ge 1$, and let $N$ be a strictly [[upper triangular|0MKABWDRNC]] $n \times n$ matrix over $R$.
Then, for every $k \ge 1$,
$$(N^k)_{ij} = 0 \quad \text{whenever } j - i < k.$$
In particular $N^n = 0$, so $N$ is [[nilpotent|0419GJC84P]].

## Remarks

### What the entry rule says

Number the diagonals of a square matrix by $j - i$, so that the main diagonal is diagonal $0$ and the top right corner is diagonal $n - 1$.
A strictly upper triangular matrix lives on the diagonals $1, \dots, n - 1$.
The theorem says that $N^k$ lives on the diagonals $k, \dots, n - 1$, so each power clears one more diagonal.
In [[the 3 × 3 example|NRNV4AJJ0E]], $N^2$ has a single nonzero entry, in the corner $(1, 3)$ on diagonal $2$, and $N^3 = 0$.

### Why each hypothesis is needed

The diagonal must be zero.
The upper triangular matrix $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has $k$-th power $\begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$, which is never $0$, because its diagonal entries are $1^k = 1$.

The exponent $n$ cannot be lowered in general.
The shift matrix $S = E_{12} + E_{23} + \dots + E_{n-1,n}$ sends $e_j$ to $e_{j-1}$ and $e_1$ to $0$, so $S^{n-1}$ sends $e_n$ to $e_1$ and $S^{n-1} = E_{1n} \neq 0$.

### What it gives you

Since $N^n = 0$, the matrix $I - N$ is invertible with
$$(I - N)^{-1} = I + N + N^2 + \dots + N^{n-1},$$
by the [[geometric series for a nilpotent matrix|N40XPYS89W]].
So every unitriangular matrix $I + N$ is invertible, and its inverse $I - N + N^2 - \dots$ is unitriangular as well.
For example, $\begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix}^{-1} = \begin{pmatrix} 1 & -a \\ 0 & 1 \end{pmatrix}$, since the strictly upper part squares to $0$.
The same results hold for strictly lower triangular matrices, by taking the [[transpose|09DXWYRD43]].

### The converse

The converse holds up to a change of basis.
Over a field, every nilpotent matrix is [[similar|0E89HQATM8]] to a strictly upper triangular matrix.
This uses [[triangularization|0363JMQ42Y]] and the fact that $0$ is the only eigenvalue of a nilpotent matrix, and it belongs to the topic on diagonalization and invariant subspaces.
Without the change of basis the converse fails: $\begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix}$ squares to $0$ but is not triangular.

## Explanations

### L1 human

A strictly upper triangular matrix has zeros on the diagonal and below it.
Each time you multiply by it, the nonzero entries move one step further toward the top right corner.
After $n$ steps for an $n \times n$ matrix there is no room left, and the power is the zero matrix.

### L2 human

Think of $N$ as a map, and let $V_j$ be the span of $e_1, \dots, e_j$, with $V_0 = 0$.
Column $j$ of $N$ has zeros from row $j$ down, so $Ne_j$ lies in $V_{j-1}$, and $N$ moves each $V_j$ one level down.
Applying $N$ $k$ times moves $V_j$ into $V_{j-k}$, and $n$ steps take $V_n = R^n$ to $V_0 = 0$.
The [[proof|YAKSRND7BW]] gives the entry version of this argument by induction.
Watch out: the index of nilpotency can be smaller than $n$, for example $N = E_{13}$ of order $3$ already has $N^2 = 0$.

### L3 human

The strictly upper triangular matrices form a two-sided ideal of the ring of upper triangular matrices, and the theorem says that this ideal is nilpotent: any product of $n$ of its elements is $0$, by the same induction.
It is the Jacobson radical of the ring of upper triangular matrices over a field.
Under the bracket $[A, B] = AB - BA$ the strictly upper triangular matrices form a nilpotent Lie algebra, and Engel's theorem says that, in a suitable basis, every Lie algebra of nilpotent matrices consists of strictly upper triangular matrices.
