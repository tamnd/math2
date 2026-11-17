---
tag: K3WXSG7WBX
kind: definition
name: Satisfiability
msc: ["03B05", "03B10"]
topics: [JDK63589SA]
audience: ug1
defines: QN7M1JCGT9
uses: [~7139c138, ~41f42e3d, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Satisfiability
    locator: lead section
  - book: isbn:9780122384523
    locator: Chapter 1
---

## Definition

Let $P$ be a set of propositional variables and let $\Gamma$ be a set of [[propositional formulas|~7139c138]] over $P$.

1. A truth assignment $v : P \to \set{0, 1}$ *satisfies* $\Gamma$ when $\bar v(\gamma) = 1$ for every $\gamma \in \Gamma$, where $\bar v$ is the [[truth valuation|~41f42e3d]] of $v$.
2. The set $\Gamma$ is *satisfiable* when some truth assignment satisfies it, and *unsatisfiable* otherwise.
3. A formula $\varphi$ is *satisfiable* when the set $\set{\varphi}$ is satisfiable.
4. The set $\Gamma$ is *finitely satisfiable* when every finite subset of $\Gamma$ is satisfiable.

In first-order logic, let $\Gamma$ be a set of formulas of a signature.
Then $\Gamma$ is *satisfiable* when some [[structure|983GZBQYT4]] $\mathcal{M}$ of the signature and some assignment $s$ of elements of $\mathcal{M}$ to the variables make every formula of $\Gamma$ true.

## Notation

We write $v \models \Gamma$ when $v$ satisfies $\Gamma$, and $v \models \varphi$ when $v$ satisfies $\varphi$.
In first-order logic one writes $\mathcal{M} \models \varphi[s]$.
This use of $\models$ has an assignment or a structure on its left; the use $\Gamma \models \varphi$ for logical consequence has a set of formulas on its left.

## Remarks

- The set $\set{p \lor q, \; \neg p \lor r, \; \neg q}$ is satisfiable, by $v(p) = 1$, $v(q) = 0$, $v(r) = 1$.
- The set $\set{p, \; p \to q, \; \neg q}$ is unsatisfiable.
- $\Gamma \models \varphi$ holds exactly when $\Gamma \cup \set{\neg \varphi}$ is unsatisfiable, and $\varphi$ is valid exactly when $\neg \varphi$ is unsatisfiable. The concept page [[satisfiability|QN7M1JCGT9]] proves both.
- Every satisfiable set is finitely satisfiable. The converse is the compactness theorem.

## Explanations

### L1 human

A collection of statements is satisfiable when they can all be true together.
"It is warm" and "it is sunny" are satisfiable together.
"It is warm" and "it is not warm" are not.

### L2 human

We check that $\set{p \to q, \; \neg q}$ is satisfiable.

1. The member $\neg q$ needs $v(q) = 0$.
2. With $v(q) = 0$, the member $p \to q$ needs $v(p) = 0$.
3. The assignment $v(p) = v(q) = 0$ makes both members true, so the set is satisfiable.

A trap: if we add $p$, the set $\set{p \to q, \; \neg q, \; p}$ becomes unsatisfiable, although each member alone is satisfiable.
