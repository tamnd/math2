---
tag: PTZ8YNEAKK
kind: definition
name: Principle of relativity
msc: [83A05, 70A05]
defines: 5ABAVATERQ
uses: [8CTX67V404]
sources:
  - url: https://en.wikipedia.org/wiki/Principle_of_relativity
---

## Definition

Let a physical theory be given by a system of equations for quantities defined on events with coordinates $(t, x, y, z)$ in an inertial frame of reference.
Let $G$ be a group of coordinate changes between inertial frames, together with a rule saying how each quantity transforms.
The theory satisfies the *principle of relativity* with symmetry group $G$ under this condition.
Every solution of its equations, written in one inertial frame and transformed by any element of $G$, is again a solution of the same equations.

## Remarks

Example: Newton's second law $m \ddot{\mathbf{x}} = \mathbf{F}$ for forces depending only on relative positions satisfies the principle with $G$ the group of [[Galilean transformations|8CTX67V404]].
Check: under $\mathbf{x}' = \mathbf{x} - \mathbf{v} t$ with constant $\mathbf{v}$, one has $\ddot{\mathbf{x}}' = \ddot{\mathbf{x}}$, and relative positions do not change.
Non-example: the wave equation $\partial_t^2 u = c^2 \partial_x^2 u$ does not satisfy it for the Galilean group.
The solution $u = f(x - ct)$ becomes $f(x' - (c - v) t')$ under $x' = x - vt$, $t' = t$, which solves the equation only with $c$ replaced by $c - v$.
The wave equation does satisfy the principle for the group of Lorentz transformations.
The principle of special relativity is the case of the Poincaré group; the general principle of relativity of general relativity asks for invariance under all smooth coordinate changes.
