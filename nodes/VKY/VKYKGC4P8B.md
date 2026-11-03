---
tag: VKYKGC4P8B
kind: definition
name: State function
msc: [80A05, 80A10]
defines: T8J5XRYBZZ
uses: [GYNNJBMTCP, TD4C13V3J6, 5EKTEE00FZ]
sources:
  - url: https://en.wikipedia.org/wiki/State_function
---

## Definition

Let $\Sigma$ be a [[thermodynamic system|GYNNJBMTCP]] and let $\mathcal{S}$ be the set of its [[equilibrium|5EKTEE00FZ]] [[states|TD4C13V3J6]].
A *state function* of $\Sigma$ is a function $F \colon \mathcal{S} \to \R$.
For a process from a state $A$ to a state $B$, the change of $F$ is $\Delta F = F(B) - F(A)$.
So $\Delta F$ depends only on $A$ and $B$, not on the path between them.

## Remarks

For a fixed amount of ideal gas with states $(p, V)$, the temperature $T = pV/(nR)$ is a state function.
Here $n$ is the amount of gas and $R$ is the gas constant.
The work done on the gas is not a state function: it is not determined by the end states, since two paths between the same states can give different work.
When $\mathcal{S}$ is a smooth manifold and $F$ is differentiable, the differential $dF$ is exact, and $\oint dF = 0$ around every closed path.
