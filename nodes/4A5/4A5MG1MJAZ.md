---
tag: 4A5MG1MJAZ
kind: statement
role: proposition
name: Length contraction
msc: [83A05]
uses: [WEVGN4C7PQ, 2E9AJVZS6E]
about: [WEVGN4C7PQ]
sources:
  - url: https://en.wikipedia.org/wiki/Length_contraction
same_as:
  wikidata: Q836595
  wikipedia: Length contraction
---

## Statement

Let $S$ and $S'$ be inertial frames with coordinates $(t, x, y, z)$ and $(t', x', y', z')$.
Let $S'$ move with velocity $v$ along the $x$ axis of $S$, where $\abs{v} < c$.
Let a rod be at rest in $S'$, lying along the $x'$ axis, with length $L_0$ in $S'$ (its proper length).
Define its length $L$ in $S$ as the distance between the positions of its two ends at one and the same time $t$ of $S$.
Then
$$L = \frac{L_0}{\gamma}, \qquad \gamma = \frac{1}{\sqrt{1 - v^2/c^2}},$$
where $\gamma$ is the [[Lorentz factor|2E9AJVZS6E]].
Lengths perpendicular to the direction of motion are the same in both frames.

## Remarks

Proof idea: the [[Lorentz transformation|WEVGN4C7PQ]] gives $x' = \gamma (x - v t)$.
For the two ends at the same time $t$, subtracting gives $L_0 = \Delta x' = \gamma \Delta x = \gamma L$.
Since $y' = y$ and $z' = z$, transverse lengths do not change.
Example: a rod of proper length $1$ metre moving at $v = 0.6c$ has length $0.8$ metre in $S$.
The measurement at equal times in $S$ is essential: the two measuring events are not simultaneous in $S'$.
This is why each observer can find the other's rods contracted without contradiction.

## Explanations

### L1 human

A moving object is shorter in its direction of motion than the same object at rest.
The shrinking factor is the Lorentz factor, so it is invisible at everyday speeds and large near the speed of light.
It does not happen because the object is squeezed; it happens because the two observers disagree about which events happen at the same time.

### L2 human

Length contraction and time dilation are two faces of one Lorentz transformation, and in many problems either one gives the answer.
For a muon flying down through the atmosphere, the Earth observer uses time dilation, while the muon uses length contraction of the atmosphere.
Paradoxes such as the ladder paradox are resolved by keeping track of which events are simultaneous in which frame.
