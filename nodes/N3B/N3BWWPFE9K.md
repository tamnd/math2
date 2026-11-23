---
tag: N3BWWPFE9K
kind: example
name: The expression x^2 + 1 is not a predicate
msc: ["03B10", "97E30"]
topics: [PM1AYWABA7]
audience: school
not_instance_of:
  - target: 0QHEWQD30B
    note: a substitution of a number for x gives a number, not a proposition, so the expression is a term and not a predicate
uses: [0QHEWQD30B, 0T3DPBG981, 0ZGC7ZESYN]
sources:
  - url: https://en.wikipedia.org/wiki/Predicate_(logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Term_(logic)
    locator: lead section
---

## Example

Consider the expression $x^2 + 1$, with $x$ ranging over $D = \mathbb{Z}$.
We show that it is not a [[predicate|0T3DPBG981]] on $D$.

1. A predicate on $D$ must give a [[proposition|0ZGC7ZESYN]] for each value of its free variable.
2. Substitute $x = 2$.
   The result is $2^2 + 1$, which is the number $5$.
3. The number $5$ is neither true nor false, so it is not a proposition.
4. So the second condition of the definition fails at $x = 2$, and $x^2 + 1$ is not a predicate.

The expression $x^2 + 1$ is a term: for each value of $x$ it names an object.
A predicate needs a relation between terms, for example the equation $x^2 + 1 = 5$.
For that predicate on $\mathbb{Z}$, the value $x = 2$ gives "$5 = 5$", which is true, and $x = 0$ gives "$1 = 5$", which is false.
Its truth set is $\{-2, 2\}$, because $x^2 + 1 = 5$ means $x^2 = 4$.

## Remarks

Expressions with variables come in two kinds: terms, whose values are objects, and formulas, whose values are truth values.
In first-order logic, terms are built from variables, constants and function symbols, and predicate symbols are applied to terms to give formulas.
So $\sin x$, $f(x)$ and $\{x\}$ are terms, while $\sin x = 0$, $f(x) > 0$ and $x \in A$ are predicates.

## Explanations

### L1 human

"$x^2 + 1$" is like a machine that turns a number into a number: $2$ becomes $5$.
A predicate is a sentence that becomes true or false.
"$x^2 + 1 = 5$" is such a sentence: it is true for $x = 2$ and false for $x = 0$.
So the equals sign, or another relation, turns the number machine into a predicate.

### L2 human

Sort four expressions with the free variable $n$ on $\mathbb{N}$.
The expression $2n + 1$ has the value $7$ at $n = 3$, a number, so it is a term.
The expression $2n + 1 > 6$ has the value "$7 > 6$" at $n = 3$, a true proposition, so it is a predicate.
The expression $\gcd(n, 6)$ has the value $2$ at $n = 4$, so it is a term.
The expression $\gcd(n, 6) = 1$ has the value "$2 = 1$" at $n = 4$, which is false, so it is a predicate, and its truth set is the set of numbers coprime to $6$.
The same test helps when you read a definition: the notion being defined, such as "$n$ is coprime to $6$", must be a predicate and not a term.
Watch out: "$f(x) = x^2$" in a definition of $f$ defines a term, and it is not a claim with a truth value.
