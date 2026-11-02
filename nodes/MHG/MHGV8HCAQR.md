---
tag: MHGV8HCAQR
kind: statement
role: proposition
name: Predictor–corrector method
msc: [65L06, 65L05]
uses: [BX4D85A79P, 0FXDW992DS]
about: [BX4D85A79P]
sources:
  - url: https://en.wikipedia.org/wiki/Predictor%E2%80%93corrector_method
---

## Statement

Let $f \colon \R \times \R^d \to \R^d$ be sufficiently smooth, and consider the [[initial value problem|0FXDW992DS]] $y' = f(t, y)$, $y(t_0) = y_0$.
Let $P$ be an explicit [[linear multistep method|BX4D85A79P]] of order $p^* \ge 1$, the predictor.
Let $C$ be an implicit linear multistep method of order $p \ge 1$, the corrector.
One step of the PECE mode with step size $h$ does the following:

1. P: compute a predicted value $y_{n+1}^{[0]}$ with $P$.
2. E: evaluate $f_{n+1}^{[0]} = f(t_{n+1}, y_{n+1}^{[0]})$.
3. C: compute $y_{n+1}$ with the formula of $C$, where $f_{n+1}^{[0]}$ replaces the unknown value $f(t_{n+1}, y_{n+1})$.
4. E: evaluate $f_{n+1} = f(t_{n+1}, y_{n+1})$ for use in later steps.

Then the PECE method is an explicit method of order $\min(p, p^* + 1)$.
If $p^* \ge p$, its principal local truncation error equals that of the corrector.

## Remarks

The corrector is applied once instead of being iterated to convergence, so no nonlinear equation is solved.
The error of the predicted value is $O(h^{p^*+1})$.
It enters the corrected value multiplied by $h$ times a coefficient of the corrector, so it adds $O(h^{p^*+2})$ to the local error.
Comparing this with the local error $O(h^{p+1})$ of the corrector gives the order $\min(p, p^*+1)$.
Example: the [[Euler method|0JARTXX4XP]] ($p^* = 1$) as predictor and the trapezoidal rule ($p = 2$) as corrector give [[Heun's method|RJEK60G28F]], of order $\min(2, 2) = 2$.
When $p^* = p$, the difference $y_{n+1} - y_{n+1}^{[0]}$ gives an estimate of the local error (Milne's device), which is used for [[adaptive step size|6MREWBZR7R]] control.

## Explanations

### L1 human

An implicit method is often more accurate and more stable, but its formula contains the unknown new value on both sides.
A predictor-corrector method first guesses the new value with a cheap explicit formula.
It then plugs the guess into the implicit formula once, which corrects it.
The result is explicit, and it keeps the order of the corrector when the guess is good enough.

### L2 human

The Adams–Bashforth–Moulton pairs are the standard example: an Adams–Bashforth predictor with an Adams–Moulton corrector of the same order.
The PECE method has the same order as the corrector, but its stability region is different and is in general smaller than that of the corrector.
So predictor-corrector methods are not suited to [[stiff equations|RR5FCG92PN]], where one solves the implicit equations with Newton's method instead.
