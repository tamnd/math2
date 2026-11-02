---
tag: 42DDDZHP7F
kind: statement
role: theorem
name: Kahane–Katznelson theorem
msc: [42A20]
uses: [VQQM4Y550T, 0X3WGX95FE, G12KXDHPPS]
about: [G12KXDHPPS, V6Q24CHJG8]
sources:
  - url: https://en.wikipedia.org/wiki/Convergence_of_Fourier_series
---

## Statement

Let $E \subset \R$ be a set of Lebesgue measure zero, that is, a [[null set|VQQM4Y550T]].
Then there is a [[continuous|0X3WGX95FE]] $2\pi$-periodic function $f \colon \R \to \C$ whose [[Fourier series|G12KXDHPPS]] diverges at every point of $E$.

## Remarks

Kahane and Katznelson proved this in 1966.
Together with [[Carleson's theorem|FBH6KG484Z]] it describes the sets of divergence exactly.
A set lies in the divergence set of the Fourier series of some continuous function if and only if it has measure zero.
The proof builds $f$ as a uniformly convergent sum of trigonometric polynomials, using covers of $E$ by intervals of small total length.
For a single point $E = \set{0}$ the result is the classical [[example of du Bois-Reymond|FPDWWD12FE]].
For example, $E$ can be the set of rational multiples of $\pi$, or the Cantor set.
Then some continuous function has a Fourier series diverging at each point of $E$.

## Explanations

### L1 human

Carleson's theorem says that the Fourier series of a continuous function can fail to converge only on a set of total length zero.
This theorem says that every set of length zero really occurs: one can choose a continuous function whose Fourier series fails to converge at each point of that set.
So nothing better than "almost everywhere" can be true.

### L2 human

The result shows that Carleson's theorem is sharp for continuous functions.
It contrasts with smooth or Hölder continuous functions, whose Fourier series converge everywhere by the [[Dini test|F5PHA35M50]].
So the divergence sets of continuous functions are as large as Carleson's theorem allows.
