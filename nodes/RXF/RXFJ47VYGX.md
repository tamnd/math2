---
tag: RXFJ47VYGX
kind: concept
name: Discrete-time Fourier transform
msc: ["42A16", "94A12", "42A38"]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete-time_Fourier_transform
same_as:
  wikidata: Q1440048
  wikipedia: Discrete-time Fourier transform
---

## Summary

The discrete-time Fourier transform turns a sequence $(x_n)_{n \in \Z}$ into a $2\pi$-periodic function $X(\omega) = \sum_n x_n e^{-i \omega n}$ of a continuous frequency $\omega$.
It is the Fourier transform of the group $\Z$, whose dual group is the circle.
Read backwards, it is a [[Fourier series|G12KXDHPPS]]: up to the sign of the index, the sequence consists of the Fourier coefficients of $X$.
It is the basic tool for analysing digital filters and sampled signals.
Sampling the frequency variable at $N$ points leads to the [[discrete Fourier transform|TST0GH66A5]].
See the [[definition|65QTEF1FTN]].

## Explanations

### L1 human

A digital signal is a list of numbers indexed by time steps, going on in both directions.
Its discrete-time Fourier transform says how much of each frequency between $-\pi$ and $\pi$ radians per step it contains.
Frequencies outside this range look the same as frequencies inside it, because time is sampled; this is why the transform is periodic.
For the signal that is $1$ at time $0$ and $0$ elsewhere, the transform is the constant $1$.
