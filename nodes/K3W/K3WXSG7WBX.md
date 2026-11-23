---
tag: K3WXSG7WBX
kind: definition
name: Satisfiability
msc: ["03B05", "03B10"]
topics: [JDK63589SA]
audience: ug1
defines: QN7M1JCGT9
uses: [TT7WT5HPN9, H31CS3HK5P, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Satisfiability
    locator: lead section
  - book: isbn:9780122384523
    locator: Chapter 1
---

## Definition

A set of formulas is satisfiable when one assignment of truth values makes all of them true.

Let $P$ be a set of propositional variables and let $\Gamma$ be a set of [[propositional formulas|TT7WT5HPN9]] over $P$.
A truth assignment $v \colon P \to \{ 0, 1 \}$ *satisfies* $\Gamma$ when $\bar v(\gamma) = 1$ for every $\gamma \in \Gamma$, where $\bar v$ is the [[truth valuation|H31CS3HK5P]] of $v$.
The set $\Gamma$ is *satisfiable* when some truth assignment satisfies it, and *unsatisfiable* otherwise.
A formula $\varphi$ is *satisfiable* when the set $\{ \varphi \}$ is satisfiable.
The set $\Gamma$ is *finitely satisfiable* when every finite subset of $\Gamma$ is satisfiable.

In first-order logic, let $\Gamma$ be a set of formulas of one signature.
Then $\Gamma$ is *satisfiable* when some [[structure|983GZBQYT4]] $\mathcal{M}$ of the signature and some assignment $s$ of elements of $\mathcal{M}$ to the variables make every formula of $\Gamma$ true.

## Notation

We write $v \models \Gamma$ when $v$ satisfies $\Gamma$, and $v \models \varphi$ when $v$ satisfies $\varphi$.
In first-order logic one writes $\mathcal{M} \models \varphi[s]$.
In this use $\models$ has an assignment or a structure on its left, while in logical consequence $\Gamma \models \varphi$ it has a set of formulas on its left.

## Remarks

### One set of each kind

The set $\{ p \lor q, \; \neg p \lor r, \; \neg q \}$ is satisfiable, by $v(p) = 1$, $v(q) = 0$, $v(r) = 1$.
The set $\{ p, \; p \to q, \; \neg q \}$ is unsatisfiable, because $p$ and $p \to q$ force $q = 1$.

### How it links to other notions

$\Gamma \models \varphi$ holds exactly when $\Gamma \cup \{ \neg \varphi \}$ is unsatisfiable, and $\varphi$ is valid exactly when $\neg \varphi$ is unsatisfiable.
The concept page [[satisfiability|QN7M1JCGT9]] proves both.
Every satisfiable set is finitely satisfiable, and the converse is the [[compactness theorem|4X9126SEMM]].

Watch out.
"Satisfiable" asks for one assignment that works for all members together.
A set can be unsatisfiable although each of its members is satisfiable alone.

## Explanations

### L1 human

A collection of statements is satisfiable when they can all be true together.
"It is warm" and "it is sunny" are satisfiable together.
"It is warm" and "it is not warm" are not.

### L2 human

We check that $\{ p \to q, \; \neg q \}$ is satisfiable.

1. The member $\neg q$ needs $v(q) = 0$.
2. With $v(q) = 0$, the member $p \to q$ needs $v(p) = 0$.
3. The assignment $v(p) = v(q) = 0$ makes both members true, so the set is satisfiable.

Check: $0 \to 0 = 1$ and $\neg 0 = 1$.
If we add $p$, the set $\{ p \to q, \; \neg q, \; p \}$ becomes unsatisfiable, since step 2 forced $v(p) = 0$.
