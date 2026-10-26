---
tag: 0Y6TH5PQVS
kind: concept
name: Variation of parameters
aliases: [variation-of-constants]
msc: [34A30]
uses: [0PB7K8M7FG, 0H4KNNCHPY, 0N5NF1RGBP, 0GHWEH6H15]
sources:
  - url: https://en.wikipedia.org/wiki/Variation_of_parameters
    locator: General second-order equation
same_as:
  wikidata: Q1205942
  wikipedia: Variation of parameters
---

## Summary

Variation of parameters is a method to find a particular solution of an inhomogeneous linear equation from a [[fundamental system|0H4KNNCHPY]] of the homogeneous equation.
Let $p, q, f$ be continuous on an open interval $I$. Let $(y_1, y_2)$ be a fundamental system of $y'' + p y' + q y = 0$ on $I$, with [[Wronskian|0N5NF1RGBP]] $W$.
One looks for $y = u_1 y_1 + u_2 y_2$ with the extra condition $u_1' y_1 + u_2' y_2 = 0$. Then the equation $y'' + p y' + q y = f$ becomes $u_1' y_1' + u_2' y_2' = f$.
This linear system gives $u_1' = -y_2 f / W$ and $u_2' = y_1 f / W$, so a particular solution is
$$y_p = -y_1 \int \frac{y_2 f}{W}\, dx + y_2 \int \frac{y_1 f}{W}\, dx.$$

## Remarks

The method works for each continuous right side, unlike the [[method of undetermined coefficients|0XRB469Z32]].
Example: for $y'' + y = \tan x$ on $(-\pi/2, \pi/2)$, with $y_1 = \cos x$, $y_2 = \sin x$ and $W = 1$, one gets $y_p = -\cos x \ln\left(\sec x + \tan x\right)$.
For first-order systems, the same idea gives the [[variation of constants formula|0S1KG0XE40]].

## Explanations

### L1 human

The general solution of the homogeneous equation is $c_1 y_1 + c_2 y_2$ with constants.
The idea is to let the constants vary with $x$.
A smart extra condition makes the equations for $u_1'$ and $u_2'$ simple.
