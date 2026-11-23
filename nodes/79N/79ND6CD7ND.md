---
tag: 79ND6CD7ND
kind: example
name: The equality axioms for the signature of groups
msc: ["03B10", "20A05"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [Q1494G7FBM]
uses: [Q1494G7FBM, WDVVEYD6AT, G5S1M9, DCSXXT4SER]
sources:
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Equality and its axioms
  - book: isbn:9781482237726
    locator: Chapter 2
---

## Example

Let $\sigma = \{ \cdot, e, {}^{-1} \}$ be the [[signature|WDVVEYD6AT]] of [[groups|G5S1M9]]: a binary function symbol, a constant and a unary function symbol.
In [[first-order logic with equality|Q1494G7FBM]] the equality axioms for $\sigma$ are these four sentences.

1. (E1) $\forall x \, (x = x)$.
2. (E2) $\forall x_1 \, \forall x_2 \, \forall y_1 \, \forall y_2 \, \big( (x_1 = y_1 \land x_2 = y_2) \to x_1 \cdot x_2 = y_1 \cdot y_2 \big)$.
3. (E3) $\forall x \, \forall y \, \big( x = y \to x^{-1} = y^{-1} \big)$.
4. (E4) $\forall x_1 \, \forall x_2 \, \forall y_1 \, \forall y_2 \, \big( (x_1 = y_1 \land x_2 = y_2) \to (x_1 = x_2 \to y_1 = y_2) \big)$.

First we check that the list is complete.
The rule asks for reflexivity and one substitution axiom for each symbol.
The constant $e$ has arity $0$, so its substitution axiom is $e = e$, an instance of (E1).
The function symbols $\cdot$ and ${}^{-1}$ have arities $2$ and $1$, and (E2) and (E3) are their axioms.
The only relation symbol is $=$, and (E4) is its axiom.

Then we check that each axiom is true in every structure for $\sigma$, where $=$ means identity.
(E1) holds because each element is itself.
For (E2), if $a_1$ is the same element as $b_1$ and $a_2$ the same as $b_2$, then $a_1 \cdot a_2$ and $b_1 \cdot b_2$ are the same element.
(E3) and (E4) hold for the same reason.

## Remarks

The four axioms are logically valid, so they add nothing to the meaning of $=$.
They are there for the proof system, which sees $=$ only as a symbol and needs rules to use it.

If you read $=$ as some other relation $E$, then (E1) to (E4) say exactly that $E$ is an equivalence relation that respects $\cdot$ and ${}^{-1}$, that is, a [[congruence|DCSXXT4SER]].
(E1) gives reflexivity, and (E4) with (E1) gives symmetry and transitivity, by the instances worked out for [[first-order logic with equality|Q1494G7FBM]].
For example, on the integers under addition the relation "same remainder mod $3$" satisfies all four axioms.

A larger signature adds one substitution axiom for each new symbol.
The signature of rings $\{ +, \cdot, -, 0, 1 \}$ needs axioms for $+$, $\cdot$ and the unary $-$, while $0$ and $1$ need none beyond (E1).
So a finite signature always has finitely many equality axioms.

## Explanations

### L1 human

The equality axioms are the rules for equals that you use in algebra without a second thought.
Everything equals itself.
If $a = b$ and $c = d$, then $a \cdot c = b \cdot d$.
If $a = b$, then $a^{-1} = b^{-1}$.
And if $a = b$, $c = d$ and $a = c$, then $b = d$.

### L2 human

We use (E2) and (E3) to prove $x = y \to (x \cdot x)^{-1} = (y \cdot y)^{-1}$.
Assume $x = y$.
Instantiate (E2) with $x_1 := x$, $x_2 := x$, $y_1 := y$ and $y_2 := y$:
$$(x = y \land x = y) \to x \cdot x = y \cdot y.$$
So $x \cdot x = y \cdot y$.
Now instantiate (E3) with the terms $x \cdot x$ for $x$ and $y \cdot y$ for $y$:
$$x \cdot x = y \cdot y \to (x \cdot x)^{-1} = (y \cdot y)^{-1}.$$
So $(x \cdot x)^{-1} = (y \cdot y)^{-1}$.
The typical use is the general fact that equal terms can replace each other inside any term, proved by induction on the term in exactly this way.
Watch out: the axioms speak about variables, so the second step needs the instantiation of $\forall$ with terms, not only with variables.
