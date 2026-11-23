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

"Both $p$ and $q$, or both $r$ and $s$" is the smallest formula where the distributive law starts to multiply clauses, so we use it to see the [[Tseitin transformation|S367PDDP61]] at work.
Let
$$\varphi = (p \land q) \lor (r \land s) .$$

1. The subformulas that are not variables are $p \land q$, $r \land s$ and $\varphi$.
   We name them $a$, $b$ and $c$.
2. The definition $a \leftrightarrow p \land q$ gives the [[clauses|T3SXVH3ZZC]] $\{ \neg a, p \}$, $\{ \neg a, q \}$, $\{ a, \neg p, \neg q \}$.
3. The definition $b \leftrightarrow r \land s$ gives $\{ \neg b, r \}$, $\{ \neg b, s \}$, $\{ b, \neg r, \neg s \}$.
4. The definition $c \leftrightarrow a \lor b$ gives $\{ c, \neg a \}$, $\{ c, \neg b \}$, $\{ \neg c, a, b \}$.
5. The root gives the unit clause $\{ c \}$.
   So $T(\varphi)$ has $10$ clauses in the $7$ variables $p, q, r, s, a, b, c$.
6. A model of $\varphi$ extends to a model of $T(\varphi)$.
   Take $p = q = 1$ and $r = s = 0$, and put $a = 1$, $b = 0$, $c = 1$; each of the $10$ clauses then has a true literal.
7. A model of $T(\varphi)$ gives a model of $\varphi$.
   The clause $\{ c \}$ gives $c = 1$, and $\{ \neg c, a, b \}$ gives $a = 1$ or $b = 1$.
8. If $a = 1$, then $\{ \neg a, p \}$ and $\{ \neg a, q \}$ give $p = q = 1$.
   If $b = 1$, then $r = s = 1$ in the same way, and in both cases $\varphi$ is true.

So $T(\varphi)$ is [[equisatisfiable|B37TYWXS74]] with $\varphi$.

Check: the literal count is $2 + 2 + 3$ for $a$, the same for $b$ and for $c$, and $1$ for the root, so $22$ literal occurrences in all.

## Remarks

The distributive law gives the equivalent form $(p \lor r) \land (p \lor s) \land (q \lor r) \land (q \lor s)$, with $4$ clauses and $8$ literal occurrences.
So for this small formula the Tseitin form is longer.
The advantage appears as the formula grows.
With $n$ conjunctions in place of $2$, the distributive form has $2^n$ clauses and the Tseitin form has $6n - 2$, as [[the size comparison|JZEBE7HZWQ]] shows.

The Tseitin form is not equivalent to $\varphi$.
The assignment with $p = q = r = s = 1$ and $c = 0$ makes $\varphi$ true and the clause $\{ c \}$ false.

Watch out.
Do not forget the clause $\{ c \}$.
Without it, $p = q = r = s = 0$ with $a = b = c = 0$ satisfies all the other clauses, although $\varphi$ is false.

Try it.
Find the model of $T(\varphi)$ that extends $p = 0$, $q = 1$, $r = s = 1$.
It has $a = 0$, $b = 1$, $c = 1$, the values of the three subformulas.

## Explanations

### L1 human

The rule says "both $p$ and $q$, or both $r$ and $s$".
We call the first part A, the second part B, and the whole rule C.
Then we write short rules: A holds exactly when $p$ and $q$ hold, and B exactly when $r$ and $s$ hold.
One more rule says that C holds exactly when A or B holds.
Finally we demand that C holds.
The short rules can be met exactly when the original rule can.

### L2 human

In practice a SAT solver receives the $10$ clauses and returns a model.
We read off the values of $p, q, r, s$ only, and steps 7 and 8 show that they satisfy $\varphi$.
The new variables $a, b, c$ are helpers, and their values are not part of the answer.
