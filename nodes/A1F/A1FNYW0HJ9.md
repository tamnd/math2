---
tag: A1FNYW0HJ9
kind: statement
role: proposition
name: Perry–Robertson formula
msc: [74G60, 74K10]
uses: [E8JCKAE09C, 13FGKM7NQ0]
about: [4GAM4KXSM8]
sources:
  - url: https://en.wikipedia.org/wiki/Perry%E2%80%93Robertson_formula
same_as:
  wikidata: Q7169884
  wikipedia: Perry–Robertson formula
---

## Statement

Let a pin-ended linear elastic column have length $L$, cross-section area $A$, radius of gyration $r$ and extreme-fibre distance $c$.
Let it have an initial crookedness $w_0(x) = a_0 \sin(\pi x / L)$ with $a_0 \ge 0$.
Let $\sigma_E = \pi^2 E / (L/r)^2$ be its Euler critical stress, let $\sigma_y$ be the yield stress, and let $\eta = a_0 c / r^2$.
Assume the column fails when the largest compressive stress first reaches $\sigma_y$.
Then the mean axial stress $\sigma = P/A$ at failure is
$$\sigma = \frac{\sigma_y + (1 + \eta)\sigma_E}{2} - \sqrt{\left( \frac{\sigma_y + (1 + \eta)\sigma_E}{2} \right)^2 - \sigma_y \sigma_E}.$$

## Remarks

Under an axial load $P < P_E$ the linearized beam equation amplifies the initial bow to the total amplitude $a_0 / (1 - P/P_E)$, where $P_E = \sigma_E A$.
The bending moment at mid-length is $P a_0 / (1 - \sigma/\sigma_E)$, so the largest stress is $\sigma \left(1 + \eta / (1 - \sigma/\sigma_E)\right)$.
Setting it equal to $\sigma_y$ gives the quadratic $(\sigma_y - \sigma)(\sigma_E - \sigma) = \eta \sigma \sigma_E$.
The failure stress is its smaller root, which is the formula above.

For $\eta = 0$ the formula gives $\sigma = \min(\sigma_y, \sigma_E)$, the larger root of the quadratic being discarded, so it reduces to the yield and Euler limits.
For $\eta > 0$ the failure stress lies below both $\sigma_y$ and $\sigma_E$.
In design practice $\eta$ is chosen as a function of the slenderness ratio to represent unavoidable imperfections.

## Explanations

### L1 human

No real column is perfectly straight.
A slight bow grows when the column is pushed, which adds bending stress on the inner side.
The Perry–Robertson formula finds the push at which that combined stress reaches the yield stress of the material.
It gives one smooth curve that covers short, medium and long columns.

### L2 human

The formula is the classic way to turn [[Euler's critical load|E8JCKAE09C]] into a design rule.
It replaces the bifurcation of a perfect column by a load–deflection curve of an imperfect one, the same idea that [[Koiter's theory|MA18D6QTV3]] makes systematic for general structures.
Compared with [[Johnson's parabolic formula|624BQC6T8E]], it has a mechanical derivation and a single parameter $\eta$ that measures imperfection.
