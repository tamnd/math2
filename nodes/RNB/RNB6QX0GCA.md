---
tag: RNB6QX0GCA
kind: statement
role: theorem
name: Sokhotski–Plemelj theorem
msc: ["30E25", "30E20", 46F10]
uses: [0V3RDQV3ZX, 0WZTM0EFR6, 0KPHENZ5S7]
about: [0SYR10HD4R]
sources:
  - url: https://en.wikipedia.org/wiki/Sokhotski%E2%80%93Plemelj_theorem
same_as:
  wikidata: Q1543149
  wikipedia: Sokhotski–Plemelj theorem
---

## Statement

Let $a < 0 < b$ and let $f \colon [a, b] \to \C$ be [[Hölder continuous|0WZTM0EFR6]].
Then the two limits below exist, and
$$\lim_{\varepsilon \to 0^+} \int_a^b \frac{f(x)}{x + i\varepsilon} \, dx = -i\pi f(0) + \mathrm{p.v.} \int_a^b \frac{f(x)}{x} \, dx,$$
$$\lim_{\varepsilon \to 0^+} \int_a^b \frac{f(x)}{x - i\varepsilon} \, dx = i\pi f(0) + \mathrm{p.v.} \int_a^b \frac{f(x)}{x} \, dx,$$
where $\mathrm{p.v.}$ denotes the [[Cauchy principal value|0V3RDQV3ZX]].

## Remarks

Proof idea: write $\frac{1}{x \pm i\varepsilon} = \frac{x}{x^2 + \varepsilon^2} \mp i \frac{\varepsilon}{x^2 + \varepsilon^2}$.
The second kernel, divided by $\pi$, is an approximate identity, so its integral against $f$ tends to $\pi f(0)$.
The first kernel, integrated against $f$, tends to the principal value; the Hölder condition makes $(f(x) - f(-x))/x$ integrable near $0$.
In the language of distributions, $\frac{1}{x \pm i0} = \mathrm{p.v.} \frac{1}{x} \mp i\pi \delta$, where $\delta$ is the [[Dirac delta|0KPHENZ5S7]].
Example: take $f = 1$ on $[-1, 1]$ and let $\operatorname{Log}$ be the principal logarithm.
The first integral is $\operatorname{Log}(1 + i\varepsilon) - \operatorname{Log}(-1 + i\varepsilon)$, which tends to $0 - i\pi$, and the principal value is $0$.
There is a version for Cauchy-type integrals over a curve, the Sokhotski–Plemelj formulae, which give the jump of $\frac{1}{2\pi i} \int_C \frac{\varphi(\zeta)}{\zeta - z} \, d\zeta$ across $C$.

## Explanations

### L1 human

The function $1/x$ cannot be integrated across $0$ in the usual sense.
Moving the pole slightly off the real line, to $\mp i\varepsilon$, makes the integral finite.
As the pole moves back, the integral splits into a principal value plus a point contribution $\mp i\pi f(0)$.
The sign of that contribution records from which side the pole approached.

### L2 human

The theorem gives the boundary values of Cauchy integrals, which is the starting point of the theory of singular integral equations and of the Riemann–Hilbert problem.
In physics it appears whenever one adds $i\varepsilon$ to a denominator, as in Green's functions of quantum mechanics and in the [[Kramers–Kronig relations|GFS95PZ5YK]].
It is also the computation that relates the [[Hilbert transform|NSCEBXM7ZM]] to boundary values of holomorphic functions on a half-plane.
