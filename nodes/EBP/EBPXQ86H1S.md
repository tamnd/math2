---
tag: EBPXQ86H1S
kind: definition
name: Closed-loop transfer function
msc: [93C80, 93B52, 93C05]
defines: RYTSV821V8
uses: [86JKV3TRFD, 7NYES2D0Z4, 0XDK9CGYKJ]
sources:
  - url: https://en.wikipedia.org/wiki/Closed-loop_transfer_function
---

## Definition

Let $G$ and $H$ be [[transfer functions|86JKV3TRFD]] of single-input single-output linear time-invariant systems, given as [[rational functions|0XDK9CGYKJ]] of $s$.
Assume that $1 + G H$ is not the zero function.
Consider the negative [[feedback|7NYES2D0Z4]] loop with reference $r$, error $e$, output $y$ and Laplace transforms $R, E, Y$:
$$E = R - H Y, \qquad Y = G E.$$
The *closed-loop transfer function* is the rational function $T$ with $Y = T R$, namely
$$T(s) = \frac{G(s)}{1 + G(s) H(s)}.$$

## Remarks

The formula follows from $Y = G(R - HY)$, which gives $(1 + GH) Y = G R$.
Example: $G(s) = 1/s$ and $H(s) = k$ give $T(s) = (1/s)/(1 + k/s) = 1/(s + k)$, with a single pole at $-k$.
Non-example: $G(s) = 1$ and $H(s) = -1$ violate the hypothesis, since $1 + GH = 0$; the loop equations $E = R + Y$, $Y = E$ have no solution unless $R = 0$, so the loop is ill-posed.
For positive feedback, $E = R + HY$, the closed-loop transfer function is $G/(1 - GH)$.
For systems with several inputs and outputs, with transfer matrices $G$ and $H$, it is $(I + GH)^{-1} G$.
The product $G H$ is called the loop transfer function.
