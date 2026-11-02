---
tag: V7H5Z35CPN
kind: concept
name: Parabolic cylinder function
msc: [33C15, 34M03]
specializes: [6AZ4ZBN1M8]
sources:
  - url: https://en.wikipedia.org/wiki/Parabolic_cylinder_function
same_as:
  wikidata: Q3754582
  wikipedia: Parabolic cylinder function
---

## Summary

Parabolic cylinder functions are solutions of Weber's equation $y'' + \left( \nu + \frac12 - \frac{z^2}{4} \right) y = 0$.
The standard solution $D_\nu(z)$ decays like $z^\nu e^{-z^2/4}$ as $z \to +\infty$.
They arise when the [[Helmholtz equation|MNXKTXJ35G]] or [[Laplace's equation|S8RG6N1PRT]] is solved by [[separation of variables|47NFRVB564]] in parabolic cylindrical coordinates.
For integer $\nu \ge 0$ they reduce to [[Hermite functions|52VS07H6GK]].
They are [[confluent hypergeometric functions|6AZ4ZBN1M8]] in the variable $z^2/2$.

## Explanations

### L1 human

Weber's equation is the Schrödinger equation of the quantum harmonic oscillator, with energy parameter $\nu + \frac12$.
For most values of $\nu$ every solution blows up at $+\infty$ or at $-\infty$.
The function $D_\nu$ is the solution that decays at $+\infty$.
For $\nu = 0$ it is the Gaussian $e^{-z^2/4}$: then $y'' = \left( \frac{z^2}{4} - \frac12 \right) y$, which is exactly the equation with $\nu = 0$.
For $\nu = n$ a nonnegative integer, $D_n$ decays at both ends, and these are the bound states of the oscillator.
