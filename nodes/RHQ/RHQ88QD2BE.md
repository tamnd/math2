---
tag: RHQ88QD2BE
kind: statement
role: proposition
name: Beeman's algorithm
msc: [65L06, 70-08]
uses: [0FXDW992DS, ESWE8Y3JD4]
about: [ESWE8Y3JD4]
sources:
  - url: https://en.wikipedia.org/wiki/Beeman%27s_algorithm
---

## Statement

Let $a \colon \R^d \to \R^d$ be continuous, and consider the equation $x'' = a(x)$.
Fix a step size $h > 0$ and write $a_n = a(x_n)$.
Beeman's algorithm computes, from $x_n$, $v_n$, $a_n$ and $a_{n-1}$,
$$x_{n+1} = x_n + h v_n + \frac{h^2}{6} (4 a_n - a_{n-1}),$$
$$v_{n+1} = v_n + \frac{h}{6} (2 a_{n+1} + 5 a_n - a_{n-1}).$$
Then for all $n \ge 2$ for which the sequences are defined,
$$x_{n+1} = 2 x_n - x_{n-1} + h^2 a_n.$$
So Beeman's algorithm produces the same positions as the [[Störmer–Verlet method|ESWE8Y3JD4]], once both start from the same $x_1$ and $x_2$.

## Remarks

Subtract the position formula at step $n - 1$ from the one at step $n$:
$$x_{n+1} - 2x_n + x_{n-1} = h (v_n - v_{n-1}) + \frac{h^2}{6} (4 a_n - 5 a_{n-1} + a_{n-2}).$$
The velocity formula gives $h (v_n - v_{n-1}) = \frac{h^2}{6}(2 a_n + 5 a_{n-1} - a_{n-2})$, and the sum is $h^2 a_n$.
The difference from Verlet lies only in the velocities, which Beeman's formula computes more accurately than the central difference $(x_{n+1} - x_{n-1})/(2h)$; this improves the computed kinetic energy.
The velocity formula above is the implicit form; a common explicit variant predicts $v_{n+1}$ first when the force depends on the velocity.

## Explanations

### L1 human

Beeman's method is a molecular dynamics integrator that uses the forces at the current and previous steps.
Its positions turn out to be exactly those of the simpler Verlet method.
What it adds is a more accurate formula for the velocities, so that the energy is measured more accurately.

### L2 human

The identity shows that Beeman's method inherits the stability and the long-time behaviour of Verlet's positions.
It is a multistep method, so it needs a starting procedure to produce $a_{-1}$ or $x_1$.
In practice velocity Verlet is more common, because it gives similar accuracy with less storage.
