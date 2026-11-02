---
tag: 7KHGQFM8A9
kind: example
name: Dirac comb
msc: ["42A38", "46F12", "94A20"]
instance_of: [AES2T5JPFP]
uses: [0KPHENZ5S7, CG9JEATW3Q, 5PVSQXCTCT, GARGJYSGFG]
sources:
  - url: https://en.wikipedia.org/wiki/Dirac_comb
same_as:
  wikidata: Q385599
  wikipedia: Dirac comb
---

## Example

Let $T > 0$.
The *Dirac comb* of period $T$ is the sum of [[Dirac deltas|0KPHENZ5S7]] at the points $kT$, $k \in \Z$:
$$\operatorname{III}_T(\varphi) = \sum_{k \in \Z} \varphi(kT) \quad \text{for } \varphi \in \mathcal{S}(\R),$$
where $\mathcal{S}(\R)$ is the [[Schwartz space|CG9JEATW3Q]].
It is a [[tempered distribution|AES2T5JPFP]].
Indeed, $\abs{\varphi(kT)} \le (1 + k^2 T^2)^{-1} \sup_x (1 + x^2) \abs{\varphi(x)}$, so
$$\abs{\operatorname{III}_T(\varphi)} \le \Big( \sum_{k \in \Z} \frac{1}{1 + k^2 T^2} \Big) \big( p_{0,0}(\varphi) + p_{2,0}(\varphi) \big),$$
where $p_{a,b}(\varphi) = \sup_x \abs{x^a \varphi^{(b)}(x)}$.
This is a bound by finitely many Schwartz seminorms.

## Remarks

Its [[Fourier transform|5PVSQXCTCT]], with the convention $\hat\varphi(\xi) = \int \varphi(x) e^{-2\pi i x \xi}\, dx$, is again a Dirac comb:
$$\widehat{\operatorname{III}_T} = \frac{1}{T} \operatorname{III}_{1/T}.$$
This identity is a restatement of the [[Poisson summation formula|GARGJYSGFG]] $\sum_k \varphi(kT) = \frac1T \sum_k \hat\varphi(k/T)$, applied to $\hat\varphi$ and using $\hat{\hat\varphi}(x) = \varphi(-x)$.
For $T = 1$ the comb is its own Fourier transform.

Multiplying a function by $\operatorname{III}_T$ models sampling at spacing $T$.
By the identity above, sampling makes the spectrum periodic with period $1/T$, which is the mechanism behind aliasing and the sampling theorem.

## Explanations

### L1 human

The Dirac comb is an infinite row of unit spikes placed at equal distance $T$.
Its spectrum is again a row of spikes, at distance $1/T$.
Spikes close together in time give spikes far apart in frequency, and the reverse.
