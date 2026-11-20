---
tag: CEK6DKRS4E
kind: example
name: The inclusion of the integers in the rationals is a ring embedding
msc: ["03C07", "13B02"]
topics: [AY09KYSW81]
audience: ug2
instance_of: [SCRB74SWQN]
uses: [SCRB74SWQN, 0B1261B5ED, 09NWETVTNY, C9494XYEMN]
sources:
  - url: https://en.wikipedia.org/wiki/Embedding
    locator: Universal algebra and model theory
---

## Example

Let $L = \set{+, -, \cdot, 0, 1}$ be the signature of [[rings|0B1261B5ED]].
Let $\mathcal{Z} = (\Z, +, -, \cdot, 0, 1)$ and $\mathcal{Q} = (\Q, +, -, \cdot, 0, 1)$ with the usual operations, and let $h \colon \Z \to \Q$ be $h(n) = n/1$.
We check that $h$ is an [[embedding|SCRB74SWQN]].

1. [[Injective|09NWETVTNY]]: $m/1 = n/1$ means $m \cdot 1 = n \cdot 1$, so $m = n$.
2. Constants: $h(0) = 0/1$ is the zero of $\Q$, and $h(1) = 1/1$ is the one of $\Q$.
3. Addition: $h(m + n) = (m + n)/1 = m/1 + n/1 = h(m) + h(n)$.
4. Negation: $h(-n) = (-n)/1 = -(n/1) = -h(n)$.
5. Multiplication: $h(m \cdot n) = (mn)/1 = (m/1)(n/1) = h(m) \cdot h(n)$.
6. Relations: $L$ has no relation symbols, so there is nothing more to check.

So $h$ is an embedding, and its image $\set{n/1 : n \in \Z}$ is a substructure of $\mathcal{Q}$ isomorphic to $\mathcal{Z}$.

## Remarks

The [[preservation theorem|C9494XYEMN]] gives three kinds of transfer along $h$.

- Quantifier-free formulas: $2 \cdot 3 = 6$ holds in $\Z$ and in $\Q$, and $x \cdot x = 1 + 1$ has no solution in either.
- Universal sentences go down: the commutativity of $\cdot$ in $\Q$ gives commutativity in $\Z$.
- Existential formulas go up but not down: $\exists y \, (x \cdot y = 1)$ holds of $2$ in $\Q$ (with $y = 1/2$) and fails of $2$ in $\Z$.

The answer changes with the signature.
If we add a unary symbol ${}^{-1}$ for inverses (with $0^{-1} = 0$) to $L$, then $\Z$ with any inverse map is not a substructure of $\Q$, because $2^{-1} = 1/2 \notin \Z$.
The field axioms are universal in this signature, so every substructure of $\Q$ is then a field.
With a relation symbol $<$ added, $h$ is still an embedding, because $m < n$ holds in $\Z$ exactly when $m/1 < n/1$ in $\Q$.

## Explanations

### L1 human

Every whole number is also a fraction: $3$ is the fraction $3/1$.
Adding, subtracting and multiplying whole numbers gives the same results when we do it with the fractions.
Different whole numbers give different fractions.
So the whole numbers sit inside the fractions without any change.

### L2 human

We use the embedding to answer a question about the integers.

1. In $\Q$ every element $x$ satisfies $x \cdot 1 = x$, a universal sentence.
2. By part 4 of the preservation theorem, the same sentence holds in $\Z$.
3. In $\Q$ the formula $\exists y \, (y + y = x)$ holds for every $x$, with $y = x/2$.
4. In $\Z$ it fails for $x = 1$, because $y + y = 1$ has no integer solution.

The typical use is to prove universal identities in a larger structure where computation is easier.
A trap is to transfer "every element is divisible by $2$" from $\Q$ to $\Z$; it has a "there exists" inside, and it fails in $\Z$.
