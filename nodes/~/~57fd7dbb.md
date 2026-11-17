---
tag: ~57fd7dbb
kind: example
name: The parity congruence and its quotient
msc: ["03B10"]
topics: [TTCRX3NFNY]
audience: grad
instance_of: [~65701c23]
uses: [~65701c23, DCSXXT4SER, 0G8VEZ3WTK, 983GZBQYT4, P3B1V182N4]
sources:
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: First-order logic without equality
  - url: https://en.wikipedia.org/wiki/Equality_(mathematics)
    locator: Congruence relation
---

## Example

We work in first-order logic without equality.
Let $L$ be the language with a unary function symbol $f$, a unary relation symbol $P$ and a binary relation symbol $E$.
The symbol $E$ plays the role of $=$.
Let $\mathcal{M}$ be the [[structure|983GZBQYT4]] with domain $\mathbb{Z}$, $f^{\mathcal{M}}(n) = n + 2$, $P^{\mathcal{M}}$ the set of even integers, and $E^{\mathcal{M}}(m, n)$ when $m \equiv n \pmod 2$.
We check that $\mathcal{M}$ satisfies the [[equality axioms|~65701c23]] $\mathrm{Eq}_L$, that $E^{\mathcal{M}}$ is not identity, and we build the quotient.

1. Reflexivity $\forall x\, E(x,x)$: every integer $n$ satisfies $n \equiv n \pmod 2$.
2. The axiom for $f$, $\forall x\,\forall y\,(E(x,y) \to E(f(x), f(y)))$: if $m \equiv n$, then $m + 2 \equiv n + 2 \pmod 2$.
3. The axiom for $P$, $\forall x\,\forall y\,(E(x,y) \to (P(x) \to P(y)))$: if $m \equiv n \pmod 2$ and $m$ is even, then $n$ is even.
4. The axiom for $E$, $\forall x_1\,\forall y_1\,\forall x_2\,\forall y_2\,(E(x_1,y_1) \land E(x_2,y_2) \to (E(x_1,x_2) \to E(y_1,y_2)))$: from $y_1 \equiv x_1 \equiv x_2 \equiv y_2$ follows $y_1 \equiv y_2$.
5. So $E^{\mathcal{M}}$ is a [[congruence|DCSXXT4SER]] of $\mathcal{M}$. It is not identity: $E^{\mathcal{M}}(0, 2)$ holds and $0 \neq 2$.
6. The quotient $\mathcal{M}/E$ has the two classes $[0]$ (even) and $[1]$ (odd) as its domain.
7. Its function is $\bar f([n]) = [n + 2] = [n]$, so $\bar f$ is the identity map. It is well defined by step 2.
8. Its relation $\bar P$ is $\{[0]\}$. It is well defined by step 3.
9. Its relation $\bar E$ holds between $[m]$ and $[n]$ exactly when $m \equiv n$, that is, when $[m] = [n]$. So $\bar E$ is identity.

## Remarks

For every formula $\varphi$ of $L$ and every assignment $s$ in $\mathbb{Z}$, $\mathcal{M} \models \varphi[s]$ exactly when $\mathcal{M}/E \models \varphi[\bar s]$, where $\bar s(x) = [s(x)]$.
The proof is an induction on $\varphi$.
By step 2, the value of a term in the quotient is the class of its value in $\mathcal{M}$.
The quantifier steps hold because every class has a representative.
So the two structures are [[elementarily equivalent|P3B1V182N4]].
Some sentences that hold in both:

1. $\forall x\, E(f(x), x)$, since $n + 2 \equiv n$.
2. $\exists x\,\exists y\, \neg E(x,y)$, witnessed by $0$ and $1$.
3. $\forall x\,\forall y\,\forall z\,(E(x,y) \lor E(x,z) \lor E(y,z))$, since among three integers two have the same parity.

Sentence 3, read with $=$ for $E$, says "there are at most two elements".
It holds in $\mathcal{M}$, whose domain is infinite.
This is no contradiction: in $\mathcal{M}$ the symbol $E$ is not identity, and only in the quotient does the sentence count elements.
So first-order sentences cannot tell a congruence from identity.
For this reason, the completeness proof may build a model in which $=$ is a congruence and then pass to the quotient.

If $f(n) = n + 1$ instead, step 2 still holds, and $\bar f$ swaps $[0]$ and $[1]$.
If $P$ is the set of positive integers instead, step 3 fails, and there is no quotient; see [[the non-example|~d0c774c8]].

## Explanations

### L1 human

Suppose that we only care whether a whole number is even or odd.
Then $0$, $2$ and $-4$ are "the same", and $1$, $3$ and $7$ are "the same".
Adding $2$ never changes the answer, and it never changes whether a number is even.
So we may glue all even numbers into one point and all odd numbers into another point.
The glued picture has only two points.
Still, every statement in our small language is true in it exactly when it is true for the integers.

### L2 human

To pass from a congruence to a quotient structure, follow these steps.

1. Check that the relation is an equivalence relation.
2. Check that each function respects it: related inputs give related outputs.
3. Check that each relation respects it: related elements satisfy the same atomic formulas.
4. Define the operations and relations on classes through representatives.

The typical use is the last step of the completeness proof for logic with equality.
A trap is to skip step 3 for one of the relation symbols; then the quotient relation is not well defined.
