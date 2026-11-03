---
tag: 7S3WHBHJTZ
kind: concept
name: Fourier analysis on the Boolean cube
msc: [43A70, "06E30", 42C10]
sources:
  - url: https://en.wikipedia.org/wiki/Analysis_of_Boolean_functions
same_as:
  wikidata: Q48996110
  wikipedia: Analysis of Boolean functions
---

## Summary

Fourier analysis on the Boolean cube studies functions $f \colon \set{-1, 1}^n \to \R$ as combinations of parity functions.
The parity function of a subset $S$ of $\set{1, \dots, n}$ is $\chi_S(x) = \prod_{i \in S} x_i$.
The parity functions are the [[characters|H1WNVN5V7F]] of the group $(\Z/2\Z)^n$, so this is Fourier analysis on a finite abelian group.
The coefficients are given by the [[Walsh–Hadamard transform|K784BA2WHV]].
It is a main tool for [[Boolean functions|0X05GS525E]] in theoretical computer science, social choice, learning theory and hardness of approximation.
Notions such as influence, noise sensitivity and the degree of a function are read off from the Fourier coefficients.

## Explanations

### L1 human

A Boolean function takes $n$ yes-or-no inputs, written as $\pm 1$, and returns a number.
Every such function is a unique polynomial in which each variable appears at most to the first power, because $x_i^2 = 1$.
The coefficients of this polynomial are the Fourier coefficients.
For example, the majority of three votes is $\frac{1}{2}(x_1 + x_2 + x_3) - \frac{1}{2} x_1 x_2 x_3$.
Most of its weight is on the single variables, which reflects that each voter has a real influence on the outcome.
