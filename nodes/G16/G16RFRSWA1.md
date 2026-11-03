---
tag: G16RFRSWA1
kind: definition
name: Controllability Gramian
msc: [93B05, 93C05]
defines: 703MCKB5SZ
uses: [020M04FN1H, 09DXWYRD43, 01MMVW8CKC, 92GVPZH9FT, A9WFM77Z4P, 9NSCZ2KBEB]
sources:
  - url: https://en.wikipedia.org/wiki/Controllability_Gramian
---

## Definition

Let $n, m \ge 1$, let $A$ be a real $n \times n$ matrix and let $B$ be a real $n \times m$ matrix, for the linear system $x' = Ax + Bu$.
For $T > 0$, the *controllability Gramian* on $[0, T]$ is the $n \times n$ matrix
$$W_c(T) = \int_0^T e^{A\tau} B B^T e^{A^T \tau} \, d\tau,$$
where $e^{A\tau}$ is the [[matrix exponential|020M04FN1H]] and $B^T$ is the [[transpose|09DXWYRD43]].
If every eigenvalue of $A$ has negative real part, the *infinite-horizon controllability Gramian* is $W_c = \int_0^\infty e^{A\tau} B B^T e^{A^T \tau} \, d\tau$.

## Remarks

$W_c(T)$ is symmetric and [[positive semidefinite|01MMVW8CKC]], since $v^T W_c(T) v = \int_0^T \abs{B^T e^{A^T \tau} v}^2 \, d\tau \ge 0$.
It is positive definite if and only if the system is [[controllable|A9WFM77Z4P]], which is the core of the proof of the [[Kalman rank condition|9NSCZ2KBEB]].
When $A$ is stable, $W_c$ is the unique solution of the [[Lyapunov equation|92GVPZH9FT]] $A W + W A^T + B B^T = 0$.
Example: for $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$ one has $e^{A\tau} B = \begin{pmatrix} \tau \\ 1 \end{pmatrix}$, so
$$W_c(T) = \begin{pmatrix} T^3/3 & T^2/2 \\ T^2/2 & T \end{pmatrix},$$
with determinant $T^4/12 > 0$.
Non-example: for $A = 0$ and $B = 1$ the integrand is $1$, so the infinite-horizon integral diverges; the hypothesis on the eigenvalues of $A$ fails.
