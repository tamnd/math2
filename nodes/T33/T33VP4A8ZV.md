---
tag: T33VP4A8ZV
kind: definition
name: Jukes–Cantor model
msc: [92D15, 60J27]
defines: TW55PBYQ3E
uses: [5G0AKZ8SXJ, 8FQFR871KM, 020M04FN1H]
sources:
  - url: https://en.wikipedia.org/wiki/Models_of_DNA_evolution
---

## Definition

Let $\mu > 0$.
The *Jukes–Cantor model* with rate $\mu$ is the [[substitution model|8FQFR871KM]] on $\Sigma = \set{A, C, G, T}$ with rate matrix
$$q_{ij} = \frac{\mu}{4} \text{ for } i \ne j, \qquad q_{ii} = -\frac{3\mu}{4}.$$

## Remarks

Since $Q = \frac{\mu}{4} J - \mu I$, where $J$ is the all-ones $4 \times 4$ matrix and $I$ the identity, the [[matrix exponential|020M04FN1H]] is $P(t) = \frac14 J + e^{-\mu t}\bigl(I - \frac14 J\bigr)$.
So $P_{ii}(t) = \frac14 + \frac34 e^{-\mu t}$ and $P_{ij}(t) = \frac14 - \frac14 e^{-\mu t}$ for $i \ne j$.
The stationary distribution is uniform, and the expected number of substitutions per site in time $t$ is $d = \frac{3}{4}\mu t$.
If $p < 3/4$ is the fraction of sites at which two aligned sequences differ, solving $p = \frac34(1 - e^{-4d/3})$ gives the *Jukes–Cantor distance*
$$d = -\frac34 \ln\Bigl(1 - \frac43 p\Bigr).$$
Example: $p = 0.3$ gives $d = -\frac34 \ln 0.6 \approx 0.383$.
Non-example: the Kimura two-parameter model with different rates for transitions and transversions is not a Jukes–Cantor model, since its off-diagonal rates are not all equal.
