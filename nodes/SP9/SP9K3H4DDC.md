---
tag: SP9K3H4DDC
kind: example
name: A switching circuit read as a propositional formula
msc: ["03B05", "94C11"]
topics: [JDK63589SA]
audience: ug1
instance_of: [09K9MWD2QQ]
uses: [025YZN3VJW, 0F72FK8EKB, 029JBBF693, 0S6GMNJ62Y, 0JMR2HM2N2]
sources:
  - url: https://en.wikipedia.org/wiki/Multiway_switching
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Claude_Shannon
    locator: Logic circuits
---

## Example

A staircase lamp with a switch at each end is a propositional formula in disguise.
Call the switches $A$ (at the bottom) and $B$ (at the top), and let $p$ mean "switch $A$ is up" and $q$ mean "switch $B$ is up".
The wires form two paths from the source to the lamp, side by side.
The first path is closed when both switches are up, and the second is closed when both are down.

Contacts in series give a [[conjunction|025YZN3VJW]], because current passes only if both are closed.
Paths in parallel give a [[disjunction|0F72FK8EKB]], because current needs only one closed path.
So the lamp is on exactly when the formula
$$\varphi = (p \land q) \lor (\neg p \land \neg q)$$
has the value $1$.
We check two facts: $\varphi$ is [[logically equivalent|0JMR2HM2N2]] to the [[biconditional|0S6GMNJ62Y]] $p \leftrightarrow q$, and each switch changes the state of the lamp.

Compute $\varphi$ and $p \leftrightarrow q$ in all four rows:
$$\begin{array}{cc|cc|c|c} p & q & p \land q & \neg p \land \neg q & \varphi & p \leftrightarrow q \\ \hline 1 & 1 & 1 & 0 & 1 & 1 \\ 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 1 & 1 \end{array}$$

1. The last two columns agree in every row, so $\varphi$ and $p \leftrightarrow q$ are equivalent.
2. A flip of switch $A$ changes $p$ and keeps $q$.
   In the table this moves between row 1 and row 3, or between row 2 and row 4, and in each pair the value of $\varphi$ differs.
3. A flip of switch $B$ moves between row 1 and row 2, or between row 3 and row 4, and again the value differs.

So either switch turns the lamp on when it is off and off when it is on.

## Remarks

The example shows the dictionary between circuits and formulas.
A switch is a variable, series is $\land$, parallel is $\lor$, and a contact that closes when the switch is down is $\neg$.
Claude Shannon's master's thesis on relay and switching circuits, published in 1938, used this reading of circuits as formulas.
The topic [[switching circuits and logic design|JWQBMJS0B1]] continues the story.

Change the wiring and the formula changes with it.
If the second path closes when $A$ is down and $B$ is up, the circuit computes $(p \land q) \lor (\neg p \land q)$, which is equivalent to $q$.
Then switch $A$ has no effect at all, which the table shows at once.
With three switches, a lamp that changes with each flip computes $p \leftrightarrow (q \leftrightarrow r)$, which is true exactly when an odd number of the three variables are true.

Watch out.
Do not join the two paths by $\land$ because both paths are present.
The lamp needs only one closed path, so parallel paths give $\lor$.

## Explanations

### L1 human

Many houses have a lamp that two switches control, one at each end of a staircase.
Each switch can be up or down, so there are four cases.
In this wiring the lamp is on when both switches are up or both are down, and off in the other two cases.
So a flip of either switch turns the lamp on if it was off, and off if it was on.
The rule "both the same" is the logical connective "if and only if".

### L2 human

The typical use goes the other way: start from a wanted table, write a formula, and build the circuit from it.
Suppose we want a lamp that is on only when $A$ is up and $B$ is down.
The wanted table has a single $1$, in the row $p = 1$, $q = 0$.
The formula $p \land \neg q$ has exactly that table:
$$p \land \neg q = 1 \iff p = 1 \text{ and } q = 0 .$$
So one path with two contacts in series does the job: a contact that closes when $A$ is up, then a contact that closes when $B$ is down.
Check: in the row $p = 1$, $q = 1$ the second contact is open, so the lamp is off, as the table wants.
