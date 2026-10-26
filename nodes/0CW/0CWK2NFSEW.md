---
tag: 0CWK2NFSEW
kind: concept
name: Improper multiple integral
aliases: [improper-double-integral]
msc: [26B15]
uses: [0WAR4F23B4, 0KTGJW1ZTH]
sources:
  - url: https://en.wikipedia.org/wiki/Improper_integral
    locator: Multivariable improper integrals
  - url: https://en.wikipedia.org/wiki/Improper_integral
    locator: Improper integrals over arbitrary domains
  - url: https://en.wikipedia.org/wiki/Multiple_integral
    locator: Multiple improper integral
---

## Summary

An improper multiple integral extends the Riemann integral to unbounded regions or unbounded functions. It is a limit of integrals over bounded regions where the function is bounded.
For a non-negative function $f$ on $\mathbb{R}^n$ that is Riemann integrable on each cube $[-a, a]^n$, the improper integral is $\int_{\mathbb{R}^n} f = \lim_{a \to \infty} \int_{[-a, a]^n} f$, when this limit exists.

## Remarks

For non-negative functions, the limit does not depend on the choice of the exhausting sequence of bounded sets. For functions of both signs one usually requires that $\int |f|$ is finite.
Example: in polar coordinates, $\iint_{\mathbb{R}^2} e^{-(x^2 + y^2)} \, dA = \lim_{a \to \infty} \int_0^{2\pi} \int_0^a e^{-r^2} r \, dr \, d\theta = \pi$.
Example with a singularity: $\iint_{\|x\| \le 1} \|x\|^{-s} \, dA$ is finite for $s < 2$ and infinite for $s \ge 2$, by the same polar computation.
An improper [[double integral|0WAR4F23B4]] can fail to exist even when both iterated integrals exist, if $\int |f| = \infty$.

## Explanations

### L1 human

The Riemann integral needs a bounded function on a bounded region.
You may want to integrate over all of the plane, or near a point where $f$ blows up. Then integrate over larger and larger bounded pieces and take the limit.
