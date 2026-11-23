---
tag: AMDZRKKT4J
kind: definition
name: Validity
msc: ["03B10"]
topics: [NJDME6F845]
audience: ug2
defines: 5SDS9T8E7J
uses: [1WTCZB4DVB, 983GZBQYT4, HYJ10AF6RT, KKNB9JY1YH]
sources:
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Validity, satisfiability, and logical consequence
  - book: isbn:9780122384523
    locator: Section 2.2
---

## Definition

A formula is valid when every structure satisfies it under every assignment.

Let $L$ be a signature and let $\varphi$ be an $L$-[[formula|HYJ10AF6RT]].
The formula $\varphi$ is valid, written $\models \varphi$, when $\mathcal{M} \models \varphi[s]$ for every $L$-[[structure|983GZBQYT4]] $\mathcal{M}$ and every assignment $s \colon \mathrm{Var} \to M$, in the sense of [[satisfaction|1WTCZB4DVB]].
The formula $\varphi$ is invalid when some structure and some assignment do not satisfy it, and such a pair is a countermodel to $\varphi$.

## Notation

$\models \varphi$ is the special case $\emptyset \models \varphi$ of [[logical consequence|KKNB9JY1YH]].
Structures have nonempty domains in this definition.

## Remarks

The definition quantifies over two things, the structure and the assignment.
For a sentence, the assignment does not matter, so a sentence is valid exactly when it is true in every structure.
For a formula with free variables, the assignment matters, and validity asks for every value of every free variable.

To prove validity, fix an arbitrary structure and an arbitrary assignment and use the clauses of satisfaction.
To refute validity, give one countermodel.
For example, $P(x)$ is not valid, because the structure with domain $\{0\}$, $P = \emptyset$ and $s(x) = 0$ does not satisfy it.
The [[concept page on validity|5SDS9T8E7J]] gives more examples and the link with provability.

## Explanations

### L1 human

A formula is valid when no choice of objects and no choice of meanings can make it false.

### L2 human

We check the definition on $\varphi = P(x) \to \exists y \, P(y)$.

1. Let $\mathcal{M}$ be a structure and $s$ an assignment.
   If $s(x) \notin P^{\mathcal{M}}$, the antecedent fails, and $\varphi$ holds by the clause for $\to$.
2. If $s(x) \in P^{\mathcal{M}}$, the variant $s[y \mapsto s(x)]$ satisfies $P(y)$.
3. So $\mathcal{M} \models \exists y \, P(y)[s]$ by the clause for $\exists$, and $\varphi$ holds.
4. Both cases give $\mathcal{M} \models \varphi[s]$, so $\varphi$ is valid.

The typical use is to check a logical axiom of a proof system.
Watch out: do not treat the free variable $x$ as fixed, because validity quantifies over all assignments, so $x$ ranges over all elements.
