---
tag: HK1TJFXNG9
kind: problem
name: Tomographic reconstruction
msc: [44A12, 92C55, 65R32]
uses: [VJNZJ352PC, PCMW7KN5P4, W09B9NZ9B5]
about: [VJNZJ352PC]
sources:
  - url: https://en.wikipedia.org/wiki/Tomographic_reconstruction
same_as:
  wikidata: Q7820109
  wikipedia: Tomographic reconstruction
history:
  posed_by: "Johann Radon"
  first_stated: "1917"
---

## Problem

Let $f$ be an unknown function on $\R^n$, $n \ge 2$, with compact support.
Given the [[Radon transform|VJNZJ352PC]] $R f$, or the X-ray transform of $f$, on a set of lines or hyperplanes, possibly with measurement errors, recover $f$.
In practice the data are values $R f(\theta_j, s_k)$ at finitely many directions $\theta_j$ and offsets $s_k$.
The task is then to compute a good approximation of $f$.

## Remarks

With complete and exact data in $\R^n$, the problem has a unique solution, given by the [[Radon inversion formula|HN93ST5CBT]]; Radon gave the inversion in the plane in 1917.
The problem is an [[inverse problem|PCMW7KN5P4]] that is not [[well-posed|W09B9NZ9B5]] in $L^2$: the inversion contains the filter $\abs{\sigma}^{n-1}$, which amplifies high-frequency noise, so some regularization is needed.
With finitely many directions, uniqueness fails: for any finite set of directions there is a nonzero smooth function with compact support whose projections in these directions all vanish.
The main algorithms are [[filtered back-projection|SJQDDY9FMX]], Fourier reconstruction based on the [[projection-slice theorem|J7VA040MC3]], and iterative algebraic methods such as the Kaczmarz method.
Limited-angle data and interior data lead to harder versions of the problem, with weaker stability.

## Explanations

### L1 human

A CT scanner sends X-rays through a body from many directions and measures how much each ray is weakened.
Tomographic reconstruction is the task of computing a picture of the inside of the body from these measurements.
Mathematically, one must recover a function from its integrals along lines.
It can be done exactly when all lines are known, but real data are finite and noisy, so the methods must balance sharpness against noise.
