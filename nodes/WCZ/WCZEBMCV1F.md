---
tag: WCZEBMCV1F
kind: concept
name: Affine term structure model
msc: [91G30, 60H10]
sources:
  - url: https://en.wikipedia.org/wiki/Affine_term_structure_model
same_as:
  wikidata: Q4688953
  wikipedia: Affine term structure model
---

## Summary

An affine term structure model is an interest rate model with few state variables.
In it the logarithm of every zero-coupon bond price is an affine function of these variables.
The [[Vasicek|QXHQ57B0R2]] and [[Cox–Ingersoll–Ross|NH54DP03BD]] models are one-factor examples.
The coefficients of the affine function solve ordinary differential equations of Riccati type, so bond prices are easy to compute.
Duffie and Kan gave the general multi-factor theory in 1996.

## Explanations

### L1 human

In an affine model, the whole yield curve is a simple linear function of a few hidden factors.
If the factor is the short rate $r$, the yield of each bond equals a fixed number plus a fixed multiple of $r$.
These two numbers depend only on the maturity.
For example, in the Vasicek model a rise of the short rate by $1\%$ raises the $T$-year yield by $\frac{1 - e^{-aT}}{aT}$ percent, less for long bonds than for short ones.
