---
tag: V90RGBV52W
kind: concept
name: Newtonian space
msc: ["46E36", "31E05"]
specializes: [06GZ956657]
sources:
  - url: https://en.wikipedia.org/wiki/Sobolev_space
---

## Summary

The Newtonian space $N^{1,p}(X)$ is a version of the [[Sobolev space|M4CEZ5K9HP]] $W^{1,p}$ for functions on a metric measure space $X$.
It replaces the gradient by an upper gradient, a function that bounds the change of $u$ along every rectifiable curve.
It was introduced by Nageswari Shanmugalingam, and it is a [[Banach space|06GZ956657]] for $1 \le p < \infty$.
It is the basic function space of nonlinear potential theory on metric spaces, where it carries $p$-capacities and [[p-harmonic functions|7BKQT71FYZ]].

## Explanations

### L1 human

In $\R^n$ a Sobolev function is one whose gradient has finite size in an average sense.
A general metric space has no gradient, but one can still measure how fast a function changes along curves.
An upper gradient of $u$ is a function $g$ with this property: along any curve, the change of $u$ between the ends is at most the integral of $g$.
For example, on the real line the function $u(x) = \abs{x}$ has the upper gradient $g = 1$, because $\abs{\abs{b} - \abs{a}} \le \abs{b - a}$.
The Newtonian space collects the functions that, together with some upper gradient, have finite $L^p$ norm.
