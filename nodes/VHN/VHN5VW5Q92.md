---
tag: VHN5VW5Q92
kind: concept
name: Fourier transform on locally compact abelian groups
msc: [43A25, 42A38]
sources:
  - url: https://en.wikipedia.org/wiki/Pontryagin_duality
---

## Summary

The Fourier transform on a locally compact abelian group $G$ sends an integrable function $f$ on $G$ to a function $\widehat{f}$ on the dual group.
The value of $\widehat{f}$ at a character is the integral of $f$ against the conjugate of that character.
It unifies Fourier series on the circle, the Fourier transform on $\R^n$ and the discrete Fourier transform on $\Z/n\Z$.
It turns convolution into pointwise multiplication, and with the right normalisation it is unitary on $L^2$.

## Explanations

### L1 human

The Fourier transform measures how much of each wave is present in a function.
On a group, the waves are the characters, and the amount of the wave $\chi$ in $f$ is the average of $f$ times the conjugate of $\chi$.
On the circle this gives the Fourier coefficients $\frac{1}{2\pi}\int_0^{2\pi} f(\theta) e^{-in\theta} \, d\theta$.
On the group $\Z/n\Z$ it gives the discrete Fourier transform used in signal processing.
One definition covers all these cases.
