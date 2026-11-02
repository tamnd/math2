---
tag: BKM0TQSCD9
kind: concept
name: Multiplier ideal
msc: [14F18, 32U05, 32U25]
specializes: [N3PGYJJQ7W]
sources:
  - url: https://en.wikipedia.org/wiki/Multiplier_ideal
same_as:
  wikidata: Q17099212
  wikipedia: Multiplier ideal
---

## Summary

The multiplier ideal of a [[plurisubharmonic function|FF2P7ER3QT]] $\varphi$ is the sheaf of holomorphic germs $f$ for which $\abs{f}^2 e^{-2\varphi}$ is locally integrable.
It measures the singularities of $\varphi$: the more singular $\varphi$ is, the smaller the ideal.
Nadel proved that it is a [[coherent analytic sheaf|DSJET02WPR]].
The Nadel vanishing theorem, a consequence of [[Hörmander's L2 estimates|TPSH4ETK67]], makes it a basic tool in complex and algebraic geometry.
In algebraic geometry, the multiplier ideal of an ideal sheaf with a rational exponent is defined through a log resolution.
It agrees with the analytic definition.

## Explanations

### L1 human

Take a function $\varphi$ that tends to $-\infty$ at some points, such as $\varphi = c \log\abs{z}$ near $0$ in $\C$.
Then $e^{-2\varphi} = \abs{z}^{-2c}$ blows up at $0$, and may fail to be integrable.
Multiplying by a holomorphic $f$ that vanishes at $0$ can tame the blow-up.
The multiplier ideal is the set of such "multipliers" $f$ that make $\abs{f}^2 e^{-2\varphi}$ integrable.
For $\varphi = c \log\abs{z}$ with $c > 0$, these are the germs that vanish to order at least $\floor{c}$ at $0$.
