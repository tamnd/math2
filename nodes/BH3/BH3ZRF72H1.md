---
tag: BH3ZRF72H1
kind: concept
name: Lee–Yang zeros
msc: [82B20, 82B26, 30C15]
sources:
  - url: https://en.wikipedia.org/wiki/Lee%E2%80%93Yang_theorem
---

## Summary

The Lee–Yang zeros of a finite spin system are the complex zeros of its partition function in the external field $h$.
Here the partition function is viewed as a polynomial in the variable $z = e^{-2\beta h}$.
For real $h$ the partition function is positive, so these zeros are never on the positive real axis of $z$.
A phase transition appears in the thermodynamic limit where the zeros accumulate on the positive real axis.
For ferromagnetic Ising models the [[Lee–Yang theorem|NYTQ2BY74G]] puts all of them on the unit circle $\abs{z} = 1$.

## Explanations

### L1 human

The partition function of a finite magnet is a polynomial, and a polynomial has complex roots.
These roots cannot sit where the field is real, because there the partition function is a sum of positive terms.
As the magnet grows, the roots can creep closer to the real field values, and a phase transition is where they finally touch.
For two Ising spins with coupling $J$, the two roots lie on the unit circle, at $z = -e^{-2\beta J} \pm i \sqrt{1 - e^{-4\beta J}}$.
