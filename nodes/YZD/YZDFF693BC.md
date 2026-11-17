---
tag: YZDFF693BC
kind: example
name: Renaming a subformula without defining clauses
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug2
not_instance_of:
  - target: S367PDDP61
    note: The new variable gets no defining clauses, so its value is not tied to the subformula that it replaces.
uses: [S367PDDP61, B37TYWXS74, QN7M1JCGT9]
sources:
  - url: https://en.wikipedia.org/wiki/Tseytin_transformation
    locator: Approach
---

## Example

Let $\varphi = p \land \neg p$.
A false shortcut replaces the subformula $\neg p$ by a new variable $x$ and keeps no other clause.
It gives $\varphi' = p \land x$, with the clauses $\set{p}$ and $\set{x}$.
This is not the [[Tseitin transformation|S367PDDP61]].

1. The formula $\varphi$ is not [[satisfiable|QN7M1JCGT9]]. If $p = 1$, then $\neg p$ is false, and if $p = 0$, then $p$ is false.
2. The set $\set{\set{p}, \set{x}}$ is satisfied by $p = x = 1$.
3. So $\varphi$ and $\varphi'$ are not [[equisatisfiable|B37TYWXS74]], and the shortcut is wrong.
4. The missing part is the definition $x \leftrightarrow \neg p$, with the clauses $\set{\neg x, \neg p}$ and $\set{x, p}$.
5. With these clauses the set $\set{\set{p}, \set{x}, \set{\neg x, \neg p}, \set{x, p}}$ is unsatisfiable. The units force $p = x = 1$, and then $\set{\neg x, \neg p}$ is false.

## Remarks

A new variable is only a name, and a name says nothing until a clause ties it to what it names.
Without the defining clauses the new variable is free, and the solver can choose its value to suit the other clauses.
The direction that matters here is $x \to \neg p$: since $x$ occurs positively in $\varphi'$, the clause $\set{\neg x, \neg p}$ alone already makes the set unsatisfiable.

## Explanations

### L1 human

The rule "it rains and it does not rain" can never hold.
Suppose we write X for "it does not rain" but forget to say what X means.
Then "it rains and X" looks harmless, and we can make it true by choosing X to be true.
The meaning of the name was lost, and so was the contradiction.

### L2 human

Check every renaming by asking which clauses tie the new variable to its subformula.
In the Tseitin transformation each new variable gets two or three such clauses.
The trap is to rename subformulas to shorten a formula and then forget the definitions.
The result is often satisfiable even when the original formula is not.
