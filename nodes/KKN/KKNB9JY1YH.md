---
tag: KKNB9JY1YH
kind: definition
name: Logical consequence
msc: ["03B05", "03B10"]
topics: [JDK63589SA]
audience: ug1
defines: 1HK0VYWTV7
uses: [~7139c138, ~41f42e3d, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_consequence
    locator: Semantic consequence
  - book: isbn:9780122384523
    locator: Chapter 1
---

## Definition

Let $P$ be a set of propositional variables, let $\Gamma$ be a set of [[propositional formulas|~7139c138]] over $P$, and let $\varphi$ be a formula over $P$.
The formula $\varphi$ is a *logical consequence* of $\Gamma$, written $\Gamma \models \varphi$, when the following holds: for every truth assignment $v : P \to \set{0, 1}$, if $\bar v(\gamma) = 1$ for every $\gamma \in \Gamma$, then $\bar v(\varphi) = 1$.
Here $\bar v$ is the [[truth valuation|~41f42e3d]] that extends $v$ to all formulas.

In first-order logic, let $\Gamma$ and $\varphi$ be formulas of one signature.
Then $\Gamma \models \varphi$ when, for every [[structure|983GZBQYT4]] $\mathcal{M}$ of the signature and every assignment $s$ of elements of $\mathcal{M}$ to the variables, if $\mathcal{M}$ satisfies every formula of $\Gamma$ under $s$, then $\mathcal{M}$ satisfies $\varphi$ under $s$.

## Notation

We write $\Gamma, \varphi \models \psi$ for $\Gamma \cup \set{\varphi} \models \psi$, and $\models \varphi$ for $\emptyset \models \varphi$.
We write $\Gamma \not\models \varphi$ when the condition fails.
The symbol $\models$ is about truth under assignments; the symbol $\vdash$ is about derivations in a proof system, and the two must not be confused.

## Remarks

- $p, \; p \to q \models q$: every assignment that makes $p$ and $p \to q$ true makes $q$ true, by the truth table of $\to$.
- $p \to q, \; q \not\models p$: the assignment $v(p) = 0$, $v(q) = 1$ makes both premises true and $p$ false.
- $\models \varphi$ says that $\varphi$ is true under every assignment, that is, $\varphi$ is a tautology.
- $\Gamma \models \varphi$ holds exactly when $\Gamma \cup \set{\neg \varphi}$ is not [[satisfiable|QN7M1JCGT9]].
- The value $\bar v(\varphi)$ depends only on the values of $v$ on the variables of $\varphi$. So for finite $\Gamma$ a finite truth table decides $\Gamma \models \varphi$.

The concept page [[logical consequence|1HK0VYWTV7]] gives examples, the basic properties and the semantic deduction theorem.

## Explanations

### L1 human

A statement follows from some other statements when no situation makes the others true and this one false.
For example, from "the light is on or the fan is on" and "the light is off" it follows that "the fan is on".
In logic, a situation is a choice of true or false for each basic statement.

### L2 human

We check $p \lor q, \; \neg p \models q$ with the definition.

1. The variables are $p$ and $q$, so there are four truth assignments.
2. The premise $\neg p$ is true only when $v(p) = 0$.
3. With $v(p) = 0$, the premise $p \lor q$ is true only when $v(q) = 1$.
4. So the only assignment that makes both premises true is $v(p) = 0$, $v(q) = 1$, and it makes $q$ true.
5. Hence $p \lor q, \; \neg p \models q$.

A trap: the definition does not ask the premises to be true in fact.
It asks that every assignment that makes them true also makes the conclusion true.
