---
tag: 0SGTMBEWRF
kind: definition
name: Equivalence relation
msc: ["03E20"]
defines: 0G8VEZ3WTK
uses: [0XEGNW851S, 0N9SA25Z3V, 0CYRECG2YQ]
sources:
  - url: https://en.wikipedia.org/wiki/Equivalence_relation
    locator: lead section
---

## Definition

Let $A$ be a set.
An equivalence relation on $A$ is a [[binary relation|08EJC6Q25H]] $\sim$ on $A$ that is [[reflexive|0XEGNW851S]], [[symmetric|0N9SA25Z3V]] and [[transitive|0CYRECG2YQ]]. For all $a, b, c \in A$:

1. $a \sim a$;
2. $a \sim b$ implies $b \sim a$;
3. $a \sim b$ and $b \sim c$ imply $a \sim c$.

## Remarks

For a fixed integer $n \ge 1$, congruence modulo $n$ on $\mathbb{Z}$ is an equivalence relation: $a \sim b$ when $n$ divides $a - b$.
An equivalence relation cuts the set into [[equivalence classes|082RMRSY26]], and these form a [[partition|09CCE86A6D]].
Each [[function|0XHDTE5YMZ]] gives an equivalence relation. See [[equivalence relation induced by a function|0QE5PFJY7V]].

## Explanations

### L1 human

An equivalence relation says when two objects are "the same for our purpose".
Two integers are congruent modulo $2$ when they have the same parity.
Then all even numbers count as one kind, and all odd numbers as another.
