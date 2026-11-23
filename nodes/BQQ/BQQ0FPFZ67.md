---
tag: BQQ0FPFZ67
kind: definition
name: Term
msc: ["03B10", "03C07"]
topics: [PSRDJXRW53]
audience: ug2
defines: 6D3WA7N2W4
uses: [WDVVEYD6AT, 1P6EP01HZF]
formal:
  - system: lean4
    library: mathlib
    decl: FirstOrder.Language.Term
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Term_(logic)
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.1
---

## Definition

The terms of a first-order language are the expressions that name elements, built from variables and constants by function symbols.

Let $\sigma$ be a [[signature|WDVVEYD6AT]], and let $V$ be a set of variables, disjoint from the symbols of $\sigma$.
The set of *terms* over $\sigma$ and $V$ is the smallest set of finite [[strings|1P6EP01HZF]] of symbols such that

1. every variable $x \in V$ is a term,
2. every constant symbol $c$ of $\sigma$ is a term, and
3. if $f$ is a function symbol of $\sigma$ of arity $n \ge 1$ and $t_1, \dots, t_n$ are terms, then the string $f(t_1, \dots, t_n)$ is a term.

A term with no variables is a *closed term*, or a *ground term*.
The set $\operatorname{Var}(t)$ of variables of a term $t$ is defined by recursion on $t$:
$$\operatorname{Var}(x) = \{ x \}, \qquad \operatorname{Var}(c) = \emptyset, \qquad \operatorname{Var}(f(t_1, \dots, t_n)) = \operatorname{Var}(t_1) \cup \dots \cup \operatorname{Var}(t_n).$$

## Notation

Binary function symbols are often written infix, as $(t_1 + t_2)$ for $+(t_1, t_2)$, and some unary ones postfix, as $t^{-1}$.
The set of terms is written $T_\sigma(V)$, $\mathrm{Term}_\sigma$ or $\mathrm{Tm}$.
In Mathlib, `FirstOrder.Language.Term L α` has two constructors: `var a` for `a : α`, and `func f ts` for `f : L.Functions n` and `ts : Fin n → L.Term α`.
There a constant is `func c` with $n = 0$, so clause 2 is the case $n = 0$ of clause 3.

## Remarks

Each clause has its job.
Clauses 1 and 2 give the leaves of a term, and clause 3 joins $n$ finished terms under one function symbol of arity $n$.
The word "smallest" says that nothing else is a term: a string is a term only when a finite chain of the clauses produces it.
That is what makes proofs by [[structural induction|12MQ2NJ29A]] over all terms valid.

For an instance, take the ring signature.
The string $\cdot(x, +(y, 1))$, usually written $x \cdot (y + 1)$, is a term by clause 1 for $x$ and $y$, clause 2 for $1$, and clause 3 for $+$ and then for $\cdot$.
Its variables are
$$\operatorname{Var}(x \cdot (y + 1)) = \{ x \} \cup (\{ y \} \cup \emptyset) = \{ x, y \}.$$
A case that fails is $x < y$ in the signature of orders: $<$ is a relation symbol, not a function symbol, so clause 3 does not apply and no other clause produces the string.
Another is $+(x)$, where $+$ has arity $2$ but gets one argument, as in [[a function symbol with the wrong number of arguments|J5BD7FZFFA]].

The recursion that defines $\operatorname{Var}$ gives one value for each term only because each term has one reading, by [[unique readability|3QPV4XW8MC]].
The concept page [[term|6D3WA7N2W4]] shows trees, values and closed terms.

## Explanations

### L1 human

The rules build terms from small pieces.
Variables and constants are terms.
A function symbol with the right number of terms as inputs gives a new term.
Nothing else is a term.

### L2 human

We check that $S(+(x, 0))$ is a term of $\{ 0, S, + \}$, with arities $0$, $1$ and $2$, and find its variables.
The string $x$ is a term by clause 1, and $0$ is a term by clause 2.
Then $+(x, 0)$ is a term by clause 3, since $+$ gets two terms and $\operatorname{ar}(+) = 2$.
Then $S(+(x, 0))$ is a term by clause 3, since $S$ gets one term and $\operatorname{ar}(S) = 1$.
The recursion for the variables gives
$$\operatorname{Var}(S(+(x, 0))) = \operatorname{Var}(x) \cup \operatorname{Var}(0) = \{ x \},$$
so the term is not closed.
The typical use of the clauses is a proof by structural induction over all terms.
Watch out: the term $0$ is closed, but so is any term made only from constants and function symbols, such as $S(+(0, 0))$.
