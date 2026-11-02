---
tag: AA29VBWBFH
kind: concept
name: Littlewood–Paley theory
msc: [42B25, 42A45]
sources:
  - url: https://en.wikipedia.org/wiki/Littlewood%E2%80%93Paley_theory
same_as:
  wikidata: Q6653183
  wikipedia: Littlewood–Paley theory
---

## Summary

Littlewood–Paley theory splits a function on $\R^n$ into pieces whose [[Fourier transforms|DPVM34ADZV]] live in dyadic annuli $\set{2^{j-1} < \abs{\xi} < 2^{j+1}}$, by the [[Littlewood–Paley decomposition|D1PAT0K446]].
Its main result is the [[Littlewood–Paley inequality|6GYQNB2862]].
It says that, for $1 < p < \infty$, the $L^p$ norm of $f$ is comparable to that of its [[square function|H4E1PW67Z1]] $\left( \sum_j \abs{\Delta_j f}^2 \right)^{1/2}$.
So the dyadic pieces behave in $L^p$ almost like orthogonal pieces in $L^2$.
The theory underlies multiplier theorems, the description of function spaces such as Sobolev, Besov and Triebel–Lizorkin spaces, and paraproduct decompositions of products.

## Explanations

### L1 human

Think of a sound signal split into octaves: low notes, then notes one octave higher, then the next octave, and so on.
In $L^2$, the energy of the signal is the sum of the energies of the octaves, by Plancherel's theorem.
Littlewood–Paley theory says that a similar statement survives for the $L^p$ norms with $1 < p < \infty$.
One only has to combine the octaves through a square root of a sum of squares.
For example, changing the signs of the octave pieces in any way only changes the $L^p$ norm by a bounded factor.
