---
tag: SXE93C9RHC
kind: example
name: Spherical model
msc: [82B20, 82B23, 82B26]
instance_of: [PAEME5EQRM]
uses: [GYNMZ9201M, FPYQWE8X12]
sources:
  - url: https://en.wikipedia.org/wiki/Spherical_model
same_as:
  wikidata: Q7576711
  wikipedia: Spherical model
---

## Example

Let $\Lambda$ be a finite box of $\Z^d$ with $N$ sites and periodic boundary conditions, let $J > 0$, $h \in \R$, and let $\beta \ge 0$ be the inverse temperature.
A configuration is a vector $s = (s_x)_{x \in \Lambda}$ of real numbers subject to the single constraint
$$\sum_{x \in \Lambda} s_x^2 = N.$$
Its energy is
$$H(s) = -J \sum_{\set{x, y}} s_x s_y - h \sum_{x \in \Lambda} s_x,$$
where the first sum runs over pairs of nearest neighbours.
The *spherical model* is the probability measure on the sphere of radius $\sqrt{N}$ in $\R^\Lambda$ with density $e^{-\beta H(s)} / Z$ with respect to the surface measure.

## Remarks

Berlin and Kac introduced it in 1952 as a version of the [[Ising model|R0KGM32QN6]] in which the condition $s_x = \pm 1$ at each site is replaced by one global constraint.
The constraint makes the integrals Gaussian up to one Lagrange multiplier, so the free energy in the [[thermodynamic limit|FPYQWE8X12]] can be computed exactly in every dimension.
For $h = 0$ it has a phase transition with spontaneous magnetization when $d \ge 3$ and none when $d \le 2$.
Its critical exponents in $3 \le d < 4$ differ from the mean-field values.
It is the limit $n \to \infty$ of the [[n-vector model|N0VMY0EF9G]].

## Explanations

### L1 human

In the Ising model each spin must be exactly $+1$ or $-1$, which makes the model hard.
The spherical model lets each spin be any real number and asks only that the squares add up to the number of sites.
This small change makes the model solvable by hand, and it still has a real phase transition in three dimensions.
