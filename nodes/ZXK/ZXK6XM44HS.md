---
tag: ZXK6XM44HS
kind: statement
role: proposition
name: Absolute continuity of the Lebesgue integral
msc: [28A25]
uses: [X7GTF3D98F, DG76G5Z6XW, G2S6H789RG]
about: [X7GTF3D98F]
sources:
  - url: https://en.wikipedia.org/wiki/Absolute_continuity
---

## Statement

Let $(X, \Sigma, \mu)$ be a measure space and let $f$ be a real or complex [[integrable function|X7GTF3D98F]] on $X$.
Then for every $\varepsilon > 0$ there is $\delta > 0$ with the following property.
For every $A \in \Sigma$ with $\mu(A) < \delta$,
$$\int_A \abs{f} \, d\mu < \varepsilon,$$
where the integral is an [[integral of a non-negative function|DG76G5Z6XW]].

## Remarks

Proof idea: let $f_N = \min(\abs{f}, N)$.
By the [[monotone convergence theorem|G2S6H789RG]], $\int (\abs{f} - f_N) \, d\mu \to 0$, so one can fix $N$ with $\int (\abs{f} - f_N) < \varepsilon / 2$.
Then $\int_A \abs{f} \le \varepsilon / 2 + N \mu(A)$, and $\delta = \varepsilon / (2N)$ works.

Example: on $[a, b]$ with Lebesgue measure, the function $F(x) = \int_a^x f(t) \, dt$ is [[absolutely continuous|5NB63N9W3P]].
Indeed, a finite union of disjoint intervals of total length less than $\delta$ has measure less than $\delta$.

Integrability is needed.
For $f(x) = 1/x$ on $(0, 1]$ with Lebesgue measure, the set $(0, \delta / 2)$ has measure less than $\delta$ but $\int_0^{\delta/2} dx / x = \infty$.

## Explanations

### L1 human

An integrable function cannot hide a lot of area on a tiny set.
If the set is small enough, the area of the function over it is as small as one wants.

### L2 human

In the language of measures, $\nu(A) = \int_A \abs{f} \, d\mu$ defines a finite measure that is absolutely continuous with respect to $\mu$, in the $\varepsilon$-$\delta$ sense.
The Radon–Nikodym theorem gives a converse: every finite measure absolutely continuous with respect to a σ-finite measure $\mu$ has this form.
The uniform version of this property, for a whole family of functions, is part of uniform integrability.
