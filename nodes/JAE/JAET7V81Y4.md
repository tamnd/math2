---
tag: JAET7V81Y4
kind: definition
name: Streamlines, streaklines and pathlines
msc: [76A02, 76M27]
defines: ZWF8B7T5NX
uses: [5E6K4ATM9W, 0299VCW1TH, 0NT64JV96A]
sources:
  - url: https://en.wikipedia.org/wiki/Streamlines,_streaklines,_and_pathlines
---

## Definition

Let $\mathbf{u} \colon \Omega \times I \to \R^n$ be a continuously differentiable velocity field on an open set $\Omega \subseteq \R^n$ and an interval $I$.
For $x_0 \in \Omega$ and $\tau \in I$, let $X(t; x_0, \tau)$ be the solution of the [[ordinary differential equation|0NT64JV96A]] $\dot X = \mathbf{u}(X, t)$ with $X(\tau) = x_0$.

1. A *streamline* at time $t_0$ is a curve $s \mapsto x(s)$ that solves $\frac{dx}{ds} = \mathbf{u}(x(s), t_0)$, so it is tangent to the velocity field frozen at time $t_0$.
2. The *pathline* of the parcel at $x_0$ at time $\tau$ is the curve $t \mapsto X(t; x_0, \tau)$.
3. The *streakline* through $x_0$ at time $t$ is the curve $\tau \mapsto X(t; x_0, \tau)$ for $\tau \le t$. It consists of the positions at time $t$ of all parcels that passed through $x_0$ earlier.

## Remarks

Example: for the unsteady plane field $\mathbf{u}(x, y, t) = (1, t)$, the streamlines at time $t_0$ are the straight lines of slope $t_0$.
The pathline of the parcel at the origin at time $0$ solves $\dot x = 1$, $\dot y = t$, so it is the parabola $(t, t^2/2)$.
Non-example: this parabola is not a streamline at any time $t_0$, because its slope $t$ changes along the curve while a streamline at time $t_0$ has constant slope $t_0$.
If $\mathbf{u}$ does not depend on $t$, then the three families of curves coincide.
Streamlines are the integral curves of the velocity field in the [[Eulerian specification|5E6K4ATM9W]], and pathlines are the trajectories of the Lagrangian specification.
