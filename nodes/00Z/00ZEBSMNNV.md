---
tag: 00ZEBSMNNV
kind: statement
role: proposition
name: Additivity of line integrals under concatenation
aliases: [line-integral-over-a-sum-of-paths]
msc: [26B12]
uses: [0YS8RX87F4, 0M50E4WYWJ, 0W3W1VYWBP]
sources:
  - url: https://en.wikipedia.org/wiki/Line_integral
    locator: Line integral of a vector field
---

## Statement

Let $\gamma_1 \colon [a, b] \to \mathbb{R}^n$ and $\gamma_2 \colon [b, c] \to \mathbb{R}^n$ be piecewise $C^1$ curves with $\gamma_1(b) = \gamma_2(b)$.
Let $\gamma \colon [a, c] \to \mathbb{R}^n$ be their concatenation: $\gamma = \gamma_1$ on $[a, b]$ and $\gamma = \gamma_2$ on $[b, c]$.
For each continuous vector field $F$ and each continuous function $f$ on the image of $\gamma$,
$$\int_\gamma F \cdot d\mathbf{r} = \int_{\gamma_1} F \cdot d\mathbf{r} + \int_{\gamma_2} F \cdot d\mathbf{r}, \qquad \int_\gamma f \, ds = \int_{\gamma_1} f \, ds + \int_{\gamma_2} f \, ds.$$

## Remarks

Proof: apply the [[parametric formula|0W3W1VYWBP]] on $[a, c]$ and split the integral at $t = b$.
If the parameter intervals do not match, first shift the parameter of $\gamma_2$. A shift does not change line integrals.
Together with [[path reversal|0FSCXYG856]], this lets one compute line integrals over the boundary of a polygon, side by side.
The concatenation is often written $\gamma_1 + \gamma_2$ or $\gamma_1 * \gamma_2$.

## Explanations

### L1 human

Walking from $A$ to $B$ and then from $B$ to $C$ is one walk from $A$ to $C$.
The line integral over the whole walk is the sum of the line integrals over the two parts.
