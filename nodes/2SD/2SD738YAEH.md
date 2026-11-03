---
tag: 2SD738YAEH
kind: concept
name: Descriptor system
msc: [93C05, 34A09]
specializes: [EY362KR0KB]
sources:
  - url: https://en.wikipedia.org/wiki/Differential-algebraic_system_of_equations
---

## Summary

A descriptor system is a linear control system of the form $E x' = Ax + Bu$, $y = Cx + Du$, in which the matrix $E$ may be singular.
It is a linear [[differential-algebraic system|EY362KR0KB]] with inputs and outputs, so some of its equations are algebraic constraints rather than differential equations.
Descriptor systems arise directly from circuit equations, constrained mechanics and interconnected models, before any variable is eliminated.
Unlike ordinary state-space systems, they can have improper transfer functions and impulsive behaviour.

## Explanations

### L1 human

When engineers write down the equations of a circuit or a machine, some equations describe how quantities change and others are fixed relations, such as Kirchhoff's laws.
A descriptor system keeps both kinds side by side, by putting a matrix $E$ in front of the derivative, with zero rows for the algebraic relations.
For example, the pair of equations $0 = x_1 - u$ and $x_1' = x_2$ with output $y = x_2$ gives $y = u'$, a differentiator.
No ordinary state-space system $x' = Ax + Bu$ can produce the derivative of its input.
