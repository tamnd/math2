---
tag: SWR6C8DMAR
kind: statement
role: theorem
name: Jeans instability in an expanding universe
msc: [85A40, 85A30, 83F05]
uses: [S1PZ23YAXQ, KCDJ1QXTEQ, PPHFS2P4G4, J70F32P86W, VXMCTGXRW6]
about: [VXMCTGXRW6, S1PZ23YAXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Structure_formation
---

## Statement

Consider a Newtonian, non-relativistic fluid in a homogeneous expanding universe, on scales much smaller than the Hubble radius.
Let $a(t)$ be the [[scale factor|J70F32P86W]], $H = \dot a / a$ the Hubble rate and $\bar\rho(t)$ the mean density.
Let $\delta$ be the density contrast and $c_s$ the adiabatic sound speed.
Let $\delta_k(t)$ be the Fourier amplitude of $\delta$ at comoving wavenumber $k$.
To first order in $\delta$,
$$\ddot\delta_k + 2 H \dot\delta_k = \left( 4 \pi G \bar\rho - \frac{c_s^2 k^2}{a^2} \right) \delta_k.$$
Hence a mode is unstable and grows when its physical wavelength $2\pi a / k$ exceeds the [[Jeans length|KCDJ1QXTEQ]] $\lambda_J = c_s \sqrt{\pi / (G \bar\rho)}$.
Shorter modes oscillate as sound waves with decaying amplitude.
In a universe of pressureless matter only, where the [[Friedmann equations|PPHFS2P4G4]] give $a \propto t^{2/3}$ and $4 \pi G \bar\rho = \tfrac{2}{3} t^{-2}$, the growing and decaying solutions for $c_s = 0$ are
$$\delta_k \propto t^{2/3} \propto a, \qquad \delta_k \propto t^{-1}.$$

## Remarks

The equation comes from linearising the continuity, Euler and Poisson equations in comoving coordinates $x = r / a$ around the expanding homogeneous solution.
The term $2 H \dot\delta_k$, the Hubble friction, is the new feature compared with the static case of the [[Jeans instability|S1PZ23YAXQ]].
For the matter-dominated case, $H = 2 / (3t)$, and trying $\delta_k = t^n$ gives $n(n - 1) + \tfrac{4}{3} n - \tfrac{2}{3} = 0$, whose roots are $n = 2/3$ and $n = -1$.

So the instability in an expanding universe gives power-law growth, not the exponential growth of a static medium.
This slow growth is why the tiny primordial fluctuations needed billions of years to form galaxies.
The hypothesis of sub-horizon scales is needed: on scales larger than the Hubble radius the Newtonian equation does not hold, and a relativistic treatment is required.

## Explanations

### L1 human

In a still gas, a slightly denser region pulls in more matter and its density grows exponentially fast.
In the expanding universe the expansion pulls matter apart and slows this down.
The result is that density differences grow only in proportion to the size of the universe.
So a ripple of one part in a thousand needs the universe to grow about a thousand times to become a real object.

### L2 human

This equation is the starting point of linear [[structure formation|VXMCTGXRW6]].
Its growing solution defines the linear growth factor $D(a)$, which scales the matter power spectrum in time as $D(a)^2$.
With a cosmological constant or with curvature, $H$ and $\bar\rho$ change and growth slows down at late times.
In the radiation era, matter perturbations below the horizon grow only logarithmically, which shapes the turnover of the matter power spectrum.
