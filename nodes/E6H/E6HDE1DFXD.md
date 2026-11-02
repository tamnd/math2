---
tag: E6HDE1DFXD
kind: concept
name: Energy of a map between Riemannian manifolds
msc: ["58E20", 53C43]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_map
---

## Summary

The energy of a smooth map between [[Riemannian manifolds|7CBT4SM83Y]] is half the integral, over the domain, of the squared norm of its differential.
It generalizes the Dirichlet energy of a function and the [[energy of a path|Q12AB1MJ64]].
Its critical points are the [[harmonic maps|KZJYG9DS3M]], and its gradient is minus the [[tension field|W8F8S8DX5X]].
It measures how much a map stretches the domain on average.

## Explanations

### L1 human

Picture the domain as a rubber sheet that the map stretches and lays onto the target.
The energy density at a point is the total squared stretching in all directions there, and the energy adds it up over the sheet.
A map that is constant does not stretch at all and has energy $0$.
For example, the map $x \mapsto 2x$ from the interval $[0, 1]$ to the line stretches everything by $2$, so its energy is $\frac{1}{2} \int_0^1 4 \, dx = 2$.
