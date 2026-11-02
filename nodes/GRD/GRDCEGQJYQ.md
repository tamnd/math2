---
tag: GRDCEGQJYQ
kind: concept
name: Input-to-state stability
msc: [93D25, 93D09, 34D20]
sources:
  - url: https://en.wikipedia.org/wiki/Input-to-state_stability
same_as:
  wikidata: Q48995800
  wikipedia: Input-to-state stability
---

## Summary

Input-to-state stability is a stability notion for systems driven by an input, $\dot x = f(x, u)$.
It asks that the state decays to a size controlled by the size of the input, whatever the initial state.
It merges global asymptotic stability of the unforced system, a strong form of [[Lyapunov stability|0F2SYCKDT2]], with a bounded-input bounded-state property.
It is a basic tool in nonlinear [[control systems|ZPDTVZQN5K]], because it behaves well under cascades and feedback interconnections.

## Explanations

### L1 human

Think of a ball in a bowl that is shaken by an outside force.
Without shaking, the ball rolls back to the bottom.
With shaking, the ball stays close to the bottom, and the distance depends on how hard the shaking is.
For the system $\dot x = -x + u$, the state satisfies $\abs{x(t)} \le e^{-t} \abs{x(0)} + \sup \abs{u}$.
So the effect of the start dies out, and what remains is bounded by the input.
