---
tag: YFNRB1JNY3
kind: definition
name: Waveguide
msc: [78A50, 78A40]
defines: EWHJ19ND64
uses: [9BWWD4QK8Y, F768YN0P2V, 5MJQ5J5H8Z, EETVA6QYX4, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Waveguide_(radio_frequency)
---

## Definition

A *waveguide* is a configuration of linear media in $\R^3$ that is invariant under translations along the $z$-axis.
So the [[permittivity|F768YN0P2V]] $\varepsilon(x, y)$ and [[permeability|5MJQ5J5H8Z]] $\mu(x, y)$ do not depend on $z$.
Any perfectly conducting walls are cylinders $\partial\Omega \times \R$ over a curve $\partial\Omega$ in the $(x, y)$-plane.
Let $\omega > 0$ and let $\beta$ be real.
A *guided mode* is a nonzero solution of the source-free [[Maxwell's equations|9BWWD4QK8Y]] of the following form:
$$\mathbf{E}(x, y, z, t) = \mathbf{e}(x, y) \, e^{i(\beta z - \omega t)}, \qquad \mathbf{H}(x, y, z, t) = \mathbf{h}(x, y) \, e^{i(\beta z - \omega t)}.$$
Its transverse profiles $\mathbf{e}$ and $\mathbf{h}$ must be square-integrable over the cross-section, and $\mathbf{E}$ must satisfy $\hat{\mathbf{n}} \times \mathbf{E} = 0$ on the conducting walls.

## Remarks

For a hollow metal guide with cross-section a bounded domain $\Omega$ filled with a homogeneous medium, put $k^2 = \omega^2 \mu \varepsilon$.
Transverse magnetic modes have $E_z = \psi(x, y) e^{i(\beta z - \omega t)}$ with $-\Delta_\perp \psi = k_c^2 \psi$ in $\Omega$ and the [[Dirichlet condition|EETVA6QYX4]] $\psi = 0$ on $\partial\Omega$, where $\Delta_\perp$ is the transverse [[Laplacian|0E0B6RA8K0]].
Transverse electric modes have $H_z = \psi$ with the same equation and the Neumann condition $\partial \psi / \partial n = 0$.
In both cases $\beta^2 = k^2 - k_c^2$.
Example: the rectangle $\Omega = (0, a) \times (0, b)$ gives $k_c^2 = (m\pi/a)^2 + (n\pi/b)^2$; the $\mathrm{TE}_{10}$ mode has $H_z \propto \cos(\pi x / a)$ and propagates when $k > \pi/a$.
Non-example: free space is translation invariant, but a plane wave $e^{i(\beta z - \omega t)}$ has constant transverse profile, which is not square-integrable over the plane, so it is not a guided mode.
