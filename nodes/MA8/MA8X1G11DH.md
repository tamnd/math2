---
tag: MA8X1G11DH
kind: concept
name: Cesàro means of Fourier series
msc: [42A24, 40G05]
specializes: [08R2V9GZF7]
sources:
  - url: https://en.wikipedia.org/wiki/Fej%C3%A9r%27s_theorem
---

## Summary

The Cesàro means of a [[Fourier series|G12KXDHPPS]] are the averages of its first $N$ partial sums.
They equal the convolution of the function with the [[Fejér kernel|DCCA2T9GKH]], a positive [[summability kernel|1QC5206K07]].
For this reason they behave much better than the partial sums: by [[Fejér's theorem|TPJZCSXSVN]] they converge uniformly for every continuous periodic function.
They are the [[Cesàro mean|08R2V9GZF7]] of the sequence of partial sums.

## Explanations

### L1 human

The partial sums of a Fourier series can oscillate and overshoot, and for some continuous functions they do not converge at all.
Averaging the first $N$ partial sums smooths out these oscillations.
In terms of the waves, the average keeps each frequency $k$ with the weight $1 - \abs{k}/N$, so high frequencies are faded out gently instead of being cut off.
For $f(x) = \cos x$ the $N$-th mean is $\frac{N-1}{N} \cos x$, which tends to $\cos x$.
