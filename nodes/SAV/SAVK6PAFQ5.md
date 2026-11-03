---
tag: SAVK6PAFQ5
kind: concept
name: Polar code
msc: [94B05, 94A24]
specializes: [E85KREWV60]
sources:
  - url: https://en.wikipedia.org/wiki/Polar_code_(coding_theory)
same_as:
  wikidata: Q7209069
  wikipedia: Polar code (coding theory)
---

## Summary

A polar code is a binary [[linear code|E85KREWV60]] of length $N = 2^n$ built from the $n$-fold [[Kronecker power|0N7ENQRCXN]] of the matrix $\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$.
The transform splits $N$ uses of a channel into $N$ synthetic channels that are nearly perfect or nearly useless, by the [[channel polarization theorem|NXN1BQD97E]].
Information is sent on the good synthetic channels, and the inputs of the bad ones are frozen to known values.
Arıkan introduced polar codes in 2009.
They were the first explicit codes proved to achieve the symmetric capacity of every binary-input memoryless channel with a low-complexity decoder.
They are used in 5G.

## Explanations

### L1 human

Combine two copies of a channel by sending $u_1 + u_2$ on the first and $u_2$ on the second.
Decoding $u_1$ first, without knowing $u_2$, is harder than using one channel; decoding $u_2$ afterwards, knowing $u_1$, is easier.
So one bad and one good channel replace two mediocre ones.
Repeating this step $n$ times makes the channels very bad or very good, and one simply avoids the bad ones.
On the [[binary erasure channel|ESYMTB37YG]] with erasure probability $\varepsilon$, one step gives channels with erasure probabilities $2\varepsilon - \varepsilon^2$ and $\varepsilon^2$.
