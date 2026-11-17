---
tag: KH30ARM9TF
kind: example
name: Satisfaction in a two-element structure, clause by clause
msc: ["03B10"]
topics: [NJDME6F845]
audience: ug2
instance_of: [2RBQPV02AS]
uses: [1WTCZB4DVB, 983GZBQYT4, 6D3WA7N2W4]
sources:
  - book: isbn:9780122384523
    locator: Section 2.2
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Evaluation of truth values
---

## Example

Let $L = \set{c, f, R}$ with a constant symbol $c$, a unary function symbol $f$ and a binary relation symbol $R$.
Let $\mathcal{M}$ be the $L$-[[structure|983GZBQYT4]] with domain $M = \set{0, 1}$ and
$$c^{\mathcal{M}} = 0, \qquad f^{\mathcal{M}}(0) = 1, \quad f^{\mathcal{M}}(1) = 0, \qquad R^{\mathcal{M}} = \set{(0, 1)}.$$
Let $s$ be the assignment with $s(x) = 0$, $s(y) = 1$, and $s(v) = 0$ for every other variable $v$.
We apply each clause of the [[definition of satisfaction|1WTCZB4DVB]] at least once.

Values of [[terms|6D3WA7N2W4]]:

1. Variable clause: $x^{\mathcal{M}}[s] = s(x) = 0$ and $y^{\mathcal{M}}[s] = 1$.
2. Constant clause: $c^{\mathcal{M}}[s] = c^{\mathcal{M}} = 0$.
3. Function clause: $f(x)^{\mathcal{M}}[s] = f^{\mathcal{M}}(0) = 1$, and $f(f(c))^{\mathcal{M}}[s] = f^{\mathcal{M}}(f^{\mathcal{M}}(0)) = f^{\mathcal{M}}(1) = 0$.

Atomic formulas:

4. Equality: $\mathcal{M} \models (f(x) = y)[s]$, because both values are $1$.
5. Equality: $\mathcal{M} \not\models (x = y)[s]$, because $0 \neq 1$.
6. Relation: $\mathcal{M} \models R(x, f(x))[s]$, because $(0, 1) \in R^{\mathcal{M}}$.
7. Relation: $\mathcal{M} \not\models R(f(x), x)[s]$, because $(1, 0) \notin R^{\mathcal{M}}$.

Connectives:

8. Negation: $\mathcal{M} \models \neg (x = y)[s]$, because of step 5.
9. Conjunction: $\mathcal{M} \not\models (R(x, f(x)) \wedge x = y)[s]$, because the second part fails by step 5.
10. Disjunction: $\mathcal{M} \models (R(x, f(x)) \vee x = y)[s]$, because the first part holds by step 6.
11. Implication with a false hypothesis: $\mathcal{M} \models (x = y \to R(f(x), x))[s]$, because the hypothesis fails by step 5.
12. Implication with a true hypothesis: $\mathcal{M} \not\models (R(x, f(x)) \to R(f(x), x))[s]$, because the hypothesis holds by step 6 and the conclusion fails by step 7.
13. Biconditional: $\mathcal{M} \models (x = y \leftrightarrow R(f(x), x))[s]$, because both sides fail by steps 5 and 7.
14. Biconditional: $\mathcal{M} \not\models (x = y \leftrightarrow R(x, f(x)))[s]$, because the left side fails and the right side holds.

Quantifiers:

15. Existential: $\mathcal{M} \models \exists y \, R(x, y)[s]$. The variant $s[y \mapsto 1]$ sends $x$ to $0$ and $y$ to $1$, and $(0, 1) \in R^{\mathcal{M}}$. The variant $s[y \mapsto 0]$ fails, but one witness is enough.
16. Universal: $\mathcal{M} \not\models \forall x \, R(x, f(x))[s]$. The variant $s[x \mapsto 0]$ gives $(0, 1) \in R^{\mathcal{M}}$, but the variant $s[x \mapsto 1]$ gives $(1, f^{\mathcal{M}}(1)) = (1, 0) \notin R^{\mathcal{M}}$.
17. Universal: $\mathcal{M} \models \forall x \, \neg (x = f(x))[s]$. For $x \mapsto 0$ the values are $0$ and $1$, and for $x \mapsto 1$ they are $1$ and $0$; they differ in both cases.
18. Nested: $\mathcal{M} \not\models \forall x \, \exists y \, R(x, y)[s]$. For the variant $x \mapsto 1$, the further variants $y \mapsto 0$ and $y \mapsto 1$ give $(1, 0)$ and $(1, 1)$, and neither lies in $R^{\mathcal{M}}$.
19. Nested: $\mathcal{M} \models \exists x \, \forall y \, \neg R(y, x)[s]$, with the witness $x \mapsto 0$. Indeed $(0, 0) \notin R^{\mathcal{M}}$ and $(1, 0) \notin R^{\mathcal{M}}$.

## Remarks

The example shows how the clauses work together: terms first, then atomic formulas, then connectives, then quantifiers from the inside out.
The value $s(y) = 1$ plays no role in step 15, because $y$ is bound in $\exists y \, R(x, y)$.
With $s(y) = 0$ instead, step 15 gives the same answer, as the [[coincidence lemma|FM580NZ9W6]] predicts.
The value $s(x)$ does matter there: with $s(x) = 1$, step 15 fails, because $(1, 0)$ and $(1, 1)$ are not in $R^{\mathcal{M}}$.
Steps 17, 18 and 19 are sentences, so their truth values do not depend on $s$ at all.
If we change $R^{\mathcal{M}}$ to $\set{(0, 1), (1, 0)}$, steps 7, 12 and 18 become satisfied.

## Explanations

### L1 human

We take a tiny world with two objects, $0$ and $1$.
The symbol $f$ swaps them, the name $c$ points to $0$, and $R$ holds only for the pair "$0$ then $1$".
We give $x$ the value $0$ and $y$ the value $1$, and we test many formulas one by one.
For example, "$f(x)$ equals $y$" holds, because swapping $0$ gives $1$.
"For every $x$, $R(x, f(x))$" fails, because for $x = 1$ we get the pair "$1$ then $0$", which is not in $R$.

### L2 human

We redo step 18 as a full table, since nested quantifiers are the most common source of errors.

1. The formula $\forall x \, \exists y \, R(x, y)$ holds when $\exists y \, R(x, y)$ holds under both $s[x \mapsto 0]$ and $s[x \mapsto 1]$.
2. Under $s[x \mapsto 0]$, the witness $y \mapsto 1$ gives $(0, 1) \in R^{\mathcal{M}}$, so $\exists y \, R(x, y)$ holds.
3. Under $s[x \mapsto 1]$, the two candidates $y \mapsto 0$ and $y \mapsto 1$ give $(1, 0)$ and $(1, 1)$. Neither is in $R^{\mathcal{M}}$, so $\exists y \, R(x, y)$ fails.
4. One value of $x$ fails, so the universal formula fails.

The typical use of such a table is to find a countermodel: here $\mathcal{M}$ shows that $\forall x \, \exists y \, R(x, y)$ does not follow from $\exists x \, \exists y \, R(x, y)$.
A trap is to swap the quantifiers: $\exists y \, \forall x \, R(x, y)$ is a different formula, and here it is also false, because no single value of $y$ works for both values of $x$.
