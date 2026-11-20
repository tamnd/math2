---
tag: F5SP7HQFFS
kind: concept
name: Partial logic
aliases: [logic-of-partial-models, partial-model]
msc: ["03B50", "03B60"]
topics: [NJB94B39QK]
audience: ug2
uses: [SZHA10A9X7, 4CBCWZQZ12, 086QKPF0A6, 5DYNDW9526, HBK5QHC1GC]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section P
    note: adopted
    mention: wikipedia://en/76765067#P78W
    sections: [Summary]
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: Many-Valued Logic (SEP entry), sections 1 and 2
  - url: https://plato.stanford.edu/entries/logic-free/
    locator: Free Logic (SEP entry), section 5.2
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Kleene and Priest logics
inventory: [4PEPYE7B9T]
---

## Summary

A *partial logic* is a logic in which a statement can be neither true nor false, because of undefined terms or incomplete information.
Its models are *partial models*: each predicate has an extension, where it is true, and an anti-extension, where it is false, and the two need not cover the domain.
The connectives follow the [[strong Kleene|SZHA10A9X7]] tables, with a third value for "undefined".
So partial logic drops the principle of [[bivalence|5DYNDW9526]], and allows [[truth-value gaps|4CBCWZQZ12]], but not gluts.
Its propositional core is strong Kleene logic K3.

## Motivation

Many mathematical terms are undefined for some arguments: $x/y$ when $y = 0$, $\sqrt{x}$ for negative real $x$, and the output of a [[partial recursive function|HBK5QHC1GC]] that does not halt.
A formula such as $x/x = 1$ then has no clear truth value at $x = 0$.
Classical [[first-order logic|086QKPF0A6]] forces a value by convention, and the convention can make a specification wrong.
Partial logic instead lets the formula be undefined and tracks how undefinedness spreads through connectives.
The same idea models incomplete information: a database or a theory may settle some facts and leave others open.

## Notation

We write $\mathsf{T}$, $\mathsf{F}$ and $\mathsf{U}$ (or $1$, $0$, $\tfrac12$) for true, false and undefined.
For a predicate $P$ in a partial model, $P^{+}$ is its extension and $P^{-}$ its anti-extension, with $P^{+} \cap P^{-} = \emptyset$.
We write $t\!\downarrow$ for "$t$ is defined".

## Remarks

### Examples

- [[The formula $x = 0 \lor x/x = 1$|~d327d464]] is true for every value of $x$ under strong Kleene disjunction, although $x/x = 1$ is undefined at $0$.
- [[A partial model where excluded middle fails|~54c9495c]]: $Pa \lor \neg Pa$ is undefined when $a$ is in neither $P^{+}$ nor $P^{-}$.
- Kripke's theory of truth uses partial models of a truth predicate; the liar sentence lies in neither the extension nor the anti-extension.

### Non-examples

- [[The logic of paradox has gluts, not gaps|~0c49b351]]; it is not a partial logic in this sense.
- Classical first-order logic, where every atom is true or false in every model.

### Basic properties

- Partial models are ordered by information: $M \sqsubseteq N$ when $N$ has the same domain and extends each $P^{+}$ and each $P^{-}$. Strong Kleene evaluation is monotone in this order, so a defined value never changes when information grows.
- Consequence in the K3 sense preserves the value $\mathsf{T}$. With this consequence, partial logic has no tautologies, because the totally undefined valuation makes every formula undefined.
- An alternative consequence relation preserves $\mathsf{T}$ forward and $\mathsf{F}$ backward; it validates contraposition.
- Free logics with neutral semantics treat atoms with non-denoting terms as undefined, and so form one kind of partial logic.

### History

Kleene introduced the strong three-valued tables in 1938 to reason about partial recursive functions, with the middle value read as "undefined".
Kripke used the same tables in 1975 for his theory of truth.
The SEP entry on free logic lists logics with partial or non-strict functions as one application of free logic.

### Common errors

- To read the third value as a truth value on a par with true and false. It means the absence of a value.
- To use the weak Kleene tables by mistake. In weak Kleene logic, any undefined part makes the whole undefined, so $x = 0 \lor x/x = 1$ is undefined at $x = 0$.
- To think that partial logic rejects all classical inferences. Every K3-valid inference is classically valid, and many classical inferences remain.

## Explanations

### L1 human

Some statements have no truth value, such as "$1/0$ is positive", because $1/0$ is not a number.
Partial logic allows such statements.
It gives them the value "undefined".
A compound statement can still be true if the defined parts already decide it, as in "true or undefined".

### L2 human

We evaluate $x \neq 0 \to x/x = 1$, read as $x = 0 \lor x/x = 1$, at $x = 0$ and at $x = 2$.

1. At $x = 0$: $x = 0$ is true, so the disjunction is true, whatever the value of $x/x = 1$.
2. At $x = 2$: $x = 0$ is false, $x/x = 1$ is true, so the disjunction is true.

So the formula is true for every $x$, as a programmer would want.
A trap is to evaluate the right disjunct first and stop at "undefined"; strong Kleene disjunction looks at both sides.

### L3 human

The partial models of a first-order language form a complete partial order under information, and the evaluation maps are monotone; this is the basis of fixed-point constructions such as Kripke's.
Proof systems for partial logic include tableaux and sequent calculi with signed formulas, which record whether a formula is true, false, not true or not false.
Logics of partial functions used in program specification combine strong Kleene connectives with a definedness predicate and free-logic quantifier rules.
