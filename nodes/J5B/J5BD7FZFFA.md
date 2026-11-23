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

A function symbol must get exactly as many arguments as its arity, or the string is not a term.
Let $\sigma = \{ 0, S, + \}$ with arities $0, 1, 2$.
We check that the strings $+(x)$ and $S(x, y)$ are not [[terms|6D3WA7N2W4]] of $\sigma$.

1. The terms are the smallest set closed under the three clauses of the [[definition|BQQ0FPFZ67]], so a string is a term only if some clause produces it from terms.
2. The string $+(x)$ starts with $+$, so it is not a variable and not a constant symbol, and only the function clause could produce it.
3. The function clause for $+$ produces only strings $+(t_1, t_2)$ with two terms, since $\operatorname{ar}(+) = 2$.
4. A string $+(t_1, t_2)$ has a comma at bracket depth $1$, between $t_1$ and $t_2$.
   The string $+(x)$ has no comma, so it is not of this form, and it is not a term.
5. In the same way, the function clause for $S$ produces only strings $S(t_1)$, since $\operatorname{ar}(S) = 1$.
6. In $S(x, y)$ the part between the outer brackets is the string $x, y$.
   This string is not a term: it starts with a variable, and a term that starts with a variable is that variable alone.

So both strings fail the [[arity|MSXX2P86CY]] condition and are not terms.

## Remarks

The arity condition is what gives every term a value.
In a structure $+$ is read as a function of two arguments, so $+(x)$ would have no value.
Some programming languages allow partial application, where $+(x)$ denotes the function $y \mapsto x + y$.
First-order logic has no such terms, because the value of a term is an element, never a function.
In Mathlib a term `func f ts` has `f : L.Functions n` and `ts : Fin n → L.Term α`, so the type checker rejects a wrong number of arguments before any proof begins.

## Explanations

### L1 human

The symbol $+$ needs two inputs, as in $x + y$.
The string $+(x)$ gives it only one input, so it does not name a number.
The symbol $S$ for "next number" needs one input, so $S(x, y)$ does not name a number either.
A term must give each symbol exactly the number of inputs that the signature says.

### L2 human

We test three nearby strings.
The string $+(x, S(0))$ is a term, since $+$ gets the two terms $x$ and $S(0)$.
The string $+(x, S)$ is not a term, since $S$ alone is not a term: it has arity $1$ and is not a constant symbol.
The string $S(+(x, x))$ is a term, since $S$ gets the one term $+(x, x)$.
A parser uses exactly this check and rejects a string as soon as a symbol has the wrong number of arguments.
Watch out: the constant symbol $0$ has arity $0$, so $0$ alone is a term and $S(0)$ is a term, but $S()$ is not.
