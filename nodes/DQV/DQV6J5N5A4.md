---
tag: DQV6J5N5A4
kind: statement
role: theorem
name: Bode's sensitivity integral
msc: [93B35, 93C80, 93D10]
uses: [7J72HJX4T7, 7NYES2D0Z4, 1TE3QF8EYC, 04DXAFN2ES, 05KQ3F99BQ]
about: [7J72HJX4T7]
sources:
  - url: https://en.wikipedia.org/wiki/Bode%27s_sensitivity_integral
same_as:
  wikidata: Q4936423
  wikipedia: Bode's sensitivity integral
---

## Statement

Let $L$ be the loop transfer function of a single-input single-output unity negative [[feedback|7NYES2D0Z4]] loop.
Assume that $L$ is a real rational function with $\lim_{\abs{s} \to \infty} s L(s) = 0$, that is, with relative degree at least $2$.
Assume that the closed loop is stable: the [[sensitivity function|7J72HJX4T7]] $S = 1/(1 + L)$ has no [[pole|1TE3QF8EYC]] with real part $\ge 0$.
Let $p_1, \ldots, p_m$ be the poles of $L$ with positive real part, counted with multiplicity.
Then
$$\int_0^\infty \ln \abs{S(i\omega)} \, d\omega = \pi \sum_{k=1}^{m} \operatorname{Re} p_k.$$
In particular, if $L$ has no pole with positive real part, the integral is $0$.

## Remarks

The zeros of $S$ in the right half-plane are the unstable poles of $L$; the proof first divides them out by Blaschke factors.
It then integrates the logarithm along the boundary of a large half-disc in the right half-plane.
The decay $sL(s) \to 0$ makes the contribution of the large half-circle vanish.

Example: for $L(s) = k/(s + 1)^2$ with $k > 0$, $L$ is stable and has relative degree $2$, and $S$ has poles at $-1 \pm i\sqrt{k}$, so the closed loop is stable.
Where $\ln \abs{S(i\omega)} < 0$, feedback reduces the effect of disturbances; where it is positive, feedback makes it worse.
The theorem says that the area of $\ln \abs{S(i\omega)}$ below the axis equals the area above it.

The relative degree hypothesis is needed.
For $L(s) = k/(s + 1)$, $S(s) = (s + 1)/(s + 1 + k)$ and the integral equals $-\pi k/2$, not $0$; in general, with relative degree $1$, a term $-\frac{\pi}{2} \lim_{s \to \infty} s L(s)$ is added to the right side.

## Explanations

### L1 human

Feedback can make a system ignore disturbances, but only at some frequencies.
The integral says that what is gained at some frequencies must be paid back at others, like pushing in a waterbed.
An unstable plant makes things worse: the total on the side of the cost grows with how unstable the plant is.

### L2 human

The integral is a hard limit on feedback design that holds for every stabilizing controller.
A real loop has limited bandwidth, so the area where $\abs{S} > 1$ is spread over a limited band.
Hence making $\abs{S}$ very small at low frequencies forces a peak of $\abs{S}$ somewhere.
The unstable poles of the plant appear in the right side and raise the cost; unstable zeros give a similar limit through the Poisson integral.
