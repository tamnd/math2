---
tag: D2DJNYGS0N
kind: concept
name: Gerchberg–Saxton algorithm
msc: [78A46, 65T50]
sources:
  - url: https://en.wikipedia.org/wiki/Gerchberg%E2%80%93Saxton_algorithm
same_as:
  wikidata: Q5550413
  wikipedia: Gerchberg–Saxton algorithm
---

## Summary

The Gerchberg–Saxton algorithm is an iterative method that finds a phase for a wave from its amplitude in two planes.
The two planes are linked by a [[Fourier transform|DPVM34ADZV]].
It goes back and forth between the two planes and in each plane keeps the current phase but replaces the amplitude by the measured one.
R. W. Gerchberg and W. O. Saxton published it in 1972 for electron microscopy.
It is the starting point of many phase retrieval methods and is used to design phase holograms for beam shaping.

## Explanations

### L1 human

A camera can measure how bright light is but not its phase, the position of the wave crests.
Suppose the brightness is known both at a lens and at its focus, which are related by a Fourier transform.
The algorithm guesses a phase, moves to the other plane, corrects the brightness there, moves back, corrects the brightness again, and repeats.
After many rounds the guess usually fits both measurements well.
It is simple and fast, but it can get stuck at a guess that is not the true answer.
