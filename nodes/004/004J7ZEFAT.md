---
tag: 004J7ZEFAT
kind: example
name: Power set Boolean algebra
msc: ["06E05"]
instance_of: [0XADJKM699]
sources:
  - url: https://en.wikipedia.org/wiki/Field_of_sets
    locator: Definitions
---

## Example

Let $X$ be a set, and let $\mathcal{P}(X)$ be the set of all subsets of $X$.
With $A \wedge B = A \cap B$, $A \vee B = A \cup B$, $\neg A = X \setminus A$, $0 = \varnothing$ and $1 = X$, the set $\mathcal{P}(X)$ is a [[Boolean algebra|06GKBTAA5E]].
Its order is inclusion $\subseteq$.

## Remarks

If $X$ has $n$ elements, this Boolean algebra has $2^n$ elements.
A field of sets on $X$ is a subset of $\mathcal{P}(X)$ that contains $\varnothing$ and is closed under complement and binary union. It is a Boolean subalgebra.
Every finite Boolean algebra is isomorphic to a power set Boolean algebra, by [[Stone's representation theorem for finite Boolean algebras|0DYS9C3HH5]].

## Explanations

### L1 human

The subsets of a set form a Boolean algebra: intersection is and, union is or, and complement is not.
Venn diagrams show the laws of this Boolean algebra.
