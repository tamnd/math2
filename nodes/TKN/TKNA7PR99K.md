---
tag: TKNA7PR99K
kind: concept
name: Nonharmonic Fourier series
msc: [42C30, 42A65, 42C15]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz_sequence
---

## Summary

A nonharmonic Fourier series is a series $\sum_n c_n e^{i\lambda_n t}$ on an interval, where the frequencies $\lambda_n$ need not be the integers.
Ordinary [[Fourier series|G12KXDHPPS]] on $[-\pi, \pi]$ are the case $\lambda_n = n$.
The main questions ask when the exponentials $e^{i\lambda_n t}$ are complete in $L^2$ of the interval.
They also ask when they form a [[Riesz basis|ZYDYD7FB1Z]] or a frame.
The answers involve the density of the frequencies and entire functions of exponential type.
They matter in sampling theory and control theory.

## Explanations

### L1 human

An ordinary Fourier series builds a function on $[-\pi, \pi]$ from the waves $e^{int}$, whose frequencies are the whole numbers.
What if the frequencies are slightly moved, say $\lambda_n = n + \delta_n$ with small $\delta_n$?
The waves are then no longer orthogonal, but they may still be able to represent every function in a stable way.
A classical answer is Kadec's theorem: if all real $\delta_n$ satisfy $\abs{\delta_n} \le L < 1/4$, the waves still form a Riesz basis.
