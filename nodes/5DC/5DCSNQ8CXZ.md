---
tag: 5DCSNQ8CXZ
kind: concept
name: Trust region method
msc: [90C30, 65K05]
sources:
  - url: https://en.wikipedia.org/wiki/Trust_region
same_as:
  wikidata: Q1535924
  wikipedia: Trust region
---

## Summary

A trust region method minimizes a smooth function step by step.
At each step it minimizes a simple model of the function inside a ball around the current point.
The ball is the region where the model is trusted.
After each step the method compares the actual decrease of the function with the decrease predicted by the model.
Then it enlarges or shrinks the ball accordingly.
It is the main alternative to [[line search|B6T5HA74QW]] methods, and it handles Hessians that are not positive definite.

## Explanations

### L1 human

A quadratic model of a function is accurate near the current point but may be poor far away.
So you only believe the model within a certain distance, the trust radius.
You find the best point of the model within that distance and check whether the true function really went down as much as promised.
If it did, you move there and may trust a larger region next time; if not, you stay and shrink the region.
