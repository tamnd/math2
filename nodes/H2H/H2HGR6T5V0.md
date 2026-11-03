---
tag: H2HGR6T5V0
kind: statement
role: proposition
name: Sackur–Tetrode equation
msc: [82B05, 82D05, 82B30]
uses: [TDGEGWHXCT, FPYQWE8X12, 0KC0F51T6A]
about: [TDGEGWHXCT]
sources:
  - url: https://en.wikipedia.org/wiki/Sackur–Tetrode_equation
same_as:
  wikidata: Q1426583
  wikipedia: Sackur–Tetrode equation
---

## Statement

Consider a classical monatomic ideal gas of $N$ identical particles of mass $m$ in a container of volume $V$ in $\R^3$, with Hamiltonian $H = \sum_{i=1}^N \abs{p_i}^2 / (2m)$.
Let $h > 0$ be the Planck constant and $k_B$ the Boltzmann constant.
Define the [[microcanonical|TDGEGWHXCT]] entropy at energy $U > 0$ by
$$S(U, V, N) = k_B \ln \frac{\abs{\set{H \le U}}}{N! \, h^{3N}},$$
where $\abs{\cdot}$ is the phase-space volume.
In the [[thermodynamic limit|FPYQWE8X12]] $N \to \infty$ with $V/N$ and $U/N$ fixed,
$$\frac{S}{N} = k_B \left[ \ln \left( \frac{V}{N} \left( \frac{4 \pi m U}{3 N h^2} \right)^{3/2} \right) + \frac{5}{2} \right] + o(1).$$

## Remarks

Proof idea: the set $\set{H \le U}$ is $V^N$ times a ball of radius $\sqrt{2 m U}$ in $\R^{3N}$.
Its volume is $V^N (2 \pi m U)^{3N/2} / \Gamma(3N/2 + 1)$, and [[Stirling's formula|0KC0F51T6A]] applied to $\Gamma(3N/2 + 1)$ and $N!$ gives the result.
With $U = \frac{3}{2} N k_B T$ the formula becomes $S = N k_B [\ln (V / (N \lambda^3)) + \frac{5}{2}]$, where $\lambda = h / \sqrt{2 \pi m k_B T}$ is the thermal wavelength.
The factor $1/N!$ is necessary: without it the entropy is not extensive, which is the [[Gibbs paradox|AVZ2R5C45M]].
The formula is reliable only when $V/N \gg \lambda^3$; for low temperatures quantum statistics takes over, and it would give negative entropy.

## Explanations

### L1 human

This is the formula for the entropy of an ideal gas of single atoms, computed from first principles.
It counts the microstates of the gas, treating identical atoms as indistinguishable and measuring phase space in units of Planck's constant.
Its predictions agree with measured entropies of monatomic gases such as argon.

### L2 human

The formula shows that $S$ is extensive: doubling $U$, $V$ and $N$ doubles $S$.
Differentiating gives back the ideal gas laws: $1/T = \partial S / \partial U$ gives $U = \frac{3}{2} N k_B T$, and $p/T = \partial S / \partial V$ gives $pV = N k_B T$.
The appearance of $h$ in a classical formula shows that absolute entropies need quantum mechanics.
