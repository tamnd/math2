---
tag: DXS1P3VAY7
kind: example
name: Non-strict inequality and inequations are not atomic in the language of strict orders
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
not_instance_of:
  - target: MCZRXR3SVB
    note: in the signature with one symbol for the strict order, the formula for non-strict inequality is a disjunction and the formula for an inequation is a negation, so both contain a connective
uses: [MCZRXR3SVB, BP6WW7H5CC, HYJ10AF6RT, 3QPV4XW8MC]
sources:
  - url: https://en.wikipedia.org/wiki/Atomic_formula
    locator: lead section
---

## Example

Whether a short formula is atomic depends on the signature, not on how short it looks.
Let $\sigma = \{ < \}$, with one binary relation symbol.
In practice we write $x \le y$ and $x \neq y$ over $\sigma$.
We check that the formulas behind these abbreviations are not [[atomic|MCZRXR3SVB]].

1. The signature has no symbol $\le$.
   So $x \le y$ is an abbreviation for the formula $(x < y \lor x = y)$.
2. By the [[definition|BP6WW7H5CC]], the atomic formulas of $\sigma$ are $u < w$ and $u = w$ for terms $u$ and $w$.
   Here the terms are only variables, because $\sigma$ has no function or constant symbols.
3. The formula $(x < y \lor x = y)$ starts with a bracket.
   An atomic formula of $\sigma$ starts with a variable, or with the symbol $<$ in prefix notation, and never with a bracket.
4. By [[unique readability|3QPV4XW8MC]], the first symbol fixes the form, so $(x < y \lor x = y)$ is not atomic.
   It is a disjunction of two atomic formulas.
5. The string $x \neq y$ abbreviates $\neg (x = y)$.
   It starts with $\neg$, so for the same reason it is not atomic.
   It is a literal, the negation of an atomic formula.

So both formulas are quantifier-free, but neither is atomic.

## Remarks

The answer changes with the signature.
In the signature $\{ \le \}$, the formula $x \le y$ is atomic, and $x < y$ abbreviates $(x \le y \land \neg (x = y))$.
In every partial order the two signatures define the same sets, but they have different atomic formulas.
This matters wherever a notion is stated in terms of atomic formulas, such as the atomic diagram of a structure or a proof by induction on formulas.
In the induction, $x \le y$ is a base case over $\{ \le \}$, but over $\{ < \}$ it is handled by the step for $\lor$.

Watch out: the inequation $x \neq y$ is never atomic, in any signature with equality as a logical symbol.
The symbol $\neq$ is not part of the language, so $x \neq y$ is always shorthand for $\neg (x = y)$.

## Explanations

### L1 human

In a language with only the symbol $<$, the statement $x \le y$ means "$x < y$ or $x = y$".
It has an "or" inside it, so it is not atomic.
The statement $x \neq y$ means "not $x = y$", with a "not" inside it.
Only $x < y$ and $x = y$ are atomic here.

### L2 human

We sort five formulas of $\sigma$ into atomic and not atomic.
The formula $x < y$ is atomic of form 2, and $y = x$ is atomic of form 1.
The formula $\neg (x < y)$ is not atomic: it is a literal, the negation of an atomic formula.
The formula $(x < y \land y < z)$ is not atomic: it is a conjunction.
The formula $\exists z \, (x < z)$ is not atomic: it starts with a quantifier.
The typical use of this sorting is in induction on [[formulas|HYJ10AF6RT]], where only the first two are base cases.
Watch out: a short formula is not always atomic, and a long equation is still atomic.
