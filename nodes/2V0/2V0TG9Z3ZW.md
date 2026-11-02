---
tag: 2V0TG9Z3ZW
kind: statement
role: theorem
name: Hankel contour integral for the gamma function
msc: [33B15, 30D10]
uses: [PY6K9AWR33, 02QGGD5G87]
about: [PY6K9AWR33, 0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Reciprocal_gamma_function
---

## Statement

Let $\mathcal{H}$ be a Hankel contour.
It is a path that comes from $-\infty$ below the negative real axis and goes once around $0$ counterclockwise.
Then it returns to $-\infty$ above the negative real axis.
For $t \notin (-\infty, 0]$ let $t^{-z} = e^{-z \operatorname{Log} t}$, with $\operatorname{Log}$ the principal [[complex logarithm|02QGGD5G87]].
On the two sides of the cut, $t^{-z}$ takes its limits from below and from above.
Then for every $z \in \C$,
$$\frac{1}{\Gamma(z)} = \frac{1}{2\pi i} \int_{\mathcal{H}} e^{t} \, t^{-z} \, dt,$$
where $1/\Gamma$ is the [[reciprocal gamma function|PY6K9AWR33]].

## Remarks

The integral converges for every $z$ because $e^t$ decays fast as $\operatorname{Re} t \to -\infty$, and it is an entire function of $z$.
For $\operatorname{Re} z < 1$, the path can be squeezed onto the cut, with $t = s e^{-i\pi}$ on the lower side and $t = s e^{i\pi}$ on the upper side, $s > 0$.
The small circle around $0$ contributes nothing in the limit.
The two sides give $\frac{1}{2\pi i}(e^{i\pi z} - e^{-i\pi z}) \int_0^\infty e^{-s} s^{-z}\, ds = \frac{\sin(\pi z)}{\pi}\,\Gamma(1 - z)$, which equals $1/\Gamma(z)$ by the [[reflection formula|WF7KQAQTS2]].
The identity theorem then extends the formula to all $z \in \C$.
At a positive integer $z = n$ the integrand $e^t t^{-n}$ is single-valued, and the formula reduces to the residue at $0$, which is $1/(n-1)!$.

## Explanations

### L1 human

Euler's integral defines the gamma function only for arguments with positive real part.
Hankel's idea is to integrate along a loop around the origin instead of along a half-line.
The resulting formula for $1/\Gamma$ works for every complex number at once.

### L2 human

The Hankel integral gives a direct proof that $1/\Gamma$ is entire, without first building the meromorphic continuation of $\Gamma$.
Similar loop integrals represent other functions with branch points, such as the Riemann zeta function, and the same technique gives their continuations.
It is also a starting point for asymptotic estimates of $1/\Gamma$ by the saddle point method.
