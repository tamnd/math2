---
tag: WZF6Y41AEV
kind: example
name: The interior operator of the real line as an S4 box
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [N60RVXSA5W]
uses: [N60RVXSA5W, 0RZH6W98HK, 0CQHFPGJ45, BDEX7HET71, G989VP2NGP]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_logic
    locator: lead section
---

## Example

A topological model on $\mathbb{R}$ assigns to each variable a set $V(p) \subseteq \mathbb{R}$.
The connectives act as set operations, and the box is the [[interior|0RZH6W98HK]]:
$$[\![ \square\varphi ]\!] = \operatorname{int} [\![ \varphi ]\!], \qquad [\![ \lozenge\varphi ]\!] = \operatorname{cl} [\![ \varphi ]\!].$$
The second formula holds because $\lozenge = \neg\square\neg$ and the closure is the complement of the interior of the complement.
A formula is valid when its truth set is $\mathbb{R}$ under every valuation.

1. $\operatorname{int}(A \cap B) = \operatorname{int} A \cap \operatorname{int} B$: the right side is open and lies in $A \cap B$, and the interior is monotone.
2. So $\square(p \wedge q) \leftrightarrow (\square p \wedge \square q)$ is valid, and axiom $\mathrm{K}$ is valid, since $\operatorname{int}((\mathbb{R} \setminus A) \cup B) \cap \operatorname{int} A = \operatorname{int}(A \cap B) \subseteq \operatorname{int} B$.
3. $\operatorname{int} A \subseteq A$, so axiom $\mathrm{T}$ is valid.
4. $\operatorname{int}\operatorname{int} A = \operatorname{int} A$, since the interior is open, so axiom $\mathrm{4}$ is valid.
5. $\operatorname{int}\mathbb{R} = \mathbb{R}$, so [[necessitation|G989VP2NGP]] preserves validity.
6. Modus ponens and uniform substitution also preserve validity. So every theorem of the [[modal logic S4|N60RVXSA5W]] is valid in this semantics.
7. Take $V(p) = [0, 1]$. Then $[\![ \square p ]\!] = (0, 1)$ and $[\![ \lozenge p ]\!] = [0, 1]$.
8. $[\![ \square\lozenge p ]\!] = \operatorname{int}[0, 1] = (0, 1)$ and $[\![ \lozenge\square p ]\!] = \operatorname{cl}(0, 1) = [0, 1]$.
9. At $0$, $\lozenge p$ is true and $\square\lozenge p$ is false, so axiom $\mathrm{5}$, $\lozenge p \to \square\lozenge p$, fails at $0$.
10. Take $V(p) = \mathbb{Q}$. Then $[\![ \square p ]\!] = \varnothing$ and $[\![ \lozenge p ]\!] = \mathbb{R}$.
11. So $[\![ \square\lozenge p ]\!] = \mathbb{R}$ and $[\![ \lozenge\square p ]\!] = \varnothing$, and $\square\lozenge p \to \lozenge\square p$ fails at every point.

## Remarks

The example shows that the box of $\mathsf{S4}$ has a natural reading as "in a neighborhood of the point".
The same proof works on every [[topological space|0CQHFPGJ45]], and the algebraic form of this semantics is the [[interior algebra|BDEX7HET71]].
McKinsey and Tarski showed that $\mathsf{S4}$ is exactly the logic of $\mathbb{R}$ in this semantics.
Steps 9 and 11 show that $\mathsf{S4}$ proves neither $\mathrm{5}$ nor the axiom $\square\lozenge p \to \lozenge\square p$.
If we replace $\mathbb{R}$ by a space with the discrete topology, then $\operatorname{int} A = A$ for all $A$, and the box does nothing.
Then the valid formulas are those of the trivial logic $\square p \leftrightarrow p$.

## Explanations

### L1 human

Think of a set of points on the number line, such as the interval from 0 to 1.
"Box $p$" holds at a point when a small window around the point stays inside the set.
This holds at $0.5$, but not at $0$, since every window around $0$ contains negative numbers.
"Diamond $p$" holds at a point when every window around it meets the set.
This holds at $0$ and at $1$, but not at $2$.

### L2 human

1. Take $V(p) = [0, 1] \cup \set{2}$.
2. The interior is $(0, 1)$, so $[\![ \square p ]\!] = (0, 1)$.
3. The closure is $[0, 1] \cup \set{2}$, so $[\![ \lozenge p ]\!] = [0, 1] \cup \set{2}$.
4. At $2$, $p$ is true, but $\square\lozenge p$ is false, since $\operatorname{int}([0, 1] \cup \set{2}) = (0, 1)$. So axiom $\mathrm{B}$, $p \to \square\lozenge p$, fails at $2$.

The typical use of the topological reading is to find countermodels for $\mathsf{S4}$ with intervals and dense sets.
A trap: the interior of an intersection of infinitely many sets can be smaller than the intersection of the interiors.
So only finite conjunctions commute with the box.
