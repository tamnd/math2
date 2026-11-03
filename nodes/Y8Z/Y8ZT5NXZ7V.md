---
tag: Y8ZT5NXZ7V
kind: concept
name: Positive-real function
msc: [93D10, 94C05, 26C15]
sources:
  - url: https://en.wikipedia.org/wiki/Positive-real_function
same_as:
  wikidata: Q7233208
  wikipedia: Positive-real function
---

## Summary

A positive-real function is a [[rational function|0XDK9CGYKJ]] with real coefficients that has nonnegative real part on the open right half-plane.
These are exactly the impedances of electric networks made of resistors, capacitors, inductors and ideal transformers, a result of network synthesis.
In control, a linear time-invariant system with a minimal realization is [[passive|HW9JJGS944]] exactly when its transfer function is positive real.
This links frequency-domain tests with energy arguments.
The [[Kalman–Yakubovich–Popov lemma|4NJC7AGT5N]] translates positive realness into matrix conditions on a state-space realization.

## Explanations

### L1 human

The impedance of a circuit tells how much it resists a current that oscillates at a given rate.
A circuit that cannot create energy has an impedance whose real part, the part that burns energy, is never negative.
Positive-real functions are the functions with this property, extended to all complex frequencies with positive real part.
For example, the impedance $1/(s + 1)$ of a resistor of $1$ ohm in parallel with a capacitor of $1$ farad is positive real.
