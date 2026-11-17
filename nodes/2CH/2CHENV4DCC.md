---
tag: 2CHENV4DCC
kind: definition
name: Well-formed formula
msc: ["03B10", "03B05"]
topics: [PSRDJXRW53]
audience: ug2
defines: HYJ10AF6RT
uses: [WDVVEYD6AT, 6D3WA7N2W4, ~de213704, QS0XVAN9BG]
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

Let $\sigma$ be a [[signature|WDVVEYD6AT]] and let $\mathrm{Var} = \set{v_0, v_1, v_2, \dots}$ be a countably infinite set of variables, disjoint from the symbols of $\sigma$.
The set of first-order *formulas* over $\sigma$ is the smallest set of finite strings such that:

1. if $t_1$ and $t_2$ are [[terms|6D3WA7N2W4]] over $\sigma$, then $t_1 = t_2$ is a formula;
2. if $R$ is a relation symbol of $\sigma$ of arity $n$ and $t_1, \dots, t_n$ are terms, then $R(t_1, \dots, t_n)$ is a formula;
3. if $\varphi$ is a formula, then $\neg \varphi$ is a formula;
4. if $\varphi$ and $\psi$ are formulas, then $(\varphi \land \psi)$, $(\varphi \lor \psi)$, $(\varphi \to \psi)$ and $(\varphi \leftrightarrow \psi)$ are formulas;
5. if $\varphi$ is a formula and $x \in \mathrm{Var}$, then $\forall x \, \varphi$ and $\exists x \, \varphi$ are formulas.

The formulas from clauses 1 and 2 are the [[atomic formulas|~de213704]].
In first-order logic without equality, clause 1 is left out.

## Notation

1. Greek letters $\varphi, \psi, \chi$ stand for formulas. They are symbols of the metalanguage, not of the formal language.
2. In text the outer brackets are dropped. The binding order is: $\neg$ and the quantifiers first, then $\land$ and $\lor$, then $\to$ and $\leftrightarrow$.
3. Books differ in the primitive [[connectives|QS0XVAN9BG]]. With $\neg$, $\to$ and $\forall$ only, the other symbols are abbreviations, for example $\exists x \, \varphi$ for $\neg \forall x \, \neg \varphi$.
4. In Mathlib, `FirstOrder.Language.BoundedFormula L α n` is the type of formulas of the language `L` with free variables from the type `α` and with $n$ further variables, numbered by `Fin n`.
5. The Mathlib constructors are falsum, equality, relations, implication and the universal quantifier. Negation, the other connectives and $\exists$ are defined from them.
6. The universal quantifier of Mathlib turns a formula with $n + 1$ numbered variables into a formula with $n$ numbered variables. It binds the variable with the last number $n$, and the truth clause appends the new value at the end of the list of values (by `Fin.snoc`).
7. So in Mathlib the outermost quantifier binds number $0$, the next one binds number $1$, and so on. The usual de Bruijn index convention counts the other way, from the innermost quantifier, and the two differ only in this direction.

## Remarks

Example: in the signature of ordered sets, $\forall x \, \exists y \, (x < y)$ is a formula.
Here $x < y$ is atomic by clause 2, $\exists y \, (x < y)$ is a formula by clause 5, and then $\forall x \, \exists y \, (x < y)$ is a formula by clause 5 again.
In Mathlib this formula is the universal quantification of the existential quantification of $x < y$, where $x$ has number $0$ and $y$ has number $1$.

Non-example: the string $\forall x \, (x \land y)$ is not a formula.
The variables $x$ and $y$ are terms, not formulas, so clause 4 does not apply to them.
No other clause produces a string whose fourth symbol is $\land$ with a term before it.

The word "smallest" is part of the definition.
The set of all strings is also closed under clauses 1 to 5, and the minimality excludes the strings that no finite chain of clauses produces.
Equivalently, a string is a formula exactly when it is the last entry of a finite sequence in which each entry comes from earlier entries by one clause.
Such a sequence is a [[formation sequence|~c3f0dab2]].

In propositional logic, the formulas are built from propositional variables by clauses 3 and 4 alone.

## Explanations

### L1 human

The definition is a list of building rules.
Simple claims such as $x = y$ and $x < y$ are formulas from the start.
Then "not", "and", "or", "if ... then", "if and only if", "for all" and "there exists" build longer formulas from shorter ones.
Only the strings that these rules produce are formulas.
For example, $\neg (x < y)$ is a formula, but $\neg x$ is not, because $x$ is a name of an object and not a claim.

### L2 human

We check that $\exists y \, (x < y \land \neg y = x)$ is a formula over $\set{<}$.

1. The strings $x < y$ and $y = x$ are atomic formulas, by clauses 2 and 1.
2. Then $\neg y = x$ is a formula, by clause 3.
3. Then $(x < y \land \neg y = x)$ is a formula, by clause 4.
4. Then $\exists y \, (x < y \land \neg y = x)$ is a formula, by clause 5.

The typical use of the definition is a proof by induction on formulas, with one case for each clause.
The trap is the number of cases: with five clauses there are five cases, unless some connectives are abbreviations.
This is why many books take few primitive symbols: each proof by induction becomes shorter.
