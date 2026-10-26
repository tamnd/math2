---
tag: 00C5P9JZBK
kind: object
name: Euler–Mascheroni constant
aliases: [euler-constant]
msc: [11Y60]
uses: [0D2Y6G4C4S, 0044CPHJBV, 05S2GSPMGA]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_constant
    locator: lead section
same_as:
  wikidata: Q273023
  wikipedia: Euler's constant
---

## Description

The Euler–Mascheroni constant is the real number
$$\gamma = \lim_{n \to \infty} \big( H_n - \ln n \big) \approx 0.5772156649,$$
where $H_n = 1 + \frac{1}{2} + \cdots + \frac{1}{n}$ is the $n$-th [[harmonic number|0D2Y6G4C4S]].

## Remarks

The [[limit exists|05S2GSPMGA]], because the sequence $H_n - \ln n$ is decreasing and bounded below by $0$.
Also $\gamma = \int_1^\infty \Big( \frac{1}{\lfloor x \rfloor} - \frac{1}{x} \Big) \, dx$.
It is not known whether $\gamma$ is rational. Mathlib defines it as `Real.eulerMascheroniConstant`.
Leonhard Euler introduced the constant in a paper of 1734. Lorenzo Mascheroni later computed it to more decimal places, with some errors.

## Explanations

### L1 human

The harmonic numbers grow like $\ln n$, and $\gamma$ is the limit of the difference.
So $H_n \approx \ln n + 0.5772$ for large $n$.
