---
tag: HAZ0NKCAXS
kind: definition
name: Traveling wave
msc: [35C07, 35K57]
defines: M37M411KP7
uses: [GC5BDZ6QBC, NEGHXN8RE1]
sources:
  - url: https://en.wikipedia.org/wiki/Wave
---

## Definition

Consider a [[partial differential equation|GC5BDZ6QBC]] for a function $u \colon \R \times \R \to \R^m$ of a space variable $x$ and a time variable $t$.
A *traveling wave* solution is a solution of the form
$$u(x, t) = U(x - c t),$$
where $c \in \R$ is the *speed* and $U \colon \R \to \R^m$ is the *profile*.
When the limits $U(\pm\infty)$ exist and differ, the wave is called a *front*.
When they exist and are equal and $U$ is not constant, it is called a *pulse*.

## Remarks

In $\R^n$ one also considers plane traveling waves $u(x, t) = U(x \cdot e - ct)$ for a unit vector $e$.
Substituting $\xi = x - ct$ turns the equation into an ordinary differential equation for $U(\xi)$, in which $c$ is an unknown parameter.

Example: the viscous [[Burgers' equation|NEGHXN8RE1]] $u_t + u u_x = \nu u_{xx}$, with $\nu > 0$, has the front $u = c\left(1 - \tanh\frac{c(x - ct)}{2\nu}\right)$ for every $c > 0$.
Check: with $U(\xi) = c(1 - \tanh \tfrac{c\xi}{2\nu})$, the equation becomes $-cU' + UU' = \nu U''$.
Integrating once with $U(+\infty) = 0$ gives $\nu U' = \tfrac12 U^2 - cU$, which this $U$ satisfies.
The front goes from $2c$ to $0$, and its speed $c$ is the average of the two states, as for a shock.

Non-example: $u(x, t) = e^{-t} \sin x$ solves the heat equation $u_t = u_{xx}$, but it is not a traveling wave.
For a traveling wave, $\sup_x \abs{u(x, t)} = \sup \abs{U}$ does not depend on $t$, while here it equals $e^{-t}$.

## Explanations

### L1 human

A traveling wave is a fixed shape that slides along the line at constant speed.
