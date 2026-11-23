---
tag: A09A5TB5SY
kind: example
name: An equivalence relation that violates the substitution schema
msc: ["03B10"]
topics: [TTCRX3NFNY]
audience: grad
not_instance_of:
  - target: Y90Z13AXY8
    note: parity on the integers is reflexive, symmetric and transitive, but it fails the substitution schema for the predicate "positive", so it does not satisfy the rules for equality
uses: [Y90Z13AXY8, 0G8VEZ3WTK, DCSXXT4SER, 983GZBQYT4, DSQ17TNW1C]
sources:
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Equality and its axioms
  - url: https://en.wikipedia.org/wiki/Equality_(mathematics)
    locator: Axioms
---

## Example

The numbers $1$ and $-1$ have the same parity, but $1$ is positive and $-1$ is not, so "same parity" cannot serve as equality in a language that can say "positive".
Let the language have a binary relation symbol $E$, which plays the role of $=$, and a unary relation symbol $P$.
Let $\mathcal{M}$ be the [[structure|983GZBQYT4]] with domain $\mathbb{Z}$, $E^{\mathcal{M}}(m, n)$ when $m \equiv n \pmod 2$, and $P^{\mathcal{M}}$ the set of positive integers.
We show that $E^{\mathcal{M}}$ is an [[equivalence relation|0G8VEZ3WTK]] but does not satisfy the [[rules for equality|Y90Z13AXY8]].

1. Reflexivity holds, because $n \equiv n \pmod 2$ for every integer $n$.
2. Symmetry holds, because $m \equiv n$ gives $n \equiv m$.
3. Transitivity holds, because $m \equiv n$ and $n \equiv k$ give $m \equiv k$.
4. The substitution schema has the instance $\forall x\, \forall y\,(E(x, y) \to (P(x) \to P(y)))$, with the atomic formula $P(x)$.
5. Take $x = 1$ and $y = -1$.
   Then $E(1, -1)$ holds, since both numbers are odd.
6. $P(1)$ holds, since $1 > 0$, and $P(-1)$ fails, since $-1 < 0$.
7. So the instance is false in $\mathcal{M}$, and $E^{\mathcal{M}}$ is not a [[congruence|DCSXXT4SER]] for $P$.

The condition that fails is the substitution principle.
The three properties of an equivalence relation are not enough.

## Remarks

### No quotient structure

Because of step 7, the quotient by $E^{\mathcal{M}}$ does not exist as a structure for this language.
The class of $1$ is the set of odd integers, and it contains both positive and negative numbers.
So the statement "the class is in $P$" has no well-defined truth value.
Read with $=$ for $E$, the structure $\mathcal{M}$ violates a logical axiom, so it is not a model in logic with equality.

### The opposite failure

Indiscernibility does not force identity in first-order logic either.
In $(\mathbb{Z}, <)$, with the true identity as $=$, the map $n \mapsto n + 1$ is an [[automorphism|DSQ17TNW1C]].
Hence $0$ and $1$ satisfy exactly the same formulas $\varphi(x)$ with one free variable.
So every formula $\varphi(x) \leftrightarrow \varphi(y)$ is true at $x = 0$, $y = 1$, while $x = y$ is false.
The identity of indiscernibles is therefore not a law of first-order logic.

### The repair

If $P$ is replaced by "even", the substitution schema holds, and the relation becomes a congruence; see [[the parity congruence and its quotient|X7B2CX7GN8]].

## Explanations

### L1 human

Call two whole numbers "alike" when both are even or both are odd.
This is a fair way to sort numbers into two groups.
But "alike" is not "equal": $1$ and $-1$ are alike, yet $1$ is positive and $-1$ is not.
Real equality must pass every property from one side to the other.
This sorting fails that test for the property "positive".

### L2 human

To test whether a relation $E$ can serve as equality in a structure, we check the schema for each symbol of the language.
For each relation symbol $R$, $E$-related arguments must give the same truth value of $R$.
For each function symbol $f$, $E$-related arguments must give $E$-related values.
Reflexivity must hold as well.
Here the test fails for $R = P$ with the arguments $1$ and $-1$.
The typical use of this test is in the construction of a quotient model.
Watch out: checking only that $E$ is an equivalence relation is not enough, because the other symbols of the language matter too.
