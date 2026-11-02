---
tag: J58YA8QNNX
kind: statement
role: theorem
name: Jump relations for layer potentials
msc: [31B10, 31A10]
uses: [9T6ZEV4125, EG8Z3FWV9A, BSJ8X2XRN9, 05D5EGMFYV, 8D56GQ4AG8, 4HH8C9V8JQ]
about: [9T6ZEV4125, EG8Z3FWV9A]
sources:
  - url: https://en.wikipedia.org/wiki/Double_layer_potential
---

## Statement

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be a bounded open set whose [[boundary|05D5EGMFYV]] $\partial\Omega$ is a $C^2$ hypersurface.
Let $\sigma$ be surface measure on $\partial\Omega$ and $\nu$ the outward unit normal.
Let $\Phi$ be the [[fundamental solution of the Laplacian|BSJ8X2XRN9]] with $-\Delta\Phi = \delta_0$, and let $\varphi \colon \partial\Omega \to \R$ be continuous.
Let $S\varphi$ be the [[single layer potential|9T6ZEV4125]] and $D\varphi$ the [[double layer potential|EG8Z3FWV9A]] with density $\varphi$.
For $x \in \partial\Omega$ put
$$K\varphi(x) = \int_{\partial\Omega} \frac{\partial \Phi(x - y)}{\partial \nu(y)}\, \varphi(y)\, d\sigma(y), \qquad K'\varphi(x) = \int_{\partial\Omega} \frac{\partial \Phi(x - y)}{\partial \nu(x)}\, \varphi(y)\, d\sigma(y);$$
both integrals converge absolutely.
Then:

1. $S\varphi$ is continuous on $\R^n$.
2. The restriction of $D\varphi$ to $\Omega$ extends continuously to $\overline{\Omega}$, with boundary values $D_-\varphi = K\varphi - \tfrac12 \varphi$ on $\partial\Omega$.
The restriction of $D\varphi$ to $\R^n \setminus \overline{\Omega}$ extends continuously to $\R^n \setminus \Omega$, with boundary values $D_+\varphi = K\varphi + \tfrac12 \varphi$ on $\partial\Omega$.
3. For $x \in \partial\Omega$ the limits
$$\partial_\nu S_\pm\varphi(x) = \lim_{h \to 0^+} \nu(x) \cdot \nabla S\varphi\big(x \pm h\,\nu(x)\big)$$
exist uniformly on $\partial\Omega$, and $\partial_\nu S_\pm \varphi = K'\varphi \mp \tfrac12 \varphi$.

## Remarks

Proof idea: for $\varphi \equiv 1$, the divergence theorem gives Gauss's integral, $D1 = -1$ in $\Omega$, $D1 = 0$ outside $\overline{\Omega}$ and $K1 = -\tfrac12$ on $\partial\Omega$.
For general $\varphi$, write $D\varphi(x) = D\big(\varphi - \varphi(x_0)\big)(x) + \varphi(x_0)\, D1(x)$ for $x$ near $x_0 \in \partial\Omega$.
The first term is continuous across $\partial\Omega$ at $x_0$, because the $C^2$ boundary makes the kernel weakly singular and the density vanishes at $x_0$.
So the whole jump comes from $\varphi(x_0)\, D1$, and the normal derivative of $S\varphi$ is handled in the same way.

The jumps can be read off: $D_+\varphi - D_-\varphi = \varphi$ and $\partial_\nu S_-\varphi - \partial_\nu S_+\varphi = \varphi$.
Example: for the unit ball in $\R^3$ and $\varphi \equiv 1$, $S1 = 1$ inside and $S1 = 1/\abs{x}$ outside.
So $\partial_\nu S_-1 = 0$ and $\partial_\nu S_+1 = -1$ on the sphere, and both equal $K'1 \mp \tfrac12$ with $K'1 = -\tfrac12$.

## Explanations

### L1 human

A layer of charge on a surface gives a potential that is continuous across the surface, but whose slope jumps by the charge density.
A layer of dipoles gives a potential that itself jumps across the surface, by the dipole density.
The jump is split evenly: half of it on each side of the value on the surface.

### L2 human

These formulas are the bridge between the Laplace equation in a domain and integral equations on its boundary.
If one looks for the solution of the [[Dirichlet problem|8D56GQ4AG8]] as $D\varphi$, part 2 turns the boundary condition into the equation $K\varphi - \tfrac12\varphi = f$; this is the boundary integral method.
For the Neumann problem one uses $S\varphi$ and part 3 in the same way.
Because $K$ and $K'$ are compact operators on $C(\partial\Omega)$ and adjoint to each other for the pairing of $L^2(\partial\Omega)$, the [[Fredholm alternative|4HH8C9V8JQ]] then governs solvability.
