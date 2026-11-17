---
tag: FPJFV3R8QP
kind: example
name: Negation and implication form a functionally complete set
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
instance_of: [TDZVCWYJ9F]
uses: [029JBBF693, 0NMG7W7Q11, 05RSK4Q657, 0GVDFAY4KW]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_completeness
    locator: Minimal functionally complete operator sets
  - book: isbn:9781482237726
    locator: Chapter 1
---

## Example

We show that $\set{\neg, \to}$ is [[functionally complete|TDZVCWYJ9F]], with [[negation|029JBBF693]] and [[implication|0NMG7W7Q11]].

1. The set $\set{\neg, \land, \lor}$ is functionally complete, by the full [[disjunctive normal form|0GVDFAY4KW]]. So it is enough to express $\land$ and $\lor$ with $\neg$ and $\to$.
2. We claim $p \lor q \equiv \neg p \to q$. The implication $\neg p \to q$ is false only when $\neg p$ is true and $q$ is false, that is, at $p = 0$, $q = 0$. This is also the only row where $p \lor q$ is false.
3. We claim $p \land q \equiv \neg(p \to \neg q)$. The implication $p \to \neg q$ is false only when $p$ is true and $\neg q$ is false, that is, at $p = 1$, $q = 1$. So its negation is true only at $p = q = 1$, like $p \land q$.
4. The [[truth table|05RSK4Q657]] confirms steps 2 and 3:

| $p$ | $q$ | $\neg p \to q$ | $p \lor q$ | $p \to \neg q$ | $\neg(p \to \neg q)$ | $p \land q$ |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| 1 | 0 | 1 | 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 | 1 | 1 |

5. Replace, from the inside out, each $\alpha \lor \beta$ by $\neg\alpha \to \beta$ and each $\alpha \land \beta$ by $\neg(\alpha \to \neg\beta)$ in a formula over $\set{\neg, \land, \lor}$. Each replacement keeps the truth function, by step 4.
6. So every truth function is expressed by a formula over $\set{\neg, \to}$.

## Remarks

This is the reason why the [[Hilbert system|1MGMQX43B8]] L has only the connectives $\neg$ and $\to$: the definitions $\varphi \lor \psi := \neg\varphi \to \psi$ and $\varphi \land \psi := \neg(\varphi \to \neg\psi)$ of step 5 are its abbreviations.
The set is minimal: $\set{\to}$ alone is not complete, because every formula over it is true when all its variables are true, and $\set{\neg}$ alone is not complete, because every formula over it has one variable.
The biconditional is expressed by $p \leftrightarrow q \equiv \neg((p \to q) \to \neg(q \to p))$, from step 3 with $(p \to q) \land (q \to p)$.

## Explanations

### L1 human

"Not" and "if, then" can say everything.
"$p$ or $q$" means "if not $p$, then $q$": if $p$ fails, $q$ must hold.
"$p$ and $q$" means "it is not the case that $p$ excludes $q$", that is, "not (if $p$, then not $q$)".
With "not", "and" and "or" we can describe every truth table, so "not" and "if, then" can too.

### L2 human

A typical use is to shorten proofs by induction on formulas.
If the language has only $\neg$ and $\to$, an induction has a base case and two steps, instead of five steps.
A trap: $p \lor q$ is not $p \to q$ and not $\neg p \to \neg q$.
At $p = 1$, $q = 0$, the formula $p \lor q$ is true, but $p \to q$ is false.
At $p = 0$, $q = 1$, the formula $p \lor q$ is true, but $\neg p \to \neg q$ is false.
