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
$C_1 = \set{p}$, $C_2 = \set{\neg p, q}$, $C_3 = \set{\neg p, \neg q, r}$, $C_4 = \set{\neg s, t}$, $C_5 = \set{\neg r, \neg t}$.
We check that $S$ is a Horn formula and decide its satisfiability with the marking algorithm.

1. $C_1$, $C_2$, $C_3$, $C_4$ each have exactly one positive literal, so they are definite clauses. $C_5$ has none, so it is a goal clause. So every clause is a Horn clause.
2. In implicative form: $C_1$ is the fact $p$, $C_2$ is $p \to q$, $C_3$ is $p \land q \to r$, $C_4$ is $s \to t$, and $C_5$ is $\neg(r \land t)$.
3. Mark $p$, by the fact $C_1$.
4. Mark $q$, by $C_2$, since $p$ is marked.
5. Mark $r$, by $C_3$, since $p$ and $q$ are marked.
6. The clause $C_4$ needs $s$, which is not marked, and no clause has head $s$. So no further mark is possible, and the marked set is $M = \set{p, q, r}$.
7. The goal clause $C_5$ needs both $r$ and $t$ marked to fail, and $t$ is not marked. So the algorithm answers "satisfiable".
8. Check: the assignment $v(p) = v(q) = v(r) = 1$, $v(s) = v(t) = 0$ satisfies $C_1$, $C_2$, $C_3$ by their heads, $C_4$ by $\neg s$, and $C_5$ by $\neg t$.

## Remarks

The assignment found is the least model of the definite clauses $C_1$ to $C_4$: every model of them makes $p$, $q$, $r$ true.
If we add the fact $\set{s}$, the algorithm marks $s$ and then $t$ by $C_4$, and the goal clause $C_5$ has $r$ and $t$ marked, so the larger set is unsatisfiable.
If instead we drop $C_1$, nothing is marked, and the assignment that makes every variable false satisfies the set.
The algorithm never chooses a value and never backtracks, which is why it runs in linear time.

## Explanations

### L1 human

Think of the five clauses as house rules, one on each line below.
The light is on.
If the light is on, the fan is on.
If the light and the fan are on, the heater is on.
If the radio is on, the TV is on.
The heater and the TV are not both on.
From the first rule we know the light is on, and then the fan, and then the heater.
Nothing forces the radio or the TV, so we leave them off, and every rule is obeyed.

### L2 human

We use the marks and the model found to answer two queries about $S$.

1. Every model of $S$ makes $p$ true by $C_1$, then $q$ by $C_2$, then $r$ by $C_3$. So $S \models r$.
2. The model of step 8 makes $t$ false, so $S \not\models t$.

The typical use: the marked set lists all variables that every model must make true, so it answers queries of the form "does $q$ follow?".
A trap: the unmarked variables are false in the model found, but the marks do not say whether they are false in every model.
Here every model makes $r$ true, so $C_5$ makes $t$ false, and then $C_4$ makes $s$ false; so $S \models \neg t$ and $S \models \neg s$, by an argument beyond the marks.
Without $C_5$, the model $\set{p, q, r, s, t}$ shows that $s$ and $t$ can be true.
