---
tag: SZHA10A9X7
kind: concept
name: Strong Kleene logic
aliases: [strong-kleene-connectives, k3]
msc: ["03B50"]
topics: [WZP584JQ06]
audience: grad
uses: [DWYCKAKXZD, P7E926JK13, TFDYXS3K1N]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section S
    note: adopted
    mention: wikipedia://en/76765067#9VXY
    sections: [Summary]
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: "2.2 From two to three truth values: gaps and gluts"
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Kleene and Priest logics
inventory: [907BAF6V51]
---

## Summary

Here is excluded middle in strong Kleene logic, with $0$ for false, $1$ for true and $\tfrac12$ for undefined.

| $p$ | $\neg p$ | $p \lor \neg p$ |
|---|---|---|
| $0$ | $1$ | $1$ |
| $\tfrac12$ | $\tfrac12$ | $\tfrac12$ |
| $1$ | $0$ | $1$ |

Negation is $1 - x$ and disjunction is $\max$, so the middle row gives $\max(\tfrac12, \tfrac12) = \tfrac12$.
When $p$ has no value, "$p$ or not $p$" has no value either, and the law fails.

Exactly, as in [[the definition|74R8A41V6M]], *strong Kleene logic* $\mathsf{K}_3$ is the [[many-valued logic|DWYCKAKXZD]] of a matrix with values $\{0, \tfrac12, 1\}$ and designated set $\{1\}$.
Its operations are $\neg x = 1 - x$, $x \land y = \min(x, y)$ and $x \lor y = \max(x, y)$.
Implication is the abbreviation $\neg \varphi \lor \psi$.
A compound gets a classical value whenever the classical values of its parts already decide it.
$\mathsf{K}_3$ has [[no tautologies|ND17WYDNA5]], yet it has a rich consequence relation, and it is the standard logic of truth-value gaps.

## Motivation

Kleene studied predicates computed by partial recursive functions, which may fail to give an answer.
Evaluate "$P$ or $Q$" by running the computations of $P$ and $Q$ in parallel, one step of each in turn.
The run can answer "true" as soon as one of them answers "true", even if the other never stops.
It can answer "false" only after both have answered "false".
The strong Kleene tables record exactly what such a parallel run can decide, as [[the example with partial predicates|DSFTFBFADA]] checks case by case.
So the value $\tfrac12$ is not a third answer; it is the absence of an answer.

## Notation

The values are also written $\mathbf{t}$, $\mathbf{f}$ and $\mathbf{u}$, as in Kleene's 1952 book.
The algebra $\langle \{0, \tfrac12, 1\}, \neg, \land, \lor \rangle$ is the three-element Kleene algebra; see also [[Kleene connectives|B7KATP4SEA]].
With the designated set $\{\tfrac12, 1\}$ instead, the same tables give Priest's [[logic of paradox|BXJZG67PX3]] $\mathsf{LP}$.

## Remarks

### No laws, many rules

[[K3 has no tautologies|ND17WYDNA5]], because the valuation that gives every variable the value $\tfrac12$ gives every formula the value $\tfrac12$.
[[Even p → p fails|MBVRGSV45Y]], since it abbreviates $\neg p \lor p$.
Valid inferences are still plentiful: $p \land q \models p$, $p \models p \lor q$, modus ponens $p, \neg p \lor q \models q$ and De Morgan's laws in both directions.
Explosion $p \land \neg p \models q$ is valid, since $\min(x, 1 - x) \le \tfrac12$ and the premise is never designated.
Every valid inference of $\mathsf{K}_3$ is classically valid, by restricting to valuations into $\{0, 1\}$.

### The order of information

Order the values by information, with $\tfrac12$ below $0$ and below $1$.
Every formula defines a function that is monotone in this order, as [[the proof by an invariant|GWPJHN5CNB]] shows in steps 6 to 10.
So filling in a missing value can never change a classical value that was already there.
This is the property that the parallel evaluation of the motivation requires.

### Neighbors on the same values

[[Łukasiewicz's three-valued logic is not K3|61J1PFA9CW]]: the implications differ only at $\tfrac12 \to \tfrac12$, where Łukasiewicz gives $1$.
[[Weak Kleene logic|BCK5QXQXA6]] is not $\mathsf{K}_3$ either, since [[it gives 1 ∨ 1/2 = 1/2|AHM8HYZDMM]].
[[One formula in all three logics|XZ2NRGZ69N]] puts the three tables side by side.
$\mathsf{LP}$ shares the tables and designates $\tfrac12$ as well, and [[the comparison with LP|BJMXHXJ7QQ]] shows how the two logics trade explosion for excluded middle.

### Inside first-degree entailment

$\mathsf{K}_3$ is the restriction of the [[Belnap-Dunn matrix|AWEG5PR3GF]] to the values true, false and neither.
So every inference valid in [[first-degree entailment|KXTP4P3GHT]] is valid in $\mathsf{K}_3$, and [[explosion separates them|QZ9FRRH7Y1]].

### Watch out

Do not read "no tautologies" as "no logic"; the consequence relation above is far from empty.
Do not use Łukasiewicz implication here: the strong Kleene implication is $\max(1 - x, y)$, with $\tfrac12 \to \tfrac12 = \tfrac12$.
Do not read $\tfrac12$ as "both true and false"; that is the reading of $\mathsf{LP}$, which designates it.
The deduction theorem fails: $p \models p$ holds, while $p \to p$ is not a tautology.

### History

Kleene introduced the strong tables in 1938, to reason about partial recursive functions.
His 1952 book *Introduction to Metamathematics* presented them with the values $\mathbf{t}$, $\mathbf{f}$ and $\mathbf{u}$.
Kripke used the strong Kleene tables in his 1975 theory of truth, with the middle value as a truth-value gap.

### Try it

First, is $p \models \neg\neg p$ valid in $\mathsf{K}_3$?
Yes: $\neg\neg x = 1 - (1 - x) = x$, so the premise and the conclusion always have the same value.

Second, find the values of $(p \to q) \lor (q \to p)$ at $p = \tfrac12$, $q = 0$ and at $p = q = \tfrac12$.
At the first, $p \to q = \max(\tfrac12, 0) = \tfrac12$ and $q \to p = \max(1, \tfrac12) = 1$, so the value is $1$.
At the second, both disjuncts are $\tfrac12$, so the value is $\tfrac12$ and the formula is not a tautology.

## Explanations

### L1 human

Strong Kleene logic has three values: true, false and undefined.
"True or undefined" is true, because one true part is enough for "or".
"False and undefined" is false, because one false part is enough for "and".
But "undefined or not undefined" stays undefined, so even "$p$ or not $p$" is not a law.

### L2 human

We check that $\neg(p \land q) \models \neg p \lor \neg q$ in $\mathsf{K}_3$.

1. The premise has the value $\neg(x \land y) = 1 - \min(x, y)$.
2. The conclusion has the value $\neg x \lor \neg y = \max(1 - x, 1 - y) = 1 - \min(x, y)$.
3. The two values are equal for all $x$ and $y$, so the premise is designated iff the conclusion is.

The typical use is to reason with partial information, where some atomic sentences have no value yet.
Watch out: the law $\neg(p \land q) \to (\neg p \lor \neg q)$ is still not a tautology, since every formula has value $\tfrac12$ when all variables do.

### L3 human

Strong Kleene logic is the logic of the three-element Kleene algebra with the top designated.
Its monotonicity in the information order is the key to Kripke's construction of a fixed point for the truth predicate, which belongs to the theory of truth and the semantic paradoxes.
Inside [[first-degree entailment|KXTP4P3GHT]], $\mathsf{K}_3$ and $\mathsf{LP}$ are the two three-valued extensions: one drops the value "both", the other drops "neither".
