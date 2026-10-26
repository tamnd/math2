---
tag: 0F0K8DB9TD
kind: statement
role: proposition
name: Prime elements are irreducible in an integral domain
msc: [13A05]
uses: [0MNHXBSX3M, 052SDEPZH7, 09S3PFBEPM]
sources:
  - url: https://en.wikipedia.org/wiki/Prime_element
    locator: Irreducible elements
---

## Statement

Let $R$ be an [[integral domain|09S3PFBEPM]] and let $p \in R$ be a [[prime element|0MNHXBSX3M]].
Then $p$ is [[irreducible|052SDEPZH7]].

## Remarks

The proof: let $p = a b$. Then $p \mid a b$, so $p \mid a$, say. Write $a = p c$. Then $p = p c b$, and [[cancellation|0GJM24EXP9]] gives $c b = 1$, so $b$ is a unit.
The converse is false in general: in $\mathbb{Z}[\sqrt{-5}]$, [[$2$ is irreducible but not prime|0CHE3J7QMX]].
In a [[unique factorization domain|06YMXJMXYS]], [[irreducible elements are prime|0QRCFZKXH8]].

## Explanations

### L1 human

Suppose that a prime $p$ factors as $a b$.
Then $p$ divides one factor, so that factor is at least as large as $p$ for divisibility.
The other factor must then be a unit.
