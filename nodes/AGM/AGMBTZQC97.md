---
tag: AGMBTZQC97
kind: definition
name: Matrix difference equation
msc: [39A06]
defines: 9VA6P5KQQT
uses: [0VD9ZSWWJG, 0G9EKM0E15]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_difference_equation
---

## Definition

Let $K$ be a field and let $m \ge 1$.
Let $A(n)$, for $n \in \N$, be $m \times m$ [[matrices|0VD9ZSWWJG]] over $K$, and let $b(n)$, for $n \in \N$, be vectors in $K^m$.
A *matrix difference equation* (of first order) is the equation
$$x(n+1) = A(n)\, x(n) + b(n) \qquad (n \in \N)$$
for a [[sequence|0G9EKM0E15]] of vectors $x \colon \N \to K^m$.

1. It is *homogeneous* if $b(n) = 0$ for all $n$.
2. It has *constant coefficients* if $A(n) = A$ does not depend on $n$.

A *solution* is a sequence $x$ that satisfies the equation for all $n \in \N$.

## Remarks

Example: with $m = 2$, $A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ and $b = 0$, the sequence $x(n) = (F_{n+1}, F_n)^T$ of [[Fibonacci numbers|0GA9K57A39]] is a solution, since $F_{n+2} = F_{n+1} + F_n$ and the second entry just shifts.
Non-example: $x(n+1) = x(n)^2$ for $x(n) \in K$ is not a matrix difference equation, since the right side is not of the form $A(n) x(n) + b(n)$.
In the homogeneous constant-coefficient case the solutions are $x(n) = A^n x(0)$.
Equations of higher order, such as $x(n+1) = A_0 x(n) + A_1 x(n-1)$, reduce to first order by stacking $(x(n), x(n-1))$ into one vector of size $2m$.
In this way a scalar linear recurrence of order $d$ becomes a first-order system with a [[companion matrix|0ZCWPNZTQ3]].
