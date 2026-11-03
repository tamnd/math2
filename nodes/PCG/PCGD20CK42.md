---
tag: PCGD20CK42
kind: statement
role: fact
name: Weber–Fechner law
msc: ["91E30"]
uses: [04DXAFN2ES, 0NT64JV96A]
sources:
  - url: https://en.wikipedia.org/wiki/Weber–Fechner_law
same_as:
  wikidata: Q835216
  wikipedia: Weber–Fechner law
---

## Statement

Let a stimulus have intensity $S > 0$ in a given sensory modality.
Let $\Delta S(S)$ be the just noticeable difference at $S$: the smallest increase of intensity that is detected with a fixed probability.

1. *Weber's law*: there is a constant $k > 0$, the Weber fraction, such that $\Delta S(S) = k S$ over the range of intensities considered.
2. *Fechner's law*: suppose moreover that the sensation magnitude $p$ is a differentiable function of $S$ with $p = 0$ at the absolute threshold $S_0 > 0$.
   Suppose that each just noticeable difference adds the same amount of sensation, so that $dp = c \, dS / S$ for a constant $c > 0$.
   Then
$$p(S) = c \ln \frac{S}{S_0}.$$

## Remarks

Fechner's law follows from Weber's law by solving the [[differential equation|0NT64JV96A]] $p'(S) = c/S$ with $p(S_0) = 0$; the solution is a [[natural logarithm|04DXAFN2ES]].
Example: with $k = 0.02$, a weight of $100$ grams must grow by about $2$ grams to feel heavier, and a weight of $1000$ grams by about $20$ grams.
Under Fechner's law, each doubling of $S$ adds the same amount $c \ln 2$ to the sensation.
Both laws are empirical approximations, not theorems: Weber's law fails near the absolute threshold and for some modalities.
Stevens's power law $p = a S^b$ is a common alternative to Fechner's law.

## Explanations

### L1 human

We notice changes in proportion, not in absolute amount.
Adding one candle to a room lit by two candles is obvious, but adding one candle to a room lit by a hundred is not.
Fechner turned this observation into the rule that felt intensity grows like the logarithm of physical intensity.
Logarithmic scales such as decibels for sound level fit this pattern.

### L2 human

Ernst Heinrich Weber found the constant-ratio rule in experiments on lifted weights, and Gustav Fechner built psychophysics on it.
The derivation treats the discrete steps of just noticeable differences as a continuum, which is where the logarithm comes from.
[[Signal detection theory|8N1NSEBJPE]] later separated sensitivity from response bias in the measurement of thresholds.
