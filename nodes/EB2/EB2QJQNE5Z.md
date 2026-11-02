---
tag: EB2QJQNE5Z
kind: concept
name: Influence function
msc: [62F35, 62G35]
sources:
  - url: https://en.wikipedia.org/wiki/Robust_statistics
---

## Summary

The influence function of a statistical functional measures the effect on the functional of adding an infinitesimal amount of contamination at a point $x$.
It is a directional derivative of the functional in the direction of a point mass, a [[Gateaux derivative|EAZF9NJW12]].
A bounded influence function means that no single observation can have a large effect, and the supremum of its absolute value is the gross-error sensitivity.
Under regularity conditions it also gives the asymptotic variance of the estimator, so it links robustness and efficiency.

## Explanations

### L1 human

Imagine a huge data set, and add one more point at position $x$.
The estimate moves a little; the influence function records how much, per unit of added weight, as a function of $x$.
For the mean, the effect grows without limit as $x$ moves away, so a far outlier has a large effect.
For the median, the effect is the same for every point above the median, however far away, so outliers have limited effect.
