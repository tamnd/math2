---
tag: 0XCYA4YERS
kind: statement
role: theorem
name: Wallis product
msc: [11Y60]
uses: [012RYET5E2, 0XMF00T4XQ]
sources:
  - url: https://en.wikipedia.org/wiki/Wallis_product
    locator: Proof using integration
same_as:
  wikidata: Q1501324
  wikipedia: Wallis product
---

## Statement

The partial products of the following infinite product converge to $\pi/2$:
$$\frac{\pi}{2} = \prod_{n=1}^{\infty} \frac{4 n^2}{4 n^2 - 1} = \frac{2}{1} \cdot \frac{2}{3} \cdot \frac{4}{3} \cdot \frac{4}{5} \cdot \frac{6}{5} \cdot \frac{6}{7} \cdots.$$

## Remarks

Let $I_n = \int_0^{\pi/2} \sin^n x \, dx$. The [[reduction formula|012RYET5E2]] gives $I_{2n}$ and $I_{2n+1}$ as explicit products.
The sequence $I_n$ is decreasing, and $I_{2n+1} / I_{2n} \to 1$ by the [[squeeze theorem|0XMF00T4XQ]]. This ratio is a partial product times $2/\pi$.
Mathlib states it as `Real.tendsto_prod_pi_div_two`.

## History

John Wallis published the product in 1656.

## Explanations

### L1 human

The Wallis product writes $\pi/2$ as an infinite product of simple fractions.
The partial products converge slowly to $\pi/2$.
