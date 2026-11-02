---
tag: W0F3YWAJ23
kind: definition
name: Helmholtz equation
msc: [35J05]
defines: MNXKTXJ35G
uses: [GC5BDZ6QBC, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Helmholtz_equation
---

## Definition

Let $n \ge 1$, let $\Omega \subseteq \R^n$ be an open set, and let $k > 0$ be a real constant.
Let $u \colon \Omega \to \C$ be twice differentiable.
The *Helmholtz equation* on $\Omega$ with wave number $k$ is the [[partial differential equation|GC5BDZ6QBC]]
$$\Delta u + k^2 u = 0,$$
where $\Delta = \partial_1^2 + \cdots + \partial_n^2$ is the [[Laplacian|0E0B6RA8K0]].
The *inhomogeneous Helmholtz equation* is $\Delta u + k^2 u = -f$ for a given function $f$ on $\Omega$.

## Remarks

Example: in $\R^n$, for a unit vector $\omega$, the plane wave $u(x) = e^{i k \, \omega \cdot x}$ is a solution, since $\Delta u = (ik)^2 \abs{\omega}^2 u = -k^2 u$.
Non-example: $u(x) = e^{k x_1}$ is not a solution, since $\Delta u + k^2 u = 2k^2 u \ne 0$; it solves instead $\Delta u - k^2 u = 0$, the modified Helmholtz equation.
If $v(x, t) = u(x) e^{-i \omega t}$ solves the wave equation $\partial_t^2 v = c^2 \Delta v$, then $u$ solves the Helmholtz equation with $k = \omega / c$.
On a bounded domain with zero boundary values, the equation has a nonzero solution exactly when $k^2$ is an eigenvalue of $-\Delta$ with that boundary condition.
Some authors allow complex $k$.
