---
tag: ST45QMRDZ6
kind: concept
name: Separation of variables in the Hamilton–Jacobi equation
msc: [70H20, 70H06]
specializes: [47NFRVB564]
sources:
  - url: https://en.wikipedia.org/wiki/Hamilton%E2%80%93Jacobi_equation
---

## Summary

Separation of variables is the main method to find complete solutions of the [[Hamilton–Jacobi equation|5TRXQKP7DY]] of a mechanical system.
One looks for a solution that is a sum of functions of one coordinate each.
Then the partial differential equation splits into ordinary differential equations.
When it works, the motion can be found by quadratures, and the separation constants are conserved quantities.
Classical examples are the Kepler problem in spherical coordinates and Euler's two-centre problem in elliptic coordinates.
See the [[definition|VDM6VE9X1Q]].

## Explanations

### L1 human

The Hamilton–Jacobi equation is a single hard equation in many variables.
If the energy splits into parts that each involve one coordinate and its momentum, one can guess a solution that is a sum of one-variable pieces.
Each piece then satisfies its own equation in one variable, with its own constant, and can be found by an integral.
For two independent oscillators, $H = \frac{1}{2}(p_1^2 + q_1^2) + \frac{1}{2}(p_2^2 + q_2^2)$, the energies of the two oscillators are the separation constants.
Whether a system separates depends strongly on the choice of coordinates.
