---
tag: ~df4f9cf2
kind: statement
role: theorem
name: Matrix exponential as the solution of a linear system
msc: [34A30, 15A16]
uses: [~c1908ddc, ~40f94cf8]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_exponential
    locator: Linear differential equation systems
---

## Statement

Let $A$ be a real $n \times n$ matrix, and for $t \in \mathbb{R}$ let $e^{t A} = \sum_{k=0}^{\infty} \frac{t^k}{k!} A^k$, a series that converges for each $t$.
Then the map $t \mapsto e^{t A}$ is differentiable on $\mathbb{R}$, and
$$\frac{d}{dt}\, e^{t A} = A\, e^{t A} = e^{t A} A.$$
Consequently, for each $x_0 \in \mathbb{R}^n$, the function $x(t) = e^{t A} x_0$ is the unique solution on $\mathbb{R}$ of the [[initial value problem|~40f94cf8]] $x' = A x$, $x(0) = x_0$.

## Remarks

Uniqueness: if $x$ is a solution, then $\frac{d}{dt}\left(e^{-tA} x(t)\right) = 0$, so $e^{-tA} x(t) = x_0$.
If $A = P D P^{-1}$ with $D$ diagonal, then $e^{tA} = P e^{tD} P^{-1}$, and $e^{tD}$ is diagonal with the entries $e^{t \lambda_k}$.
The matrix $e^{tA}$ is the [[fundamental matrix|~65b51670]] of $x' = A x$ with value $I$ at $t = 0$.

## Explanations

### L1 human

For one equation $y' = a y$, the solution is $e^{a t} y_0$.
The matrix exponential is the same formula for a system, with the matrix $A$ in place of the number $a$.
The series is the same as the series of $e^x$.
