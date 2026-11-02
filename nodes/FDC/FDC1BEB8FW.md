---
tag: FDC1BEB8FW
kind: statement
role: theorem
name: Noether theorems for singular integral equations
msc: ["45E05", 47A53]
uses: [E30EA6ETZ4, GW3B4K1WA5, 012PBA0FMD, 2V9Q4KHY1T]
about: [E30EA6ETZ4, GW3B4K1WA5]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_integral_operators_on_closed_curves
---

## Statement

Let $\Gamma$ be a smooth simple closed curve in $\C$, oriented counterclockwise.
Let $a$ and $b$ be [[Hölder continuous|012PBA0FMD]] functions on $\Gamma$ with $a(t)^2 - b(t)^2 \ne 0$ for all $t \in \Gamma$, and let $k$ be Hölder continuous on $\Gamma \times \Gamma$.
Let $K$ be the operator of the [[singular integral equation|E30EA6ETZ4]]
$$K \varphi(t) = a(t) \, \varphi(t) + \frac{b(t)}{\pi i} \, \mathrm{p.v.} \int_\Gamma \frac{\varphi(\tau)}{\tau - t} \, d\tau + \int_\Gamma k(t, \tau) \, \varphi(\tau) \, d\tau,$$
and let $K'$ be its adjoint operator
$$K' \psi(t) = a(t) \, \psi(t) - \frac{1}{\pi i} \, \mathrm{p.v.} \int_\Gamma \frac{b(\tau) \, \psi(\tau)}{\tau - t} \, d\tau + \int_\Gamma k(\tau, t) \, \psi(\tau) \, d\tau.$$
All functions below are Hölder continuous on $\Gamma$.
Let $\kappa$ be the [[index|GW3B4K1WA5]] of $K$.
Then:

1. The homogeneous equations $K \varphi = 0$ and $K' \psi = 0$ each have a finite number of linearly independent solutions; call these numbers $\ell$ and $\ell'$.
2. For Hölder continuous $f$, the equation $K \varphi = f$ has a solution if and only if $\int_\Gamma f(t) \, \psi(t) \, dt = 0$ for every solution $\psi$ of $K' \psi = 0$.
3. $\ell - \ell' = \kappa$.

## Remarks

The adjoint is taken for the bilinear pairing $\int_\Gamma u(t) \, v(t) \, dt$; exchanging the order of integration in $\int_\Gamma (K \varphi) \psi \, dt$ gives $\int_\Gamma \varphi \, (K' \psi) \, dt$.
Proof idea: the dominant operator $K^0 = a + b S$, with $S \varphi = \frac{1}{\pi i} \mathrm{p.v.} \int_\Gamma \frac{\varphi(\tau)}{\tau - t} \, d\tau$, is solved explicitly through the [[Sokhotski–Plemelj formulae|DRT1E6WY6K]] and a Riemann–Hilbert problem, which shows that $\ell - \ell' = \kappa$ for $K^0$.
One then builds a regularizer $M$ with $M K = I + T$ for a compact operator $T$, and the Fredholm theory of $I + T$ transfers the results to $K$.
The term with $k$ is compact, so it changes neither the finiteness nor the index.

Example: on the unit circle, take $a(t) = (t + 1)/2$, $b(t) = (t - 1)/2$ and $k = 0$, so $\kappa = -1$.
With $P = \frac12 (I + S)$ and $Q = \frac12 (I - S)$, one has $K = a + bS = t P + Q$.
On $\varphi = \sum_n c_n t^n$, $P$ keeps the terms with $n \ge 0$ and $Q$ the terms with $n < 0$, so $K \varphi = \sum_{n \ge 0} c_n t^{n+1} + \sum_{n < 0} c_n t^n$.
So $K \varphi = 0$ forces $\varphi = 0$, and $K \varphi = f$ is solvable only if the constant Fourier coefficient of $f$ vanishes: $\ell = 0$, $\ell' = 1$, and $\ell - \ell' = -1 = \kappa$.

The normal type condition $a^2 - b^2 \ne 0$ is needed: without it, the homogeneous equation may have infinitely many independent solutions or the range may fail to be closed.
When $\kappa = 0$, the three statements give the classical Fredholm alternative, but in general $\ell \ne \ell'$, unlike for Fredholm equations of the second kind.

## Explanations

### L1 human

A singular integral equation of normal type behaves almost like a system of linear equations.
There are finitely many independent solutions of the homogeneous equation and finitely many conditions for the general equation to be solvable.
The difference of these two numbers is the index, and it can be computed by counting how many times a function made from the coefficients winds around $0$.

### L2 human

These are the singular analogues of Fredholm's theorems.
They were proved by Fritz Noether, and the singular integral operators of normal type are classical examples of Fredholm operators with nonzero [[Fredholm index|2V9Q4KHY1T]].
The index formula $\ell - \ell' = \kappa$ is an early case of an index theorem, which expresses an analytic quantity through a topological one, here a winding number.
In the Hölder setting the theorems are presented in Muskhelishvili's book on singular integral equations; the same results hold for operators on $L^p(\Gamma)$, $1 < p < \infty$, with continuous coefficients.
