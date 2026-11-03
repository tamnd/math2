---
tag: GG80GYTSP5
kind: definition
name: Thermodynamic square
msc: [80A10]
defines: S46V4S6MVA
uses: [F6JVQ12X43, 722RZK72P5, JXKY6C8JTA, RBG5ZBM35Y, SPY89W0RJ7, 41NHDR6MH6, MAHDE6JZYT]
sources:
  - url: https://en.wikipedia.org/wiki/Thermodynamic_square
---

## Definition

Consider a closed simple system with entropy $S$, volume $V$, temperature $T$ and pressure $p$.
The *thermodynamic square* is the square diagram with these labels:

1. Corners: $-S$ at the top left, $V$ at the top right, $T$ at the bottom right, $-p$ at the bottom left.
2. Sides: [[internal energy|F6JVQ12X43]] $U$ on top, [[Helmholtz free energy|JXKY6C8JTA]] $F$ right, [[Gibbs free energy|RBG5ZBM35Y]] $G$ bottom, [[enthalpy|722RZK72P5]] $H$ left.

It is read with this rule.
For a potential on a side, its natural variables are the two adjacent corners, taken without sign.
For such a variable $v$, let $c_v$ be the label, with its sign, at the corner diagonally opposite to $v$.
The differential of the potential is the sum of $c_v \, dv$ over its two natural variables $v$.

## Remarks

Example: $G$ lies between $T$ and $p$.
The corner opposite $T$ is $-S$, and the corner opposite $p$ is $V$, so $dG = -S \, dT + V \, dp$, which agrees with the [[fundamental relation|41NHDR6MH6]].
In the same way the square gives $dU = T \, dS - p \, dV$, $dF = -S \, dT - p \, dV$ and $dH = T \, dS + V \, dp$, where $S$ is the [[entropy|SPY89W0RJ7]].
Non-example: a square with $F$ and $H$ swapped is not the thermodynamic square, since its rule would give $dF = T \, dS + V \, dp$, which is false.
The [[Maxwell relations|MAHDE6JZYT]] can also be read off from the corners of the square.

## Explanations

### L1 human

The thermodynamic square packs eight formulas into one small picture.
One remembers the order of the labels around the square, and the rule gives the differentials of the four potentials.
