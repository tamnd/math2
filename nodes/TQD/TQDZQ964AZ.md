---
tag: TQDZQ964AZ
kind: concept
name: Lemniscate elliptic functions
msc: ["33E05"]
specializes: [FF9ZPCZ59K]
sources:
  - url: https://en.wikipedia.org/wiki/Lemniscate_elliptic_functions
same_as:
  wikidata: Q6521248
  wikipedia: Lemniscate elliptic functions
---

## Summary

The lemniscate sine $\operatorname{sl}$ and lemniscate cosine $\operatorname{cl}$ are [[elliptic functions|FF9ZPCZ59K]].
They play for the lemniscate of Bernoulli the role that sine and cosine play for the circle.
The lemniscate sine is the inverse of the integral $\int_0^x dt/\sqrt{1 - t^4}$, which measures arc length on the lemniscate.
Their period lattice is the square lattice of Gaussian integers multiplied by $(1 + i)\varpi$, with $\varpi$ the [[lemniscate constant|V5A2S8QYQQ]].
So they have complex multiplication by $i$.
They were studied by Fagnano, Euler and Gauss, and Abel's work on dividing the lemniscate grew out of them.

## Explanations

### L1 human

The lemniscate of Bernoulli is the figure-eight curve $(x^2 + y^2)^2 = x^2 - y^2$.
If you walk along it from the centre, the arc length you have covered when you are at distance $r$ from the centre is $\int_0^r dt/\sqrt{1 - t^4}$.
The lemniscate sine reverses this: given the arc length, it returns the distance from the centre.
This mirrors the circle, where $\arcsin x = \int_0^x dt/\sqrt{1 - t^2}$ and the sine reverses it.
The whole figure-eight has length $2\varpi \approx 5.244$.
