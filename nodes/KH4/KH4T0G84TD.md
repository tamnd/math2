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

Let $p$ be the shared variable, $q$ the variable of $A$ and $r$ the variable of $B$.
Let $A(p, q) = \set{q, \ \neg q \vee p}$ and $B(p, r) = \set{\neg p \vee r, \ \neg r}$.
The variable $p$ occurs only positively in $A$.
The following is a [[resolution refutation|6JSH907W5R]] of $A \wedge B$ with $L = 7$ clauses.

1. $C_1 = q$, a clause of $A$.
2. $C_2 = \neg q \vee p$, a clause of $A$.
3. $C_3 = p$, from $C_1$ and $C_2$ with pivot $q$.
4. $C_4 = \neg p \vee r$, a clause of $B$.
5. $C_5 = \neg r$, a clause of $B$.
6. $C_6 = \neg p$, from $C_4$ and $C_5$ with pivot $r$.
7. $C_7 = \square$, from $C_3$ and $C_6$ with pivot $p$.

We follow the construction in the [[proof|66YH6V1HBG]] of the [[interpolation theorem for resolution|YHGCN7BBEP]].

1. **Axioms.** $I_1 = I_2 = 0$, since $C_1$ and $C_2$ are in $A$, and $I_4 = I_5 = 1$, since $C_4$ and $C_5$ are in $B$.
2. **Pivot $q$.** $I_3 = I_1 \vee I_2 = 0$.
3. **Pivot $r$.** $I_6 = I_4 \wedge I_5 = 1$.
4. **Pivot $p$, general rule.** The premise with $p$ is $C_3$ and the premise with $\neg p$ is $C_6$. So $I_7 = (p \wedge I_6) \vee (\neg p \wedge I_3) = p$.
5. **Pivot $p$, monotone rule.** $I_7 = I_6 \wedge (p \vee I_3) = p$, with no NOT gate.
6. **Check at $p = 0$.** $I(0) = 0$, and $A(0, q) = \set{q, \neg q}$ is unsatisfiable.
7. **Check at $p = 1$.** $I(1) = 1$, and $B(1, r) = \set{r, \neg r}$ is unsatisfiable.

So $I(p) = p$ is an interpolating circuit, and the construction gives it with at most $4L = 28$ gates.

## Remarks

The circuit $p$ is also a Craig interpolant: $A$ implies $p$, and $p$ implies the negation of $B$.

If we change $A$ to $\set{q, \neg q \vee \neg p}$ and $B$ to $\set{p \vee r, \neg r}$, the same pattern of steps gives a refutation with $C_3 = \neg p$ and $C_6 = p$.
Then the general rule gives $I_7 = (p \wedge I_3) \vee (\neg p \wedge I_6) = \neg p$.
Now $p$ occurs negatively in $A$, the monotone rule does not apply, and indeed $\neg p$ is not monotone.

## Explanations

### L1 human

The rules of $A$ say "$q$ holds" and "$q$ forces $p$", so $A$ forces $p$ to be true.
The rules of $B$ force $p$ to be false.
So the shared switch $p$ alone tells which side fails: if $p$ is off, $A$ fails, and if $p$ is on, $B$ fails.
The construction finds this answer by reading the proof line by line.

### L2 human

We label each line of the proof with $0$ for "side $A$" or $1$ for "side $B$".

1. Lines from $A$ get $0$, and lines from $B$ get $1$.
2. A step on a variable of $A$ only takes the OR of the labels, and a step on a variable of $B$ only takes the AND.
3. A step on the shared variable $p$ picks the label of one premise, chosen by the value of $p$.
4. The label of the last line is the interpolant.

The typical use is in lower bounds, where the same construction is applied to a family of formulas.
A trap is to choose the premise in step 3 the wrong way: for $p = 1$, take the premise that contains $\neg p$.
