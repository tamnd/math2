---
tag: 095ZHQ7WCJ
kind: statement
role: theorem
name: In a PID a nonzero element is irreducible iff it generates a maximal ideal
msc: [13F10]
uses: [0RZYDVZ475, 052SDEPZH7, 09J6KGT65G, 00A2EDFT9Q]
sources:
  - url: https://en.wikipedia.org/wiki/Principal_ideal_domain
    locator: Properties
---

## Statement

Let $R$ be a [[principal ideal domain|0RZYDVZ475]] and let $p \in R$ with $p \neq 0$.
Then $p$ is [[irreducible|052SDEPZH7]] if and only if the principal ideal $(p)$ is a [[maximal ideal|09J6KGT65G]].

## Remarks

The proof: an ideal $I$ with $(p) \subseteq I$ is $(a)$ with $a \mid p$. If $p$ is irreducible, then $a$ is a unit or an associate of $p$, so $I = R$ or $I = (p)$.
A consequence is that $R/(p)$ is a [[field|0QA8CHH8MG]] for each irreducible $p$. For example, $\mathbb{Q}[x]/(x^2 - 2)$ is a field.
In a principal ideal domain, every nonzero prime ideal is maximal.

## Explanations

### L1 human

In a principal ideal domain, ideals that contain $(p)$ come from the divisors of $p$.
An irreducible $p$ has only trivial divisors.
So no ideal fits strictly between $(p)$ and the whole ring.
