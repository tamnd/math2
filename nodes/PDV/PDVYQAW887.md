---
tag: PDVYQAW887
kind: concept
name: Fast wavelet transform
msc: [65T60, 42C40]
sources:
  - url: https://en.wikipedia.org/wiki/Fast_wavelet_transform
same_as:
  wikidata: Q338438
  wikipedia: Fast wavelet transform
---

## Summary

The fast wavelet transform is the recursive filter-bank algorithm that computes the [[discrete wavelet transform|P3H4MMC4ZH]] of a signal.
At each level it convolves the current approximation with a low-pass and a high-pass filter and keeps every second output.
For a signal of length $N$ and filters of fixed length, it uses $O(N)$ operations, which is even faster than the fast Fourier transform.
It is also known as Mallat's algorithm, and it rests on the structure of a [[multiresolution analysis|1GHQMBR7DE]].

## Explanations

### L1 human

Start with a list of numbers.
Replace neighbouring pairs by a smoothed value and a difference value, which halves the length of each list.
Keep the differences, and repeat the same step on the smoothed list.
For the Haar wavelet, $(4, 2, 5, 5)$ becomes averages $(6, 10)/\sqrt{2}$ and differences $(2, 0)/\sqrt{2}$, and then the averages are split again.
Each level costs half as much as the one before, so the total work is about twice the cost of the first level.
