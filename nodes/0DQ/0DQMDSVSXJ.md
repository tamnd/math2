---
tag: 0DQMDSVSXJ
kind: statement
role: theorem
name: Universal property of the polynomial ring
msc: [13F20]
uses: [0Q9EZS90GY, 0GGE0Z0JQ1, 0125QVNCFQ]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_ring
    locator: Categorical characterization
---

## Statement

Let $R$ and $S$ be [[commutative rings|0GYGHKX834]], let $\varphi \colon R \to S$ be a [[ring homomorphism|0GGE0Z0JQ1]] and let $s \in S$.
Then there is exactly one ring homomorphism $\Phi \colon R[x] \to S$ such that $\Phi(r) = \varphi(r)$ for all $r \in R$ and $\Phi(x) = s$.
It is given by $\Phi(a_0 + a_1 x + \dots + a_n x^n) = \varphi(a_0) + \varphi(a_1) s + \dots + \varphi(a_n) s^n$.

## Remarks

With $S = R$, $\varphi$ the identity and $s = c$, the map $\Phi$ is the [[evaluation homomorphism|0125QVNCFQ]] at $c$.
In the language of algebras: for each commutative $R$-algebra $A$ and each $a \in A$, there is exactly one $R$-algebra homomorphism $R[x] \to A$ that sends $x$ to $a$.
This property characterizes $R[x]$ up to a unique isomorphism.

## Explanations

### L1 human

A ring homomorphism from $R[x]$ is fixed by two choices: what it does on the coefficients, and where it sends $x$.
Every pair of choices works, and it gives exactly one homomorphism.
Evaluation at a number is the main example.
