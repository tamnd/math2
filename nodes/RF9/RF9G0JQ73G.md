---
tag: RF9G0JQ73G
kind: example
name: A material implication that is not a strict implication
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
not_instance_of:
  - target: 5JW54NP52K
    note: the implication is true at the actual world but fails at an accessible world, so it is not strict
uses: [5JW54NP52K, NGHWZ9Y7ZV, 05006AJ7DZ, E87G6ZTMTN, G989VP2NGP]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_logic
    locator: lead section
---

## Example

Take the [[Kripke model|NGHWZ9Y7ZV]]
$$W = \set{1, 2}, \quad R = \set{(1, 1), (1, 2), (2, 2)}, \quad V(p) = \set{1, 2}, \quad V(q) = \set{1}.$$
We show that at $1$ the material implication $p \to q$ is true, while the [[strict implication|5JW54NP52K]] $\square(p \to q)$ is false.

1. At $1$, $q$ is true, so $p \to q$ is true.
2. At $2$, $p$ is true and $q$ is false, so $p \to q$ is false.
3. The world $1$ sees $2$, so $\square(p \to q)$ is false at $1$.
4. So $p \to q$ holds at $1$, but $p$ does not strictly imply $q$ at $1$.
5. The formula $q \to (p \to q)$ is a [[tautology|05006AJ7DZ]].
6. The formula $q \to \square(p \to q)$ is false at $1$: $q$ is true at $1$ by the valuation, and $\square(p \to q)$ is false by step 3.
7. By [[soundness|E87G6ZTMTN]], $\mathsf{K}$ does not prove $q \to \square(p \to q)$.

## Remarks

The example shows that a true consequent makes a material implication true, but not a strict one.
Strict implication asks for $p \to q$ at every successor, and the successor $2$ is a world where $q$ fails.
Step 7 contrasts with the theorem $\square q \to \square(p \to q)$: a necessary $q$ is strictly implied by every $p$, a true $q$ is not.
The box does not pass inside an implication: $\square(q \to (p \to q))$ is a theorem by [[necessitation|G989VP2NGP]], while $q \to \square(p \to q)$ is not.
If we remove the pair $(1, 2)$, then $1$ sees only itself, and $\square(p \to q)$ becomes true at $1$.
If we change $V(q)$ to $W$, then $p \to q$ is true at both worlds, and the strict implication holds at both.

## Explanations

### L1 human

"If it is Monday, then the shop is open" can be true today just because the shop is open today.
"Necessarily, if it is Monday, then the shop is open" asks for more.
It must hold in every situation we consider possible.
If in some possible Monday the shop is closed, the strict form fails.
So a material "if then" can be true by accident, and a strict one cannot.

### L2 human

1. Take the model above and test $\square(q \to (p \to q))$ at $1$.
2. At $1$ and at $2$, the tautology $q \to (p \to q)$ is true.
3. So $\square(q \to (p \to q))$ is true at $1$, as necessitation predicts.
4. But $q \to \square(p \to q)$ is false at $1$, so the box cannot be moved past $q$.

The typical use of this example is to test a proposed reading of "if then" against the strict reading.
A trap: from $q$ and the tautology $q \to (p \to q)$ we get $p \to q$, but not $\square(p \to q)$; strictness needs $\square q$.
