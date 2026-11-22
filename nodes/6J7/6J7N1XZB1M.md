---
tag: 6J7N1XZB1M
kind: example
name: The real part of a complex number is not semilinear
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: grad
not_instance_of:
  - target: BNPDDM95KF
    note: Re is additive, but Re(i · 1) = 0 while σ(i) Re(1) = σ(i) ≠ 0 for each automorphism σ of C
uses: [BNPDDM95KF, DSQ17TNW1C, 0FTH2E9TAS]
sources:
  - url: https://en.wikipedia.org/wiki/Semilinear_map
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Antilinear_map
    locator: Definitions and characterizations
---

## Example

The real part respects sums, but it kills $i$ while keeping $1$, and no twist of the scalars can do that.
View $\C$ as a vector space of dimension $1$ over $\C$, and let $f \colon \C \to \C$ be $f(z) = \operatorname{Re} z$.

1. The map $f$ is additive, since $\operatorname{Re}(z + w) = \operatorname{Re} z + \operatorname{Re} w$.
2. Suppose that $f$ is $\sigma$-[[semilinear|BNPDDM95KF]] for an [[automorphism|DSQ17TNW1C]] $\sigma$ of $\C$.
3. Then $f(i \cdot 1) = \sigma(i)\, f(1) = \sigma(i) \cdot 1 = \sigma(i)$.
4. But $f(i) = \operatorname{Re} i = 0$, so $\sigma(i) = 0$.
5. An automorphism is injective with $\sigma(0) = 0$, so $\sigma(i) \ne 0$, which contradicts step 4.
6. So $f$ is semilinear for no automorphism of $\C$, and in particular it is neither linear nor antilinear.

Check: $f(1) = 1$ and $f(i) = 0$, while any semilinear $T$ with $T(1) = 1$ has $T(i) = \sigma(i) \ne 0$.

## Remarks

The map $f$ is linear over $\R$, since $\operatorname{Re}(rz) = r \operatorname{Re} z$ for real $r$.
We have $\operatorname{Re} z = \tfrac12 (z + \bar z)$, the average of the identity, which is linear, and [[complex conjugation|0FTH2E9TAS]], which is antilinear.
So a sum of semilinear maps for different automorphisms need not be semilinear.
If we change $f$ to the imaginary part, the same argument applies, since $\operatorname{Im}(i) = 1$ but $\operatorname{Im}(-i \cdot i) = \operatorname{Im}(1) = 0$.

## Explanations

### L1 human

Taking the real part respects sums.
But it sends $i$ to $0$ and $1$ to $1$, and no twist of the scalars can turn $1$ into $0$.
So the real part is not semilinear over the complex numbers.

### L2 human

To show that an additive map is not semilinear, find a vector $v$ with $T(v) \ne 0$ and a scalar $\lambda \ne 0$ with $T(\lambda v) = 0$.
Here $v = 1$ and $\lambda = i$ work.
Watch out: a real-linear map between complex spaces need not be linear or antilinear.
