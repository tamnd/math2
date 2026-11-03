---
tag: SM1Z40QVDC
kind: definition
name: Photonic crystal
msc: [78A48, 35Q61, 35P05]
defines: 2PBQKKP2N5
uses: [9BWWD4QK8Y, F768YN0P2V, WN9V7WSJKF, 0NEGN5CRSC]
sources:
  - url: https://en.wikipedia.org/wiki/Photonic_crystal
---

## Definition

Let $\Lambda \subset \R^3$ be the set of integer combinations of $d \in \set{1, 2, 3}$ linearly independent vectors, a [[lattice|WN9V7WSJKF]] in their span.
A *photonic crystal* is a non-magnetic linear medium in $\R^3$ whose relative [[permittivity|F768YN0P2V]] $\varepsilon(\mathbf{x})$ is a real, measurable function that satisfies:

1. $\varepsilon(\mathbf{x} + \mathbf{R}) = \varepsilon(\mathbf{x})$ for all $\mathbf{R} \in \Lambda$ and $\mathbf{x} \in \R^3$;
2. $\varepsilon_{\min} \le \varepsilon(\mathbf{x}) \le \varepsilon_{\max}$ for constants $0 < \varepsilon_{\min} \le \varepsilon_{\max}$;
3. $\varepsilon$ is not constant, and it does not depend on the directions orthogonal to $\Lambda$.

Its time-harmonic modes are the solutions of the source-free [[Maxwell's equations|9BWWD4QK8Y]], which reduce to
$$\nabla \times \left( \frac{1}{\varepsilon(\mathbf{x})} \nabla \times \mathbf{H} \right) = \frac{\omega^2}{c^2} \mathbf{H}, \qquad \nabla \cdot \mathbf{H} = 0.$$
A *photonic band gap* is an open interval $I$ of frequencies $\omega > 0$ such that $\omega^2/c^2$ lies outside the spectrum of this operator for every $\omega \in I$.

## Remarks

The operator on the left is a non-negative [[self-adjoint operator|0NEGN5CRSC]] on square-integrable divergence-free fields, so its spectrum is real and $\omega^2 \ge 0$.
By the [[Bloch theorem for photonic crystals|JYR7Z44DST]], its spectrum is a union of bands $\omega_n(\mathbf{k})$.
Example: a Bragg stack is a one-dimensional photonic crystal.
Its permittivity takes two values $\varepsilon_1 \neq \varepsilon_2$ on alternating layers, with period $a$ along $z$.
For waves along $z$ it has a gap around each frequency at which $a$ is about a multiple of half a wavelength in the medium.
Non-example: a homogeneous medium is invariant under every lattice but fails clause 3; its modes $\omega = c\abs{\mathbf{k}}/\sqrt{\varepsilon}$ fill all frequencies and there is no gap.
