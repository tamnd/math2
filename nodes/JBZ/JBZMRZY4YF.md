---
tag: JBZMRZY4YF
kind: definition
name: Field homomorphism
msc: [12F05, "12E99"]
defines: EZVN87C88J
uses: [0QA8CHH8MG, 0GGE0Z0JQ1]
sources:
  - url: https://en.wikipedia.org/wiki/Field_(mathematics)
---

## Definition

Let $K$ and $L$ be [[fields|0QA8CHH8MG]].
A field homomorphism is a map $f \colon K \to L$ such that:

1. $f(a + b) = f(a) + f(b)$ for all $a, b \in K$;
2. $f(ab) = f(a) f(b)$ for all $a, b \in K$;
3. $f(1) = 1$.

## Remarks

So a field homomorphism is a [[ring homomorphism|0GGE0Z0JQ1]] between two fields.
Example: complex conjugation $f(a + bi) = a - bi$ on $\C$ satisfies the three clauses, since conjugation respects sums and products and fixes $1$.
Non-example: $f(a) = 2a$ on $\Q$ is additive, but $f(1) = 2 \ne 1$ and $f(1 \cdot 1) = 2 \ne 4 = f(1) f(1)$.
Every field homomorphism is injective, by [[ring homomorphisms from a field are injective|09N7DZ7SDB]].
So $f(K)$ is a [[subfield|07QY5RPFBR]] of $L$ isomorphic to $K$, and $f$ is also called an embedding of $K$ into $L$.
Since $f(n \cdot 1) = n \cdot 1$ and $f$ is injective, $K$ and $L$ have the same [[characteristic|1ZB13N78XW]].
A bijective field homomorphism is a field isomorphism.

## Explanations

### L1 human

A field homomorphism is a map that keeps sums, products and the number $1$.
Because a field has inverses, such a map cannot collapse anything.
