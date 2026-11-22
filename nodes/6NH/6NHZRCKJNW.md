---
tag: 6NHZRCKJNW
kind: definition
name: Identity matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
defines: 06DW9BAWB1
uses: [0CP7YY6NAG]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.one
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Identity_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Identity_matrix
    locator: Properties
  - book: isbn:9780321982384
    locator: Section 2.1
---

## Definition

The identity matrix of order $n$ is the square matrix with ones on the main diagonal and zeros elsewhere.
Let $R$ be a ring with identity $1$, and let $n \ge 0$ be an integer.
The *identity matrix* of order $n$ is the [[square matrix|0CP7YY6NAG]] $I_n$ with entries
$$(I_n)_{ij} = \delta_{ij} = \begin{cases} 1 & \text{if } i = j, \\ 0 & \text{if } i \neq j, \end{cases} \qquad 1 \le i, j \le n.$$
The symbol $\delta_{ij}$ is the *Kronecker delta*.

## Notation

Books write $I_n$, $I$, $E_n$, $E$, $1_n$ or $\mathbf{1}$, and they drop the order $n$ when the context fixes it.
The letter $E$ comes from the German *Einheitsmatrix*, and it must not be confused with a [[matrix unit|A4HTT7JFD1]] $E_{ij}$.
In Mathlib the identity matrix is `1 : Matrix n n α`, given by the instance `Matrix.one`, and its entry `1 i j` is `if i = j then 1 else 0`.
This needs a decidable equality on the index type `n`, so that the test $i = j$ can be evaluated.

## Remarks

Each part of the definition has a job.
The ring must have an identity $1$, since that element sits on the diagonal; over a ring without $1$ there is no identity matrix.
The matrix must be square, because the condition $i = j$ needs the rows and the columns to be indexed by the same set.
The order is part of the data, so $I_2$ and $I_3$ are different matrices.

For a small case, the definition with $n = 2$ gives $(I_2)_{11} = (I_2)_{22} = 1$ and $(I_2)_{12} = (I_2)_{21} = 0$, so $I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$.
A matrix that fails the definition is $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, since its entry $(1, 2)$ is $1$ although $1 \ne 2$.

The Kronecker delta turns the identity laws into one line.
In the sum $\sum_k a_{ik} \delta_{kj}$, every term with $k \ne j$ is zero, and the term $k = j$ is $a_{ij}$, so $A I_n = A$.
The [[example on the identity law|FG3K8FHYNE]] does this on both sides, and the [[identity matrix|06DW9BAWB1]] page shows that the columns of $I_n$ are the [[standard basis vectors|0V7ZD6P7RK]].

## Explanations

### L1 human

The identity matrix has ones on the main diagonal and zeros everywhere else.
It plays the role of the number $1$: multiplying a matrix by it changes nothing.
For order 3 it is the $3 \times 3$ table with ones from the top left corner to the bottom right corner.

### L2 human

The Kronecker delta is a compact way to write the entries, and it also shortens sums.
For $x = (3, 5, 8)$, the sum $\sum_{k=1}^{3} x_k \delta_{k2}$ is
$$3 \cdot 0 + 5 \cdot 1 + 8 \cdot 0 = 5 = x_2.$$
So a sum against $\delta_{kj}$ picks out the term with index $j$.
This is the whole proof of $A I = A$ and $I A = A$.
The trap is to forget the order, for example to write $I$ for $I_3$ next to a $2 \times 3$ matrix on its left side.
