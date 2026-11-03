---
tag: KTFS80Y2PC
kind: statement
role: proposition
name: Lami's theorem
msc: [70C20]
uses: [KHT3FBB7NZ]
about: [KHT3FBB7NZ]
sources:
  - url: https://en.wikipedia.org/wiki/Lami%27s_theorem
same_as:
  wikidata: Q1149522
  wikipedia: Lami's theorem
---

## Statement

Let three nonzero forces $F_A$, $F_B$, $F_C$ in a plane act at one point, not all along one line.
Suppose they are in [[equilibrium|KHT3FBB7NZ]], that is, $F_A + F_B + F_C = 0$.
Let $\alpha$ be the angle between $F_B$ and $F_C$, $\beta$ the angle between $F_C$ and $F_A$, and $\gamma$ the angle between $F_A$ and $F_B$.
Then
$$\frac{\abs{F_A}}{\sin\alpha} = \frac{\abs{F_B}}{\sin\beta} = \frac{\abs{F_C}}{\sin\gamma}.$$

## Remarks

Proof idea: placing the three vectors head to tail gives a closed triangle, since they sum to zero.
The interior angle of this triangle opposite the side $F_A$ is $\pi - \alpha$, and similarly for the others.
The law of sines and $\sin(\pi - \alpha) = \sin\alpha$ give the result.
The hypotheses ensure that no two of the forces are parallel, so all three angles lie strictly between $0$ and $\pi$ and the sines are nonzero.

Example: a weight of $W$ newtons hangs from two strings that each make an angle of $60^\circ$ with the vertical.
The angle between the two strings is $120^\circ$ and each string makes $180^\circ - 60^\circ = 120^\circ$ with the downward weight.
So $W / \sin 120^\circ = T / \sin 120^\circ$, and each string tension $T$ equals $W$.

## Explanations

### L1 human

When three pulls on a knot balance, each pull is proportional to the sine of the angle between the other two.
So the largest pull is the one opposite the smallest angle between the other two.
For example, a small weight hung from the middle of a nearly straight, taut wire makes the two halves of the wire pull very hard.
It gives quick answers for weights hanging from strings or for loads on a crane.

### L2 human

Lami's theorem is the law of sines applied to the triangle of forces.
It is a special case of the equilibrium conditions of statics for concurrent forces, where the torque condition is automatic.
For more than three forces, or forces not meeting at one point, one uses the full equilibrium equations instead.
