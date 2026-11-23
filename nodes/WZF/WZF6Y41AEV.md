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

Let $p$ be true on the interval $[0, 1]$ of the real line.
Read $\square p$ at a point as "a small open window around the point lies inside the set of $p$".
Then $\square p$ is true on $(0, 1)$ and false at $0$ and at $1$.
This reading turns the box into the [[interior|0RZH6W98HK]] operator, and the theorems of $\mathsf{S4}$ into laws of interior.

### The theorems of S4 are valid

A topological model on $\mathbb{R}$ gives each variable a set $V(p) \subseteq \mathbb{R}$.
The connectives act as set operations, and the modalities act as follows:
$$[\![ \square\varphi ]\!] = \operatorname{int} [\![ \varphi ]\!], \qquad [\![ \lozenge\varphi ]\!] = \operatorname{cl} [\![ \varphi ]\!].$$
The second rule holds because $\lozenge = \neg\square\neg$, and the closure is the complement of the interior of the complement.
A formula is valid when its truth set is $\mathbb{R}$ under every valuation.

1. $\operatorname{int}(A \cap B) = \operatorname{int} A \cap \operatorname{int} B$, because the right side is open and lies in $A \cap B$, and the interior is monotone.
2. So axiom $\mathrm{K}$ is valid, since $\operatorname{int}((\mathbb{R} \setminus A) \cup B) \cap \operatorname{int} A = \operatorname{int}(A \cap B) \subseteq \operatorname{int} B$.
3. $\operatorname{int} A \subseteq A$, so axiom $\mathrm{T}$ is valid.
4. $\operatorname{int}\operatorname{int} A = \operatorname{int} A$, because the interior is open, so axiom $\mathrm{4}$ is valid.
5. $\operatorname{int}\mathbb{R} = \mathbb{R}$, so [[necessitation|G989VP2NGP]] preserves validity.
6. Modus ponens and uniform substitution also preserve validity.
   So every theorem of the [[modal logic S4|N60RVXSA5W]] is valid in this semantics.

### Two countermodels

Two valuations refute formulas that are not theorems.

7. With $V(p) = [0, 1]$, we get $[\![ \square p ]\!] = (0, 1)$ and $[\![ \lozenge p ]\!] = [0, 1]$, so $[\![ \square\lozenge p ]\!] = (0, 1)$.
8. At $0$, $\lozenge p$ is true and $\square\lozenge p$ is false, so axiom $\mathrm{5}$, $\lozenge p \to \square\lozenge p$, fails at $0$.
9. With $V(p) = \mathbb{Q}$, the rationals have empty interior and dense closure, so $[\![ \square p ]\!] = \varnothing$ and $[\![ \lozenge p ]\!] = \mathbb{R}$.
10. Then $[\![ \square\lozenge p ]\!] = \mathbb{R}$ and $[\![ \lozenge\square p ]\!] = \varnothing$, so $\square\lozenge p \to \lozenge\square p$ fails at every point.

## Remarks

The example shows that the box of $\mathsf{S4}$ has a natural reading as "in a neighborhood of the point".
Steps 1 to 6 work in every [[topological space|0CQHFPGJ45]], and the algebraic form of this semantics is the [[interior algebra|BDEX7HET71]].
McKinsey and Tarski showed in 1944 that the converse holds for $\mathbb{R}$: a formula valid on the real line is a theorem of $\mathsf{S4}$.
Steps 8 and 10 show that $\mathsf{S4}$ proves neither $\mathrm{5}$ nor $\square\lozenge p \to \lozenge\square p$.

What changes with the space?
In a space with the discrete topology every set is open, so $\operatorname{int} A = A$, and the box does nothing.
There the valid formulas are those of the trivial logic, with $\square p \leftrightarrow p$ valid.

## Explanations

### L1 human

Think of a set of points on the number line, such as the interval from 0 to 1.
"Box $p$" holds at a point when a small window around the point stays inside the set.
This holds at $0.5$, but not at $0$, since every window around $0$ contains negative numbers.
"Diamond $p$" holds at a point when every window around it meets the set.
This holds at $0$ and at $1$, but not at $2$.

### L2 human

We refute axiom $\mathrm{B}$, $p \to \square\lozenge p$, with an isolated point.
Take $V(p) = [0, 1] \cup \{ 2 \}$.
The closure of this set is the set itself, so $[\![ \lozenge p ]\!] = [0, 1] \cup \{ 2 \}$.
The interior of that set drops the isolated point $2$ and the end points:
$$[\![ \square\lozenge p ]\!] = \operatorname{int}([0, 1] \cup \{ 2 \}) = (0, 1).$$
At $2$, $p$ is true and $\square\lozenge p$ is false, so $\mathrm{B}$ fails at $2$.
This is the typical use of the topological reading: intervals, single points and dense sets give quick countermodels for $\mathsf{S4}$.
Watch out: the interior of an intersection of infinitely many sets can be smaller than the intersection of the interiors, as with the sets $(-1/n, 1/n)$, whose intersection $\{ 0 \}$ has empty interior.
So the box commutes only with finite conjunctions.
