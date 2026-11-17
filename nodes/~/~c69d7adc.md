---
tag: ~c69d7adc
kind: example
name: Non-strict inequality and inequations are not atomic in the language of strict orders
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
not_instance_of:
  - target: ~de213704
    note: in the signature with one symbol for the strict order, the formula for non-strict inequality is a disjunction and the formula for an inequation is a negation, so both contain a connective
uses: [~de213704, ~7e884063, HYJ10AF6RT, ~62799b98]
sources:
  - url: https://en.wikipedia.org/wiki/Atomic_formula
    locator: lead section
---

## Example

Let $\sigma = \set{<}$ with one binary relation symbol.
Usual practice writes $x \le y$ and $x \neq y$.
We check that the formulas behind these abbreviations are not [[atomic|~de213704]].

1. The signature has no symbol $\le$. So $x \le y$ is an abbreviation for the formula $(x < y \lor x = y)$.
2. The atomic formulas of $\sigma$ are $u < w$ and $u = w$ for terms $u, w$, by the [[definition|~7e884063]]. Here the terms are only variables, as $\sigma$ has no function symbols.
3. The formula $(x < y \lor x = y)$ starts with a bracket. An atomic formula of $\sigma$ starts with a variable, or with the symbol $<$ in prefix notation, and never with a bracket.
4. By [[unique readability|~62799b98]], the first symbol fixes the form, so $(x < y \lor x = y)$ is not atomic. It is a disjunction of two atomic formulas.
5. The string $x \neq y$ abbreviates $\neg (x = y)$. It starts with $\neg$, so by the same reason it is not atomic. It is a literal, the negation of an atomic formula.

So both formulas are quantifier-free but not atomic.

## Remarks

The answer depends on the signature.
In the signature $\set{\le}$, the formula $x \le y$ is atomic, and $x < y$ abbreviates $(x \le y \land \neg (x = y))$.
The two signatures give the same definable sets in each order, but different atomic formulas.
This matters for substructures and for quantifier elimination, which speak about atomic formulas.

## Explanations

### L1 human

In a language with only the symbol $<$, the statement $x \le y$ means "$x < y$ or $x = y$".
It has an "or" inside it, so it is not atomic.
The statement $x \neq y$ means "not $x = y$", with a "not" inside it.
Only $x < y$ and $x = y$ are atomic here.

### L2 human

We sort the following formulas of $\sigma$ into atomic and not atomic.

1. $x < y$: atomic, form 2.
2. $y = x$: atomic, form 1.
3. $\neg (x < y)$: not atomic, a literal.
4. $(x < y \land y < z)$: not atomic, a conjunction.
5. $\exists z \, (x < z)$: not atomic, a quantified formula.

The typical use of this distinction is in induction on formulas, where only items 1 and 2 are base cases.
A trap: a short formula is not always atomic, and a long equation is still atomic.
