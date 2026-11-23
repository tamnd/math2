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

Let $L = \{c, f, R\}$ with a constant symbol $c$, a unary function symbol $f$ and a binary relation symbol $R$.
Let $\mathcal{M}$ be the $L$-[[structure|983GZBQYT4]] with domain $M = \{0, 1\}$ and
$$c^{\mathcal{M}} = 0, \qquad f^{\mathcal{M}}(0) = 1, \quad f^{\mathcal{M}}(1) = 0, \qquad R^{\mathcal{M}} = \{ (0, 1) \}.$$
So $f$ swaps the two elements, and $R$ holds only for the pair "$0$ then $1$".
Let $s$ be the assignment with $s(x) = 0$, $s(y) = 1$, and $s(v) = 0$ for every other variable $v$.
We apply each clause of the [[definition of satisfaction|1WTCZB4DVB]] at least once, in the order terms, atomic formulas, connectives, quantifiers.

First the values of [[terms|6D3WA7N2W4]]:

1. Variables: $x^{\mathcal{M}}[s] = s(x) = 0$ and $y^{\mathcal{M}}[s] = 1$.
2. Constants: $c^{\mathcal{M}}[s] = c^{\mathcal{M}} = 0$.
3. Functions: $f(x)^{\mathcal{M}}[s] = f^{\mathcal{M}}(0) = 1$, and $f(f(c))^{\mathcal{M}}[s] = f^{\mathcal{M}}(f^{\mathcal{M}}(0)) = f^{\mathcal{M}}(1) = 0$.

Then the atomic formulas:

4. $\mathcal{M} \models (f(x) = y)[s]$, because both values are $1$.
5. $\mathcal{M} \not\models (x = y)[s]$, because $0 \neq 1$.
6. $\mathcal{M} \models R(x, f(x))[s]$, because $(0, 1) \in R^{\mathcal{M}}$.
7. $\mathcal{M} \not\models R(f(x), x)[s]$, because $(1, 0) \notin R^{\mathcal{M}}$.

Then the connectives, each one reduced to the steps above:

8. $\mathcal{M} \models \neg (x = y)[s]$, by step 5.
9. $\mathcal{M} \not\models (R(x, f(x)) \wedge x = y)[s]$, because the second conjunct fails by step 5.
10. $\mathcal{M} \models (R(x, f(x)) \vee x = y)[s]$, because the first disjunct holds by step 6.
11. $\mathcal{M} \models (x = y \to R(f(x), x))[s]$, because the hypothesis fails by step 5.
12. $\mathcal{M} \not\models (R(x, f(x)) \to R(f(x), x))[s]$, because the hypothesis holds by step 6 and the conclusion fails by step 7.
13. $\mathcal{M} \models (x = y \leftrightarrow R(f(x), x))[s]$, because both sides fail, by steps 5 and 7.
14. $\mathcal{M} \not\models (x = y \leftrightarrow R(x, f(x)))[s]$, because the left side fails and the right side holds.

Last the quantifiers, where each clause looks at variants of $s$:

15. $\mathcal{M} \models \exists y \, R(x, y)[s]$.
    The variant $s[y \mapsto 1]$ sends $x$ to $0$ and $y$ to $1$, and $(0, 1) \in R^{\mathcal{M}}$, so one witness exists.
16. $\mathcal{M} \not\models \forall x \, R(x, f(x))[s]$.
    The variant $s[x \mapsto 0]$ gives $(0, 1) \in R^{\mathcal{M}}$, but the variant $s[x \mapsto 1]$ gives $(1, 0) \notin R^{\mathcal{M}}$.
17. $\mathcal{M} \models \forall x \, \neg (x = f(x))[s]$.
    For $x \mapsto 0$ the two values are $0$ and $1$, and for $x \mapsto 1$ they are $1$ and $0$, so they differ in both cases.
18. $\mathcal{M} \not\models \forall x \, \exists y \, R(x, y)[s]$.
    Under the variant $x \mapsto 1$, the further variants $y \mapsto 0$ and $y \mapsto 1$ give $(1, 0)$ and $(1, 1)$, and neither lies in $R^{\mathcal{M}}$.
19. $\mathcal{M} \models \exists x \, \forall y \, \neg R(y, x)[s]$, with the witness $x \mapsto 0$.
    Both $(0, 0)$ and $(1, 0)$ lie outside $R^{\mathcal{M}}$.

## Remarks

The clauses work from the inside out: terms first, then atomic formulas, then connectives, then quantifiers.
In step 15 the value $s(y) = 1$ plays no role, because $y$ is bound in $\exists y \, R(x, y)$.
With $s(y) = 0$ the answer is the same, as the [[coincidence lemma|FM580NZ9W6]] predicts.
The value $s(x)$ does matter there: with $s(x) = 1$, step 15 fails, because $(1, 0)$ and $(1, 1)$ are not in $R^{\mathcal{M}}$.
Steps 17, 18 and 19 are sentences, so their truth values do not depend on $s$ at all.

Now change one parameter, and let $R^{\mathcal{M}} = \{ (0, 1), (1, 0) \}$, so that $R$ becomes symmetric.
Then steps 7, 12, 16 and 18 become satisfied, because $(1, 0)$ is now in $R^{\mathcal{M}}$.
Steps 13 and 19 now fail.
In step 13 the left side is still false while the right side is now true.
In step 19 each candidate $x$ now has some $y$ with $R(y, x)$, namely $y = 1$ for $x = 0$ and $y = 0$ for $x = 1$.

## Explanations

### L1 human

We take a tiny world with two objects, $0$ and $1$.
The symbol $f$ swaps them, the name $c$ points to $0$, and $R$ holds only for the pair "$0$ then $1$".
We give $x$ the value $0$ and $y$ the value $1$, and we test many formulas one by one.
For example, "$f(x)$ equals $y$" holds, because swapping $0$ gives $1$.
"For every $x$, $R(x, f(x))$" fails, because for $x = 1$ we get the pair "$1$ then $0$", which is not in $R$.

### L2 human

We redo step 18 as a full search, since nested quantifiers cause the most errors.
The formula $\forall x \, \exists y \, R(x, y)$ holds when $\exists y \, R(x, y)$ holds under both $s[x \mapsto 0]$ and $s[x \mapsto 1]$.
Under $s[x \mapsto 0]$, the witness $y \mapsto 1$ gives $(0, 1) \in R^{\mathcal{M}}$, so the inner formula holds.
Under $s[x \mapsto 1]$, the two candidates give
$$(1, 0) \notin R^{\mathcal{M}}, \qquad (1, 1) \notin R^{\mathcal{M}},$$
so the inner formula fails, and one failing value of $x$ is enough to make the universal formula fail.

The typical use of such a search is to find a countermodel.
Here $\mathcal{M}$ shows that $\forall x \, \exists y \, R(x, y)$ does not follow from $\exists x \, \exists y \, R(x, y)$.
Watch out: $\exists y \, \forall x \, R(x, y)$ is a different formula, and here it is false too, because no single value of $y$ works for both values of $x$.
