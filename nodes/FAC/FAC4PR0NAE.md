---
tag: FAC4PR0NAE
kind: concept
name: Monte Carlo method for radiative transfer
msc: ["80M31", "80A21", 65C05]
specializes: [HWP11G3HTN]
sources:
  - url: https://en.wikipedia.org/wiki/Monte_Carlo_method_for_photon_transport
---

## Summary

The Monte Carlo method for radiative transfer estimates radiative quantities by simulating the random histories of many bundles of photons.
Each bundle is emitted, travels a random distance, and is then absorbed or scattered according to the probabilities that the [[radiative transfer equation|EX9YYRMAJA]] encodes.
Averages over the histories estimate heat fluxes, absorbed powers and intensities, with a statistical error that decreases like $N^{-1/2}$ in the number $N$ of bundles.
It is a [[Monte Carlo method|HWP11G3HTN]] that handles complicated geometry, scattering and spectral properties in [[radiative heat transfer in participating media|FYYQNDT6X2]] with little extra effort.
See the [[definition|SDVM01S0X6]].

## Explanations

### L1 human

Instead of solving an equation for the light in a furnace or a fog, one plays a game of chance many times.
A photon starts somewhere, flies in a random direction, and travels a random distance before it hits a particle.
At the hit it is either swallowed, or bounced off in a new random direction, and the dice decide which.
After following thousands or millions of photons, one counts how many reached each wall or were absorbed in each region.
These counts, divided by the number of photons, approximate the true shares of the radiation.
