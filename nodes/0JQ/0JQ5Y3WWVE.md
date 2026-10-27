---
tag: 0JQ5Y3WWVE
kind: example
name: Alternating harmonic series
msc: [40A05]
instance_of: [0AF7X08PCR, 0QED0GPYKY]
uses: [0PK8QH1W1V, 0CXTMAY5PX]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_logarithm_of_2
    locator: Series representations
  - url: https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)
    locator: Alternating harmonic series
inventory: [J8295WDSXJ]
---

## Example

The alternating harmonic series is
$$\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots.$$
It converges by the [[alternating series test|0PK8QH1W1V]], since $1/n$ decreases to $0$.
Its sum is $\ln 2 \approx 0.6931$.

## Remarks

The series of absolute values is the [[harmonic series|0CXTMAY5PX]], which diverges. So the convergence is [[conditional|02YRQXZDCS]].
The value $\ln 2$ comes from the [[Mercator series|0YZXNE3HFR]] $\ln(1 + x) = x - x^2/2 + x^3/3 - \cdots$ at $x = 1$, with [[Abel's theorem|0S4EMDQS2F]].
By the [[Riemann rearrangement theorem|0E7VBYGFF7]], a reordering of the terms can give any real sum.

## Explanations

### L1 human

The partial sums are $1, 0.5, 0.833, 0.583, 0.783, \dots$.
They swing around $\ln 2 \approx 0.693$ and close in on it slowly.
