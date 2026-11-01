---
tag: SFPKB3NC0E
kind: concept
name: Hilbertian field
msc: ["12E25", "12E30"]
sources:
  - url: https://en.wikipedia.org/wiki/Thin_set_(Serre)
---

## Summary

A field is Hilbertian if irreducible polynomials in several variables stay irreducible after suitable values in the field are substituted for all but one variable.
[[Hilbert's irreducibility theorem|N1V3YEYHNP]] says that the field $\Q$ of rational numbers is Hilbertian.
Hilbertian fields are the natural setting for realizing finite groups as [[Galois groups|0XTY86BZKY]] by specialization, an approach to the [[inverse Galois problem|YJS6X8JN7D]].
In characteristic $0$, a field is Hilbertian exactly when its affine line is not a thin set in the sense of Serre.

## Explanations

### L1 human

Take a polynomial such as $X^2 - T$, which cannot be factored as a polynomial in $X$ and $T$.
If you put a number in place of $T$, the result may factor: $X^2 - 4 = (X - 2)(X + 2)$.
Over the rational numbers, most choices, such as $T = 2$ or $T = 3$, keep it irreducible.
A field is Hilbertian if this always happens: for any irreducible polynomial in $X$ and $T$ that involves $X$, some (in fact infinitely many) values of $T$ keep it irreducible.
The real numbers are not Hilbertian, since $X^2 - T^2 - 1$ factors for every real value of $T$.
