---
tag: K71Y3KPMFT
kind: definition
name: Observability Gramian
msc: [93B07, 93C05]
defines: 9YEW705KHA
uses: [020M04FN1H, 09DXWYRD43, 01MMVW8CKC, 92GVPZH9FT, C4HN3EAQWM]
sources:
  - url: https://en.wikipedia.org/wiki/Observability_Gramian
---

## Definition

Let $n, p \ge 1$, let $A$ be a real $n \times n$ matrix and let $C$ be a real $p \times n$ matrix, for the linear system $x' = Ax$, $y = Cx$.
For $T > 0$, the *observability Gramian* on $[0, T]$ is the $n \times n$ matrix
$$W_o(T) = \int_0^T e^{A^T \tau} C^T C e^{A \tau} \, d\tau,$$
where $e^{A\tau}$ is the [[matrix exponential|020M04FN1H]] and $C^T$ is the [[transpose|09DXWYRD43]].
If every eigenvalue of $A$ has negative real part, the *infinite-horizon observability Gramian* is $W_o = \int_0^\infty e^{A^T \tau} C^T C e^{A \tau} \, d\tau$.

## Remarks

For the output $y(t) = C e^{At} x_0$ one has $\int_0^T \abs{y(t)}^2 \, dt = x_0^T W_o(T) x_0$.
So $W_o(T)$ is symmetric and [[positive semidefinite|01MMVW8CKC]], and it is positive definite if and only if the system is [[observable|C4HN3EAQWM]].
When $A$ is stable, $W_o$ is the unique solution of the [[Lyapunov equation|92GVPZH9FT]] $A^T W + W A + C^T C = 0$.
Example: for $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $C = \begin{pmatrix} 1 & 0 \end{pmatrix}$ one has $C e^{A\tau} = \begin{pmatrix} 1 & \tau \end{pmatrix}$, so
$$W_o(T) = \begin{pmatrix} T & T^2/2 \\ T^2/2 & T^3/3 \end{pmatrix},$$
which is positive definite.
Non-example: for $A = 0$ and $C = 1$ the infinite-horizon integral diverges, since the hypothesis on the eigenvalues of $A$ fails.
