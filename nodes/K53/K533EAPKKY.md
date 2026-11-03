---
tag: K533EAPKKY
kind: concept
name: Helgason Fourier transform
msc: ["43A85", "43A90", "22E30"]
specializes: [DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Plancherel_theorem_for_spherical_functions
---

## Summary

The Helgason Fourier transform is the Fourier transform on a Riemannian [[symmetric space|PAA93R4WYD]] $X = G / K$ of noncompact type.
It expands a function on $X$, not only a radial one, in plane waves $e^{(i \lambda + \rho)(A(x, b))}$ indexed by a frequency $\lambda$ and a boundary point $b$.
On radial functions it reduces to the [[spherical transform|E06PG40SVD]].
It satisfies an inversion formula and a Plancherel formula with the density $\abs{c(\lambda)}^{-2}$ of the [[Harish-Chandra c-function|4X2N0BN3M0]].

## Explanations

### L1 human

In $\R^n$ a plane wave $e^{i \xi \cdot x}$ is constant on hyperplanes perpendicular to a direction.
In the hyperbolic plane the analogue of a family of parallel hyperplanes is a family of horocycles, circles tangent to the boundary at one point $b$.
A hyperbolic plane wave is constant on the horocycles through $b$ and oscillates as one moves toward or away from $b$.
The Helgason Fourier transform measures how much of each such wave, for each frequency $\lambda$ and each boundary point $b$, a function contains.
