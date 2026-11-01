---
tag: 6XM4CCVTKE
kind: concept
name: Normal closure
msc: [12F05, 12F10]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_extension
---

## Summary

The normal closure of an algebraic extension $L/K$ is the smallest extension of $L$ that is [[normal|08S0NW8SES]] over $K$.
It is obtained by adjoining to $L$ all the roots of the [[minimal polynomials|0VX9EP2GS8]] over $K$ of the elements of $L$.
It exists and is unique up to an isomorphism over $L$.
When $L/K$ is finite and separable, its normal closure is the smallest [[Galois extension|0QMZAQ6QQ4]] of $K$ containing $L$.
This lets Galois theory study extensions that are not themselves Galois.

## Explanations

### L1 human

Some extensions contain one root of a polynomial but not the others.
The normal closure adds the missing roots, and nothing more.
For example, $\Q(\sqrt[3]{2})$ contains the real cube root of $2$ but not the two complex cube roots.
Adding them gives $\Q(\sqrt[3]{2}, \omega)$ with $\omega = e^{2\pi i/3}$, a field of degree $6$ over $\Q$.
This field is the normal closure of $\Q(\sqrt[3]{2})$ over $\Q$.
