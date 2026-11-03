---
tag: HJJYA2X1ZQ
kind: concept
name: Jarrow–Turnbull model
msc: [91G40, 91G30]
sources:
  - url: https://en.wikipedia.org/wiki/Jarrow%E2%80%93Turnbull_model
same_as:
  wikidata: Q6161129
  wikipedia: Jarrow–Turnbull model
---

## Summary

The Jarrow–Turnbull model is a reduced-form model of credit risk, introduced by Robert Jarrow and Stuart Turnbull in 1995.
Default is not explained by the firm's balance sheet, as in the [[Merton model|TQSRSNWX51]], but arrives as the first jump of a Poisson process.
The intensity of this process is the instantaneous default rate.
The model prices defaultable bonds and credit derivatives with the same tools used for default-free interest rate models.

## Explanations

### L1 human

In the Jarrow–Turnbull model, default comes as a surprise, like the arrival of a random event with a known rate.
If the rate is $\lambda = 2\%$ per year, the chance of surviving one more short moment is always the same, and the chance of surviving $T$ years is $e^{-0.02 T}$.
A risky bond is then worth less than a safe bond because the payment may never come.
For example, with zero recovery, a risky bond paying $1$ in $5$ years is worth $e^{-0.1} \approx 0.905$ times the safe bond.
