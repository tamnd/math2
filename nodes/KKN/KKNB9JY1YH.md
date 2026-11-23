---
tag: KKNB9JY1YH
kind: definition
name: Logical consequence
msc: ["03B05", "03B10"]
topics: [JDK63589SA]
audience: ug1
defines: 1HK0VYWTV7
uses: [TT7WT5HPN9, H31CS3HK5P, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_consequence
    locator: Semantic consequence
  - book: isbn:9780122384523
    locator: Chapter 1
---

## Definition

Logical consequence is the relation "every interpretation that makes the premises true makes the conclusion true".

Let $P$ be a set of propositional variables, let $\Gamma$ be a set of [[propositional formulas|TT7WT5HPN9]] over $P$, and let $\varphi$ be a formula over $P$.
The formula $\varphi$ is a *logical consequence* of $\Gamma$, written $\Gamma \models \varphi$, when for every truth assignment $v \colon P \to \{ 0, 1 \}$,
$$\bar v(\gamma) = 1 \text{ for every } \gamma \in \Gamma \implies \bar v(\varphi) = 1 .$$
Here $\bar v$ is the [[truth valuation|H31CS3HK5P]] that extends $v$ to all formulas.

In first-order logic, let $\Gamma$ and $\varphi$ be formulas of one signature.
Then $\Gamma \models \varphi$ when, for every [[structure|983GZBQYT4]] $\mathcal{M}$ of the signature and every assignment $s$ of elements of $\mathcal{M}$ to the variables, if $\mathcal{M}$ satisfies every formula of $\Gamma$ under $s$, then $\mathcal{M}$ satisfies $\varphi$ under $s$.

## Notation

We write $\Gamma, \varphi \models \psi$ for $\Gamma \cup \{ \varphi \} \models \psi$, and $\models \varphi$ for $\emptyset \models \varphi$.
We write $\Gamma \not\models \varphi$ when the condition fails.
The symbol $\models$ is about truth under assignments, and the symbol $\vdash$ is about derivations in a proof system.

## Remarks

### Reading the definition

The definition is a "for every" statement over assignments, with an "if ... then" inside.
So it fails only when some assignment makes every premise true and the conclusion false, and such an assignment is a countermodel.
It holds automatically when no assignment makes all of $\Gamma$ true, because then the "if" part is never met.
With $\Gamma = \emptyset$ the "if" part is always met, so $\models \varphi$ says that $\varphi$ is a tautology.

The assignment ranges over all of $P$, but only the variables in $\Gamma \cup \{ \varphi \}$ matter, because the value of a formula depends only on its own variables.
So for finite $\Gamma$ a finite truth table decides $\Gamma \models \varphi$.

### One case that holds and one that fails

$p, \; p \to q \models q$ holds: an assignment that makes $p$ and $p \to q$ true has $p = 1$, and the table of $\to$ then forces $q = 1$.
$p \to q, \; q \not\models p$: the assignment $p = 0$, $q = 1$ makes both premises true and $p$ false.

In general, $\Gamma \models \varphi$ holds exactly when $\Gamma \cup \{ \neg \varphi \}$ is not [[satisfiable|QN7M1JCGT9]].
The concept page [[logical consequence|1HK0VYWTV7]] gives more examples, the basic rules and the semantic deduction theorem.

## Explanations

### L1 human

A statement follows from some other statements when no situation makes the others true and this one false.
For example, from "the light is on or the fan is on" and "the light is off" it follows that "the fan is on".
In logic, a situation is a choice of true or false for each basic statement.

### L2 human

We check $p \lor q, \; \neg p \models q$ with the definition.
There are four assignments to $p$ and $q$.
The premise $\neg p$ is true only when $p = 0$, and then $p \lor q$ is true only when $q = 1$.
So the only assignment that makes both premises true is $p = 0$, $q = 1$, and it makes $q$ true.
Check: the definition asks only about this one row, and the conclusion holds there.

Watch out.
The definition does not ask the premises to be true in fact.
It asks that every assignment that makes them true also makes the conclusion true.
