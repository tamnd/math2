---
tag: 0CXTMAY5PX
kind: example
name: Harmonic series
msc: [40A05]
instance_of: [0JWMJSTBSG]
uses: [0JH4MN4K1C, 0NBRP6093V]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)
    locator: Definition and divergence
same_as:
  wikidata: Q464100
  wikipedia: Harmonic series (mathematics)
---

## Example

The harmonic series is the series
$$\sum_{n=1}^{\infty} \frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \cdots.$$
Its terms tend to $0$, but the series is a [[divergent series|0NBRP6093V]].
Its partial sums are the [[harmonic numbers|0D2Y6G4C4S]] $H_N = \sum_{n=1}^{N} 1/n$, and they tend to $+\infty$.

## Remarks

The node [[harmonic series diverges|0E9M24KS9J]] gives a proof.
It shows that the converse of the [[term test|0VVY4H92G2]] is false.
The partial sums grow very slowly, like $\ln N$. The node [[harmonic numbers grow like log n|05S2GSPMGA]] makes this precise.
The name comes from music. The wavelengths of the overtones of a string are $1/2, 1/3, 1/4, \dots$ of the wavelength of the string.

## Explanations

### L1 human

The terms $1, 1/2, 1/3, \dots$ become small, but not fast enough.
You can group them into blocks that each add up to at least $1/2$, so the total grows without bound.
