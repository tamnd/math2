---
tag: 2P90CV9QKH
kind: concept
name: Fourier–Mukai transform
msc: [14F08, 18G80]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier%E2%80%93Mukai_transform
same_as:
  wikidata: Q3537566
  wikipedia: Fourier–Mukai transform
---

## Summary

A Fourier–Mukai transform is an exact functor between the [[derived categories of coherent sheaves|2VP2D51KB8]] of two varieties $X$ and $Y$.
It is given by an object on $X \times Y$ called the kernel.
Mukai showed that the Poincaré bundle gives an equivalence between the derived categories of an abelian variety and of its dual.
By a theorem of Orlov, all fully faithful exact functors between such derived categories of smooth projective varieties are of this form.

## Explanations

### L1 human

The classical Fourier transform turns a function $f(x)$ into a function of a new variable by integrating $f(x)$ against a kernel $e^{-2\pi i x y}$.
A Fourier–Mukai transform does the same with sheaves instead of functions: pull back, multiply by a kernel on the product, and push forward, which is the analogue of integration.
Different varieties can have equivalent derived categories, and Fourier–Mukai transforms are the tool that detects and produces such equivalences.
The simplest kernel is the structure sheaf of the diagonal, which gives the identity functor.
