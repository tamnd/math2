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

Let $R$ be a ring with identity $1$, and let $n \ge 0$ be an integer.
The *identity matrix* of order $n$ is the [[square matrix|0CP7YY6NAG]] $I_n$ with entries
$$(I_n)_{ij} = \delta_{ij} = \begin{cases} 1 & \text{if } i = j, \\ 0 & \text{if } i \neq j. \end{cases}$$
The symbol $\delta_{ij}$ is the *Kronecker delta*.
So $I_n$ has $1$ at each position of the main diagonal and $0$ at each other position.

## Notation

- Books write $I_n$, $I$, $E_n$, $E$, $1_n$ or $\mathbf{1}$.
- Some books use $E$ from the German *Einheitsmatrix*; do not confuse it with a [[matrix unit|A4HTT7JFD1]] $E_{ij}$.
- In Mathlib the identity matrix is `1 : Matrix n n α`, given by the instance `Matrix.one`, and `1 i j` is `if i = j then 1 else 0`.

## Remarks

- For each $m \times n$ matrix $A$, $I_m A = A$ and $A I_n = A$. The [[identity example|FG3K8FHYNE]] checks this entry by entry.
- So $I_n$ is the identity element of the [[matrix ring|AB2MD5CD13]] $M_n(R)$.
- The columns of $I_n$ are the [[standard basis vectors|0V7ZD6P7RK]] $e_1, \dots, e_n$.
- The identity matrix is the matrix of the identity map in any basis.

## Explanations

### L1 human

The identity matrix has ones on the main diagonal and zeros everywhere else.
It plays the role of the number $1$: multiplying a matrix by it changes nothing.

### L2 human

The Kronecker delta is a compact way to write the entries.
In a sum $\sum_k a_{ik} \delta_{kj}$, only the term $k = j$ survives, and this gives $A I = A$ in one line.
