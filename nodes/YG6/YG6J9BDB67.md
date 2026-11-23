---
tag: YG6J9BDB67
kind: example
name: One symbol for unary and binary minus is not a signature
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
not_instance_of:
  - target: WDVVEYD6AT
    note: in a signature each symbol has exactly one arity, and a minus sign of arity 1 and 2 makes a string of symbols readable in two ways
uses: [WDVVEYD6AT, 6D3WA7N2W4, MSXX2P86CY]
sources:
  - url: https://en.wikipedia.org/wiki/Signature_(logic)
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.3
---

## Example

School algebra uses one minus sign for two jobs, $-3$ and $5 - 3$, but a formal language cannot.
Take the symbols $+$, $-$, $0$ and $1$, and let $-$ stand both for negation, with arity $1$, and for subtraction, with arity $2$.
Write terms in prefix notation, as Enderton does: a function symbol of arity $n$ comes first and is followed by its $n$ arguments, with no brackets.
We check that this list is not a signature and that the double use makes terms ambiguous.

1. A [[signature|WDVVEYD6AT]] gives each symbol one [[arity|MSXX2P86CY]], through a function $\operatorname{ar}$.
   Here $\operatorname{ar}(-)$ would have the two values $1$ and $2$, so the list is not a signature.
2. Consider the string $- - x \, y$, and read the first $-$ as binary.
   Its arguments must be two terms: $- x$ with unary minus, and $y$, which gives $(-x) - y$.
3. Now read the first $-$ as unary.
   Its one argument must be the rest of the string, $- x \, y$, which with binary minus is $x - y$, so the whole is $-(x - y)$.
4. The other two choices fail.
   In step 2 a binary second $-$ uses up both $x$ and $y$ and leaves no second argument, and in step 3 a unary second $-$ leaves $y$ unused.
5. So the string has exactly two readings, $(-x) - y$ and $-(x - y)$.
6. For $x = 1$ and $y = 2$ in $\mathbb{Z}$, the two readings have different values:
   $$(-1) - 2 = -3, \qquad -(1 - 2) = 1.$$

So a symbol with two arities breaks the unique readability of [[terms|6D3WA7N2W4]], and with it the value of a term.

## Remarks

The fix is to use two different symbols, such as $-$ for subtraction and $\mathrm{neg}$ for negation.
Books on rings often take only negation as a symbol and write $u - w$ as short for $u + (-w)$.
With fully bracketed infix notation, $(x - y)$ and $(-x)$ can be told apart by the brackets.
Even then the formal signature has two symbols, which are only printed alike.
Mathlib avoids the problem by construction, since a symbol lives in `Functions n` for exactly one $n$.

## Explanations

### L1 human

School mathematics uses the minus sign in two ways: $-3$ and $5 - 3$.
In a formal language each symbol must have a fixed number of inputs.
Without brackets, the string "minus minus $x$ $y$" can mean "$(-x) - y$" or "$-(x - y)$".
For $x = 1$ and $y = 2$ these are $-3$ and $1$.
So a formal language needs two different symbols.

### L2 human

We repeat the test with two different symbols, $\mathrm{neg}$ of arity $1$ and $-$ of arity $2$.
The string $- \, \mathrm{neg} \, x \, y$ has one reading: $-$ needs two terms, which must be $\mathrm{neg} \, x$ and $y$, so it means $(-x) - y$.
The string $\mathrm{neg} - x \, y$ has one reading: $\mathrm{neg}$ needs one term, which must be $- x \, y$, so it means $-(x - y)$.
The string $- - x \, y$ is now not a term at all: the second $-$ takes $x$ and $y$, and the first $-$ has no second argument.
Each string now has at most one reading, as the [[unique readability theorem|3QPV4XW8MC]] promises.
Watch out: brackets in printed formulas often hide such ambiguities, but a program that parses prefix strings meets them directly.
