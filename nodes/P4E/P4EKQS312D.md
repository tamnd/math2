---
tag: P4EKQS312D
kind: concept
name: Hankel operator
msc: [47B35]
sources:
  - url: https://en.wikipedia.org/wiki/Hankel_matrix
---

## Summary

A Hankel operator is a bounded operator on $\ell^2$ whose matrix $(a_{j+k})_{j,k \ge 0}$ is constant along each anti-diagonal, an infinite [[Hankel matrix|PQ1D8FQB3E]].
Up to a unitary identification of the spaces, the same operators arise in a function form.
They are the maps $f \mapsto (I - P)(\varphi f)$ from the [[Hardy space|PNNNFJVF6W]] $H^2$ to $L^2 \ominus H^2$ on the circle.
Here $\varphi$ is a bounded symbol and $P$ is the projection onto $H^2$.
Hankel operators are close relatives of [[Toeplitz operators|GQ0X3R3WM2]] and appear in rational approximation, control theory and prediction theory.
Nehari's theorem describes the bounded ones, and Kronecker's theorem the ones of finite rank.

## Explanations

### L1 human

A Hankel matrix has the same entry along every line that runs from the lower left to the upper right.
So the whole matrix is built from one sequence $a_0, a_1, a_2, \ldots$, with $a_{j+k}$ in row $j$ and column $k$.
The Hilbert matrix, with entries $1/(j + k + 1)$, is the classical example.
The operator theory question is which sequences give a bounded operator on square-summable sequences.
