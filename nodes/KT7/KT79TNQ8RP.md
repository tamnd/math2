---
tag: KT79TNQ8RP
kind: definition
name: Fatigue
msc: [74R99, 74A45]
defines: A8X23QRKVF
uses: [HXGCGHS070]
sources:
  - url: https://en.wikipedia.org/wiki/Fatigue_(material)
---

## Definition

Let a specimen of a material be loaded cyclically, so that the [[stress|HXGCGHS070]] at a point oscillates between $\sigma_{\min}$ and $\sigma_{\max}$.
The stress amplitude is $\sigma_a = (\sigma_{\max} - \sigma_{\min})/2$ and the mean stress is $\sigma_m = (\sigma_{\max} + \sigma_{\min})/2$.
*Fatigue* is the progressive and localized damage of the material under such loading, by crack initiation and crack growth.
It leads to fracture after a finite number of cycles, even when $\sigma_{\max}$ is below the static tensile strength.
The *fatigue life* $N_f(\sigma_a, \sigma_m)$ is the number of cycles to failure, and the graph of $N_f$ against $\sigma_a$ at fixed $\sigma_m$ is the *S–N curve*.
The *endurance limit*, when it exists, is the amplitude below which $N_f = \infty$.

## Remarks

Example: in the high-cycle regime many metals follow Basquin's law $\sigma_a = \sigma_f' (2 N_f)^b$, with material constants $\sigma_f' > 0$ and $b < 0$; then halving the stress amplitude multiplies the life by $2^{-1/b}$.
Non-example: failure of a bar under a single load above its tensile strength is static fracture, not fatigue, because no cycling is involved.
Many steels show an endurance limit, while aluminium alloys do not, and their S–N curves keep decreasing.

## Explanations

### L1 human

Fatigue is failure caused by repeating a load many times, each time below the load that would break the part at once.
