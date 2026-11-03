---
tag: 6RARBNW07Y
kind: definition
name: Berlekamp–Welch algorithm
msc: [94B35, 94B05]
defines: D2WZ0M5RWX
uses: [5VBWJ7EFTX, 0ZXZ82FTX2, 0SDC934R52, EP5HNGSXFA]
sources:
  - url: https://en.wikipedia.org/wiki/Berlekamp%E2%80%93Welch_algorithm
---

## Definition

Let $\F_q$ be a [[finite field|0ZXZ82FTX2]], let $1 \le k \le n$, and let $a_1, \dots, a_n \in \F_q$ be distinct.
Let $C$ be the [[Reed–Solomon code|5VBWJ7EFTX]] of polynomials of degree less than $k$ evaluated at $a_1, \dots, a_n$, and let $e = \floor{(n - k)/2}$.
The *Berlekamp–Welch algorithm* takes a received word $y = (y_1, \dots, y_n) \in \F_q^n$ and does the following.

1. Find polynomials $E, Q \in \F_q[x]$ with $E$ monic of degree $e$ and $\deg Q \le e + k - 1$ such that $Q(a_i) = y_i E(a_i)$ for $i = 1, \dots, n$. This is a linear system in the coefficients of $E$ and $Q$. If there is no solution, output "failure".
2. Divide $Q$ by $E$. Output $f = Q/E$ if the remainder is $0$, $\deg f < k$, and $(f(a_1), \dots, f(a_n))$ is at [[Hamming distance|EP5HNGSXFA]] at most $e$ from $y$. Otherwise output "failure".

## Remarks

Correctness: suppose that some $f$ with $\deg f < k$ has $y_i \ne f(a_i)$ for at most $e$ indices $i$.
Then a solution exists: take $E$ monic of degree $e$ vanishing at the error positions, and $Q = fE$.
For any solution $(E, Q)$, the polynomial $R = Q - fE$ has degree at most $e + k - 1$ and vanishes at the at least $n - e$ points where $y_i = f(a_i)$.
Since $n - e \ge e + k > e + k - 1$, $R = 0$, so the algorithm outputs $f$.
The linear system has $n$ equations and $2e + k$ unknowns, so the algorithm runs in time polynomial in $n$.

Example: over $\F_5$ with $n = 4$, $k = 2$, points $0, 1, 2, 3$, so $e = 1$.
The sent word for $f(x) = 1 + x$ is $(1, 2, 3, 4)$, and the received word is $y = (1, 2, 0, 4)$.
The pair $E = x - 2$ and $Q = (1 + x)(x - 2)$ solves the system, and $Q/E = 1 + x$ is the output.

Non-example: if more than $e$ values are wrong, step 1 may still find a solution, but the quotient need not be the sent polynomial.
The algorithm only promises correct decoding within radius $e$.
