---
tag: J5BD7FZFFA
kind: example
name: A function symbol with the wrong number of arguments does not give a term
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
not_instance_of:
  - target: 6D3WA7N2W4
    note: the strings +(x) and S(x, y) apply a function symbol to a number of arguments that differs from its arity, so no clause of the definition of terms produces them
uses: [6D3WA7N2W4, BQQ0FPFZ67, MSXX2P86CY]
sources:
  - url: https://en.wikipedia.org/wiki/Term_(logic)
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.1
---

## Example

Let $\sigma = \set{0, S, +}$ with arities $0, 1, 2$.
We check that the strings $+(x)$ and $S(x, y)$ are not [[terms|6D3WA7N2W4]] of $\sigma$.

1. The set of terms is the smallest set closed under the three clauses of the [[definition|BQQ0FPFZ67]]. So a string is a term only if some clause produces it from terms.
2. The string $+(x)$ starts with $+$. It is not a variable and not a constant symbol, so only the function clause could produce it.
3. The function clause for $+$ produces only strings $+(t_1, t_2)$ with two terms, since $\operatorname{ar}(+) = 2$.
4. A string $+(t_1, t_2)$ contains a comma outside of $t_1$ and $t_2$, at bracket depth $1$. The string $+(x)$ has no comma, so it is not of this form.
5. So no clause produces $+(x)$, and it is not a term.
6. In the same way, the function clause for $S$ produces only strings $S(t_1)$, with $\operatorname{ar}(S) = 1$.
7. In $S(x, y)$ the part between the outer brackets is $x, y$. This string is not a term: it starts with a variable, and a term that starts with a variable is that variable alone.

So both strings fail the [[arity|MSXX2P86CY]] condition and are not terms.

## Remarks

The arity condition makes the value of a term well defined: in a structure, $+$ is interpreted as a function of two arguments, and $+(x)$ would have no value.
Some programming languages allow partial application, where $+(x)$ denotes the function $y \mapsto x + y$.
First-order logic has no such terms, because the values of terms are elements, not functions.
In Mathlib a term `func f ts` has `f : L.Functions n` and `ts : Fin n → L.Term α`, so the type checker rejects a wrong number of arguments.

## Explanations

### L1 human

The symbol $+$ needs two inputs, as in $x + y$.
The string $+(x)$ gives it only one input, so it does not name a number.
The symbol $S$ for "next number" needs one input, so $S(x, y)$ does not name a number either.
A term must give each symbol exactly the number of inputs that the signature says.

### L2 human

We check three nearby strings.

1. $+(x, S(0))$ is a term: $+$ gets the two terms $x$ and $S(0)$.
2. $+(x, S)$ is not a term: $S$ alone is not a term, because $S$ has arity $1$ and is not a constant symbol.
3. $S(+(x, x))$ is a term: $S$ gets the one term $+(x, x)$.

The typical use of the arity check is in a parser, which rejects a string as soon as a symbol has the wrong number of arguments.
A trap: the constant symbol $0$ has arity $0$, so it is a term by itself, and $S(0)$ is a term, but $S()$ is not.
