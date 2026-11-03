---
tag: 2SD3GSXTB1
kind: definition
name: Keller's geometrical theory of diffraction
msc: [78A45, 78M35, 78A05]
defines: ES9KPGJAGS
uses: [90F3NWRHVD, RKX9XJ0RVW, AQ5ZKPZ88R, MNXKTXJ35G]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_theory_of_diffraction
---

## Definition

Let $u$ be a time-harmonic field, a solution of the [[Helmholtz equation|MNXKTXJ35G]] $\Delta u + k^2 n^2 u = 0$ outside an obstacle, with large wavenumber $k$.
*Keller's geometrical theory of diffraction* approximates $u$, as $k \to \infty$, by a sum over rays $u \approx \sum_j A_j \, e^{i k L_j}$ built by these rules.

1. The rays are the incident, reflected and refracted rays of [[geometrical optics|90F3NWRHVD]], together with *diffracted rays*. A diffracted ray starts where a ray hits an edge or a vertex, or grazes a smooth surface.
2. Diffracted rays obey a generalised [[Fermat's principle|RKX9XJ0RVW]]: they are paths of stationary [[optical path length|AQ5ZKPZ88R]] among the paths that touch the edge, vertex or surface.
3. Along each ray the phase is $k L_j$, where $L_j$ is the optical path length. The amplitude $A_j$ changes so that energy is conserved in each narrow tube of rays.
4. Where a diffracted ray starts, its amplitude is the incident field times a *diffraction coefficient*. This coefficient comes from the asymptotics of an exactly solvable model problem with the same local geometry.

## Remarks

For an edge, rule 2 gives the law of edge diffraction: the diffracted rays make the same angle with the edge as the incident ray.
So they fill a cone around the edge, the Keller cone.
The model problem for a straight edge is the diffraction of a plane wave by a half-plane or a wedge, and the edge diffraction coefficient is of order $k^{-1/2}$.
The approximation fails where rays focus, at caustics, and on the shadow boundaries of the incident and reflected rays, where the diffraction coefficient becomes infinite.
A situation outside the theory is a scatterer that is small compared with the wavelength, where no ray picture applies and Rayleigh scattering is used instead.

## Explanations

### L1 human

The theory keeps the simple picture of light as rays, but allows extra rays to start at edges and corners.
Each extra ray carries a small amount of light, computed once and for all from a simple model problem.
