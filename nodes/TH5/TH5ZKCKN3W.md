---
tag: TH5ZKCKN3W
kind: concept
name: Hilbert's epsilon calculus
aliases: [epsilon-calculus, epsilon-operator, hilbert-epsilon-operator]
msc: ["03B10", "03F05"]
topics: [PSRDJXRW53]
audience: grad
uses: [086QKPF0A6, 6D3WA7N2W4, HYJ10AF6RT, NCDZ969V7X, 0FWBQ53MPJ]
sources:
  - url: https://en.wikipedia.org/wiki/Epsilon_calculus
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Epsilon_calculus
    locator: Epsilon operator
same_as:
  wikipedia: Epsilon calculus
---

## Summary

The term $\varepsilon x \, (3 < x)$ is read "some $x$ with $3 < x$".
Over the natural numbers it might denote $4$, or $10$; the logic only promises that, if some number exceeds $3$, then this one does.
Hilbert's epsilon calculus adds such terms $\varepsilon x \, A(x)$, for every formula $A(x)$, to [[first-order logic|086QKPF0A6]].

Its characteristic axiom schema is the critical formula
$$A(t) \to A(\varepsilon x \, A(x)),$$
for every term $t$: if anything satisfies $A$, then $\varepsilon x \, A(x)$ does.
With it the quantifiers become definable, since $\exists x \, A(x)$ is equivalent to $A(\varepsilon x \, A(x))$.
Hilbert and his school used the calculus for consistency proofs, and the two epsilon theorems show that $\varepsilon$-terms prove nothing new about $\varepsilon$-free formulas.

## Motivation

In Hilbert's program, consistency proofs had to treat quantifiers over infinite domains by finite means.
The epsilon operator replaces each quantifier by a term, so a proof with quantifiers becomes a proof with terms and quantifier-free formulas.
A consistency proof then has to find values for finitely many $\varepsilon$-terms that make the finitely many critical formulas of the proof true.
The operator also makes explicit the witnesses that $\exists$ only asserts, like a Skolem function built into the syntax.

## Notation

The term $\varepsilon x \, A$ binds $x$ in $A$, like a quantifier, and its free variables are those of $A$ other than $x$.
The critical formula of $A$ and $t$ is $A(t) \to A(\varepsilon x \, A)$, with $t$ substitutable for $x$ in $A$.
Bourbaki writes $\tau_x(A)$ for $\varepsilon x \, A$, and draws links from $\tau$ to the places of $x$ instead of writing $x$.
In Isabelle/HOL the operator is written $\mathrm{SOME}\ x.\ A\, x$, and in Lean it is `Classical.epsilon`.

## Remarks

### Examples and non-examples

[[Quantifiers as epsilon terms|QVCYWZWT3F]] turns the sentence $\exists x \, \forall y \, R(x, y)$ into a quantifier-free formula with nested $\varepsilon$-terms.
[[An epsilon term in the natural numbers|4S9PJC485C]] reads $\varepsilon$ as "least element", so that $\varepsilon x \, (3 < x)$ denotes $4$.
A Skolem function is an $\varepsilon$-term in disguise: $\forall x \, \exists y \, R(x, y)$ is equivalent to $\forall x \, R(x, \varepsilon y \, R(x, y))$.

On the other side, [[an epsilon term is not a first-order term|QE8C6BP0BD]], since the term rules of first-order logic have no binding operator.
The description $\iota x \, A$ of a [[definite description|PD2R4XT79Q]] is not an $\varepsilon$-term either.
It needs exactly one $x$ with $A$, while $\varepsilon x \, A$ denotes an object even when there are several or none.
A new constant $c$ with the axiom $A(c)$ is tied to one formula, while $\varepsilon$ applies to all formulas uniformly.

### Quantifiers and semantics

Both quantifiers are definable from the critical formulas:
$$\exists x \, A \leftrightarrow A(\varepsilon x \, A), \qquad \forall x \, A \leftrightarrow A(\varepsilon x \, \neg A).$$
The second says that $A$ holds everywhere exactly when it holds at the chosen counterexample.

For the semantics, fix in a structure $\mathcal{M}$ a [[choice function|0FWBQ53MPJ]] $\Phi$ on the nonempty subsets of $M$, with a default value for $\emptyset$.
Then $\varepsilon x \, A$ denotes $\Phi$ of the set of $a \in M$ that satisfy $A$, and every critical formula is true.
The extensional calculus adds the axiom $\forall x \, (A \leftrightarrow B) \to \varepsilon x \, A = \varepsilon x \, B$, and this semantics satisfies it, because the value depends only on the set.

### The epsilon theorems

The first epsilon theorem says that a quantifier-free, $\varepsilon$-free formula derivable in the $\varepsilon$-calculus from quantifier-free axioms is derivable from them without quantifiers or $\varepsilon$.
The second epsilon theorem says that the $\varepsilon$-calculus is conservative over first-order logic: an $\varepsilon$-free formula derivable with $\varepsilon$ is derivable in first-order logic.
Both are proved by eliminating the critical formulas of a proof one $\varepsilon$-term at a time.

### Watch out

The term $\varepsilon x \, A$ is "some $x$ with $A$", not "the $x$ with $A$", and it denotes an object also when no $x$ satisfies $A$.
Equivalent formulas $A$ and $B$ need not give equal terms $\varepsilon x \, A$ and $\varepsilon x \, B$ unless the extensionality axiom is assumed.
The variable $x$ is bound in $\varepsilon x \, A$, so the rules of [[substitution|NCDZ969V7X]] for quantifiers apply to it, and a term with a free $x$ cannot be substituted inside without renaming.

### History

Hilbert introduced the epsilon operator in the early 1920s, as a tool of his program for the foundations of mathematics.
Ackermann's dissertation of 1924 used the $\varepsilon$-substitution method for a consistency proof of arithmetic, which turned out to cover only a fragment.
Hilbert and Bernays proved the two epsilon theorems in the second volume of their Grundlagen der Mathematik, in 1939.
Ackermann completed the substitution method for arithmetic in 1940, with induction up to $\varepsilon_0$, after Gentzen's work.

### Try it

Translate $\forall x \, P(x)$ into the epsilon calculus.
The answer is $P(\varepsilon x \, \neg P(x))$: the chosen candidate for a non-$P$ has $P$.

## Explanations

### L1 human

The symbol $\varepsilon x \, A(x)$ is a name for "an object with property $A$, if there is one".
For example, $\varepsilon x \, (x \text{ is a prime number})$ names some prime number, without saying which.
With this name, "there is a prime" can be written as "$\varepsilon x \, (x \text{ is prime})$ is prime".
The words "there is" disappear, and only a name remains.

### L2 human

We derive $\exists x \, A \leftrightarrow A(\varepsilon x \, A)$ from the critical formula, in a calculus with quantifiers.

1. The critical formula gives $A(y) \to A(\varepsilon x \, A)$ for a variable $y$ not occurring in $A$.
2. The variable $y$ is not free in $A(\varepsilon x \, A)$.
   So the rule for $\exists$ on the left of $\to$ gives $\exists y \, A(y) \to A(\varepsilon x \, A)$.
3. Renaming the bound variable turns $\exists y \, A(y)$ into $\exists x \, A(x)$.
4. The converse $A(\varepsilon x \, A) \to \exists x \, A$ is an instance of the axiom $A(t) \to \exists x \, A$ with $t = \varepsilon x \, A$.

The typical use is to drop $\exists$ altogether and to take $A(\varepsilon x \, A)$ as its definition.
Watch out: the axiom is the critical formula, not $A(\varepsilon x \, A)$ alone.
That would claim that some $x$ satisfies $A$ for every $A$, including $x \ne x$.

### L3 human

The epsilon calculus is a first-order logic with a global choice operator built into its terms.
Its two epsilon theorems are conservation results, proved by eliminating the critical formulas one $\varepsilon$-term at a time.
The extended first epsilon theorem yields Herbrand's theorem, with $\varepsilon$-terms in place of Skolem functions.
The $\varepsilon$-substitution method assigns values to $\varepsilon$-terms by a convergent process of trial and error, and its termination proof for arithmetic uses induction up to $\varepsilon_0$.
In set theory, $\varepsilon$ gives global choice: $\varepsilon x \, (x \in S)$ picks an element of each nonempty set $S$.
Bourbaki's $\tau$ and the choice operators of higher-order provers descend from it.
