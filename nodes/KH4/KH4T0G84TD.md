---
tag: KH4T0G84TD
kind: example
name: An interpolant from a refutation of seven clauses
msc: ["03F20"]
topics: [CBAF7J051K]
audience: research
instance_of: [59GJCM8C66]
uses: [YHGCN7BBEP, 66YH6V1HBG, 6JSH907W5R]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Feasible interpolation
---

## Example

Let $p$ be the shared variable, $q$ the private variable of $A$, and $r$ the private variable of $B$.
Take $A(p, q) = \{q, \ \neg q \vee p\}$ and $B(p, r) = \{\neg p \vee r, \ \neg r\}$.
The variable $p$ occurs only positively in $A$.
Here is a [[resolution refutation|6JSH907W5R]] of $A \wedge B$ with $L = 7$ clauses.

1. $C_1 = q$, a clause of $A$.
2. $C_2 = \neg q \vee p$, a clause of $A$.
3. $C_3 = p$, from $C_1$ and $C_2$ with pivot $q$.
4. $C_4 = \neg p \vee r$, a clause of $B$.
5. $C_5 = \neg r$, a clause of $B$.
6. $C_6 = \neg p$, from $C_4$ and $C_5$ with pivot $r$.
7. $C_7 = \square$, from $C_3$ and $C_6$ with pivot $p$.

We follow the construction in the [[proof|66YH6V1HBG]] of the [[interpolation theorem for resolution|YHGCN7BBEP]], one circuit $I_i$ per clause.

1. The axioms $C_1$ and $C_2$ belong to $A$, so $I_1 = I_2 = 0$.
   The axioms $C_4$ and $C_5$ belong to $B$, so $I_4 = I_5 = 1$.
2. The pivot of $C_3$ is $q$, a variable of $A$, so $I_3 = I_1 \vee I_2 = 0$.
3. The pivot of $C_6$ is $r$, a variable of $B$, so $I_6 = I_4 \wedge I_5 = 1$.
4. The pivot of $C_7$ is the shared variable $p$.
   The premise with $p$ is $C_3$, and the premise with $\neg p$ is $C_6$.
   The general rule gives the following circuit:
   $$I_7 = (p \wedge I_6) \vee (\neg p \wedge I_3) = (p \wedge 1) \vee (\neg p \wedge 0) = p.$$
5. The monotone rule gives $I_7 = I_6 \wedge (p \vee I_3) = 1 \wedge (p \vee 0) = p$, with no NOT gate.

Check both values of $p$.
At $p = 0$ we have $I(0) = 0$, and $A(0, q) = \{q, \neg q\}$ is unsatisfiable.
At $p = 1$ we have $I(1) = 1$, and $B(1, r) = \{r, \neg r\}$ is unsatisfiable.
So $I(p) = p$ is an interpolating circuit, well inside the bound of $4L = 28$ gates.

## Remarks

The circuit $p$ is also a Craig interpolant in the usual sense: $A$ implies $p$, and $p$ implies the negation of $B$.

What changes when $p$ occurs negatively in $A$?
Take $A = \{q, \ \neg q \vee \neg p\}$ and $B = \{p \vee r, \ \neg r\}$.
The same pattern of steps gives $C_3 = \neg p$ and $C_6 = p$, so now $C_6$ is the premise with $p$ and $C_3$ the premise with $\neg p$.
The general rule gives the following circuit:
$$I_7 = (p \wedge I_3) \vee (\neg p \wedge I_6) = (p \wedge 0) \vee (\neg p \wedge 1) = \neg p.$$
Check: at $p = 1$ the set $A$ becomes $\{q, \neg q\}$ and fails, and at $p = 0$ the set $B$ becomes $\{r, \neg r\}$ and fails.
The monotone rule does not apply here, and indeed $\neg p$ is not a monotone function.

## Explanations

### L1 human

The rules of $A$ say "$q$ holds" and "$q$ forces $p$", so $A$ forces $p$ to be on.
The rules of $B$ force $p$ to be off.
So the shared switch $p$ alone tells which side fails: if $p$ is off, $A$ fails, and if $p$ is on, $B$ fails.
The construction finds this answer by reading the proof line by line.

### L2 human

The labels follow a simple logic.
A label $0$ on a clause means "this clause, restricted to the side of $A$, follows from $A$ at the current value of $p$", and a label $1$ says the same for $B$.
A step on $q$ uses only facts about $A$, so an OR keeps the label $0$ when both premises carry it.
A step on $p$ looks at the value of $p$ and keeps the premise whose pivot literal is false, since that premise still says something.
Watch out for the direction of that choice: at $p = 1$ the literal $\neg p$ is false, so the rule takes the label of the premise that contains $\neg p$.
