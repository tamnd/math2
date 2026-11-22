---
tag: 1GVCRBXQT8
kind: definition
name: Involutory matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
defines: NH2QE3671N
uses: [0CP7YY6NAG, 076JGP6R3T, 6NHZRCKJNW]
sources:
  - url: https://en.wikipedia.org/wiki/Involutory_matrix
    locator: lead section
---

## Definition

An involutory matrix is a square matrix whose square is the identity.
Let $R$ be a ring and let $A$ be an $n \times n$ [[square matrix|0CP7YY6NAG]] over $R$.
We call $A$ *involutory* when $A^2 = I_n$, where $A^2 = AA$ is the [[matrix product|076JGP6R3T]] and $I_n$ is the [[identity matrix|6NHZRCKJNW]].

## Notation

An involutory matrix is also called an *involution*.

## Remarks

The matrix must be square so that $AA$ is defined and can be compared with $I_n$.
The single condition $A^2 = I_n$ says that $A$ is invertible and that its inverse is $A$ itself, since $AA = I_n$ holds in both orders at once.

For example, $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is involutory, and so are $I$ and $-I$.
In contrast, $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ is not, because its square is $-I$.
The ring matters as well: $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has square $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$, so it is involutory over $\mathbb{F}_2$ but not over $\mathbb{R}$.

When $2$ is invertible in a commutative ring $R$, the matrix $A$ is involutory if and only if $\tfrac12 (I + A)$ is [[idempotent|0K7TD9BV2D]].
The concept page on [[involutory matrices|NH2QE3671N]] explains this link with projections and gives the reflections as examples.

## Explanations

### L1 human

An involutory matrix undoes itself: applying it twice gives back every vector.
Exchanging two coordinates is an example, since exchanging them again puts them back.

### L2 human

To test the definition, compute $A^2$ and compare it with $I$.
For $A = \begin{pmatrix} 1 & 0 \\ 3 & -1 \end{pmatrix}$ the square has entries $1$, $0$, $3 - 3 = 0$ and $1$, so $A^2 = I$ and $A$ is involutory.
Watch out: $A^2 = I$ does not force $A = \pm I$, as this example shows.
