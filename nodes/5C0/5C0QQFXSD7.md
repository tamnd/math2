---
tag: 5C0QQFXSD7
kind: statement
role: theorem
name: Mermin–Wagner theorem
msc: [82B20, 82B26, 82D40]
uses: [PAEME5EQRM, DG9F3W6MZM, PNFN3A36N4]
about: [N0VMY0EF9G, JPCEWASHGQ]
sources:
  - url: https://en.wikipedia.org/wiki/Mermin%E2%80%93Wagner_theorem
same_as:
  wikidata: Q1547975
  wikipedia: Mermin–Wagner theorem
---

## Statement

Let $d \in \set{1, 2}$ and $N \ge 2$, and let $S^{N-1} \subset \R^N$ be the unit sphere.
Consider the classical [[lattice model|PAEME5EQRM]] on $\Z^d$ with spins $\sigma_x \in S^{N-1}$ and nearest-neighbour coupling $J > 0$.
Add a field $h \ge 0$ along the first unit vector $e_1$, so that the energy on a finite box $\Lambda$ is
$$H_\Lambda(\sigma) = -J \sum_{\set{x, y}} \sigma_x \cdot \sigma_y - h \sum_{x \in \Lambda} \sigma_x \cdot e_1.$$
The first sum runs over the neighbouring pairs in $\Lambda$.
The reference measure at each site is the uniform measure on $S^{N-1}$.
Let $m(\beta, h)$ be the limit of $\langle \sigma_0 \cdot e_1 \rangle$ under the Gibbs distribution on boxes growing to $\Z^d$, at inverse temperature $\beta$.
Then for every $\beta < \infty$, the spontaneous magnetization vanishes:
$$\lim_{h \to 0^+} m(\beta, h) = 0.$$

## Remarks

N. David Mermin and Herbert Wagner proved the theorem in 1966 for the quantum Heisenberg model.
They allowed couplings $J(x)$ of longer range, under the condition $\sum_x \abs{x}^2 \abs{J(x)} < \infty$, and the classical case follows in the same way.
Their proof uses the Bogoliubov inequality to bound the squared magnetization by a constant divided by an integral over wave vectors $k$.
As $h \to 0$ this integral behaves like $\int d^d k / \abs{k}^2$ near $k = 0$, which diverges in $d \le 2$.
In words, long-wavelength spin waves cost little energy in low dimension, and at any positive temperature they destroy long-range order.
The continuous symmetry is necessary: the two-dimensional Ising model, with discrete symmetry, is ordered at low temperature by the [[Peierls argument|PNFN3A36N4]].
The dimension is necessary: in $d \ge 3$ these models have spontaneous magnetization at low temperature, by the infrared bounds of Fröhlich, Simon and Spencer.
Later work showed that in $d = 2$ every infinite-volume [[Gibbs measure|DG9F3W6MZM]] of such models is invariant under rotations of the spins.

## Explanations

### L1 human

Consider magnets whose spins can point in any direction in a plane or in space, rather than just up or down.
In one or two dimensions, any positive temperature makes slow, long waves of spin twisting cheap enough to scramble the direction over large distances.
So such magnets cannot hold a spontaneous magnetization at positive temperature.
The theorem is a rule of thumb across physics: continuous symmetries do not break spontaneously at positive temperature in dimension two or less.

### L2 human

The theorem applies to the [[n-vector models|N0VMY0EF9G]], including the XY and classical Heisenberg models, and its versions cover superfluids and crystals.
It rules out [[spontaneous magnetization|JPCEWASHGQ]] but not every phase transition: the two-dimensional XY model has a Berezinskii–Kosterlitz–Thouless transition, where correlations change from exponential to power-law decay.
Its proof is a good model of how fluctuations at long wavelengths decide whether order survives.
Comparing with the Peierls argument shows the difference between discrete and continuous symmetries.
