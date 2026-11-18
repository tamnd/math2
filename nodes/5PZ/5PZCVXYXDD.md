---
tag: 5PZCVXYXDD
kind: example
name: The trivial logic and the verum logic
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [D1TJYZZDCY]
uses: [D1TJYZZDCY, JS8W7PA6JK, E87G6ZTMTN, NGHWZ9Y7ZV, 05006AJ7DZ, 12MQ2NJ29A]
sources:
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Example

Let $\mathsf{Triv}$ be the smallest [[normal modal logic|D1TJYZZDCY]] that contains $\square p \leftrightarrow p$.
Let $\mathsf{Ver}$ be the smallest normal modal logic that contains $\square\bot$.
Let $\mathfrak{F}_\circ$ be one world $w$ with $w R w$, and let $\mathfrak{F}_\bullet$ be one world $w$ with the empty relation.

1. $\mathfrak{F}_\circ$ validates $\square p \leftrightarrow p$. The only successor of $w$ is $w$, so $\square\varphi$ is true at $w$ exactly when $\varphi$ is.
2. $\mathfrak{F}_\bullet$ validates $\square\bot$. The world $w$ has no successors, so every formula $\square\varphi$ is true at $w$.
3. Both logics are consistent. By [[soundness of normal modal logics|E87G6ZTMTN]], every theorem of $\mathsf{Triv}$ is valid on $\mathfrak{F}_\circ$, and $\bot$ is not. The same holds for $\mathsf{Ver}$ and $\mathfrak{F}_\bullet$.
4. $\mathsf{Triv} \nvdash \square\bot$, since $\square\bot$ is false at $w$ in $\mathfrak{F}_\circ$: the successor $w$ makes $\bot$ false.
5. $\mathsf{Ver} \nvdash \square p \to p$. On $\mathfrak{F}_\bullet$ with $V(p) = \varnothing$, $\square p$ is true and $p$ is false.
6. So the two logics are distinct, and neither contains the other.
7. $\mathsf{Ver} \vdash \square\varphi$ for every $\varphi$. The formula $\bot \to \varphi$ is a tautology, so RM of [[normal modal logic K|JS8W7PA6JK]] gives $\square\bot \to \square\varphi$, and modus ponens with $\square\bot$ gives $\square\varphi$.

## Remarks

The example shows two consistent normal logics that are as strong as possible in opposite directions.
In $\mathsf{Triv}$, every formula is equivalent to the formula $\varphi^\circ$ obtained by deleting all boxes.
The proof is a [[structural induction|12MQ2NJ29A]]: if $\mathsf{Triv} \vdash \psi \leftrightarrow \psi^\circ$, then RE gives $\square\psi \leftrightarrow \square\psi^\circ$, and the axiom gives $\square\psi^\circ \leftrightarrow \psi^\circ$.
So $\mathsf{Triv} \vdash \varphi$ exactly when $\varphi^\circ$ is a [[tautology|05006AJ7DZ]].
One direction uses the equivalence, and the other uses $\mathfrak{F}_\circ$, where $\varphi$ and $\varphi^\circ$ have the same truth value under each valuation.
In $\mathsf{Ver}$, by step 7, every boxed formula is equivalent to $\top$; the [[canonical model of the verum logic|B464EAG58T]] gives the same reduction.
If we replace the axiom $\square\bot$ by $\square\square\bot$, we get a weaker logic, valid on frames where no world has a path of length 2.

## Explanations

### L1 human

A modal logic says how "necessarily" behaves.
The trivial logic says that "necessarily $p$" means just "$p$", so the box does nothing.
The verum logic says that "necessarily $p$" is always true, whatever $p$ is.
Each of them has a one-point picture.
For the trivial logic it is a point with a loop, and for the verum logic it is a point without a loop.
Neither logic proves a contradiction, since a contradiction is false on its picture.

### L2 human

1. Take $\varphi = \square(p \to \square q) \to (\square p \to q)$.
2. Delete the boxes: $\varphi^\circ = (p \to q) \to (p \to q)$, a tautology.
3. So $\mathsf{Triv} \vdash \varphi$.
4. In $\mathsf{Ver}$, both boxed parts are equivalent to $\top$, so $\varphi$ is equivalent to $q$. On $\mathfrak{F}_\bullet$ with $V(q) = \varnothing$, $\varphi$ is false, so $\mathsf{Ver} \nvdash \varphi$.

The typical use of these logics is as the two maximal consistent normal logics: every consistent normal logic is contained in $\mathsf{Triv}$ or in $\mathsf{Ver}$.
A trap: $\mathsf{Ver}$ proves $\square\bot$ but not $\bot$, so a theorem $\square\varphi$ does not give the theorem $\varphi$.
