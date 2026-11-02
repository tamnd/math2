---
tag: 4A5MJY4XPV
kind: statement
role: theorem
name: Fefferman's ball multiplier theorem
msc: [42B15, 28A75]
uses: [RAGR38Q40B, 6PEN7AKC7M]
about: [RAGR38Q40B]
sources:
  - url: https://en.wikipedia.org/wiki/Bochner%E2%80%93Riesz_mean
---

## Statement

Let $n \ge 2$, let $B = \set{\xi \in \R^n : \abs{\xi} \le 1}$ be the closed unit ball, and let $\mathbf{1}_B$ be its indicator function.
Then $\mathbf{1}_B$ is an [[$L^p$ multiplier|RAGR38Q40B]] on $\R^n$ if and only if $p = 2$.

## Remarks

For $p = 2$, the indicator is bounded, so the Plancherel theorem gives the bound.
For $p \ne 2$, Charles Fefferman's 1971 proof uses [[Kakeya sets|6PEN7AKC7M]] of small measure in the plane.
By a lemma of Yves Meyer, a bound for the ball multiplier would give a vector-valued bound for the multipliers of many half-planes with different normal directions.
A Kakeya construction gives many thin rectangles whose union has small area while their translates in the direction of their long sides are disjoint, and this contradicts that vector-valued bound.
By duality, it suffices to disprove the case $p > 2$.

The theorem contrasts with dimension one, where the indicator of an interval is an $L^p$ multiplier for all $1 < p < \infty$, since it is a combination of modulated Hilbert transforms.
It also contrasts with cubes: the indicator of a cube is a product of indicators of intervals, so it is an $L^p$ multiplier for $1 < p < \infty$.

A consequence is that the spherical partial sums $(\mathbf{1}_{RB} \hat f)^\vee$ of the Fourier integral of $f \in L^p(\R^n)$ need not converge to $f$ in $L^p$ when $p \ne 2$ and $n \ge 2$.

## Explanations

### L1 human

Take a function in several variables and keep only its frequencies inside a ball, throwing the rest away.
For the energy norm $L^2$ this is harmless.
The theorem says that for every other $L^p$ norm, this sharp round cut can make functions arbitrarily large compared to what they were.
The curved boundary of the ball is the problem: cutting along a flat face, as with a cube, is fine.

### L2 human

This result explains why one studies the smoothed [[Bochner–Riesz means|AFS2DCWCD3]] instead of sharp spherical partial sums in higher dimensions.
Its proof brought the Kakeya problem into Fourier analysis, a link that runs through the [[restriction conjecture|9CE11G48JY]] as well.
