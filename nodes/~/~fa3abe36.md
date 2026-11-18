---
tag: ~fa3abe36
kind: example
name: An extended resolution refutation is not a resolution refutation
msc: ["03F20", "03B35"]
topics: [CBAF7J051K]
audience: research
not_instance_of:
  - target: ~586b5042
    note: the extension clauses that define a new variable are neither clauses of F nor resolvents, so the sequence is not a resolution refutation of F
uses: [~586b5042, ~6925f591, ZDW6N1PGJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Resolution_(logic)
    locator: Resolution in propositional logic
  - url: https://en.wikipedia.org/wiki/Frege_system
    locator: Extended Frege system
---

## Example

*Extended resolution*, introduced by Tseitin, allows a new variable $z$ as a name for $a \land b$.
It adds the three *extension clauses*
$$\set{\neg z, a}, \qquad \set{\neg z, b}, \qquad \set{z, \neg a, \neg b},$$
which say $z \leftrightarrow (a \land b)$, when $z$ occurs in no earlier clause.

Let $F$ have the clauses $\set{a}$, $\set{b}$ and $\set{\neg a, \neg b}$.
Here is an extended resolution refutation of $F$.

1. $\set{\neg z, a}$, $\set{\neg z, b}$, $\set{z, \neg a, \neg b}$: extension clauses for $z$.
2. $\set{z, \neg b}$, resolvent of $\set{z, \neg a, \neg b}$ and $\set{a}$ on $a$.
3. $\set{z}$, resolvent of step 2 and $\set{b}$ on $b$.
4. $\set{\neg a, \neg z}$, resolvent of $\set{\neg a, \neg b}$ and $\set{\neg z, b}$ on $b$.
5. $\set{\neg z}$, resolvent of step 4 and $\set{a}$ on $a$.
6. $\square$, resolvent of $\set{z}$ and $\set{\neg z}$ on $z$.

This sequence is not a [[resolution refutation|~586b5042]] of $F$.
The three clauses of step 1 are not in $F$, and they are not resolvents of earlier clauses.

## Remarks

The extension clauses do not change satisfiability.
Every assignment that satisfies $F$ extends to one that satisfies $F$ and the extension clauses, by $z := a \land b$.
So extended resolution is sound.

Here the extension saves nothing, since $F$ has a refutation of $5$ clauses without $z$.
For other formulas the saving is exponential.
Cook gave polynomial-size extended resolution refutations of the [[pigeonhole formulas|~7468ccc3]] in 1976, while [[Haken's theorem|~dd16430c]] says that resolution refutations of them have exponential size.
Extended resolution is p-equivalent to [[extended Frege|~6925f591]].

## Explanations

### L1 human

A resolution proof may only combine clauses it already has.
Extended resolution may also say "let $z$ mean $a$ and $b$", and add clauses that state this definition.
Those clauses are not consequences of the given clauses alone, so the proof is not a plain resolution proof.

### L2 human

We check that the extension clauses define $z$ correctly.

1. $\set{\neg z, a}$ says $z \to a$.
2. $\set{\neg z, b}$ says $z \to b$.
3. $\set{z, \neg a, \neg b}$ says $(a \land b) \to z$.
4. Together they say $z \leftrightarrow (a \land b)$.

The typical use of the example is to separate resolution from its extension.
A trap: soundness of extended resolution needs $z$ to be new, as in the condition on [[extension variables|~6925f591]].
