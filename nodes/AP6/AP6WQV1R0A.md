---
tag: AP6WQV1R0A
kind: example
name: Solving a Horn formula by marking
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug2
instance_of: [QR92EZDTKF]
uses: [T3SXVH3ZZC, QN7M1JCGT9, H31CS3HK5P]
sources:
  - url: https://en.wikipedia.org/wiki/Horn-satisfiability
    locator: Algorithm
---

## Example

Let $S$ be the set of the five clauses
$$C_1 = \{ p \}, \quad C_2 = \{ \neg p, q \}, \quad C_3 = \{ \neg p, \neg q, r \}, \quad C_4 = \{ \neg s, t \}, \quad C_5 = \{ \neg r, \neg t \}.$$
We check that $S$ is a Horn formula, and we decide its [[satisfiability|QN7M1JCGT9]] with the marking algorithm.

1. The clauses $C_1$ to $C_4$ each have exactly one positive literal, so they are definite clauses, and $C_5$ has none, so it is a goal clause.
   Every clause is therefore a [[Horn clause|QR92EZDTKF]].
2. In implicative form, $C_1$ is the fact $p$, $C_2$ is $p \to q$, $C_3$ is $p \land q \to r$, $C_4$ is $s \to t$, and $C_5$ is $\neg(r \land t)$.
3. Mark $p$ by the fact $C_1$, then $q$ by $C_2$, then $r$ by $C_3$, since its body $p, q$ is now marked.
4. The clause $C_4$ needs $s$, which is unmarked, and no clause has head $s$.
   So no further mark is possible, and the marked set is $M = \{ p, q, r \}$.
5. The goal clause $C_5$ fails only if both $r$ and $t$ are marked, and $t$ is not.
   So the algorithm answers "satisfiable".

Check: the assignment with $p, q, r$ true and $s, t$ false satisfies $C_1$, $C_2$ and $C_3$ through their heads, $C_4$ through $\neg s$, and $C_5$ through $\neg t$.

## Remarks

The assignment found is the least model of the definite clauses $C_1$ to $C_4$, because every model of them makes $p$, $q$ and $r$ true.
If we add the fact $\{ s \}$, the algorithm marks $s$ and then $t$ by $C_4$, the goal clause $C_5$ now has both $r$ and $t$ marked, and the larger set is unsatisfiable.
If instead we drop $C_1$, nothing is marked, and the assignment that makes every variable false satisfies the set.
At no point does the algorithm choose a value or backtrack, which is why it runs in linear time.

## Explanations

### L1 human

Think of the five clauses as house rules.
The light is on.
If the light is on, the fan is on.
If the light and the fan are on, the heater is on.
If the radio is on, the TV is on.
The heater and the TV are not both on.
From the first rule the light is on, then the fan, then the heater.
Nothing forces the radio or the TV, so we leave them off, and every rule is obeyed.

### L2 human

The marks answer queries of the form "does $x$ follow from $S$?".
Every model makes $p$ true by $C_1$, then $q$ by $C_2$, then $r$ by $C_3$, so $S \models r$.
The model found above makes $t$ false, so $S \not\models t$.
Watch out: an unmarked variable is false in the model found, but the marks alone do not say that it is false in every model.
Here more is true.
Every model makes $r$ true, so $C_5$ forces $t$ false, and then $C_4$ forces $s$ false, so $S \models \neg t$ and $S \models \neg s$.
Without $C_5$ that argument fails, and the model $\{ p, q, r, s, t \}$ shows that $s$ and $t$ can both be true.
