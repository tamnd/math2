---
tag: V6Q24CHJG8
kind: concept
name: Convergence of Fourier series
msc: [42A20, 42A24]
sources:
  - url: https://en.wikipedia.org/wiki/Convergence_of_Fourier_series
same_as:
  wikidata: Q5166386
  wikipedia: Convergence of Fourier series
---

## Summary

Let $S_N f$ be the partial sums of the [[Fourier series|G12KXDHPPS]] of a periodic function $f$.
The convergence of Fourier series is the question whether, and in which sense, $S_N f$ tends to $f$.
The answer depends on the mode of convergence: at a point, uniformly, almost everywhere, or in the norm of $L^p$.
Smoothness or bounded variation of $f$ gives pointwise convergence, while mere continuity does not.
In $L^2$ the partial sums always converge, and by Carleson's theorem they also converge almost everywhere for $f \in L^2$.

## Explanations

### L1 human

Adding more and more waves of the Fourier series should give a better and better picture of the function, but this can fail.
For a smooth function the picture improves everywhere at once.
At a jump the sums settle at the midpoint of the jump and overshoot nearby.
There even exist continuous functions whose Fourier series diverge at some point.
Measured by the average squared error instead of point by point, the picture always improves, for every square integrable function.
