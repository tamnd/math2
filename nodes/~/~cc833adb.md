---
tag: ~cc833adb
kind: definition
name: Involutory matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
defines: ~c8443172
uses: [0CP7YY6NAG, 076JGP6R3T, ~495c2486]
sources:
  - url: https://en.wikipedia.org/wiki/Involutory_matrix
    locator: lead section
---

## Definition

Let $R$ be a ring and let $A$ be an $n \times n$ [[square matrix|0CP7YY6NAG]] over $R$.
The matrix $A$ is *involutory* when $A^2 = I_n$, where $A^2$ is the [[matrix product|076JGP6R3T]] $AA$ and $I_n$ is the [[identity matrix|~495c2486]].

## Notation

- An involutory matrix is also called an *involution*.

## Remarks

- An involutory matrix is invertible, and it is its own inverse.
- $I$, $-I$ and $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ are involutory.
- When $2$ is invertible in a commutative ring $R$, $A$ is involutory if and only if $\tfrac12 (I + A)$ is [[idempotent|0K7TD9BV2D]].

## Explanations

### L1 human

An involutory matrix undoes itself: applying it twice gives back every vector.

### L2 human

The definition asks for $A^{-1} = A$, so the matrix and its inverse are the same.
