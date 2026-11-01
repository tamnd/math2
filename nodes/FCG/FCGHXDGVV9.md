---
tag: FCGHXDGVV9
kind: concept
name: Henstock–Kurzweil integral
msc: [26A39]
sources:
  - url: https://en.wikipedia.org/wiki/Henstock%E2%80%93Kurzweil_integral
same_as:
  wikidata: Q82029
  wikipedia: Henstock–Kurzweil integral
---

## Summary

The Henstock–Kurzweil integral, also called the gauge integral, is an integral of Riemann type.
In its sums the allowed size of a subinterval may vary from point to point.
This one change makes it integrate every derivative, so that $\int_a^b F' = F(b) - F(a)$ holds whenever $F$ is differentiable everywhere on $[a, b]$.
It integrates every Lebesgue integrable function with the same value, and it gives the same integral as the [[Perron integral|M077AXJACA]].
Unlike the Lebesgue integral, it also integrates some functions whose absolute value is not integrable.

## Explanations

### L1 human

In a Riemann sum all pieces must be short, with one bound on their length.
In the Henstock–Kurzweil sum each point $t$ comes with its own allowed size $\delta(t)$, and a piece tagged by $t$ must fit within distance $\delta(t)$ of $t$.
Near a point where the function misbehaves, one demands very short pieces; elsewhere longer ones are fine.
For example, the derivative of $x^2 \sin(1/x^2)$ is not Lebesgue integrable on $[0, 1]$, but it is Henstock–Kurzweil integrable with integral $\sin 1$.
