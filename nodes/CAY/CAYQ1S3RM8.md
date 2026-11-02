---
tag: CAYQ1S3RM8
kind: definition
name: Method of matched asymptotic expansions
msc: ["34E05", "34E15"]
defines: QQ1YT0MV2X
uses: [G6J21TGRMM, YCFPD0GE5G, Q26QN6GYZX]
sources:
  - url: https://en.wikipedia.org/wiki/Method_of_matched_asymptotic_expansions
---

## Definition

Let $y_\varepsilon$ solve a [[singularly perturbed|G6J21TGRMM]] problem on an interval $[a, b]$ that has a [[boundary layer|YCFPD0GE5G]] at $a$ of thickness $\delta(\varepsilon) \to 0$.
The *method of matched asymptotic expansions* builds an approximation in four steps.

1. Outer expansion: solve the reduced equations order by order in $\varepsilon$, with the boundary conditions away from $a$, to get $y^{\mathrm{out}}(x)$.
2. Inner expansion: set $X = (x - a) / \delta(\varepsilon)$ and rewrite the problem in $X$.
   Solve it order by order with the boundary conditions at $a$, to get $Y^{\mathrm{in}}(X)$, which may contain free constants.
3. Matching: choose the free constants so that the two expansions agree in the overlap.
   At leading order this is Prandtl's rule $\lim_{X \to \infty} Y^{\mathrm{in}}(X) = \lim_{x \to a^+} y^{\mathrm{out}}(x)$.
   This common value is the *common part*.
4. Composite expansion: $y^{\mathrm{comp}}(x) = y^{\mathrm{out}}(x) + Y^{\mathrm{in}}((x - a)/\delta(\varepsilon)) - (\text{common part})$.

Each expansion is an [[asymptotic expansion|Q26QN6GYZX]] valid in its own region, and the composite one is meant to be valid uniformly on $[a, b]$.

## Remarks

Example: $\varepsilon y'' + y' + y = 0$ on $[0, 1]$, $y(0) = 0$, $y(1) = 1$.
Outer: $y' + y = 0$ with $y(1) = 1$ gives $y^{\mathrm{out}} = e^{1 - x}$.
Inner: with $X = x / \varepsilon$, the leading equation is $Y'' + Y' = 0$ with $Y(0) = 0$, so $Y^{\mathrm{in}} = A (1 - e^{-X})$.
Matching gives $A = y^{\mathrm{out}}(0) = e$, so the common part is $e$.
Composite: $y^{\mathrm{comp}} = e^{1 - x} - e^{1 - x/\varepsilon}$; it satisfies $y(0) = 0$ exactly and $y(1) = 1 - e^{1 - 1/\varepsilon}$, which is exponentially close to $1$.

Non-example: putting the outer solution and the inner solution side by side without step 3 fails, since the constant $A$ stays undetermined.
The layer must also be placed correctly: a trial layer at $x = 1$ leads to inner solutions that grow like $e^{X}$ away from the boundary and cannot match.

## Explanations

### L1 human

Solve the easy problem far from the layer, solve the zoomed-in problem in the layer, and glue the two by making them agree in between.
