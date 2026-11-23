---
tag: 2RBQPV02AS
kind: concept
name: Satisfaction
aliases: [satisfaction-relation, tarskis-definition-of-satisfaction]
msc: ["03B10", "03C07"]
topics: [NJDME6F845]
audience: ug2
uses: [983GZBQYT4, HYJ10AF6RT, 6D3WA7N2W4, 0EPAT51DXQ]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section S
    note: adopted
    mention: wikipedia://en/76765067#NNZG
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Evaluation of truth values
  - url: https://en.wikipedia.org/wiki/Interpretation_(logic)
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.2
  - url: https://builds.openlogicproject.org/
    locator: Syntax and Semantics
inventory: [7NCRZSVNQT]
---

## Summary

Satisfaction is the rule that decides, in a given structure, whether a formula holds once each of its variables has a value.
Take the formula $\exists y \, (x < y)$ in the structure $(\mathbb{Z}, <)$, and give $x$ the value $5$.
The formula asks for some integer $y$ above $5$, and $y = 6$ is one, so the formula is satisfied.
No choice of $x$ makes it fail, so the sentence $\forall x \, \exists y \, (x < y)$ is true in $(\mathbb{Z}, <)$.

In exact terms, let $\mathcal{M}$ be a [[structure|983GZBQYT4]] with domain $M$, and let $s$ be a variable assignment, a [[function|0EPAT51DXQ]] from the set of variables to $M$.
Each [[term|6D3WA7N2W4]] $t$ gets a value $t^{\mathcal{M}}[s] \in M$, and each [[formula|HYJ10AF6RT]] $\varphi$ is either satisfied by $s$ in $\mathcal{M}$, written $\mathcal{M} \models \varphi[s]$, or not.
The relation is defined by recursion on $\varphi$ with Tarski's clauses.
Atomic formulas are checked directly, the connectives follow their truth tables, and the quantifiers use variants of $s$:
$$\mathcal{M} \models \forall x \, \varphi[s] \iff \mathcal{M} \models \varphi[s[x \mapsto a]] \text{ for every } a \in M,$$
and the clause for $\exists x$ asks for some $a \in M$ instead of every $a$.
The $x$-variant $s[x \mapsto a]$ agrees with $s$ except that it sends $x$ to $a$.
The [[formal definition|1WTCZB4DVB]] lists all the clauses.

## Motivation

We want to know when a sentence such as $\forall x \, \exists y \, (x < y)$ is true, and a sentence is built from parts that are not sentences.
Its part $x < y$ has free variables, and it is neither true nor false in $(\mathbb{N}, <)$: it holds when $x$ is $1$ and $y$ is $3$, and fails when $x$ is $3$ and $y$ is $1$.
So a recursive definition of truth must pass through formulas with free variables, and these need values for their variables.
A variable assignment supplies the values, and satisfaction is the recursion that uses them.

The quantifier clause is where the work happens.
To decide $\forall x \, \varphi$, we try every value of $x$ and keep the values of the other variables.
This works in every structure, also when most elements have no name in the language.
Truth, [[models|MVCH6N9SNW]], [[validity|5SDS9T8E7J]] and [[logical consequence|1HK0VYWTV7]] are all defined from satisfaction, and the soundness and completeness theorems of later sub-areas are statements about it.

## Notation

We write $\mathcal{M} \models \varphi[s]$ and read it "$s$ satisfies $\varphi$ in $\mathcal{M}$".
Enderton writes $\models_{\mathfrak{A}} \varphi[s]$, and some books write $\mathcal{M}, s \models \varphi$.
When the free variables of $\varphi$ are among $x_1, \ldots, x_n$, we write $\mathcal{M} \models \varphi[a_1, \ldots, a_n]$ for $\mathcal{M} \models \varphi[s]$ with $s(x_i) = a_i$, and model theory books such as Hodges write $\mathcal{M} \models \varphi(a_1, \ldots, a_n)$.
The [[coincidence lemma|FM580NZ9W6]] says that the other values of $s$ do not matter, so both notations are safe.
The value of a term is $t^{\mathcal{M}}[s]$ here and $\overline{s}(t)$ in Enderton.
In Mathlib, term values are `FirstOrder.Language.Term.realize`, and satisfaction is `FirstOrder.Language.BoundedFormula.Realize` and `FirstOrder.Language.Formula.Realize`.

## Remarks

### Tarski's clauses on one formula

Let us evaluate $\exists z \, (x < z \wedge z < y)$ in $(\mathbb{N}, <)$ under an assignment $s$ with $s(x) = 1$ and $s(y) = 3$.
The clause for $\exists z$ asks for some $a \in \mathbb{N}$ with
$$\mathcal{M} \models (x < z \wedge z < y)[s[z \mapsto a]].$$
Try $a = 2$.
The variant sends $x$ to $1$, $y$ to $3$ and $z$ to $2$.
The clause for $\wedge$ asks for both conjuncts, and the atomic clause checks each one: $(1, 2) \in {<}$ and $(2, 3) \in {<}$.
So the formula is satisfied, with the witness $2$, as the [[worked example|YJ0VEETN8J]] shows in full.

Change $s(y)$ to $2$, and the same formula fails.
A witness $a$ would need $1 < a < 2$, and no natural number lies strictly between $1$ and $2$.
Every clause, including both quantifiers and all connectives, is checked on one small structure in the [[two-element example|KH30ARM9TF]].

### A sentence that fails

In $(\mathbb{Z}, <)$, write $x \leq y$ for $x < y \vee x = y$, and consider $\exists x \, \forall y \, (x \leq y)$.
It would need an integer $a$ that is at most every integer.
For any candidate $a$, the variant with $y \mapsto a - 1$ gives $a \leq a - 1$, which is false.
So no assignment satisfies the sentence, as the [[example on least elements|73YT05DXRB]] checks in detail.
In $(\mathbb{N}, <)$ the same sentence is true, with the witness $0$.

### The rules that follow

Satisfaction of $\varphi$ depends only on the values of $s$ at the free variables of $\varphi$, and only on the interpretations of the symbols in $\varphi$; this is the [[coincidence lemma|FM580NZ9W6]].
Substituting a term matches changing the assignment: if $t$ is substitutable for $x$ in $\varphi$, then
$$\mathcal{M} \models \varphi[t/x][s] \iff \mathcal{M} \models \varphi[s[x \mapsto t^{\mathcal{M}}[s]]].$$
That is the [[semantic substitution lemma|A7S460KHBM]].
An isomorphism $h \colon \mathcal{M} \to \mathcal{N}$ preserves satisfaction, so $\mathcal{M} \models \varphi[s]$ exactly when $\mathcal{N} \models \varphi[h \circ s]$, by [[isomorphism invariance of truth|NDTJ2E895C]].

Two more facts come straight from the clauses.
For every $\varphi$ and $s$, exactly one of $\mathcal{M} \models \varphi[s]$ and $\mathcal{M} \models \neg \varphi[s]$ holds.
The clauses also give $\mathcal{M} \models \exists x \, \varphi[s]$ exactly when $\mathcal{M} \models \neg \forall x \, \neg \varphi[s]$, so books with fewer primitive symbols get the same relation.

### Watch out: variants, not names

A tempting shortcut reads "$\exists x \, \varphi$ holds when $\varphi[c/x]$ holds for some closed term $c$".
It fails when some elements have no name.
Let $L = \{c, P\}$ with $c$ a constant symbol and $P$ unary, and let $M = \{0, 1\}$, $c^{\mathcal{M}} = 0$ and $P^{\mathcal{M}} = \{1\}$.
The only closed term is $c$, and $0 \notin P^{\mathcal{M}}$, so the shortcut says that $\exists x \, P(x)$ is false.
Tarski's clause uses the variant $s[x \mapsto 1]$, and $1 \in P^{\mathcal{M}}$, so $\exists x \, P(x)$ is true.
The two rules agree only when every element is the value of a closed term.

### Watch out: what the variant changes

The clause for $\forall x$ does not mean "for all assignments".
It changes the value of $x$ only, and every other variable keeps its value from $s$.
In $(\{0, 1, 2\}, <)$ with $s(x) = 0$, the formula $\forall y \, (x \leq y)$ is satisfied, since $0$ is at most $0$, $1$ and $2$.
With $s(x) = 1$ it fails, at the variant $y \mapsto 0$.
If we also varied $x$, both answers would come out the same, which is wrong.

Also keep symbols and objects apart.
In $\mathcal{M} \models \varphi[s]$, the formula is a string of symbols, and $s$ sends variables to elements of $M$, which are not terms of $L$.

### History

Alfred Tarski gave the recursive definition of satisfaction in his 1933 monograph on the concept of truth in formalized languages.
He defined the truth of a sentence through the satisfaction of formulas by sequences of objects, which play the role of assignments.
The form used today, relative to an arbitrary structure, appears in the 1957 paper of Tarski and Vaught on arithmetical extensions of relational systems.

### Try it

In $(\mathbb{Z}, <)$ with $s(x) = 0$ and $s(y) = 1$, is $\exists z \, (x < z \wedge z < y)$ satisfied?
No: a witness would be an integer strictly between $0$ and $1$, and there is none.

In $(\mathbb{Q}, <)$ with the same assignment, is it satisfied?
Yes: the variant $z \mapsto \tfrac{1}{2}$ gives $0 < \tfrac{1}{2}$ and $\tfrac{1}{2} < 1$.

## Explanations

### L1 human

A formula such as "$x$ is less than $y$" is not true or false by itself, because we do not know what $x$ and $y$ are.
An assignment fills in a value for each letter, for example $x$ is $1$ and $y$ is $3$.
Then the formula becomes a plain statement, "$1$ is less than $3$", and we can check it.
Satisfaction is the rule that says, for each formula and each choice of values, whether the formula holds.
For "for all $x$" we try every value of $x$, and for "there is an $x$" we look for one good value.
So "there is a $z$ with $x < z$ and $z < y$" holds for $x = 1$ and $y = 3$, because $z = 2$ works.

### L2 human

We check one universal clause in full.
Let $\mathcal{M} = (\{0, 1, 2\}, <)$ with the usual order, let $s(x) = 0$, and decide whether $\mathcal{M} \models \forall y \, (x < y \vee x = y)[s]$.
The clause for $\forall y$ sends us to three variants, each with $x \mapsto 0$:
$$s[y \mapsto 0], \qquad s[y \mapsto 1], \qquad s[y \mapsto 2].$$
Under the first, the disjunct $x = y$ holds, since $0 = 0$.
Under the second and the third, the disjunct $x < y$ holds, since $0 < 1$ and $0 < 2$.
All three variants satisfy the disjunction, so $s$ satisfies the universal formula.

With $s(x) = 1$ instead, the variant $s[y \mapsto 0]$ fails both disjuncts, so the formula is not satisfied.
The typical use is to compute truth values in small structures, and to prove the lemmas of first-order semantics by induction on formulas.

### L3 human

Satisfaction is compositional: the meaning of a compound formula depends only on the meanings of its parts.
In algebraic terms, the map $\varphi \mapsto \{ s : \mathcal{M} \models \varphi[s] \}$ sends the connectives to Boolean operations on sets of assignments, and $\exists x$ to the cylindrification along $x$, which is the starting point of cylindric algebras.
The same pattern, with other clauses, gives Kripke semantics for modal and intuitionistic logic and the semantics of many-sorted and higher-order logics.

The [[game-theoretic semantics|D45Z7HETDA]] gives an equivalent definition by a game between two players.
Tarski's undefinability theorem shows that for a rich structure such as $(\mathbb{N}, +, \cdot)$, the set of codes of true sentences of its own language is not definable by a formula of that language.
