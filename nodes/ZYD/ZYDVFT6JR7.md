---
tag: ZYDVFT6JR7
kind: statement
role: theorem
name: Boundary integral equation for the Dirichlet problem
msc: [31B10, 31A10, 45B05]
uses: [EG8Z3FWV9A, BSJ8X2XRN9, 8KJCN49V64, 0DEB0JMN0W]
about: [8D56GQ4AG8, EG8Z3FWV9A]
sources:
  - url: https://en.wikipedia.org/wiki/Double_layer_potential
---

## Statement

Let $m \in \set{2, 3}$, and let $D \subset \R^m$ be a bounded domain whose boundary $\partial D$ is a connected $C^2$ curve or surface with outward unit normal $\nu$.
Let $\Phi$ be the [[fundamental solution of the Laplacian|BSJ8X2XRN9]] with $-\Delta \Phi = \delta_0$, so $\Phi(x) = \frac{1}{2\pi} \ln \frac{1}{\abs{x}}$ for $m = 2$ and $\Phi(x) = \frac{1}{4\pi \abs{x}}$ for $m = 3$.
For a continuous density $\varphi$ on $\partial D$ put
$$(K\varphi)(x) = \int_{\partial D} \frac{\partial \Phi(x - y)}{\partial \nu(y)} \, \varphi(y) \, ds(y), \quad x \in \partial D.$$
Let $f \colon \partial D \to \R$ be continuous.
Then:

1. The [[integral equation of the second kind|8KJCN49V64]] $\varphi - 2K\varphi = -2f$ has exactly one continuous solution $\varphi$ on $\partial D$.
2. For this $\varphi$, the [[double layer potential|EG8Z3FWV9A]] $u(x) = \int_{\partial D} \frac{\partial \Phi(x - y)}{\partial \nu(y)} \varphi(y) \, ds(y)$, $x \in D$, extends continuously to $\overline{D}$, is [[harmonic|0DEB0JMN0W]] in $D$, and equals $f$ on $\partial D$.

So $u$ is the unique solution of the interior [[Dirichlet problem|8D56GQ4AG8]] with boundary values $f$.

## Remarks

Part 2 follows from the [[jump relations for layer potentials|J58YA8QNNX]]: the limit of the double layer potential from inside is $K\varphi - \frac12 \varphi$, and this equals $f$ exactly when $\varphi - 2K\varphi = -2f$.
For part 1, $K$ is a [[compact operator|M2NEP1K5AE]] on $C(\partial D)$ because its kernel is continuous for $m = 2$ and weakly singular for $m = 3$.
By the [[Fredholm alternative|4HH8C9V8JQ]] it suffices to show that $\varphi - 2K\varphi = 0$ forces $\varphi = 0$.
For such $\varphi$ the double layer potential vanishes in $D$ by the maximum principle.
Its normal derivative is continuous across $\partial D$, so it solves an exterior Neumann problem with zero data and vanishes outside as well.
The jump of the potential across $\partial D$ is $\varphi$, so $\varphi = 0$.

Example: on the unit disc in $\R^2$ one has $\frac{\partial \Phi(x - y)}{\partial \nu(y)} = -\frac{1}{4\pi}$ for $x \ne y$ on the unit circle, so $K\varphi = -\frac{1}{4\pi} \int_{\partial D} \varphi \, ds$.
For $f = 1$ the equation becomes $\varphi + \frac{1}{2\pi} \int \varphi \, ds = -2$, whose solution is the constant $\varphi = -1$, and then $u = 1$ in $D$.

The method turns a problem on the domain $D$ into an equation on its boundary, one dimension lower, which is the basis of boundary element methods.

## Explanations

### L1 human

To find a harmonic function inside a region with given boundary values, one can place a layer of dipoles on the boundary and look for its strength.
The strength must satisfy an integral equation on the boundary alone.
This equation of the second kind always has exactly one solution, which proves that the Dirichlet problem is solvable and gives a way to compute the solution.

### L2 human

The theorem is the classical route, going back to the work of Neumann and Fredholm, from potential theory to [[Fredholm theory|242TFD41KZ]].
Its proof uses the jump relations, the compactness of $K$ and the Fredholm alternative, and uniqueness for the exterior Neumann problem.
For the interior Neumann problem one uses a single layer potential instead, see the [[boundary integral equation for the Neumann problem|CN7NP6R1AQ]].
For the exterior Dirichlet problem the corresponding equation $\varphi + 2K\varphi = 2f$ is not always uniquely solvable, and the ansatz has to be modified.
