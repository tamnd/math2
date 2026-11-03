---
tag: JN6FBJP0P9
kind: definition
name: Spherical collapse model
msc: [85A40, 85A05]
defines: A8YJ7EKMV7
uses: [NFPXPMNTP9]
sources:
  - url: https://en.wikipedia.org/wiki/Structure_formation
---

## Definition

Consider an [[Einstein–de Sitter universe|NFPXPMNTP9]], a flat universe that contains only pressureless matter, with mean density $\bar\rho(t) = 1/(6\pi G t^2)$, where $G$ is the gravitational constant.
The *spherical collapse model* describes a region of mass $M$ by the following assumptions.

1. The region is a sphere of uniform density, larger than the mean (a top hat), and it has no internal pressure.
2. Each spherical shell moves only under the gravity of the mass inside it, and shells do not cross before the final collapse.
3. The sphere has negative total energy, so its radius $R$ follows the cycloid
$$R = A (1 - \cos\theta), \qquad t = B (\theta - \sin\theta), \qquad A^3 = G M B^2,$$
with a parameter $\theta \in [0, 2\pi]$ and constants $A, B > 0$.

## Remarks

The sphere reaches its largest radius (turnaround) at $\theta = \pi$ and collapses to a point at $\theta = 2\pi$.
The density contrast at turnaround is $1 + \delta = 9\pi^2/16 \approx 5.55$.
The overdensity predicted by linear theory at the time of collapse is
$$\delta_c = \frac{3}{20} (12\pi)^{2/3} \approx 1.686 ,$$
independent of $M$.
In practice the collapse stops when the matter virializes.
By the virial theorem the final radius is half of the turnaround radius.
The mean density is then $18\pi^2 \approx 178$ times the background density at the collapse time.

Example: a sphere whose linear overdensity, extrapolated to today, is $2$ has exceeded $\delta_c \approx 1.686$, so the model predicts it has already collapsed.

Non-example: an ellipsoidal overdensity violates clause 1.
Tidal shear makes it collapse first along its shortest axis, and the collapse threshold then depends on its shape and on $M$.
