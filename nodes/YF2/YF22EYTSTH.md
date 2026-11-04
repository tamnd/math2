---
tag: YF22EYTSTH
kind: proof
name: Proof of the logarithm of a product
msc: [33B10]
proves: 0K2FNY6DYV
uses: [0044CPHJBV, 0E8HNVBCSP, 0RKW2X63YR]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_logarithm
    locator: Definition and properties
---

## Proof

We apply the exponential function and use that it turns sums into products.

1. Let $x > 0$ and $y > 0$, and let $\ln$ be the [[natural logarithm|0044CPHJBV]]. Then $x y > 0$, so $\ln(x y)$ is defined.
2. By the [[exponential of a sum|0E8HNVBCSP]], $e^{\ln x + \ln y} = e^{\ln x} \, e^{\ln y}$.
3. By the [[inverse relation|0RKW2X63YR]] $e^{\ln t} = t$ for $t > 0$, the right side of step 2 equals $x y$.
4. Apply $\ln$ to both sides of $e^{\ln x + \ln y} = x y$. The inverse relation $\ln(e^s) = s$ for real $s$ gives $\ln x + \ln y = \ln(x y)$.

## Idea

The exponential function turns a sum into a product, and $\ln$ undoes the exponential function. So $\ln$ turns a product into a sum.
