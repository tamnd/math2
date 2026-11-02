---
tag: FP37BTP93K
kind: concept
name: Gaussian quadrature
msc: [65D32, 41A55, 33C45]
specializes: [ADSVMCY77A]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_quadrature
same_as:
  wikidata: Q767680
  wikipedia: Gaussian quadrature
---

## Summary

Gaussian quadrature is a [[quadrature rule|ADSVMCY77A]] with $n$ nodes in which both the nodes and the weights are free.
They are chosen to make the rule exact for all polynomials of degree up to $2n - 1$.
This is the highest [[degree of exactness|ZYT1JNT1Y0]] that an $n$-point rule can reach.
The nodes are the zeros of the degree $n$ [[orthogonal polynomial|8TXASARQN1]] for the weight of the integral, and the weights are positive.
For smooth integrands it converges very fast, and it is one of the standard tools of numerical integration.

## Explanations

### L1 human

A simple rule such as the trapezoidal rule fixes the sample points in advance and only chooses the weights.
Gaussian quadrature also lets the sample points move, which doubles the number of free parameters.
With these extra parameters it can integrate polynomials of about twice the degree exactly.
For example, the two-point rule $\int_{-1}^{1} f(x)\,dx \approx f(-1/\sqrt{3}) + f(1/\sqrt{3})$ is exact for every cubic polynomial.
