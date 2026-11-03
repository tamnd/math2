---
tag: CYP0N13QVX
kind: definition
name: Linear-feedback shift register
msc: [94A55, 11B37, 11T71]
defines: WHX90SGEJ5
uses: [0ZXZ82FTX2, 0NDVHBVBXB]
sources:
  - url: https://en.wikipedia.org/wiki/Linear-feedback_shift_register
---

## Definition

Let $F$ be a [[finite field|0ZXZ82FTX2]] and let $L \ge 0$ be an integer.
A *linear-feedback shift register* of length $L$ over $F$ is given by feedback coefficients $c_1, \dots, c_L \in F$.
Its *connection polynomial* is $C(x) = 1 + c_1 x + c_2 x^2 + \cdots + c_L x^L \in F[x]$.
Given an initial state $(s_0, \dots, s_{L-1}) \in F^L$, the register *generates* the sequence $(s_j)_{j \ge 0}$ defined by
$$s_j = -\sum_{i=1}^{L} c_i \, s_{j-i} \quad \text{for } j \ge L.$$
At time $j$ the *state* of the register is $(s_j, \dots, s_{j+L-1})$.

## Remarks

The sequence satisfies the [[linear recurrence with constant coefficients|0NDVHBVBXB]] $s_j + c_1 s_{j-1} + \cdots + c_L s_{j-L} = 0$.
Over $F = \F_2$ the minus sign does not matter, and each new bit is the sum mod $2$ of selected earlier bits.
Since there are at most $\abs{F}^L$ states and each state determines the next, the sequence is eventually periodic.
If $c_L \ne 0$, the step is invertible, the sequence is purely periodic, and its period is at most $\abs{F}^L - 1$ when the initial state is nonzero.

Example: over $\F_2$ take $L = 2$, $c_1 = c_2 = 1$, so $C(x) = 1 + x + x^2$, and the initial state $(1, 1)$.
Then $s_2 = s_1 + s_0 = 0$, $s_3 = s_2 + s_1 = 1$, $s_4 = s_3 + s_2 = 1$, and the output is $1, 1, 0, 1, 1, 0, \dots$ with period $3 = 2^2 - 1$.

Non-example: the rule $s_j = s_{j-1} s_{j-2}$ over $\F_2$ is a feedback shift register whose feedback is not linear, so it is not an LFSR.
Registers of this kind are called nonlinear feedback shift registers.
