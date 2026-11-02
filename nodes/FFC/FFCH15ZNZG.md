---
tag: FFCH15ZNZG
kind: problem
name: Fourier restriction problem
msc: [42B10, 42B20]
uses: [DPVM34ADZV, SASP14MA1Z, CG9JEATW3Q]
about: [DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Restriction_conjecture
history:
  posed_by: "Elias Stein"
---

## Problem

Let $n \ge 2$, let $S \subseteq \R^n$ be a compact smooth hypersurface, and let $\sigma$ be its surface measure.
Let $\hat f$ be the [[Fourier transform|DPVM34ADZV]] of $f$.
For which pairs of exponents $1 \le p, q \le \infty$ is there a constant $C$ such that
$$\Big( \int_S \abs{\hat f(\xi)}^q \, d\sigma(\xi) \Big)^{1/q} \le C \norm{f}_{L^p(\R^n)}$$
for every [[Schwartz function|CG9JEATW3Q]] $f$ on $\R^n$?

## Remarks

For $p = 1$ the estimate holds for all $q$, since $\abs{\hat f} \le \norm{f}_{L^1}$ everywhere.
For $p = 2$ it fails for every $q$, since $\hat f$ is then an arbitrary $L^2$ function and has no meaningful values on a set of measure zero.
When $S$ is a piece of a hyperplane, it fails for every $p > 1$.
When $S$ has nonzero Gaussian curvature, the [[Stein–Tomas restriction theorem|ZZVWHNFY6F]] gives the estimate for $q = 2$ and $1 \le p \le 2(n+1)/(n+3)$.
For the sphere, the conjectured answer is the [[restriction conjecture|9CE11G48JY]]; it is known for $n = 2$ and open for $n \ge 3$.

## Explanations

### L1 human

The Fourier transform of a general function is only known up to sets of measure zero, so its values on a surface seem to have no meaning.
The problem asks for which $L^p$ spaces the Fourier transform can nevertheless be restricted to a curved surface, with a bound on the result.
The answer depends on the curvature of the surface and is a central open question of harmonic analysis.
