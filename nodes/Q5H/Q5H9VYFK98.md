---
tag: Q5H9VYFK98
kind: concept
name: Method of steepest descent
msc: [41A60, "30E15"]
sources:
  - url: https://en.wikipedia.org/wiki/Method_of_steepest_descent
same_as:
  wikidata: Q1997812
  wikipedia: Method of steepest descent
---

## Summary

The method of steepest descent, also called the saddle point method, finds the asymptotic behaviour of contour integrals $\int_C g(z)\, e^{\lambda f(z)}\,dz$ as the parameter $\lambda$ grows.
One deforms the contour so that it passes through [[saddle points|0JW6MDHAZD]] of the holomorphic function $f$ along paths on which $\operatorname{Im} f$ is constant.
On these paths the integrand does not oscillate, and [[Laplace's method|9G7K8DBT9Y]] gives the leading terms.
It yields the asymptotics of many special functions, such as the Airy and Bessel functions, and of coefficients of generating functions.

## Explanations

### L1 human

Picture $\operatorname{Re} f$ as a landscape over the complex plane, with mountains and valleys.
A holomorphic function has no peaks or pits, only passes, the saddle points.
For large $\lambda$ the integrand is tiny everywhere except where $\operatorname{Re} f$ is largest along the path.
The trick is to walk from one valley to the next over the lowest pass, along the steepest route.
Then the integrand is concentrated at the pass and does not oscillate.
For example, rotating the line of integration of $\int_{\R} e^{i\lambda x^2}\,dx$ by $45$ degrees turns it into a real Gaussian integral and gives $\sqrt{\pi/\lambda}\, e^{i\pi/4}$.
