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

Let $\mathsf{Triv}$ be the smallest [[normal modal logic|D1TJYZZDCY]] that contains $\square p \leftrightarrow p$, and let $\mathsf{Ver}$ be the smallest normal modal logic that contains $\square\bot$.
Let $\mathfrak{F}_\circ$ be one world $w$ with $w R w$, and let $\mathfrak{F}_\bullet$ be one world $w$ with the empty relation.
We show that both logics are consistent, that they differ, and how strong each one is.

1. $\mathfrak{F}_\circ$ validates $\square p \leftrightarrow p$.
   The only successor of $w$ is $w$, so $\square\varphi$ is true at $w$ exactly when $\varphi$ is.
2. $\mathfrak{F}_\bullet$ validates $\square\bot$.
   The world $w$ has no successors, so every formula $\square\varphi$ is true at $w$.
3. Both logics are consistent.
   By [[soundness of normal modal logics|E87G6ZTMTN]], every theorem of $\mathsf{Triv}$ is valid on $\mathfrak{F}_\circ$, and $\bot$ is not; the same holds for $\mathsf{Ver}$ and $\mathfrak{F}_\bullet$.
4. $\mathsf{Triv} \nvdash \square\bot$, since on $\mathfrak{F}_\circ$ the successor $w$ makes $\bot$ false, so $\square\bot$ is false at $w$.
5. $\mathsf{Ver} \nvdash \square p \to p$, since on $\mathfrak{F}_\bullet$ with $V(p) = \varnothing$ the formula $\square p$ is true and $p$ is false.
6. So the two logics are distinct, and neither contains the other.
7. $\mathsf{Ver} \vdash \square\varphi$ for every $\varphi$.
   The formula $\bot \to \varphi$ is a tautology, so the rule RM of [[normal modal logic K|JS8W7PA6JK]] gives $\square\bot \to \square\varphi$, and modus ponens with $\square\bot$ gives $\square\varphi$.

## Remarks

The two logics are as strong as a consistent normal logic can be, in opposite directions.

In $\mathsf{Triv}$ every formula is equivalent to the formula $\varphi^\circ$ that we get by deleting all boxes.
The proof is a [[structural induction|12MQ2NJ29A]]: if $\mathsf{Triv} \vdash \psi \leftrightarrow \psi^\circ$, then RE gives $\square\psi \leftrightarrow \square\psi^\circ$, and the axiom gives $\square\psi^\circ \leftrightarrow \psi^\circ$.
So $\mathsf{Triv} \vdash \varphi$ exactly when $\varphi^\circ$ is a [[tautology|05006AJ7DZ]].
One direction uses the equivalence, and the other uses $\mathfrak{F}_\circ$, where $\varphi$ and $\varphi^\circ$ get the same truth value under each valuation.

In $\mathsf{Ver}$, by step 7, every boxed formula is equivalent to $\top$, and the [[canonical model of the verum logic|B464EAG58T]] gives the same reduction.
If we replace the axiom $\square\bot$ by $\square\square\bot$, we get a weaker logic, which is valid on the frames where no world starts a path of length $2$.

## Explanations

### L1 human

A modal logic says how "necessarily" behaves.
The trivial logic says that "necessarily $p$" means just "$p$", so the box does nothing.
The verum logic says that "necessarily $p$" is always true, whatever $p$ is.
Each of them has a picture with one point: a point with a loop for the trivial logic, and a point without a loop for the verum logic.
Neither logic proves a contradiction, since a contradiction is false on its picture.

### L2 human

Take $\varphi = \square(p \to \square q) \to (\square p \to q)$ and test it in both logics.
Deleting the boxes gives the following formula, which is a tautology:
$$\varphi^\circ = (p \to q) \to (p \to q).$$
So $\mathsf{Triv} \vdash \varphi$.
In $\mathsf{Ver}$ both boxed parts are equivalent to $\top$, so $\varphi$ is equivalent to $\top \to (\top \to q)$, that is to $q$.
On $\mathfrak{F}_\bullet$ with $V(q) = \varnothing$ the formula $\varphi$ is false, so $\mathsf{Ver} \nvdash \varphi$.
The typical use of these logics is as the two maximal consistent normal logics: every consistent normal logic is contained in $\mathsf{Triv}$ or in $\mathsf{Ver}$.
Watch out: $\mathsf{Ver}$ proves $\square\bot$ but not $\bot$, so a theorem $\square\varphi$ does not give the theorem $\varphi$.
