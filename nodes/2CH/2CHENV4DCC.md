---
tag: 2CHENV4DCC
kind: definition
name: Well-formed formula
msc: ["03B10", "03B05"]
topics: [PSRDJXRW53]
audience: ug2
defines: HYJ10AF6RT
uses: [WDVVEYD6AT, 6D3WA7N2W4, MCZRXR3SVB, QS0XVAN9BG]
formal:
  - system: lean4
    library: mathlib
    decl: FirstOrder.Language.BoundedFormula
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Well-formed_formula
    locator: lead section
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Formation rules
  - book: isbn:9780122384523
    locator: Section 2.1
---

## Definition

A first-order formula is a string that five formation rules produce, starting from equations and relation symbols applied to terms.

Let $\sigma$ be a [[signature|WDVVEYD6AT]], and let $\mathrm{Var} = \{ v_0, v_1, v_2, \dots \}$ be a countably infinite set of variables, disjoint from the symbols of $\sigma$.
The set of first-order *formulas* over $\sigma$ is the smallest set of finite strings such that:

1. if $t_1$ and $t_2$ are [[terms|6D3WA7N2W4]] over $\sigma$, then $t_1 = t_2$ is a formula;
2. if $R$ is a relation symbol of $\sigma$ of arity $n$ and $t_1, \dots, t_n$ are terms, then $R(t_1, \dots, t_n)$ is a formula;
3. if $\varphi$ is a formula, then $\neg \varphi$ is a formula;
4. if $\varphi$ and $\psi$ are formulas, then $(\varphi \land \psi)$, $(\varphi \lor \psi)$, $(\varphi \to \psi)$ and $(\varphi \leftrightarrow \psi)$ are formulas;
5. if $\varphi$ is a formula and $x \in \mathrm{Var}$, then $\forall x \, \varphi$ and $\exists x \, \varphi$ are formulas.

The formulas given by clauses 1 and 2 are the [[atomic formulas|MCZRXR3SVB]].
In first-order logic without equality, clause 1 is left out.

## Notation

Greek letters $\varphi, \psi, \chi$ stand for formulas; they belong to the metalanguage, not to the formal language.
In text we drop outer brackets, and $\neg$ and the quantifiers bind more strongly than $\land$ and $\lor$, which bind more strongly than $\to$ and $\leftrightarrow$.
Books differ in the primitive [[connectives|QS0XVAN9BG]]: with only $\neg$, $\to$ and $\forall$, the other symbols are abbreviations, such as $\exists x \, \varphi$ for $\neg \forall x \, \neg \varphi$.
A binary relation symbol such as $<$ is usually written between its arguments, as $x < y$ for $<(x, y)$.

In Mathlib, `FirstOrder.Language.BoundedFormula L α n` is the type of formulas of the language `L` with free variables from the type `α` and with $n$ further variables, numbered by `Fin n`.
The constructors are falsum, equality, relations, implication and the universal quantifier, and the other connectives and $\exists$ are defined from them.
The universal quantifier turns a formula with $n + 1$ numbered variables into one with $n$, and it binds the variable with the last number $n$.
So the outermost quantifier binds number $0$, the next one binds number $1$, and so on.
The usual de Bruijn indices count the other way, from the innermost quantifier outward, so watch the direction when you move between books and Lean.

## Remarks

The word "smallest" does real work.
The set of all strings is also closed under clauses 1 to 5, so without minimality every string would count.
Minimality says that a string is a formula only when some finite chain of clauses produces it.
Such a chain, written as a list, is a [[formation sequence|R99VNXVM8P]], and a string is a formula exactly when it is the last entry of one.

Clause 5 asks for a variable after the quantifier, and that is why $\forall c \, P(c)$ with a constant $c$ is [[not a formula|4SV9Q67884]].
Clause 4 adds brackets, and that is why each binary combination can be read in only one way.
Clause 5 does not ask that $x$ occurs in $\varphi$, so $\forall x \, (y = y)$ is a formula with a vacuous quantifier.

For example, over the signature of orders, $\forall x \, \exists y \, (x < y)$ is a formula.
The string $x < y$ is atomic by clause 2, then $\exists y \, (x < y)$ comes by clause 5, and then $\forall x \, \exists y \, (x < y)$ comes by clause 5 again.
In Mathlib this formula is the universal quantification of the existential quantification of an atomic formula, with $x$ as number $0$ and $y$ as number $1$.

For a failing case, take $\forall x \, (x \land y)$.
The strings $x$ and $y$ are terms, not formulas, so clause 4 cannot join them, and no other clause yields a string with $\land$ between two terms.

The concept page [[well-formed formula|HYJ10AF6RT]] has more examples, and in propositional logic the formulas are built from propositional variables by clauses 3 and 4 alone.

## Explanations

### L1 human

The definition is a list of building rules.
Equations such as $x = y$ and claims such as $x < y$ are formulas from the start.
Then "not", "and", "or", "if ... then", "if and only if", "for all" and "there exists" build longer formulas from shorter ones.
Only the strings that these rules produce are formulas.
So $\neg (x < y)$ is a formula, but $\neg x$ is not, because $x$ names an object and is not a claim.

### L2 human

We check that $\exists y \, (x < y \land \neg y = x)$ is a formula over $\{ < \}$, one clause at a time.
The strings $x < y$ and $y = x$ are atomic, by clauses 2 and 1.
Clause 3 gives $\neg y = x$, and clause 4 joins it with $x < y$ to give $(x < y \land \neg y = x)$.
Clause 5 with the variable $y$ then gives the whole string.
The typical use of the definition is a proof by induction on formulas with one case for each clause.
With five clauses there are five cases, and this is why many books take few primitive symbols: each induction becomes shorter.
