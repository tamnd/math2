---
tag: VGB11C8TTN
kind: statement
role: theorem
name: Bourgain's dimension bound for harmonic measure
msc: [31B15, 28A78, 31B25]
uses: [CFD7BPM51W, SSNFTHZ6YJ, CM9BDNEA10]
about: [CFD7BPM51W]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_measure
---

## Statement

Let $n \ge 2$.
There is a number $\varepsilon_n > 0$, depending only on $n$, with the following property.
Let $\Omega \subseteq \R^n$ be a bounded domain, let $x \in \Omega$, and let $\omega^x$ be the [[harmonic measure|CFD7BPM51W]] of $\Omega$ at $x$.
Then there is a Borel set $F \subseteq \partial\Omega$ with $\omega^x(\partial\Omega \setminus F) = 0$ and [[Hausdorff dimension|SSNFTHZ6YJ]] at most $n - \varepsilon_n$.

## Remarks

In short, $\dim \omega^x \le n - \varepsilon_n$: harmonic measure never fills a set of full dimension $n$, even when the boundary itself has dimension $n$.
By mutual absolute continuity of harmonic measures, the conclusion does not depend on $x$.
Idea of the proof: a multiscale argument looks at cubes that meet the boundary.
In each such cube, harmonic measure is spread unevenly over the subcubes by a uniform amount.
This loss at each scale accumulates into the dimension drop $\varepsilon_n$.
Example: in the plane one can take $\varepsilon_2 = 1$.
This is the theorem of Jones and Wolff that planar harmonic measure is carried by a set of dimension at most $1$.
For Jordan domains it also follows from [[Makarov's theorem|CM9BDNEA10]].
The value of the best constant $\varepsilon_n$ is unknown for $n \ge 3$.
It cannot be taken equal to $1$ in $\R^3$: Wolff constructed domains in $\R^3$ whose harmonic measure has dimension larger than $2$.
The theorem was proved by J. Bourgain in 1987.

## Explanations

### L1 human

Start a random path in a domain in space and record where it first hits the boundary.
Even if the boundary is so rough that it has full dimension, the hitting points concentrate on a set of strictly smaller dimension.
The drop in dimension is at least a fixed amount that depends only on the dimension of the space.

### L2 human

This is the main general result on the dimension of harmonic measure in higher dimensions.
In the plane the sharp answer is known: dimension at most $1$ for all domains, and exactly $1$ for simply connected ones.
In space, Wolff's examples show that the planar answer $n - 1$ is wrong, and Bourgain's bound is the general upper estimate.
The question of the optimal $\varepsilon_n$ connects potential theory with geometric measure theory and the study of rough boundaries.
