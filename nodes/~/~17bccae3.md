---
tag: ~17bccae3
kind: concept
name: General solution and particular solution
msc: [34A05]
uses: [~31ca077a, ~4841430a]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinary_differential_equation
    locator: Solutions
---

## Summary

The general solution of an [[ordinary differential equation|~4841430a]] of order $n$ is a family of [[solutions|~31ca077a]] that depends on $n$ arbitrary constants $C_1, \dots, C_n$.
In the usual case, each solution of the equation is a member of the family, with the possible exception of [[singular solutions|~97131c1c]].
A particular solution is one solution of the equation. It is often the member of the general solution for one choice of the constants.

## Remarks

The general solution of $y'' + y = 0$ is $y = C_1 \cos x + C_2 \sin x$. The choice $C_1 = 1$, $C_2 = 0$ gives the particular solution $y = \cos x$.
An [[initial value problem|~40f94cf8]] fixes the constants. For an equation of order $n$, one needs $n$ initial conditions.
For a linear equation, the [[general solution of the inhomogeneous equation|~50b07833]] is one particular solution plus the general solution of the homogeneous equation.

## Explanations

### L1 human

The general solution is the list of all answers, written with free constants.
A particular solution is one answer from the list.
For $y' = 2x$, the general solution is $y = x^2 + C$, and $y = x^2 + 5$ is a particular solution.
