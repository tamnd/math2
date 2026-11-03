---
tag: 8SRS8C88ZT
kind: definition
name: Wheeler–Feynman absorber theory
msc: [78A25, 78A35]
defines: 1GVQ2T5D0B
uses: [9Q1NE5EP37, B6SKCGENY8, WRZJRJS44W]
sources:
  - url: https://en.wikipedia.org/wiki/Wheeler%E2%80%93Feynman_absorber_theory
---

## Definition

Consider a system of point charges $q_1, \dots, q_N$ moving in Minkowski space.
For each $j$ let $F_j^{\mathrm{ret}}$ and $F_j^{\mathrm{adv}}$ be the retarded and advanced [[Liénard–Wiechert|B6SKCGENY8]] fields of charge $j$, written as [[electromagnetic tensors|WRZJRJS44W]].
They come from the [[retarded potential|9Q1NE5EP37]] and its time-reversed counterpart.
In *Wheeler–Feynman absorber theory*:

1. the field acting on charge $i$ is $\displaystyle F^{(i)} = \sum_{j \neq i} \tfrac{1}{2}\left( F_j^{\mathrm{ret}} + F_j^{\mathrm{adv}} \right)$, with no self-interaction;
2. each charge obeys the Lorentz force law $m_i \dfrac{du_i^\mu}{d\tau} = q_i F^{(i)\mu}{}_{\nu} u_i^\nu$ with this field;
3. the system is a *complete absorber*: $\displaystyle \sum_{j=1}^{N} \left( F_j^{\mathrm{ret}} - F_j^{\mathrm{adv}} \right) = 0$ everywhere outside the absorbing matter.

## Remarks

Under clause 3, an algebraic rearrangement gives
$$F^{(i)} = \sum_{j \neq i} F_j^{\mathrm{ret}} + \tfrac{1}{2}\left( F_i^{\mathrm{ret}} - F_i^{\mathrm{adv}} \right).$$
The first term is the usual retarded field of the other charges.
The second term is finite on the world line of charge $i$ and gives the Dirac radiation reaction force of the [[Abraham–Lorentz–Dirac equation|GDMRN1NBGE]].
Example: a single charge accelerated inside a perfectly absorbing box feels exactly the radiation reaction of ordinary electrodynamics, supplied by the advanced response of the absorber.
Non-example: if the absorber is incomplete, so clause 3 fails, the equations of motion differ from those of retarded electrodynamics, and the radiation reaction is not reproduced.
The theory was published by Wheeler and Feynman in 1945 and 1949.
