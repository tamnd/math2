---
tag: 3Z1Z7TDPHZ
kind: statement
role: proposition
name: Discretization of linear systems
msc: [93C57, 93C55, 93C05]
uses: [PQ5FJ334WR, 6J9MPVHSMF, 020M04FN1H, 0YC8JT513J, 0EB9N0S33C]
about: [PQ5FJ334WR, 6J9MPVHSMF]
sources:
  - url: https://en.wikipedia.org/wiki/Discretization
    locator: Discretization of linear state space models
---

## Statement

Let $A \in \R^{n \times n}$, $B \in \R^{n \times m}$, $C \in \R^{p \times n}$, $D \in \R^{p \times m}$ and $T > 0$.
Consider the [[linear time-invariant system|6J9MPVHSMF]] $x' = Ax + Bu$, $y = Cx + Du$ whose input $u$ is the [[zero-order hold|PQ5FJ334WR]] of a sequence $(u_k)_{k \ge 0}$ in $\R^m$ with period $T$.
Let $x_k = x(kT)$ and $y_k = y(kT)$.
Then for every $k \ge 0$,
$$x_{k+1} = A_d x_k + B_d u_k, \qquad y_k = C x_k + D u_k,$$
where
$$A_d = e^{AT}, \qquad B_d = \left( \int_0^T e^{A\tau}\, d\tau \right) B$$
and $e^{AT}$ is the [[matrix exponential|020M04FN1H]].
If $A$ is [[invertible|0EB9N0S33C]], then $B_d = A^{-1} (e^{AT} - I) B$.

## Remarks

The [[exponential solution|0YC8JT513J]] of $x' = Ax$ extends to the variation of constants formula, which gives $x((k+1)T) = e^{AT} x(kT) + \int_{kT}^{(k+1)T} e^{A((k+1)T - t)} B u(t)\, dt$.
On this interval $u(t) = u_k$ is constant, and the substitution $\tau = (k+1)T - t$ turns the integral into $\int_0^T e^{A\tau}\, d\tau\, B u_k$.
The relation is exact at the sampling instants; no approximation is made, unlike in Euler's method, which uses $A_d \approx I + TA$ and $B_d \approx TB$.

Example: for the double integrator $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $B = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$, one has $e^{A\tau} = \begin{pmatrix} 1 & \tau \\ 0 & 1 \end{pmatrix}$, so
$$A_d = \begin{pmatrix} 1 & T \\ 0 & 1 \end{pmatrix}, \qquad B_d = \begin{pmatrix} T^2/2 \\ T \end{pmatrix}.$$
Here $A$ is not invertible, so the integral form of $B_d$ is needed.

If $u$ is not held constant between samples, the formula fails, because the integral then depends on the values of $u$ inside the interval.

## Explanations

### L1 human

A computer controls a physical system by sending a new input value every $T$ seconds and holding it in between.
The proposition says that, seen only at the clock ticks, the system then follows an exact step-by-step recursion.
The matrices of this recursion come from the matrix exponential of the continuous model.

### L2 human

This zero-order hold discretization is the standard way to design digital controllers for continuous plants.
Each eigenvalue $\lambda$ of $A$ becomes the eigenvalue $e^{\lambda T}$ of $A_d$, so the open left half-plane is mapped into the open unit disc and stability is preserved.
Other discretizations, such as the bilinear (Tustin) transform, approximate the system instead of being exact for held inputs.
Controllability and observability are preserved under sampling, except possibly for special values of $T$ at which distinct eigenvalues $\lambda \ne \mu$ of $A$ satisfy $e^{\lambda T} = e^{\mu T}$.
