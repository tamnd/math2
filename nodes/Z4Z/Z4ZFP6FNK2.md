---
tag: Z4ZFP6FNK2
kind: statement
role: theorem
name: Whittaker–Shannon interpolation formula
msc: ["94A20", "42A38"]
uses: [P3T104G564, DPVM34ADZV, SASP14MA1Z, HPZHRZ0502, G12KXDHPPS]
about: [P3T104G564]
sources:
  - url: https://en.wikipedia.org/wiki/Whittaker%E2%80%93Shannon_interpolation_formula
same_as:
  wikidata: Q2018853
  wikipedia: Whittaker–Shannon interpolation formula
---

## Statement

Let $B > 0$, and let $f \in L^2(\R)$ be a continuous [[band-limited function|P3T104G564]] with bandwidth $B$, that is, its [[Fourier transform|DPVM34ADZV]] vanishes almost everywhere outside $[-B, B]$.
Let $\operatorname{sinc}(t) = \sin(\pi t)/(\pi t)$ for $t \ne 0$ and $\operatorname{sinc}(0) = 1$.
Then
$$f(x) = \sum_{k \in \Z} f\Big( \frac{k}{2B} \Big)\, \operatorname{sinc}(2Bx - k) \quad \text{for every } x \in \R,$$
where the series converges in [[$L^2(\R)$|SASP14MA1Z]] and uniformly on $\R$.

## Remarks

The proof expands $\hat f$, restricted to $[-B, B]$, in a [[Fourier series|G12KXDHPPS]] of period $2B$.
Writing $\hat f(\xi) = \sum_k c_k e^{-2\pi i k \xi/(2B)}$ on $[-B, B]$, Fourier inversion gives $c_k = \frac{1}{2B} f(\frac{k}{2B})$.
Inverting term by term, the inverse transform of $e^{-2\pi i k \xi/(2B)} \mathbf{1}_{[-B, B]}(\xi)$ is $2B \operatorname{sinc}(2Bx - k)$, which gives the formula.
The functions $\sqrt{2B}\, \operatorname{sinc}(2Bx - k)$, $k \in \Z$, form an orthonormal basis of the band-limited functions of bandwidth $B$, so the series converges in $L^2$, with $\sum_k \abs{f(k/(2B))}^2 = 2B \norm{f}_2^2$ by the [[Plancherel theorem|HPZHRZ0502]].
Uniform convergence follows from the bound $\sup \abs{g} \le \sqrt{2B} \norm{g}_2$ for band-limited $g$ of bandwidth $B$.

Example: for $f = \operatorname{sinc}$, $B = \frac12$, the samples are $f(k) = 0$ for $k \ne 0$ and $f(0) = 1$, and the formula reduces to $f(x) = \operatorname{sinc}(x)$.

The sample spacing $1/(2B)$ cannot be enlarged; if the band is wider than $[-B, B]$, different functions can have the same samples, which is aliasing.

## Explanations

### L1 human

A signal with no frequencies above $B$ can be rebuilt exactly from its values at the times $k/(2B)$.
Each sample is replaced by a sinc pulse centred at its time and scaled by its value, and the pulses are added.
Each pulse is $1$ at its own sample time and $0$ at all the others, so the sum has the right values at the sample points.
The band limit forces it to be right everywhere in between.

### L2 human

This is the explicit form of the sampling theorem.
It is also the expansion of $f$ in an orthonormal basis of the Paley–Wiener space, made of translates of one sinc function.
In practice the slow decay of sinc makes truncation errors large, so oversampling and smoother interpolation kernels are used.
