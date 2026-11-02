---
tag: KKNB9JY1YH
kind: definition
name: Logical consequence
msc: [03B05, 03B10]
defines: 1HK0VYWTV7
uses: [09K9MWD2QQ, HYJ10AF6RT, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_consequence
---

## Definition

Let $\Gamma$ be a set of [[formulas|HYJ10AF6RT]] and $\varphi$ a formula, all over the same signature.
Then $\varphi$ is a *logical consequence* of $\Gamma$, written $\Gamma \models \varphi$, if every interpretation that makes every formula of $\Gamma$ true also makes $\varphi$ true.
In [[propositional logic|09K9MWD2QQ]] an interpretation is a truth assignment to the variables.
In first-order logic it is a [[structure|983GZBQYT4]] together with an assignment of its elements to the variables.

## Remarks

$\set{p, \; p \to q} \models q$: in every assignment where $p$ and $p \to q$ are true, $q$ is true by the truth table of $\to$.
$\set{p \to q, \; q} \not\models p$: the assignment $p = \mathsf{F}$, $q = \mathsf{T}$ makes both premises true and $p$ false.
$\emptyset \models \varphi$ means that $\varphi$ is valid, written $\models \varphi$.
$\Gamma \models \varphi$ holds exactly when $\Gamma \cup \set{\neg \varphi}$ is not [[satisfiable|QN7M1JCGT9]].
