---
tag: ~9ea8a9ef
kind: example
name: The real part of a complex number is not semilinear
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: grad
not_instance_of:
  - target: ~8c967182
    note: Re is additive, but Re(i · 1) = 0 while σ(i) Re(1) = σ(i) ≠ 0 for each automorphism σ of C
uses: [~8c967182, DSQ17TNW1C, 0FTH2E9TAS]
sources:
  - url: https://en.wikipedia.org/wiki/Semilinear_map
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Antilinear_map
    locator: Definitions and characterizations
---

## Example

View $\C$ as a vector space of dimension $1$ over $\C$, and let $f \colon \C \to \C$ be $f(z) = \operatorname{Re} z$.

1. $f$ is additive: $\operatorname{Re}(z + w) = \operatorname{Re} z + \operatorname{Re} w$.
2. Suppose $f$ is $\sigma$-[[semilinear|~8c967182]] for an [[automorphism|DSQ17TNW1C]] $\sigma$ of $\C$.
3. Then $f(i \cdot 1) = \sigma(i)\, f(1) = \sigma(i) \cdot 1 = \sigma(i)$.
4. But $f(i) = \operatorname{Re} i = 0$. So $\sigma(i) = 0$.
5. An automorphism is injective and $\sigma(0) = 0$, so $\sigma(i) \ne 0$. This contradicts step 4.
6. So $f$ is semilinear for no automorphism of $\C$. In particular, it is neither linear nor antilinear.

## Remarks

- $f$ is linear over $\R$: $\operatorname{Re}(rz) = r \operatorname{Re} z$ for real $r$.
- $\operatorname{Re} z = \tfrac12 (z + \bar z)$ is the average of the identity, which is linear, and [[complex conjugation|0FTH2E9TAS]], which is antilinear. So a sum of semilinear maps for different automorphisms need not be semilinear.
- The same argument shows that $\operatorname{Im} z$ is not semilinear: $\operatorname{Im}(1) = 0$ but $\operatorname{Im}(i) = 1$.

## Explanations

### L1 human

Taking the real part respects sums.
But it sends $i$ to $0$ and $1$ to $1$, and no twist of the scalars can turn $1$ into $0$.
So the real part is not semilinear over the complex numbers.

### L2 human

To show that an additive map is not semilinear, find a vector $v$ with $T(v) \ne 0$ and a scalar $\lambda \ne 0$ with $T(\lambda v) = 0$.
Here $v = 1$ and $\lambda = i$ work.
The trap is to think that every real-linear map of complex spaces is linear or antilinear.
