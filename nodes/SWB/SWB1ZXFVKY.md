---
tag: SWB1ZXFVKY
kind: definition
name: Strict partial order
msc: [06A06]
defines: 60FNZ35H6R
uses: [08EJC6Q25H, 0CYRECG2YQ]
sources:
  - url: https://en.wikipedia.org/wiki/Partially_ordered_set
    locator: Strict partial orders
---

## Definition

Let $A$ be a set.
A *strict partial order* on $A$ is a [[binary relation|08EJC6Q25H]] $<$ on $A$ with these two properties.

1. Irreflexivity: $a < a$ holds for no $a \in A$.
2. [[Transitivity|0CYRECG2YQ]]: for all $a, b, c \in A$, if $a < b$ and $b < c$, then $a < c$.

## Remarks

The relation "is a proper subset of" on the [[power set|0BC7KX51Z8]] of a set is a strict partial order.
It is irreflexive since no set is a proper subset of itself, and it is transitive since $X \subsetneq Y \subsetneq Z$ gives $X \subsetneq Z$.
The relation $\ne$ on $\R$ is irreflexive but not transitive: $1 \ne 2$ and $2 \ne 1$, but $1 \ne 1$ fails.
A strict partial order is asymmetric: $a < b$ and $b < a$ together would give $a < a$.
From a [[partial order|011C29Q1S1]] $\le$ one gets a strict partial order by $a < b$ if and only if $a \le b$ and $a \ne b$.
Conversely, from a strict partial order one gets a partial order by $a \le b$ if and only if $a < b$ or $a = b$.
These two constructions are inverse to each other.

## Explanations

### L1 human

A strict partial order is the relation "strictly smaller than" in an order where some pairs may be incomparable.
The relation $<$ on numbers is the main example.
