---
tag: YHZ9BCNDRZ
kind: concept
name: Lax–Wendroff method
msc: [65M06, 35L65]
specializes: [X7HYEBA5SA]
sources:
  - url: https://en.wikipedia.org/wiki/Lax%E2%80%93Wendroff_method
same_as:
  wikidata: Q259958
  wikipedia: Lax–Wendroff method
---

## Summary

The Lax–Wendroff method is an explicit [[finite difference|X7HYEBA5SA]] scheme of second order in space and time for hyperbolic equations and [[conservation laws|8RA7AMWSAF]].
It comes from a Taylor expansion in time in which the time derivatives are replaced by space derivatives using the equation.
It is stable under the CFL condition and accurate for smooth solutions, but it produces oscillations next to discontinuities.
This is why it is often combined with a first-order scheme through a flux limiter.

## Explanations

### L1 human

For the [[transport equation|PVD7VZJZ9B]] $u_t + a u_x = 0$, the value at the next time is $u + \Delta t\, u_t + \frac{\Delta t^2}{2} u_{tt}$ up to higher terms.
The equation says $u_t = -a u_x$ and $u_{tt} = a^2 u_{xx}$, so one only needs space derivatives, and these are replaced by centred differences.
The result uses three neighbouring grid values and is accurate to second order.
Near a jump, it overshoots and undershoots, creating small wiggles.
