---
tag: T11MGWEKJ3
kind: statement
role: fact
name: Second law of thermodynamics
msc: [80A05, 80A10]
uses: [GYNNJBMTCP, SPY89W0RJ7, CY4GJQGF06, AJ8M9MGZGF, F3DHZ45H6A, 4JYJ1X6143]
about: [SPY89W0RJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Second_law_of_thermodynamics
same_as:
  wikidata: Q177045
  wikipedia: Second law of thermodynamics
---

## Statement

Let a closed [[thermodynamic system|GYNNJBMTCP]] pass by some process from an equilibrium state $A$ to an equilibrium state $B$.
Suppose that during the process the system takes in small amounts of [[heat|CY4GJQGF06]] $\delta Q$ through parts of its boundary at [[thermodynamic temperature|AJ8M9MGZGF]] $T$.
Then the [[entropy|SPY89W0RJ7]] $S$ of the system satisfies
$$S(B) - S(A) \ge \int_A^B \frac{\delta Q}{T},$$
with equality when the process is [[reversible|F3DHZ45H6A]].
In particular, if the system is isolated, then $S(B) \ge S(A)$.

## Remarks

The inequality follows from the [[Clausius theorem|4JYJ1X6143]].
Close the process into a cycle by a reversible path from $B$ back to $A$.
The Clausius theorem gives $\oint \delta Q / T \le 0$ for the cycle, and the reversible return path contributes $S(A) - S(B)$.
Rearranging gives the inequality above.
For example, when two blocks at temperatures $T_1 > T_2$ exchange a small amount of heat $q$ inside an isolated box, the total entropy changes by $q/T_2 - q/T_1 > 0$.
The law has several equivalent classical forms: the Clausius statement and the Kelvin–Planck statement, both about cyclic machines.
It is a law of nature: it is not derived from mechanics, and it fixes the direction in which spontaneous processes run.

## Explanations

### L1 human

Heat flows by itself from hot to cold, never the other way.
Entropy is the quantity that measures this one-way character.
In a system cut off from its surroundings, entropy can grow or stay the same, but it never decreases.
This is why a hot cup of coffee cools in a room but never heats up by itself.

### L2 human

The second law limits what engines and refrigerators can do.
It gives Carnot's bound $1 - T_c/T_h$ on the efficiency of a heat engine working between temperatures $T_h > T_c$.
For reversible processes it gives $\delta Q = T \, dS$, and with the first law this yields the fundamental relation $dU = T \, dS - p \, dV$.
It also leads to the extremum principles: an isolated system in equilibrium has maximal entropy among the states allowed by its constraints.
