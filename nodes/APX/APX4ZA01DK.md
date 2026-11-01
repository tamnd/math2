---
tag: APX4ZA01DK
kind: definition
name: Algebraic Riccati equation
msc: [15A24, 49N10, 93C05]
defines: GGZV75ZZMV
uses: [0VD9ZSWWJG, 0VR671PHE5, 01MMVW8CKC, 0KX66CZMBB, 09DXWYRD43]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_Riccati_equation
---

## Definition

Let $n, m \ge 1$.
Let $A$ be a real $n \times n$ [[matrix|0VD9ZSWWJG]] and $B$ a real $n \times m$ matrix.
Let $Q$ be a real [[symmetric|0VR671PHE5]] [[positive semidefinite|01MMVW8CKC]] $n \times n$ matrix.
Let $R$ be a real symmetric [[positive definite|0KX66CZMBB]] $m \times m$ matrix.
Write $M^T$ for the [[transpose|09DXWYRD43]] of $M$.

1. The *continuous-time algebraic Riccati equation* is
$$A^T X + XA - XBR^{-1}B^T X + Q = 0$$
for an unknown real symmetric $n \times n$ matrix $X$.
2. The *discrete-time algebraic Riccati equation* is
$$X = A^T X A - A^T X B (R + B^T X B)^{-1} B^T X A + Q$$
for an unknown real symmetric positive semidefinite $n \times n$ matrix $X$.

## Remarks

A solution $X$ of the continuous equation is *stabilising* if every eigenvalue of $A - BR^{-1}B^T X$ has negative real part.
If the pair $(A, B)$ is stabilisable and the pair $(Q^{1/2}, A)$ is detectable, the continuous equation has a unique positive semidefinite solution, and it is stabilising.
The optimal feedback of the linear-quadratic regulator is then $u = -R^{-1}B^T X x$.
Example: for $n = m = 1$, $A = 0$ and $B = Q = R = 1$, the continuous equation is $1 - X^2 = 0$, with solutions $X = 1$ and $X = -1$.
Only $X = 1$ is stabilising, since $A - BR^{-1}B^T X = -X$.
For $B = 0$ the continuous equation becomes the [[Lyapunov equation|92GVPZH9FT]] $A^T X + XA + Q = 0$, which is linear and not of Riccati type.
