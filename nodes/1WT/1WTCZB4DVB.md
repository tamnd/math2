---
tag: 1WTCZB4DVB
kind: definition
name: Satisfaction
msc: ["03B10", "03C07"]
topics: [NJDME6F845]
audience: ug2
defines: 2RBQPV02AS
uses: [983GZBQYT4, HYJ10AF6RT, 6D3WA7N2W4, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Evaluation of truth values
  - book: isbn:9780122384523
    locator: Section 2.2
  - url: https://builds.openlogicproject.org/
    locator: Syntax and Semantics
---

## Definition

Satisfaction is the relation between a structure, a formula and an assignment of values to the variables that says when the formula holds.

Let $L$ be a signature, and let $\mathcal{M}$ be an $L$-[[structure|983GZBQYT4]] with domain $M$.
A variable assignment in $\mathcal{M}$ is a [[function|0EPAT51DXQ]] $s$ from the set of all variables to $M$.
For a variable $x$ and an element $a \in M$, the $x$-variant $s[x \mapsto a]$ sends $x$ to $a$ and each variable $y \neq x$ to $s(y)$.

The value $t^{\mathcal{M}}[s] \in M$ of a [[term|6D3WA7N2W4]] $t$ is defined by recursion on $t$: $x^{\mathcal{M}}[s] = s(x)$ for a variable $x$, $c^{\mathcal{M}}[s] = c^{\mathcal{M}}$ for a constant symbol $c$, and
$$f(t_1, \ldots, t_n)^{\mathcal{M}}[s] = f^{\mathcal{M}}(t_1^{\mathcal{M}}[s], \ldots, t_n^{\mathcal{M}}[s]).$$

The relation $\mathcal{M} \models \varphi[s]$ is defined by recursion on the [[formula|HYJ10AF6RT]] $\varphi$.

1. $\mathcal{M} \models (t_1 = t_2)[s]$ if and only if $t_1^{\mathcal{M}}[s] = t_2^{\mathcal{M}}[s]$.
2. For an $n$-ary relation symbol $R$, $\mathcal{M} \models R(t_1, \ldots, t_n)[s]$ if and only if $(t_1^{\mathcal{M}}[s], \ldots, t_n^{\mathcal{M}}[s]) \in R^{\mathcal{M}}$.
3. $\mathcal{M} \models \neg \varphi[s]$ if and only if $\mathcal{M} \not\models \varphi[s]$.
4. $\mathcal{M} \models (\varphi \wedge \psi)[s]$ if and only if $\mathcal{M} \models \varphi[s]$ and $\mathcal{M} \models \psi[s]$.
5. $\mathcal{M} \models (\varphi \vee \psi)[s]$ if and only if $\mathcal{M} \models \varphi[s]$ or $\mathcal{M} \models \psi[s]$.
6. $\mathcal{M} \models (\varphi \to \psi)[s]$ if and only if $\mathcal{M} \not\models \varphi[s]$ or $\mathcal{M} \models \psi[s]$.
7. $\mathcal{M} \models (\varphi \leftrightarrow \psi)[s]$ if and only if $s$ satisfies both $\varphi$ and $\psi$ in $\mathcal{M}$, or neither of them.
8. $\mathcal{M} \models \forall x \, \varphi[s]$ if and only if $\mathcal{M} \models \varphi[s[x \mapsto a]]$ for every $a \in M$.
9. $\mathcal{M} \models \exists x \, \varphi[s]$ if and only if $\mathcal{M} \models \varphi[s[x \mapsto a]]$ for some $a \in M$.

## Notation

Equality $=$ is a logical symbol, and the connectives are $\neg$, $\wedge$, $\vee$, $\to$ and $\leftrightarrow$.
The notation $\mathcal{M} \models \varphi[s]$ follows Enderton, who writes $\models_{\mathfrak{A}} \varphi[s]$.
When the free variables of $\varphi$ are among $x_1, \ldots, x_n$, the notation $\mathcal{M} \models \varphi[a_1, \ldots, a_n]$ means $\mathcal{M} \models \varphi[s]$ for any $s$ with $s(x_i) = a_i$.
In Mathlib the relation is `FirstOrder.Language.Formula.Realize`, and the value of a term is `FirstOrder.Language.Term.realize`.

## Remarks

The recursion is well defined because each formula is built in exactly one way from its immediate parts, by the unique readability of formulas.
The term clauses need $f^{\mathcal{M}}$ to be total, which the definition of a structure guarantees.

Clauses 8 and 9 use $x$-variants, so only the value of $x$ changes and every other variable keeps its value.
They do not substitute names for $x$, because most elements of an infinite structure, such as most real numbers in $(\mathbb{R}, <)$, are not the value of any closed term.
The [[concept page on satisfaction|2RBQPV02AS]] shows a two-element structure in which the rule of names gives the wrong answer.
Clause 9 also shows why the domain must be nonempty: with $M = \emptyset$ there would be no variable assignments at all.

Books that take only $\neg$, $\to$ and $\forall$ as primitive treat the other symbols as abbreviations, and clauses 4, 5, 7 and 9 then become consequences.
For a small example, in $(\{0, 1, 2\}, <)$ with $s(x) = 2$, clause 9 shows that $\exists y \, (y < x)$ is satisfied, with $a = 0$, while clause 8 shows that $\forall y \, (y < x)$ fails, at $a = 2$.

## Explanations

### L1 human

To decide whether a formula holds, we first give each variable a value.
Then we compute the value of each term, as in school algebra.
An equation holds when both sides have the same value, and a relation holds when the values are in the relation.
"Not", "and", "or", "if then" and "if and only if" work as in truth tables.
"For all $x$" means that every value of $x$ works, and "there is an $x$" means that some value of $x$ works.

### L2 human

We test every kind of clause on one structure, and the [[worked example|KH30ARM9TF]] gives all the details.
Let $L = \{c, f, R\}$ with $c$ a constant symbol, $f$ unary and $R$ binary.
Let $M = \{0, 1\}$, $c^{\mathcal{M}} = 0$, $f^{\mathcal{M}}(a) = 1 - a$ and $R^{\mathcal{M}} = \{ (0, 1) \}$, and let $s(x) = 0$ and $s(y) = 1$.

1. Terms: $x$ has the value $0$, $f(x)$ has the value $1$, and $f(f(c))$ has the value $f^{\mathcal{M}}(1) = 0$.
2. Equality: $f(x) = y$ holds, since $1 = 1$, and $x = y$ fails, since $0 \neq 1$.
3. Relation: $R(x, f(x))$ holds, since $(0, 1) \in R^{\mathcal{M}}$, and $R(f(x), x)$ fails, since $(1, 0) \notin R^{\mathcal{M}}$.
4. Connectives: $\neg (x = y)$ holds, $R(x, f(x)) \wedge x = y$ fails, and $x = y \to R(f(x), x)$ holds, because its hypothesis fails.
5. Quantifiers: $\exists y \, R(x, y)$ holds with the variant $s[y \mapsto 1]$, and $\forall x \, R(x, f(x))$ fails at the variant $s[x \mapsto 1]$, since $(1, 0) \notin R^{\mathcal{M}}$.

Watch out in step 5: the witness $y \mapsto 1$ lives only inside the clause, and $s$ itself does not change.
