---
tag: DWMTKJ07PT
kind: concept
name: Method of separation of variables for heat conduction
msc: [35K05, 35C05, "80A19"]
specializes: [47NFRVB564]
sources:
  - url: https://en.wikipedia.org/wiki/Separation_of_variables
---

## Summary

The method of separation of variables solves linear heat conduction problems on simple domains.
It looks for temperatures that are products of a function of position and a function of time.
For the [[heat equation|VP2HN86VAG]] with homogeneous boundary conditions, the products are eigenfunctions of the spatial problem times decaying exponentials.
The general solution is then a series of such products, fitted to the initial temperature as a [[Fourier series|G12KXDHPPS]].
It is the special case for heat conduction of the general [[separation of variables|47NFRVB564]], and it is the method by which Fourier introduced Fourier series.
See the [[definition|33WFDJAXQ3]].

## Explanations

### L1 human

A hot rod whose ends are kept in ice water cools down.
Some temperature profiles keep their shape as they cool and only shrink in size: these are the sine waves that vanish at both ends.
A sine wave with more humps shrinks faster, because heat has a shorter way to travel between hot and cold spots.
Any initial profile is a sum of such sine waves, so its cooling is the sum of the separate cooling of each wave.
For a rod of length $\pi$ and diffusivity $1$, the profile $\sin x$ becomes $e^{-t} \sin x$, and $\sin 2x$ becomes $e^{-4t} \sin 2x$.
