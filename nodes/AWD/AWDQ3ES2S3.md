---
tag: AWDQ3ES2S3
kind: concept
name: Full state feedback
msc: [93B52, 93C05, 93B55]
sources:
  - url: https://en.wikipedia.org/wiki/Full_state_feedback
same_as:
  wikidata: Q925922
  wikipedia: Full state feedback
---

## Summary

Full state feedback is a control law in which the input is computed from the whole current state of the system.
Typically it has the form $u = -Kx$ for a gain matrix $K$.
For a linear system $x' = Ax + Bu$ it gives the closed loop $x' = (A - BK)x$, so the gain changes the dynamics matrix and its eigenvalues.
It is the basic design tool of state-space control, used for [[pole placement|SCY6X79XVP]] and for the linear quadratic regulator.
When the state is not measured, it is combined with a [[state observer|TQ7E9S194T]].

## Explanations

### L1 human

Imagine balancing a cart: you watch both its position and its speed and push according to both.
Full state feedback means the push is a fixed combination of all the quantities that describe the system at this moment.
For the cart $x_1' = x_2$, $x_2' = u$, the law $u = -x_1 - 2x_2$ pulls the cart back to the origin without oscillating.
Choosing the weights in the combination lets one decide how fast and how smoothly the system settles.
