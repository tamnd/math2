---
tag: QE8C6BP0BD
kind: example
name: An epsilon term is not a first-order term
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: grad
not_instance_of:
  - target: 6D3WA7N2W4
    note: the string epsilon x (3 < x) contains a formula and binds a variable, while first-order terms are built from variables and constant symbols by function symbols alone
uses: [6D3WA7N2W4, TH5ZKCKN3W, 9CNGDRAMGC]
sources:
  - url: https://en.wikipedia.org/wiki/Epsilon_calculus
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.1
---

## Example

Let $\sigma = \{ <, 3 \}$, with a binary relation symbol and a constant symbol.
We show that the string $\varepsilon x \, (3 < x)$ of the [[epsilon calculus|TH5ZKCKN3W]] is not a $\sigma$-[[term|6D3WA7N2W4]], and not a term over any signature.

1. A $\sigma$-term is a variable, the constant $3$, or $f(t_1, \dots, t_n)$ for a function symbol $f$ of $\sigma$.
   Here $\sigma$ has no function symbols.
2. So every $\sigma$-term is a variable or the constant $3$, a string of length $1$.
3. The string $\varepsilon x \, (3 < x)$ is longer than $1$, so it is not a $\sigma$-term.
4. Adding symbols does not help.
   By induction on terms, a term over any signature contains no relation symbol, while $\varepsilon x \, (3 < x)$ contains $<$.
5. In $\varepsilon x \, (3 < x)$ the variable $x$ is bound.
   In a first-order term every variable occurrence is [[free|9CNGDRAMGC]], because only quantifiers bind.

So $\varepsilon$-terms need a new formation rule, which makes terms and formulas mutually recursive.

## Remarks

In the epsilon calculus, terms and formulas are defined together: if $A$ is a formula and $x$ a variable, then $\varepsilon x \, A$ is a term.
The [[definite description|PD2R4XT79Q]] operator $\iota x \, A$ and the set-builder $\{ x \mid A \}$ are other term-forming binders of this kind.
In first-order logic they are eliminated in favor of formulas, for example by Russell's analysis of descriptions.

## Explanations

### L1 human

First-order terms are names built from symbols such as $0$, $+$ and variables.
They never contain a statement inside.
The expression "some $x$ bigger than $3$" contains the statement "$3 < x$", so it is a new kind of name.

### L2 human

We see why the mutual recursion matters.
In first-order logic, terms are built first, and formulas are built from terms.
With $\varepsilon$, the formula $3 < x$ gives the term $\varepsilon x \, (3 < x)$, which gives the formula $3 < \varepsilon x \, (3 < x)$, and so on.
So unique readability and definitions by recursion on syntax must be handled for terms and formulas at once.
The typical use of this non-example is to place the epsilon calculus outside first-order syntax, with a conservative translation back.
Watch out: some books write $\varepsilon$ for a constant, such as a small positive number, and then $\varepsilon$ is an ordinary term.
The test is whether a formula and a bound variable occur inside.
