---
tag: EZ1HMS875F
kind: statement
role: theorem
name: Nyquist stability criterion
msc: [93D10, 93C80, 30C15]
uses: [Z7SPHAWMDX, RYTSV821V8, 7NYES2D0Z4, 0PN2BXRS8G, 0NQSV2EWDR, 019MA1VTR2]
about: [Z7SPHAWMDX, RYTSV821V8]
sources:
  - url: https://en.wikipedia.org/wiki/Nyquist_stability_criterion
same_as:
  wikidata: Q1756793
  wikipedia: Nyquist stability criterion
---

## Statement

Let $L = n/d$ be the loop transfer function of a single-input single-output unity negative [[feedback|7NYES2D0Z4]] loop.
Here $n$ and $d$ are real polynomials with no common [[root|019MA1VTR2]] and $\deg n \le \deg d$.
Assume that $d$ has no root on the imaginary axis and that $1 + L(s) \ne 0$ for $s$ on the imaginary axis and in the limit $\abs{s} \to \infty$.
Let $P$ be the number of roots of $d$ with positive real part, counted with multiplicity.
Let $Z$ be the number of roots of $d + n$ with positive real part, counted with multiplicity.
Let $N$ be the [[winding number|0NQSV2EWDR]] around $-1$ of the [[Nyquist plot|Z7SPHAWMDX]] $\omega \mapsto L(i\omega)$, $\omega$ running from $-\infty$ to $+\infty$, counted positive for counterclockwise turns.
Then
$$Z = P - N.$$
The poles of the [[closed-loop transfer function|RYTSV821V8]] $L/(1 + L)$ are the roots of $d + n$.
In particular, they all lie in the open left half-plane if and only if $N = P$.

## Remarks

The proof applies the [[argument principle|0PN2BXRS8G]] to $1 + L = (d + n)/d$ along a contour made of the segment $[-iR, iR]$ and the half-circle of radius $R$ in the right half-plane, with $R$ large.
This contour runs clockwise around the right half-plane, so the image of $1 + L$ turns clockwise $Z - P$ times around $0$.
The image of the large half-circle shrinks to the point $1 + L(\infty)$, so only the imaginary axis counts, and turns of $1 + L$ around $0$ are turns of $L$ around $-1$.

Example: for $L(s) = k/(s - 1)$ with $k > 0$, $P = 1$.
The plot $L(i\omega)$ is the circle with diameter $[-k, 0]$, run once counterclockwise, so $N = 1$ when $k > 1$ and $N = 0$ when $k < 1$.
So the loop is stable exactly when $k > 1$, which agrees with the closed-loop pole $1 - k$.

The hypothesis that $n$ and $d$ have no common root is needed: a cancelled unstable root of $d$ is a closed-loop pole that the plot of $L$ cannot see.

## Explanations

### L1 human

To know whether closing a feedback loop gives a stable system, draw the frequency response of the open loop and count how often it goes around the point $-1$.
If the open loop is already stable, the closed loop is stable exactly when the curve does not go around $-1$ at all.
So stability can be read off measured data, without a formula for the system.

### L2 human

The criterion turns the location of the roots of $d + n$ into a count of turns, by the argument principle.
It handles open-loop systems that are unstable, which simple tests on the open loop cannot.
The distance of the Nyquist plot from $-1$ measures robustness and leads to the gain and phase margins.
With imaginary-axis poles of $L$, such as integrators, the imaginary axis is indented around them by small half-circles, and the same count holds.
