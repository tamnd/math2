---
tag: FZQ7MVMPTN
kind: concept
name: Fourier–Stieltjes transform of a measure
msc: [43A25, 43A10]
sources:
  - url: https://en.wikipedia.org/wiki/Pontryagin_duality
---

## Summary

Let $\mu$ be a finite complex Radon measure on a [[locally compact abelian group|ZR09S9R3AW]] $G$.
Its Fourier–Stieltjes transform is the function $\widehat{\mu}(\chi) = \int_G \overline{\chi(x)}\, d\mu(x)$ on the [[Pontryagin dual|FMW57WNPDB]] $\widehat{G}$.
It extends the [[Fourier transform on locally compact abelian groups|VHN5VW5Q92]] from integrable functions to measures, and it turns convolution of measures into products.
On $\R^n$ it is the classical [[Fourier–Stieltjes transform|5X8PK7H6W3]], and in probability it is the characteristic function of a distribution.
A measure is determined by its transform.

## Explanations

### L1 human

Some objects one wants to analyse by frequency are point masses or other measures rather than functions.
The transform integrates each wave on the group against the measure.
A unit mass at a point $a$ gives the transform $\chi \mapsto \overline{\chi(a)}$, a pure wave in the dual variable.
On the circle, the transform of a measure is its sequence of Fourier coefficients $\int e^{-in\theta}\, d\mu(\theta)$.
