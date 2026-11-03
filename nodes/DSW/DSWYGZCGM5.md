---
tag: DSWYGZCGM5
kind: concept
name: Kutta condition
msc: [76B10, 76G25]
sources:
  - url: https://en.wikipedia.org/wiki/Kutta_condition
same_as:
  wikidata: Q1154278
  wikipedia: Kutta condition
---

## Summary

The Kutta condition selects the circulation of a two-dimensional potential flow past a body with a sharp trailing edge, such as an airfoil.
Potential flow past such a body is not unique: there is one flow for each value of the circulation.
The Kutta condition picks the one flow in which the fluid leaves the trailing edge smoothly, with finite velocity.
Together with the Kutta–Joukowski theorem it predicts the lift of an airfoil.

## Explanations

### L1 human

Ideal flow past a wing could in principle wrap around the sharp rear edge at infinite speed.
Real air never does that: it leaves the rear edge smoothly, from both the upper and the lower surface.
The Kutta condition imposes this observed behaviour on the model.
For a thin flat plate tilted at a small angle $\alpha$ to the stream, it gives a lift coefficient of $2\pi\sin\alpha$.
