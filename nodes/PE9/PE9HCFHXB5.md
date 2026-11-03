---
tag: PE9HCFHXB5
kind: concept
name: Detectability
msc: [93B07, 93D15, 93C05]
sources:
  - url: https://en.wikipedia.org/wiki/Observability
---

## Summary

A linear system $x' = Ax$, $y = Cx$ is detectable if every motion of the state that the output cannot see decays to zero by itself.
It is weaker than [[observability|C4HN3EAQWM]].
It is exactly what is needed to build an observer whose estimate of the state converges to the true state.
Detectability is the dual of [[stabilizability|C2KM20J9DZ]]: $(C, A)$ is detectable exactly when $(A^T, C^T)$ is stabilizable.
It appears as a hypothesis in Kalman filtering and in linear-quadratic control.

## Explanations

### L1 human

A sensor may miss some parts of a system.
That is fine if those hidden parts fade away on their own, because then one can ignore them in the long run.
A system is detectable when every hidden part fades away like this.
For example, with $x_1' = -x_1$, $x_2' = x_2$ and output $y = x_2$, the part $x_1$ is invisible but decays, so the system is detectable.
