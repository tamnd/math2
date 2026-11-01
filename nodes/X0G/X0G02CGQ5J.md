---
tag: X0G02CGQ5J
kind: problem
name: Matrix multiplication exponent
msc: [68Q25, 65Y20, 15A69]
uses: [032Q9FB8MT, 0TGV80E6A4, W84NTF77M0, 3CVWXDS4JQ]
about: [032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Computational_complexity_of_matrix_multiplication
history:
  posed_by: "Volker Strassen"
  first_stated: "1969"
---

## Problem

Fix a field $F$.
Consider the real numbers $\tau$ such that an algebraic algorithm multiplies two $n \times n$ matrices over $F$ with $O(n^\tau)$ operations in $F$ (see [[big O notation|0TGV80E6A4]]).
The *matrix multiplication exponent* $\omega$ is the infimum of these $\tau$.
Determine the value of $\omega$; in particular, decide whether $\omega = 2$.

## Remarks

The bound $\omega \ge 2$ holds because the output has $n^2$ entries, and the schoolbook [[matrix multiplication|032Q9FB8MT]] gives $\omega \le 3$.
The [[Strassen algorithm|3CVWXDS4JQ]] gave $\omega \le \log_2 7 \approx 2.807$ in 1969.
Coppersmith and Winograd obtained $\omega < 2.376$ in 1990.
Refinements of their method by several groups since 2010 have brought the upper bound below $2.372$.
The problem is open: no lower bound better than $2$ is known.
Strassen showed that $\omega$ can be read off from the [[tensor rank|W84NTF77M0]] of the matrix multiplication tensor $\langle n, n, n \rangle$.
It is the infimum of the $\tau$ such that this rank is $O(n^\tau)$.
Many other problems of linear algebra, such as inverting a matrix or computing a determinant, can be solved with $O(n^{\omega + \varepsilon})$ operations for every $\varepsilon > 0$.

## Explanations

### L1 human

Multiplying two $n \times n$ matrices the usual way needs about $n^3$ multiplications.
The exponent $\omega$ measures how much better one can do in the best case, as a power of $n$.
Strassen showed that the power $3$ is not optimal, and later work has pushed it down to about $2.37$.
Nobody knows whether one can get as low as $2$, which would mean that multiplying matrices costs hardly more than reading them.
