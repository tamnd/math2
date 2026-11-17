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

Let $\mathcal{M}$ be a [[structure|983GZBQYT4]] with domain $M$ for a signature $L$, and let $s$ be a variable assignment, that is, a [[function|0EPAT51DXQ]] from the set of variables to $M$.
Each [[term|6D3WA7N2W4]] $t$ gets a value $t^{\mathcal{M}}[s] \in M$, and each [[formula|HYJ10AF6RT]] $\varphi$ is either satisfied or not satisfied by $s$ in $\mathcal{M}$, written $\mathcal{M} \models \varphi[s]$ or $\mathcal{M} \not\models \varphi[s]$.
The relation is defined by recursion on $\varphi$ with Tarski's clauses.
An atomic formula is satisfied when the values of its terms stand in the interpreted relation, and the connectives follow their truth tables.
$\mathcal{M} \models \forall x \, \varphi[s]$ holds when $\mathcal{M} \models \varphi[s[x \mapsto a]]$ for every $a \in M$, and the clause for $\exists x$ asks for some $a \in M$.
Here the $x$-variant $s[x \mapsto a]$ agrees with $s$, except that it sends $x$ to $a$.
The full list of clauses is on the [[definition page|~cf18e0d7]].
Satisfaction is the base of all semantic notions of first-order logic: truth, models, validity and logical consequence are all defined from it.

## Motivation

A sentence such as $\forall x \, \exists y \, (x < y)$ is built from the formula $x < y$, which has free variables.
The formula $x < y$ is neither true nor false in $(\N, <)$: it holds when $x$ is $1$ and $y$ is $3$, and it fails when $x$ is $3$ and $y$ is $1$.
So a recursive definition of truth must pass through formulas with free variables, and these need values for their variables.
A variable assignment gives these values.
The quantifier clause then says how the truth of $\forall x \, \varphi$ depends on $\varphi$: we try every value of $x$ and keep the values of the other variables.
This gives one recursive definition that works for every structure, also when most elements have no name in the language.

## Notation

We write $\mathcal{M} \models \varphi[s]$, read "$\mathcal{M}$ satisfies $\varphi$ under $s$" or "$s$ satisfies $\varphi$ in $\mathcal{M}$".
Enderton writes $\models_{\mathfrak{A}} \varphi[s]$, and some books write $\mathcal{M}, s \models \varphi$.
When the free variables of $\varphi$ are among $x_1, \ldots, x_n$, we write $\mathcal{M} \models \varphi[a_1, \ldots, a_n]$ for $\mathcal{M} \models \varphi[s]$ with $s(x_i) = a_i$; by the [[coincidence lemma|~7b107606]] the other values of $s$ do not matter.
Model theory books such as Hodges write $\mathcal{M} \models \varphi(a_1, \ldots, a_n)$ for the same thing.
The value of a term is written $t^{\mathcal{M}}[s]$ here, $\overline{s}(t)$ in Enderton, and $t^{\mathcal{M}}(a_1, \ldots, a_n)$ in model theory.
In Mathlib, the value of a term is `FirstOrder.Language.Term.realize`, and satisfaction is `FirstOrder.Language.BoundedFormula.Realize` and `FirstOrder.Language.Formula.Realize`.
Mathlib uses de Bruijn style indices for bound variables, so its assignment has two parts: a map for the free variables and a tuple for the bound ones.

## Remarks

### Examples

1. In the [[two-element structure of the definition page|~c020b5e3]], every clause is checked on one assignment, including both quantifiers.
2. In $(\N, <)$, the [[formula $\exists z \, (x < z \wedge z < y)$ is satisfied when $x \mapsto 1$ and $y \mapsto 3$|~b60a1de0]], with the witness $z \mapsto 2$.
3. In the [[directed 3-cycle|~3db99883]], the sentence $\forall x \, \exists y \, E(x, y)$ is satisfied by every assignment, because each vertex has an outgoing edge.
4. In every structure, the formula $x = x$ is satisfied by every assignment, because $s(x) = s(x)$.

### Non-examples

1. In $(\Z, <)$, [[no assignment satisfies $\exists x \, \forall y \, (x < y \vee x = y)$|~32355403]]. The condition that fails is the existence of a witness for $\exists x$: no integer is a least element.
2. In $(\N, <)$, the formula $\exists z \, (x < z \wedge z < y)$ is not satisfied when $x \mapsto 1$ and $y \mapsto 2$. The condition that fails is the existence of a witness for $\exists z$, because no natural number lies strictly between $1$ and $2$.

### Basic properties

1. Satisfaction of $\varphi$ depends only on the values of $s$ at the free variables of $\varphi$, and only on the interpretations of the symbols in $\varphi$. This is the [[coincidence lemma|~7b107606]].
2. Substitution and assignment change agree: $\mathcal{M} \models \varphi[t/x][s]$ if and only if $\mathcal{M} \models \varphi[s[x \mapsto t^{\mathcal{M}}[s]]]$, when $t$ is substitutable for $x$ in $\varphi$. This is the [[semantic substitution lemma|~761225ef]].
3. An isomorphism $h \colon \mathcal{M} \to \mathcal{N}$ preserves satisfaction: $\mathcal{M} \models \varphi[s]$ if and only if $\mathcal{N} \models \varphi[h \circ s]$. This is [[isomorphism invariance of truth|~5166a0b3]].
4. The clauses give $\mathcal{M} \models \exists x \, \varphi[s]$ if and only if $\mathcal{M} \models \neg \forall x \, \neg \varphi[s]$. So books that take only $\neg$, $\to$ and $\forall$ as primitive get the same relation for the other symbols.
5. For every $\varphi$ and $s$, exactly one of $\mathcal{M} \models \varphi[s]$ and $\mathcal{M} \models \neg \varphi[s]$ holds, by the clause for $\neg$.

### History

Alfred Tarski gave the recursive definition of satisfaction in his 1933 monograph on the concept of truth in formalized languages, published in Polish, with a German translation in 1935.
He defined truth of a sentence through satisfaction of formulas by sequences of objects, which play the role of assignments.
The form used today, relative to an arbitrary structure, appears in Tarski and Vaught's 1957 paper "Arithmetical extensions of relational systems".

### Common errors

- Reading the clause for $\forall x$ as "for all assignments". The clause changes the value of $x$ only; the values of the other variables stay as in $s$.
- Replacing the quantifier clause by substitution of names. The rule "$\exists x \, \varphi$ is true when $\varphi[c/x]$ is true for some closed term $c$" fails when some elements have no name; see the example after this list.
- Mixing symbols and objects. In $\mathcal{M} \models \varphi[s]$, the formula $\varphi$ is a string of symbols and $s$ sends variables to elements of $M$; an element of $M$ is not a term of $L$.

An example for the second error: let $L = \set{c, P}$ with $c$ a constant symbol and $P$ unary, and let $M = \set{0, 1}$, $c^{\mathcal{M}} = 0$, $P^{\mathcal{M}} = \set{1}$.
The only closed term is $c$, and $0 \notin P^{\mathcal{M}}$, so the rule of names says that $\exists x \, P(x)$ is false.
Tarski's clause uses the variant $s[x \mapsto 1]$, and $1 \in P^{\mathcal{M}}$, so $\exists x \, P(x)$ is true.
The two rules agree only when every element is the value of a closed term.

## Explanations

### L1 human

A formula such as "$x$ is less than $y$" is not true or false by itself, because we do not know what $x$ and $y$ are.
An assignment fills in a value for each letter, for example $x$ is $1$ and $y$ is $3$.
Then the formula becomes a plain statement, "$1$ is less than $3$", and we can check it.
Satisfaction is the rule that says, for each formula and each choice of values, whether the formula holds.
For "for all $x$" we try every possible value of $x$, and for "there is an $x$" we look for one good value.
So "there is a $z$ with $x < z$ and $z < y$" holds for $x = 1$ and $y = 3$, because $z = 2$ works.

### L2 human

We check one quantifier clause in full.
Let $\mathcal{M} = (\set{0, 1, 2}, <)$ with the usual order, and let $s(x) = 0$.
We decide whether $\mathcal{M} \models \forall y \, (x < y \vee x = y)[s]$.

1. By the clause for $\forall y$, we must check $x < y \vee x = y$ under $s[y \mapsto 0]$, $s[y \mapsto 1]$ and $s[y \mapsto 2]$. Each of these sends $x$ to $0$.
2. Under $s[y \mapsto 0]$, the disjunct $x = y$ holds, because $0 = 0$.
3. Under $s[y \mapsto 1]$, the disjunct $x < y$ holds, because $0 < 1$.
4. Under $s[y \mapsto 2]$, the disjunct $x < y$ holds, because $0 < 2$.
5. All three variants satisfy the disjunction, so $\mathcal{M} \models \forall y \, (x < y \vee x = y)[s]$.

With $s(x) = 1$ instead, the variant $s[y \mapsto 0]$ fails both disjuncts, so the formula is not satisfied.
The typical use is to compute truth values in small structures and to prove the lemmas of first-order semantics by induction on formulas.
The trap is in step 1: the variants keep $x \mapsto 0$; we do not also vary $x$.

### L3 human

Satisfaction is a recursion on the syntax that is compositional: the meaning of a compound formula depends only on the meanings of its parts.
In algebraic terms, the map $\varphi \mapsto \set{s : \mathcal{M} \models \varphi[s]}$ sends the connectives to Boolean operations on the power set of $M^{\mathrm{Var}}$, and $\exists x$ to the cylindrification along $x$; this is the starting point of cylindric algebras.
The same pattern, with different clauses for the operators, gives Kripke semantics for modal and intuitionistic logic and the semantics of many-sorted and higher-order logics.
The [[game-theoretic semantics|D45Z7HETDA]] gives an equivalent definition by a game between two players.
Tarski's undefinability theorem shows that for a rich structure such as $(\N, +, \cdot)$, the satisfaction relation of its own language is not definable by a formula in that language.
