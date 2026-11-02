---
tag: XWV6VS7BQM
kind: statement
role: theorem
name: Landau's necessary density conditions for sampling
msc: [94A20, 42C15, 30D15]
uses: [P3T104G564, DPVM34ADZV, SASP14MA1Z]
about: [P3T104G564]
sources:
  - url: https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem
---

## Statement

Let $d \ge 1$ and let $S \subset \R^d$ be a compact set of positive measure whose boundary has Lebesgue measure zero.
Let $PW_S$ be the space of [[band-limited functions|P3T104G564]] with spectrum in $S$: the $f \in L^2(\R^d)$ whose [[Fourier transform|DPVM34ADZV]] $\hat f(\xi) = \int f(x) e^{-i x \cdot \xi} \, dx$ vanishes outside $S$.
Let $\Lambda \subset \R^d$ be uniformly discrete, that is, $\inf \set{\abs{\lambda - \lambda'} : \lambda \ne \lambda' \in \Lambda} > 0$.
Define the lower and upper Beurling densities
$$D^-(\Lambda) = \liminf_{r \to \infty} \inf_{x \in \R^d} \frac{\#(\Lambda \cap (x + [0, r]^d))}{r^d}, \qquad D^+(\Lambda) = \limsup_{r \to \infty} \sup_{x \in \R^d} \frac{\#(\Lambda \cap (x + [0, r]^d))}{r^d}.$$

1. If $\Lambda$ is a sampling set for $PW_S$, that is, there are $0 < A \le B$ with $A \norm{f}_2^2 \le \sum_{\lambda \in \Lambda} \abs{f(\lambda)}^2 \le B \norm{f}_2^2$ for all $f \in PW_S$, then $D^-(\Lambda) \ge \abs{S} / (2\pi)^d$.
2. If $\Lambda$ is an interpolation set for $PW_S$, that is, for every square-summable $(a_\lambda)_{\lambda \in \Lambda}$ there is $f \in PW_S$ with $f(\lambda) = a_\lambda$ for all $\lambda$, then $D^+(\Lambda) \le \abs{S} / (2\pi)^d$.

Here $\abs{S}$ is the Lebesgue measure of $S$.

## Remarks

Henry Landau proved these conditions in 1967.
The proof compares the eigenvalues of two concentration operators: the operator that restricts $f \in PW_S$ to a large cube, and its discrete analogue on the samples in that cube.
The number of eigenvalues of the first operator that are not close to $0$ or $1$ is small compared with the volume of the cube.
The main count is $\abs{S} r^d / (2\pi)^d$.

Example: for $d = 1$ and $S = [-\pi, \pi]$, the integers form a sampling and interpolation set, and $D^-(\Z) = D^+(\Z) = 1 = \abs{S}/2\pi$.
This is the critical case of the [[Nyquist–Shannon sampling theorem|BMXDMHRXBG]].
So uniform sampling at the Nyquist rate is optimal, and no irregular scheme can sample stably at a lower average rate.

Since $f(\lambda) = (2\pi)^{-d} \int_S \hat f(\xi) e^{i\lambda \cdot \xi} \, d\xi$, the set $\Lambda$ is a sampling set if and only if the exponentials $e^{i\lambda \cdot \xi}$, $\lambda \in \Lambda$, form a frame of $L^2(S)$.
It is a sampling and interpolation set if and only if they form a [[Riesz basis|ZYDYD7FB1Z]] of $L^2(S)$, and then both parts give $D^-(\Lambda) = D^+(\Lambda) = \abs{S}/(2\pi)^d$.

## Explanations

### L1 human

To record a signal whose frequencies lie in a set $S$, one measures its values at a set of points.
Landau's theorem says that stable recording needs, on average, at least $\abs{S}/(2\pi)^d$ points per unit volume, however cleverly the points are placed.
And one cannot prescribe arbitrary values at more than that many points per unit volume.

### L2 human

The Shannon sampling theorem gives a sufficient condition for one regular lattice.
Landau's theorem gives a necessary condition for every uniformly discrete set, measured by the Beurling densities.
It shows that the Nyquist rate is sharp also for irregular sampling.
It also implies that a Riesz basis of exponentials for $L^2(S)$ must have uniform density exactly $\abs{S}/(2\pi)^d$, which links it with the theory of [[nonharmonic Fourier series|TKNA7PR99K]].
The theorem has analogues for Gabor systems and for other spaces of functions with localized transforms.
