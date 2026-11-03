---
tag: FANDMJWCV9
kind: definition
name: Correlation function
msc: [82B05, 82B20, 60G60]
defines: ENWMTRJRND
uses: [DG9F3W6MZM, R0KGM32QN6]
sources:
  - url: https://en.wikipedia.org/wiki/Correlation_function_(statistical_mechanics)
---

## Definition

Let $d \ge 1$, and let $\mu$ be an infinite-volume [[Gibbs measure|DG9F3W6MZM]] for a spin system on $\Z^d$ with bounded real spins $\sigma_x$, $x \in \Z^d$.
Write $\langle \cdot \rangle$ for the expectation under $\mu$.

1. For $x_1, \dots, x_n \in \Z^d$, the $n$-point correlation function is $\langle \sigma_{x_1} \cdots \sigma_{x_n} \rangle$.
2. The truncated, or connected, two-point function is $G(x, y) = \langle \sigma_x \sigma_y \rangle - \langle \sigma_x \rangle \langle \sigma_y \rangle$.
3. If $\mu$ is invariant under translations, $G(x, y)$ depends only on $x - y$ and is written $G(x - y)$.

The correlation length in the direction of the unit vector $e_1$ is $\xi = \big( \lim_{n \to \infty} -\frac{1}{n} \log \abs{G(n e_1)} \big)^{-1}$, when this limit exists.

## Remarks

Example: the one-dimensional [[Ising model|R0KGM32QN6]] with coupling $J > 0$ at zero field has a unique Gibbs measure, with $\langle \sigma_x \rangle = 0$ and $G(n) = \langle \sigma_0 \sigma_n \rangle = (\tanh \beta J)^n$.
Check: write $e^{\beta J \sigma_i \sigma_{i+1}} = \cosh(\beta J) (1 + \sigma_i \sigma_{i+1} \tanh \beta J)$ and expand; only the term containing all the bonds between $0$ and $n$ survives the sum over spins.
So $\xi = -1 / \log \tanh(\beta J)$, which is finite for every $\beta$.

Non-example: in a finite box with boundary conditions, $\langle \sigma_x \sigma_y \rangle$ depends on the position of $x$ and $y$ in the box, not only on $x - y$.
So clause 3 fails there, which is one reason to define $G(x - y)$ in infinite volume.

For a fluid, the corresponding object is the pair correlation of the particle density, encoded by the radial distribution function.
