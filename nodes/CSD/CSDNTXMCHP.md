---
tag: CSDNTXMCHP
kind: concept
name: Cyclotomic fast Fourier transform
sources:
  - wikipedia: en:41435967@r1366536498
    locator: Cyclotomic fast Fourier transform
    note: adopted
    mention: wikipedia://en/41435967
    sections: [Summary]
same_as:
  wikidata: Q17006372
  wikipedia: Cyclotomic fast Fourier transform
inventory: [9WK1HXGBC6]
---

## Summary

The **cyclotomic fast Fourier transform** is a type of fast Fourier transform algorithm over [[finite fields|0ZXZ82FTX2]]. This algorithm first decomposes a discrete Fourier transform into several circular convolutions. This then derives the discrete Fourier transform results from the circular convolution results. When applied to a discrete Fourier transform over $\mathrm{GF}(2^m)$, this algorithm has a very low multiplicative complexity. In practice, since there usually exist efficient algorithms for circular convolutions with specific lengths, this algorithm is very efficient.
