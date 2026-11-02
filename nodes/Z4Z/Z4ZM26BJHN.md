---
tag: Z4ZM26BJHN
kind: definition
name: Abstract Wiener space
msc: [28C20, 60B11, 46G12]
defines: CPA34DVD8J
uses: [HM2HHE3J51, 06GZ956657, 0Z2P41SVDP, 03TM135G0N, 059TJN0NZ1, 3N66TM3TSQ, 05AQE0QR0D, P0DV2TCH1N, G95YDNFXQN, 5Z00K7K1HY]
sources:
  - url: https://en.wikipedia.org/wiki/Abstract_Wiener_space
---

## Definition

Let $H$ be a real separable [[Hilbert space|HM2HHE3J51]] with inner product $\ip{\cdot}{\cdot}$ and norm $\norm{\cdot}_H$.
Let $E$ be a real [[separable|0Z2P41SVDP]] [[Banach space|06GZ956657]] with dual space $E^*$.
Let $i \colon H \to E$ be an injective [[continuous linear map|03TM135G0N]] with dense image.
For $\ell \in E^*$, let $i^* \ell \in H$ be the vector with $\ip{i^* \ell}{h} = \ell(i h)$ for all $h \in H$.
The triple $(i, H, E)$ is an *abstract Wiener space* if there is a Borel [[probability measure|059TJN0NZ1]] $\mu$ on $E$ with the following property.
For every $\ell \in E^*$, the [[pushforward|3N66TM3TSQ]] $\ell_* \mu$ is the centered [[normal distribution|05AQE0QR0D]] with variance $\norm{i^* \ell}_H^2$.

## Remarks

The measure $\mu$ is unique, and it is called the abstract Wiener measure; it is a centered [[Gaussian measure|P0DV2TCH1N]].
Equivalently, the image under $i$ of the canonical Gaussian [[cylinder set measure|G95YDNFXQN]] of $H$ extends to a countably additive measure on $E$.
Conversely, every centered Gaussian measure on a separable Banach space arises in this way, with $H$ its Cameron–Martin space.

Example: let $E = C_0([0, 1])$ be the [[classical Wiener space|5Z00K7K1HY]] with the sup norm.
Let $H$ be the space of absolutely continuous $h \in E$ with $h' \in L^2$, with $\ip{h}{k} = \int_0^1 h' k' \, dt$, and let $i$ be the inclusion.
With $\mu$ the Wiener measure, take $\ell(\omega) = \omega(t)$.
Then $i^* \ell$ is $s \mapsto \min(s, t)$, whose norm squared is $t$, and indeed $\omega(t)$ has law $N(0, t)$.

Non-example: let $E = H$ be infinite-dimensional and $i$ the identity.
For an orthonormal sequence $(e_k)$, the readings $\ip{x}{e_k}$ would be independent standard normal variables under $\mu$.
Then $\sum_k \ip{x}{e_k}^2 = \infty$ almost surely, which is impossible for $x \in H$, so no such $\mu$ exists.

## Explanations

### L1 human

The Hilbert space fixes the shape of the Gaussian, and the Banach space is large enough to carry the actual measure.
Wiener measure on continuous paths is the model case.
