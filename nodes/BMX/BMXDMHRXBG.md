---
tag: BMXDMHRXBG
kind: statement
role: theorem
name: Nyquist–Shannon sampling theorem
msc: ["94A20", "42A38"]
uses: [P3T104G564, DPVM34ADZV, SASP14MA1Z, Z4ZFP6FNK2]
about: [P3T104G564]
sources:
  - url: https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem
same_as:
  wikidata: Q679800
  wikipedia: Nyquist–Shannon sampling theorem
---

## Statement

Let $B > 0$.
Let $f, g \in L^2(\R)$ be continuous [[band-limited functions|P3T104G564]] with bandwidth $B$, that is, their [[Fourier transforms|DPVM34ADZV]] vanish almost everywhere outside $[-B, B]$.
If $f(k / (2B)) = g(k / (2B))$ for every $k \in \Z$, then $f = g$.

## Remarks

The difference $h = f - g$ is band-limited and vanishes at all points $k/(2B)$.
On $[-B, B]$, $\hat h$ has the Fourier coefficients $\frac{1}{2B} \int_{-B}^{B} \hat h(\xi) e^{-2\pi i k \xi / (2B)}\, d\xi = \frac{1}{2B} h(-\frac{k}{2B})$ by Fourier inversion, and they are all zero.
So $\hat h = 0$ in [[$L^2$|SASP14MA1Z]], and $h = 0$.
The [[Whittaker–Shannon interpolation formula|Z4ZFP6FNK2]] gives $f$ explicitly from its samples.

The rate $2B$ samples per unit length is called the Nyquist rate.
It cannot be lowered: if the spacing is $h > 1/(2B)$, then $f(x) = \sin(\pi x / h)\, \operatorname{sinc}(2\delta x)^2$ with $\delta = \frac12 (B - \frac{1}{2h}) > 0$ is a nonzero function, band-limited with bandwidth $B$, in $L^2(\R)$, that vanishes at every point $kh$.
Here $\operatorname{sinc}(t) = \sin(\pi t)/(\pi t)$, and $\operatorname{sinc}(2\delta x)^2$ has transform supported in $[-2\delta, 2\delta]$.

The theorem is named after H. Nyquist and C. E. Shannon; E. T. Whittaker and V. A. Kotelnikov found equivalent results.

## Explanations

### L1 human

If a signal has no frequencies above $B$ cycles per second, then sampling it $2B$ times per second loses nothing: the samples determine the signal.
Sampling more slowly can confuse a high frequency with a lower one, which is called aliasing.
This is why audio is sampled at a little more than twice the highest audible frequency.

### L2 human

The proof is a duality between the line and the circle.
The samples of $f$ are the Fourier coefficients of $\hat f$, viewed as a periodic function on an interval of length $2B$.
Equivalently, multiplying $f$ by a Dirac comb of spacing $1/(2B)$ periodizes $\hat f$ with period $2B$, and the copies do not overlap exactly when the band fits.
Landau's density theorem extends the necessity of the Nyquist rate to irregular sampling sets.
