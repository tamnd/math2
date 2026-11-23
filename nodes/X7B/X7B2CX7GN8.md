---
tag: X7B2CX7GN8
kind: example
name: The parity congruence and its quotient
msc: ["03B10"]
topics: [TTCRX3NFNY]
audience: grad
instance_of: [Y90Z13AXY8]
uses: [Y90Z13AXY8, DCSXXT4SER, 0G8VEZ3WTK, 983GZBQYT4, P3B1V182N4]
sources:
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: First-order logic without equality
  - url: https://en.wikipedia.org/wiki/Equality_(mathematics)
    locator: Congruence relation
---

## Example

On the integers, "has the same parity as" satisfies every equality axiom of a small language, although it is not identity, and gluing each parity class to a point gives a two-element model.
We work in first-order logic without equality.
Let $L$ be the language with a unary function symbol $f$, a unary relation symbol $P$ and a binary relation symbol $E$, which plays the role of $=$.
Let $\mathcal{M}$ be the [[structure|983GZBQYT4]] with domain $\mathbb{Z}$, $f^{\mathcal{M}}(n) = n + 2$, $P^{\mathcal{M}}$ the set of even integers, and $E^{\mathcal{M}}(m, n)$ when $m \equiv n \pmod 2$.
We check that $\mathcal{M}$ satisfies the [[equality axioms|Y90Z13AXY8]] $\mathrm{Eq}_L$, that $E^{\mathcal{M}}$ is not identity, and we build the quotient.

1. Reflexivity $\forall x\, E(x, x)$ holds, because every integer $n$ satisfies $n \equiv n \pmod 2$.
2. The axiom for $f$ is $\forall x\, \forall y\,(E(x, y) \to E(f(x), f(y)))$.
   It holds, because $m \equiv n$ gives $m + 2 \equiv n + 2 \pmod 2$.
3. The axiom for $P$ is $\forall x\, \forall y\,(E(x, y) \to (P(x) \to P(y)))$.
   It holds, because if $m \equiv n \pmod 2$ and $m$ is even, then $n$ is even.
4. The axiom for $E$ is $\forall x_1\, \forall y_1\, \forall x_2\, \forall y_2\,(E(x_1, y_1) \land E(x_2, y_2) \to (E(x_1, x_2) \to E(y_1, y_2)))$.
   It holds, because $y_1 \equiv x_1 \equiv x_2 \equiv y_2$ gives $y_1 \equiv y_2$.
5. So $E^{\mathcal{M}}$ is a [[congruence|DCSXXT4SER]] of $\mathcal{M}$.
   It is not identity, since $E^{\mathcal{M}}(0, 2)$ holds and $0 \neq 2$.
6. The quotient $\mathcal{M}/E$ has the two classes $[0]$, the even integers, and $[1]$, the odd integers, as its domain.
7. Its function is $\bar f([n]) = [n + 2] = [n]$, so $\bar f$ is the identity map.
   It is well defined by step 2.
8. Its relation $\bar P$ is $\{ [0] \}$.
   It is well defined by step 3.
9. Its relation $\bar E$ holds between $[m]$ and $[n]$ exactly when $m \equiv n$, that is, when $[m] = [n]$.
   So $\bar E$ is identity.

## Remarks

### The quotient satisfies the same formulas

For every formula $\varphi$ of $L$ and every assignment $s$ in $\mathbb{Z}$, $\mathcal{M} \models \varphi[s]$ exactly when $\mathcal{M}/E \models \varphi[\bar s]$, where $\bar s(x) = [s(x)]$.
The proof is an induction on $\varphi$.
By step 2, the value of a term in the quotient is the class of its value in $\mathcal{M}$.
The quantifier steps hold because every class has a representative.
So the two structures are [[elementarily equivalent|P3B1V182N4]].

For example, $\forall x\, E(f(x), x)$ holds in both, since $n + 2 \equiv n$.
The sentence $\exists x\, \exists y\, \neg E(x, y)$ holds in both, with witnesses $0$ and $1$.

### A sentence that seems to count

The sentence $\forall x\, \forall y\, \forall z\,(E(x, y) \lor E(x, z) \lor E(y, z))$ holds in both structures, since among three integers two have the same parity.
Read with $=$ for $E$, it says "there are at most two elements", yet it holds in $\mathcal{M}$, whose domain is infinite.
This is no contradiction, because in $\mathcal{M}$ the symbol $E$ is not identity, and only in the quotient does the sentence count elements.
So first-order sentences cannot tell a congruence from identity.
For this reason, the completeness proof may build a model in which $=$ is a congruence and then pass to the quotient.

### Changing the structure

If $f(n) = n + 1$ instead, step 2 still holds, and $\bar f$ swaps $[0]$ and $[1]$.
If $P$ is the set of positive integers instead, step 3 fails, and there is no quotient; see [[the non-example|A09A5TB5SY]].

## Explanations

### L1 human

Suppose that we only care whether a whole number is even or odd.
Then $0$, $2$ and $-4$ are "the same", and $1$, $3$ and $7$ are "the same".
Adding $2$ never changes the answer, and it never changes whether a number is even.
So we may glue all even numbers into one point and all odd numbers into another point.
The glued picture has only two points.
Still, every statement in our small language is true in it exactly when it is true for the integers.

### L2 human

To pass from a congruence to a quotient structure, we first check that the relation is an equivalence relation.
Next we check that each function respects it, so that related inputs give related outputs.
Then we check that each relation respects it, so that related elements satisfy the same atomic formulas.
Last we define the operations and relations on classes through representatives.
The typical use is the last step of the completeness proof for logic with equality.
Watch out: if we skip the check for one relation symbol, the quotient relation may not be well defined.
