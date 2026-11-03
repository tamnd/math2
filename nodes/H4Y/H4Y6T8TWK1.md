---
tag: H4Y6T8TWK1
kind: definition
name: Receiver function
msc: [86A15, 86A22, 94A12]
defines: XBTEF7WPY6
uses: [BWBB42GNEH, DPVM34ADZV, JAFNCJNF6E]
sources:
  - url: https://en.wikipedia.org/wiki/Receiver_function
---

## Definition

Let a teleseismic P wave arrive at a three-component station.
Let $u_Z(t)$ and $u_R(t)$ be the vertical and radial components, the radial direction pointing from the source to the station.
Let $U_Z(\omega)$ and $U_R(\omega)$ be their [[Fourier transforms|DPVM34ADZV]].
The *radial receiver function* is the time series $h_R$ with
$$H_R(\omega) = \frac{U_R(\omega)}{U_Z(\omega)},$$
that is, the [[deconvolution|BWBB42GNEH]] of $u_Z$ from $u_R$.
In practice the quotient is stabilised, for example by the water-level method
$$H_R(\omega) = \frac{U_R(\omega)\, \overline{U_Z(\omega)}}{\max\bigl(\abs{U_Z(\omega)}^2,\ c \max_{\omega'} \abs{U_Z(\omega')}^2\bigr)}\, G(\omega),$$
with a small constant $c > 0$ and a Gaussian low-pass filter $G$.

## Remarks

The vertical component of a steep P wave is close to the source time function convolved with the path response.
So the division removes them and leaves the local converted phases.
Example: take a single layer of thickness $H$ over a half-space, with P speed $\alpha$ and S speed $\beta$ in the layer.
For [[ray parameter|JAFNCJNF6E]] $p$, the P-to-S converted phase arrives after the direct P wave by
$$t_{Ps} = H \Bigl( \sqrt{\beta^{-2} - p^2} - \sqrt{\alpha^{-2} - p^2} \Bigr).$$
With $H = 35$ km, $\alpha = 6.3$ km/s, $\beta = 3.6$ km/s and $p = 0.06$ s/km this gives $t_{Ps} \approx 35 \times (0.2712 - 0.1470) \approx 4.3$ s.
Non-example: the same division for a local earthquake does not give a receiver function in this sense.
The incoming wave is then not a near-plane P wave from below.
Stacking receiver functions of many earthquakes over trial values of $H$ and $\alpha/\beta$ gives estimates of crustal thickness and of the ratio of the speeds.

## Explanations

### L1 human

Dividing the horizontal recording by the vertical one, in the frequency domain, removes what the earthquake and the long path did.
What remains are the echoes and conversions from the layers below the station.
