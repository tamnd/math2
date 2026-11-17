---
tag: 9SSASE41M5
kind: example
name: Tseitin transformation of a disjunction of conjunctions
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug2
instance_of: [S367PDDP61]
uses: [S367PDDP61, T3SXVH3ZZC, B37TYWXS74]
sources:
  - url: https://en.wikipedia.org/wiki/Tseytin_transformation
    locator: Examples
---

## Example

We apply the [[Tseitin transformation|S367PDDP61]] to $\varphi = (p \land q) \lor (r \land s)$.

1. The subformulas that are not variables are $p \land q$, $r \land s$ and $\varphi$. We name them $a$, $b$ and $c$.
2. The definition $a \leftrightarrow p \land q$ gives the [[clauses|T3SXVH3ZZC]] $\set{\neg a, p}$, $\set{\neg a, q}$, $\set{a, \neg p, \neg q}$.
3. The definition $b \leftrightarrow r \land s$ gives $\set{\neg b, r}$, $\set{\neg b, s}$, $\set{b, \neg r, \neg s}$.
4. The definition $c \leftrightarrow a \lor b$ gives $\set{c, \neg a}$, $\set{c, \neg b}$, $\set{\neg c, a, b}$.
5. The root gives the unit clause $\set{c}$. So $T(\varphi)$ has 10 clauses in the 7 variables $p, q, r, s, a, b, c$.
6. A model of $\varphi$ extends to a model of $T(\varphi)$. Take $p = q = 1$ and $r = s = 0$, and put $a = 1$, $b = 0$, $c = 1$. Each of the 10 clauses then has a true literal.
7. A model of $T(\varphi)$ gives a model of $\varphi$. The clause $\set{c}$ gives $c = 1$, and $\set{\neg c, a, b}$ gives $a = 1$ or $b = 1$.
8. If $a = 1$, then $\set{\neg a, p}$ and $\set{\neg a, q}$ give $p = q = 1$. If $b = 1$, then $r = s = 1$ in the same way. In both cases $\varphi$ is true.

So $T(\varphi)$ is [[equisatisfiable|B37TYWXS74]] with $\varphi$.

## Remarks

The distributive law gives the equivalent CNF $(p \lor r) \land (p \lor s) \land (q \lor r) \land (q \lor s)$, with 4 clauses and 8 literal occurrences.
The Tseitin form has 10 clauses and 22 literal occurrences, so for this small formula it is longer.
The advantage appears as the formula grows.
With $n$ conjunctions instead of 2, the distributive CNF has $2^n$ clauses and the Tseitin form has $6 n - 2$; see [[the size comparison|JZEBE7HZWQ]].
The Tseitin form is not equivalent to $\varphi$: the assignment with $p = q = r = s = 1$ and $c = 0$ makes $\varphi$ true and $T(\varphi)$ false.

## Explanations

### L1 human

The rule says "both p and q, or both r and s".
We call the first part A, the second part B, and the whole rule C.
Then we write short rules: A holds exactly when p and q hold, and B exactly when r and s hold.
One more rule says that C holds exactly when A or B holds.
Finally we demand that C holds.
The short rules can be met exactly when the original rule can.

### L2 human

The worked example above checks both directions of the equisatisfiability.
In practice a SAT solver receives the 10 clauses and returns a model, and one reads off the values of $p, q, r, s$ only.
The new variables $a, b, c$ are helpers.
A trap is to forget the clause $\set{c}$: without it, $p = q = r = s = 0$ and $a = b = c = 0$ satisfy all the other clauses, although $\varphi$ is false.
