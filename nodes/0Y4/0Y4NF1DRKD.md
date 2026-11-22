---
tag: 0Y4NF1DRKD
kind: statement
role: theorem
name: Cyclic property of the trace
msc: ["15A15"]
topics: [Y1ESNQ2V52]
audience: ug1
about: [0XC1RDBY7A]
uses: [07PTPSZPME, 076JGP6R3T]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.trace_mul_comm
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace of a product
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Cyclic property
---

## Statement

The products $AB$ and $BA$ are usually different matrices, possibly of different sizes, but they always have the same trace.
Let $R$ be a commutative ring.
Let $A$ be an $m \times n$ matrix and $B$ an $n \times m$ matrix over $R$.
Then
$$\operatorname{tr}(AB) = \operatorname{tr}(BA),$$
where $\operatorname{tr}$ is the [[trace|07PTPSZPME]].

## Remarks

### Why each hypothesis is needed

The ring must be commutative.
Over the quaternions, the $1 \times 1$ matrices $(i)$ and $(j)$ give $\operatorname{tr}(ij) = k$ but $\operatorname{tr}(ji) = -k$.
The sizes must make both $AB$ and $BA$ square, but $m$ and $n$ need not be equal.
For a column $x$ and a row $y^{\mathsf{T}}$ of the same length, the theorem says $\operatorname{tr}(x y^{\mathsf{T}}) = y^{\mathsf{T}} x$, a trace of an $n \times n$ matrix equal to a single number.

### A worked case

Take the row $A = \begin{pmatrix} 1 & 2 & 3 \end{pmatrix}$ and the column $B = \begin{pmatrix} 4 & 5 & 6 \end{pmatrix}^{\mathsf{T}}$.
Then $AB = (4 + 10 + 18) = (32)$ is $1 \times 1$, while $BA$ is $3 \times 3$:
$$BA = \begin{pmatrix} 4 & 8 & 12 \\ 5 & 10 & 15 \\ 6 & 12 & 18 \end{pmatrix}, \qquad \operatorname{tr}(BA) = 4 + 10 + 18 = 32.$$
The two traces add the same three products $a_j b_j$, and that is the whole proof in miniature.
The [[proof|JW4MFX4Y8J]] does the same with a double sum.

### What it gives you

Apply the theorem to $A_1$ and the product $A_2 \cdots A_k$ to move the first factor to the end:
$$\operatorname{tr}(A_1 A_2 \cdots A_k) = \operatorname{tr}(A_2 \cdots A_k A_1).$$
Repeating this gives all cyclic shifts, so $\operatorname{tr}(ABC) = \operatorname{tr}(BCA) = \operatorname{tr}(CAB)$.
Other orders can give other values, as [[this counterexample|GMT2VT9841]] shows with $\operatorname{tr}(ABC) = 1$ and $\operatorname{tr}(BAC) = 0$.
For an [[invertible|0EB9N0S33C]] $P$, $\operatorname{tr}(P^{-1} A P) = \operatorname{tr}(A P P^{-1}) = \operatorname{tr} A$, so [[similar matrices|0E89HQATM8]] have the same trace.
For square $A$ and $B$, $\operatorname{tr}(AB - BA) = 0$, and hence [[AB − BA = I has no solution|E2P5TNE0G9]] over a field of characteristic $0$.

### Generalizations

For linear maps $f : V \to W$ and $g : W \to V$ between finite-dimensional spaces, $\operatorname{tr}(g \circ f) = \operatorname{tr}(f \circ g)$, which is the theorem read in bases; see the [[trace of a linear map|0KZDNGA561]].
Over a field there is a stronger result: $x^n \det(xI_m - AB) = x^m \det(xI_n - BA)$, so $AB$ and $BA$ have the same nonzero eigenvalues with the same multiplicities.
Comparing the coefficients of $x^{m+n-1}$ in that identity gives the theorem again.

## Explanations

### L1 human

The matrices $AB$ and $BA$ are usually different, but they have the same trace.
Each diagonal sum adds the same products $a_{ij} b_{ji}$, only in another order.
For example, $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ times $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has trace $2 + 3 = 5$ in either order.

### L2 human

The trace of $AB$ is the sum of $a_{ij} b_{ji}$ over all $i$ and $j$:
$$\operatorname{tr}(AB) = \sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij} b_{ji}.$$
This expression stays the same when you exchange the roles of $A$ and $B$, as long as $a_{ij} b_{ji} = b_{ji} a_{ij}$.
The main use is the invariance $\operatorname{tr}(P^{-1} A P) = \operatorname{tr} A$, which makes the trace a property of a linear map and not of the basis.
Watch out: the rule lets you rotate a product, never reorder it freely.

### L3 human

The theorem says that the trace is a linear form on $M_n(R)$ that vanishes on all commutators $AB - BA$.
Over a field, these commutators span the matrices of trace $0$, so the trace is, up to a scalar, the only such form.
In the language of linear maps, $\operatorname{tr}$ is the contraction $V^* \otimes V \to F$, $\varphi \otimes v \mapsto \varphi(v)$.
For rank one maps $f(x) = \varphi(x) w$ from $V$ to $W$ and $g(y) = \psi(y) v$ from $W$ to $V$, both $\operatorname{tr}(g \circ f)$ and $\operatorname{tr}(f \circ g)$ equal $\varphi(v) \psi(w)$, and bilinearity extends this to all $f$ and $g$.
