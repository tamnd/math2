---
tag: SX9CD5NEPD
kind: statement
role: proposition
name: Alternating and skew-symmetric bilinear forms
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
about: [0DGDS5XY84, 0PBY4E9GQF]
uses: [08ZQAKBKHF, 0P24YW565F, 1ZB13N78XW]
sources:
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Symmetric, skew-symmetric, and alternating forms
  - url: https://en.wikipedia.org/wiki/Skew-symmetric_matrix
    locator: Skew-symmetric and alternating forms
---

## Statement

The result says that an alternating form always changes sign under a swap, that the converse needs $1 + 1 \ne 0$, and how to test both on a matrix.
Let $B$ be a [[bilinear form|0P799D6AMN]] on a vector space $V$ over a field $F$.

1. If $B$ is [[alternating|08ZQAKBKHF]], then $B$ is skew-symmetric.
2. If the [[characteristic|1ZB13N78XW]] of $F$ is not $2$ and $B$ is skew-symmetric, then $B$ is alternating.
3. If the characteristic of $F$ is $2$, then $B$ is skew-symmetric if and only if $B$ is symmetric.
4. Let $V$ have finite dimension with a basis $(e_1, \dots, e_n)$, and let $A$ be the [[matrix|0P24YW565F]] of $B$, with $A_{ij} = B(e_i, e_j)$. Then $B$ is alternating if and only if $A^{\mathsf{T}} = -A$ and $A_{ii} = 0$ for $i = 1, \dots, n$.

The [[proof|MA5AD01GHA]] expands $B(u + v, u + v)$ and then reads the result off the matrix.

## Remarks

### Why the characteristic matters

Part 2 is the only part with a hypothesis on $F$, and it cannot be dropped.
Over $\mathbb{F}_2$, the [[identity form $x_1 y_1 + x_2 y_2$|1V7NMPCSK9]] is skew-symmetric, because $-1 = 1$, but $B(e_1, e_1) = 1$.
The reason shows in one line: skew-symmetry with $u = v$ gives $B(v, v) = -B(v, v)$, that is $2B(v, v) = 0$, and this forces $B(v, v) = 0$ only when $2$ can be cancelled.
The [[one-dimensional form xy on the field with two elements|QFAWSF1A04]] is an even smaller counterexample.

Part 4 needs both of its conditions in characteristic $2$.
Over $\mathbb{F}_2$ the matrix $I_2$ satisfies $I_2^{\mathsf{T}} = -I_2$ but has a nonzero diagonal.
Outside characteristic $2$ the diagonal condition follows from the first one, since $A_{ii} = -A_{ii}$ gives $2A_{ii} = 0$.

### What it gives you

Outside characteristic $2$ there is no difference between the two words, and a form is alternating exactly when its matrix is [[skew-symmetric|0PBY4E9GQF]].
For example, over $\mathbb{Q}$ the form with matrix $\begin{pmatrix} 0 & 4 \\ -4 & 0 \end{pmatrix}$ is alternating, and so $B(v, v) = 0$ for every $v$ without further checks.

In characteristic $2$, part 3 says that the skew-symmetric forms are the symmetric ones, and part 4 picks out the alternating forms among them as those with a zero diagonal.
So the alternating forms are a proper subspace of the symmetric forms whenever $V \ne 0$.
In every characteristic, the alternating forms on a space of dimension $n$ form a space of dimension $n(n - 1)/2$, since the entries above the diagonal fix an alternating matrix.
For $n = 3$ this is $3$, one parameter for each of the places $(1, 2)$, $(1, 3)$ and $(2, 3)$.

### The converse of part 1

The converse of part 1 is part 2, and it holds exactly when the characteristic is not $2$.
In characteristic $2$ it fails for every $V \ne 0$: pick a nonzero linear form $a$ and put $B(u, v) = a(u)\, a(v)$; it is symmetric, so skew-symmetric, but $B(v, v) = a(v)^2 \ne 0$ when $a(v) \ne 0$.

### Generalizations

The same relation holds for [[alternating multilinear maps|0K6CH0MT0F]] of any number of arguments, by the [[antisymmetry statement|VJZVSTWYYW]]: alternating maps change sign under each swap of two arguments, and the converse needs $1 + 1 \ne 0$.

## Explanations

### L1 human

There are two ways to say that a form behaves like a signed area.
The first way says that an arrow paired with itself gives $0$.
The second way says that swapping the two arrows changes the sign.
The first way always gives the second.
The second way gives the first, except in number systems where $1 + 1 = 0$.

### L2 human

Here is part 4 at work on $\mathbb{Q}^3$.
Take
$$A = \begin{pmatrix} 0 & 1 & -2 \\ -1 & 0 & 3 \\ 2 & -3 & 0 \end{pmatrix}.$$
The matrix satisfies $A^{\mathsf{T}} = -A$ and has a zero diagonal, so $B(x, y) = x^{\mathsf{T}} A y$ is alternating.
Check with $x = (1, 2, 1)$: $Ax = (0 + 2 - 2,\ -1 + 0 + 3,\ 2 - 6 + 0) = (0, 2, -4)$, and $x^{\mathsf{T}} A x = 0 + 4 - 4 = 0$.
The typical use is exactly this: one look at the matrix replaces a check over all vectors.
Watch out: over a field of characteristic $2$ you must look at the diagonal too.

### L3 human

Part 4 says that the alternating matrices are the matrices $C - C^{\mathsf{T}}$, since an alternating $A$ equals $U - U^{\mathsf{T}}$ for its strictly upper triangular part $U$.
In the language of tensors, the alternating forms are the linear forms on $\Lambda^2 V$, while the skew-symmetric forms are the forms that change sign under the swap of the two tensor factors.
The two classes agree exactly when $2$ is invertible, and that is why quadratic and symplectic geometry in characteristic $2$ need their own treatment.
