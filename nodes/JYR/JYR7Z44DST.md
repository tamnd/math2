---
tag: JYR7Z44DST
kind: statement
role: theorem
name: Bloch theorem for photonic crystals
msc: [78A48, 35P05, 35Q61]
uses: [2PBQKKP2N5, SM1Z40QVDC, BJVZXPB297, 0NEGN5CRSC, WN9V7WSJKF]
about: [2PBQKKP2N5]
sources:
  - url: https://en.wikipedia.org/wiki/Bloch%27s_theorem
---

## Statement

Let $\varepsilon$ be the permittivity of a three-dimensional [[photonic crystal|2PBQKKP2N5]] with [[lattice|WN9V7WSJKF]] $\Lambda$ of rank $3$.
Let $\Lambda^*$ be its reciprocal lattice, and let $B$ be a fundamental domain of $\R^3 / \Lambda^*$, the Brillouin zone.
Let $M$ be the Maxwell operator $M\mathbf{H} = \nabla \times (\varepsilon^{-1} \nabla \times \mathbf{H})$ acting on divergence-free fields in $L^2(\R^3)^3$.
For $\mathbf{k} \in B$, let $M_{\mathbf{k}}$ be the same operator acting on divergence-free fields of the form $\mathbf{H}(\mathbf{x}) = e^{i\mathbf{k} \cdot \mathbf{x}} \mathbf{u}(\mathbf{x})$ with $\mathbf{u}$ locally square-integrable and $\Lambda$-periodic.
Then:

1. for each $\mathbf{k}$, the spectrum of $M_{\mathbf{k}}$ consists of eigenvalues of finite multiplicity $0 \le \lambda_1(\mathbf{k}) \le \lambda_2(\mathbf{k}) \le \cdots$ tending to infinity, with eigenfunctions of the Bloch form $e^{i\mathbf{k} \cdot \mathbf{x}} \mathbf{u}(\mathbf{x})$;
2. each band function $\lambda_n$ is continuous in $\mathbf{k}$ and extends to a $\Lambda^*$-periodic function on $\R^3$;
3. the spectrum of $M$ is the union of the bands, $\sigma(M) = \bigcup_{n \ge 1} \set{\lambda_n(\mathbf{k}) : \mathbf{k} \in B}$.

The band frequencies are $\omega_n(\mathbf{k}) = c\sqrt{\lambda_n(\mathbf{k})}$.

## Remarks

The proof uses the Floquet–Bloch transform, which decomposes $L^2(\R^3)$ into a direct integral over $\mathbf{k} \in B$ of spaces of $\mathbf{k}$-quasi-periodic functions, and commutes with $M$ because $\varepsilon$ is periodic.
On each fibre the problem lives on a compact torus, and the curl–curl operator restricted to divergence-free fields has compact resolvent, which gives the discrete eigenvalues.
Continuity of the bands follows from the analytic dependence of $M_{\mathbf{k}}$ on $\mathbf{k}$ and the min-max principle.
Example: for a homogeneous medium with $\varepsilon = 1$, the Bloch modes are plane waves and the bands are $\lambda = \abs{\mathbf{k} + \mathbf{G}}^2$ for $\mathbf{G} \in \Lambda^*$, folded into $B$.
Periodicity is essential: without it there is no decomposition into $\mathbf{k}$-fibres, and the spectrum of a random medium need not have band structure.
This is the photonic analogue of [[Floquet theory|BJVZXPB297]] for periodic ordinary differential equations and of Bloch's theorem for electrons in a periodic potential.

## Explanations

### L1 human

In a periodic material, a light wave that keeps its shape looks like a plane wave times a pattern that repeats with the crystal.
For each direction and wavelength of the plane-wave part, only a ladder of frequencies is allowed.
Following each rung as the direction changes traces out the bands, and gaps between bands are frequencies that cannot travel through the crystal.

### L2 human

The theorem reduces a problem on all of space to a family of problems on one unit cell.
This is how band diagrams are computed in practice, by plane-wave expansion or finite elements.
A complete photonic band gap appears when some interval is missed by every band for every $\mathbf{k}$.
Defects in the crystal create localized modes with frequencies in the gap, which is the principle of photonic crystal cavities and waveguides.
The same decomposition applies to Schrödinger operators with periodic potentials in solid state physics.
