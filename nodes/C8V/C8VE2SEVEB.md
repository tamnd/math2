---
tag: C8VE2SEVEB
kind: definition
name: Archimedean equivalence classes
msc: ["06F20"]
defines: RQ4X0EH6NH
uses: [1P8087YGYQ, 071DDFVG4J]
sources:
  - url: https://en.wikipedia.org/wiki/Archimedean_property
---

## Definition

Let $(G, +, \le)$ be a [[linearly ordered group|1P8087YGYQ]] that is an [[abelian group|071DDFVG4J]].
For $a \in G$, let $\abs{a} = \max(a, -a)$.
Two elements $a, b \in G$ are *Archimedean equivalent*, written $a \sim b$, if there are integers $m, n \ge 1$ with
$$\abs{a} \le n \abs{b} \quad \text{and} \quad \abs{b} \le m \abs{a}.$$
This is an equivalence relation on $G$.
Its classes are the *Archimedean classes* of $G$, and the class of $0$ is $\set{0}$.
For nonzero $a, b$ with $a \not\sim b$, one says that $a$ is *infinitely larger* than $b$ if $n \abs{b} < \abs{a}$ for all $n \ge 1$.

## Remarks

Exactly one of $a \sim b$, "$a$ is infinitely larger than $b$" and "$b$ is infinitely larger than $a$" holds, so the classes of nonzero elements are totally ordered by size.
Example: in $\Z^2$ with the lexicographic order, $(0, 2) \sim (0, 3)$, since $\abs{(0, 2)} \le 1 \cdot (0, 3)$ and $(0, 3) \le 2 \cdot (0, 2)$.
Non-example: $(1, 0) \not\sim (0, 1)$, since $n \cdot (0, 1) = (0, n) < (1, 0)$ for all $n$, so no multiple of $(0, 1)$ bounds $(1, 0)$.
So $\Z^2$ with this order has exactly two classes of nonzero elements, those with first coordinate $0$ and the others.
The group $G$ is Archimedean if and only if all its nonzero elements are equivalent.
Conventions on the direction of the order of classes differ between texts.
