---
tag: 0ZVHXDSZC7
kind: definition
name: Quotient set
msc: ["03E20"]
defines: 0011MTQMR6
uses: [082RMRSY26, 0XHDTE5YMZ]
sources:
  - url: https://en.wikipedia.org/wiki/Equivalence_class
    locator: Definition and notation
inventory: [2ZKR7AM3JN]
---

## Definition

Let $\sim$ be an [[equivalence relation|0SGTMBEWRF]] on a set $A$.
The quotient set of $A$ by $\sim$ is the set
$$A/{\sim} = \{[a] \mid a \in A\}$$
of all [[equivalence classes|082RMRSY26]].
The canonical projection is the [[function|0XHDTE5YMZ]] $\pi \colon A \to A/{\sim}$ with $\pi(a) = [a]$.

## Remarks

For congruence modulo $n$ on $\mathbb{Z}$, the quotient set $\mathbb{Z}/n\mathbb{Z}$ has the $n$ elements $[0], [1], \dots, [n-1]$.
The canonical projection is [[surjective|0XKH881BZ7]].
A function on $A/{\sim}$ is often defined by a formula on representatives. The formula must give the same value for equivalent representatives.

## Explanations

### L1 human

In the quotient set, each class becomes a single point.
From $\mathbb{Z}$ with congruence modulo $2$ you get a set with two elements: "even" and "odd".
