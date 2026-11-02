---
tag: NY6TYHRGMS
kind: concept
name: Complex measure
msc: [28A10]
specializes: [PS28BSAJKJ]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_measure
same_as:
  wikidata: Q1153427
  wikipedia: Complex measure
---

## Summary

A complex measure is a countably additive function from a σ-algebra to the complex numbers.
Its real and imaginary parts are finite [[signed measures|VG2P7R91Z7]].
Complex measures form a Banach space under the total variation norm.
On a locally compact Hausdorff space, the Riesz–Markov–Kakutani theorem identifies the complex Radon measures with the dual of the continuous functions vanishing at infinity.
They are the natural measures for Fourier analysis, where one integrates complex exponentials.

## Explanations

### L1 human

A complex measure assigns a complex number to each measurable set, and adds up correctly over countably many disjoint pieces.
One can think of it as two signed measures side by side, one for the real part and one for the imaginary part.
For example, on $[0, 2\pi]$ the rule $\nu(E) = \int_E e^{i t} \, dt$ is a complex measure, and $\nu([0, 2\pi]) = 0$.
Unlike a signed measure, a complex measure never takes infinite values.
