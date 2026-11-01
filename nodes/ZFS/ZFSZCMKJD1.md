---
tag: ZFSZCMKJD1
kind: definition
name: Lyapunov equation
msc: [15A24, 93D05, 34D20]
defines: 92GVPZH9FT
uses: [0JXZKX526R, 0P17NGQQMQ, 0DXKE10PHF, M9SW4NVP2H]
sources:
  - url: https://en.wikipedia.org/wiki/Lyapunov_equation
---

## Definition

Let $n \ge 1$, let $A$ be an $n \times n$ complex [[matrix|0JXZKX526R]], and let $Q$ be an $n \times n$ [[Hermitian matrix|0P17NGQQMQ]].
Write $A^*$ for the [[conjugate transpose|0DXKE10PHF]] of $A$.

1. The *continuous Lyapunov equation* is $AX + XA^* + Q = 0$ for an unknown $n \times n$ matrix $X$.
2. The *discrete Lyapunov equation* is $AXA^* - X + Q = 0$ for an unknown $n \times n$ matrix $X$.

## Remarks

The continuous equation is the [[Sylvester equation|M9SW4NVP2H]] $AX + XA^* = -Q$.
Many texts in control write it as $A^* P + PA + Q = 0$ instead, which is the same equation with $A^*$ in place of $A$; for real $A$ this reads $A^T P + PA + Q = 0$.
If every eigenvalue of $A$ has negative real part, the continuous equation has the unique solution $X = \int_0^\infty e^{At} Q e^{A^* t} \, dt$, and $X$ is positive definite when $Q$ is.
If every eigenvalue of $A$ has absolute value less than $1$, the discrete equation has the unique solution $X = \sum_{k=0}^{\infty} A^k Q (A^*)^k$.
Example: for $n = 1$, $A = -1$ and $Q = 2$, the continuous equation $-2X + 2 = 0$ gives $X = 1$.
Without the eigenvalue condition a solution may fail to exist: for $n = 1$, $A = 0$ and $Q = 1$, the continuous equation reads $1 = 0$.
