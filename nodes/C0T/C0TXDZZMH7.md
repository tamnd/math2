---
tag: C0TXDZZMH7
kind: concept
name: Shanks transformation
msc: [65B05, 65B10, 40A25]
specializes: [B1S2XJPGYD]
sources:
  - url: https://en.wikipedia.org/wiki/Shanks_transformation
same_as:
  wikidata: Q3537519
  wikipedia: Shanks transformation
---

## Summary

The Shanks transformation is a nonlinear [[series acceleration|B1S2XJPGYD]] method.
Its first-order form takes three consecutive partial sums and returns the limit they would have if the error were exactly geometric.
This form coincides with [[Aitken's delta-squared process|WF08BMN6Q6]].
Higher orders $e_k$ use $2k + 1$ terms and model the error as a sum of $k$ geometric sequences.
In practice it is computed with [[Wynn's epsilon algorithm|6X0C4HNMAZ]], and applied to the partial sums of a power series it produces [[Padé approximants|1F16G4V64X]].

## Explanations

### L1 human

Many slowly converging series have partial sums that overshoot and undershoot their limit, like a damped oscillation.
The Shanks transformation fits a simple model to a few consecutive partial sums and reads off the limit of the model.
For the Leibniz series $1 - \frac13 + \frac15 - \cdots = \frac{\pi}{4}$, the first three partial sums $1, \frac23, \frac{13}{15}$ already give $\frac{19}{24} \approx 0.792$, close to $\frac{\pi}{4} \approx 0.785$.
Applying the transformation again to the new sequence improves the values further.
