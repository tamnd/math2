---
tag: CN7NP6R1AQ
kind: statement
role: theorem
name: Boundary integral equation for the Neumann problem
msc: [31B10, 31A10, 45B05]
uses: [9T6ZEV4125, BSJ8X2XRN9, 8KJCN49V64, 0DEB0JMN0W, GS3KT2H645]
about: [GS3KT2H645, 9T6ZEV4125]
sources:
  - url: https://en.wikipedia.org/wiki/Neumann_boundary_condition
---

## Statement

Let $m \in \set{2, 3}$, and let $D \subset \R^m$ be a bounded domain whose boundary $\partial D$ is a connected $C^2$ curve or surface with outward unit normal $\nu$.
Let $\Phi$ be the [[fundamental solution of the Laplacian|BSJ8X2XRN9]] with $-\Delta \Phi = \delta_0$.
For a continuous density $\psi$ on $\partial D$ put
$$(K'\psi)(x) = \int_{\partial D} \frac{\partial \Phi(x - y)}{\partial \nu(x)} \, \psi(y) \, ds(y), \quad x \in \partial D.$$
Let $g \colon \partial D \to \R$ be continuous.
Then:

1. The [[integral equation of the second kind|8KJCN49V64]] $\psi + 2K'\psi = 2g$ has a continuous solution $\psi$ if and only if $\int_{\partial D} g \, ds = 0$.
2. For such a solution $\psi$, the [[single layer potential|9T6ZEV4125]] $u(x) = \int_{\partial D} \Phi(x - y) \psi(y) \, ds(y)$ is [[harmonic|0DEB0JMN0W]] in $D$, and its normal derivative from inside equals $g$ on $\partial D$.

So the interior Neumann problem $\Delta u = 0$ in $D$, $\partial_\nu u = g$ on $\partial D$, is solvable exactly when $\int_{\partial D} g \, ds = 0$, and its solutions differ by constants.

## Remarks

Part 2 follows from the [[jump relations for layer potentials|J58YA8QNNX]]: the normal derivative of the single layer potential from inside is $K'\psi + \frac12 \psi$.
For part 1, $K'$ is compact on $C(\partial D)$ and is the adjoint of the double layer operator $K$ with respect to the pairing $\int_{\partial D} \varphi \psi \, ds$.
The null space of $I + 2K$ consists of the constants, since $K1 = -\frac12$ by Gauss's formula for the double layer potential of a constant density.
By the [[Fredholm alternative|4HH8C9V8JQ]], $\psi + 2K'\psi = 2g$ is solvable if and only if $2g$ is orthogonal to the constants.

Example: on the unit disc in $\R^2$, $\frac{\partial \Phi(x - y)}{\partial \nu(x)} = -\frac{1}{4\pi}$ for $x \ne y$ on the unit circle, so $K'\psi = -\frac{1}{4\pi} \int \psi \, ds$.
For $g(\theta) = \cos\theta$ the equation $\psi + 2K'\psi = 2g$ has the solution $\psi = 2\cos\theta$, since $\int_0^{2\pi} \cos\theta \, d\theta = 0$; the resulting single layer potential is $u(x) = x_1$ in the disc, whose normal derivative on the circle is $\cos\theta$.
For $g = 1$ the condition $\int g \, ds = 0$ fails, and indeed no harmonic $u$ in $D$ has $\partial_\nu u = 1$, because $\int_{\partial D} \partial_\nu u \, ds = \int_D \Delta u \, dx = 0$.

## Explanations

### L1 human

Here the flux of a harmonic function through the boundary is prescribed instead of its values.
Since nothing is created inside the region, the total flux must be zero, and that is the only obstruction.
One looks for the solution as the potential of a layer of charges on the boundary, whose density solves an integral equation on the boundary.

### L2 human

This is the companion of the [[boundary integral equation for the Dirichlet problem|ZYDVFT6JR7]], which uses the double layer potential.
The two boundary operators $K$ and $K'$ are adjoint to each other, and the solvability condition comes from the Fredholm alternative applied to this pair.
The same equations, with the signs changed, treat the exterior problems.
Numerically, both equations are discretized by boundary element or Nyström methods, which reduce the dimension of the problem by one.
