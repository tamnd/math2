---
tag: EK3A1GMMFM
kind: statement
role: proposition
name: Christoffel equation for anisotropic waves
msc: [74J05, 74J10, "74E10"]
uses: [T1PYEBKBAJ, SX32X1D537, NMDDYDXT0V, 0VR671PHE5, 0BQAA2BK3Q, EEPJJHC5JZ, GZ7E9GHQYB]
about: [T1PYEBKBAJ, NMDDYDXT0V]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_elasticity
---

## Statement

Let a homogeneous linear elastic medium in $\R^3$ have density $\rho > 0$ and [[elasticity tensor|SX32X1D537]] $C_{ijkl}$ with the symmetries $C_{ijkl} = C_{jikl} = C_{klij}$.
Assume strong ellipticity: $\sum_{i,j,k,l} C_{ijkl} a_i b_j a_k b_l > 0$ for all nonzero $a, b \in \R^3$.
For a unit vector $n$ define the Christoffel matrix $\Gamma(n)$ by $\Gamma_{ik}(n) = \sum_{j,l} C_{ijkl} n_j n_l$.
Let $d \in \R^3$ be nonzero, $c \in \R$, and $F$ a twice differentiable function with $F''$ not identically zero.
Then the plane wave $u(x, t) = d \, F(n \cdot x - c t)$ solves the [[elastodynamic|T1PYEBKBAJ]] equations $\rho \, \partial_t^2 u_i = \sum_{j,k,l} C_{ijkl} \, \partial_j \partial_l u_k$ if and only if
$$\Gamma(n) \, d = \rho c^2 \, d.$$
Moreover $\Gamma(n)$ is a [[symmetric|0VR671PHE5]] positive definite matrix.
So for each direction $n$ there are three real speeds $c > 0$, counted with multiplicity, with mutually orthogonal polarizations $d$.

## Remarks

Substituting the plane wave gives $\rho c^2 d_i F'' = \sum_{j,k,l} C_{ijkl} n_j n_l d_k F''$, which is the Christoffel equation after dividing by $F''$ at a point where it is not zero.
Symmetry of $\Gamma(n)$ follows from $C_{ijkl} = C_{klij}$, and strong ellipticity with $b = n$ gives $d^T \Gamma(n) d > 0$ for $d \ne 0$.
So the squared speeds $\rho c^2$ are the [[eigenvalues|0BQAA2BK3Q]] of $\Gamma(n)$ and the polarizations are its eigenvectors.

Example: for an isotropic medium with Lamé parameters $\lambda$ and $\mu$, $\Gamma(n) = (\lambda + \mu) \, n n^T + \mu I$.
Its eigenvalue $\lambda + 2\mu$ has eigenvector $n$, giving the [[P-wave|EEPJJHC5JZ]], and its double eigenvalue $\mu$ has the plane $n^\perp$ as eigenspace, giving the [[S-waves|GZ7E9GHQYB]].

Without strong ellipticity some eigenvalue of $\Gamma(n)$ can be zero or negative, so some plane waves have no real speed, and the equations are no longer hyperbolic.

## Explanations

### L1 human

In a crystal or in wood, waves travel at different speeds in different directions.
The Christoffel equation computes these speeds.
For each direction one builds a $3 \times 3$ matrix from the elastic constants.
Its eigenvalues are the density times the squares of the three wave speeds.
The eigenvectors tell in which direction the material shakes for each of the three waves.

### L2 human

In an [[anisotropic|NMDDYDXT0V]] medium the three waves for a given direction are called quasi-longitudinal and quasi-shear waves.
The reason is that their polarizations are in general neither exactly along nor exactly across $n$.
Plotting $1/c$ over all directions $n$ gives the slowness surface, which determines refraction at interfaces and the directions in which energy travels.
Measuring the speeds in several directions and inverting the Christoffel equation is a standard way to determine the elastic constants of a crystal.
