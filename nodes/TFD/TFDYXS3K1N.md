---
tag: TFDYXS3K1N
kind: definition
name: Propositional formula
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
defines: TT7WT5HPN9
uses: [AC4HD34AXX, QS0XVAN9BG, 1P6EP01HZF]
sources:
  - url: https://en.wikipedia.org/wiki/Well-formed_formula
    locator: Propositional calculus
  - url: https://en.wikipedia.org/wiki/Propositional_formula
    locator: lead section
  - book: isbn:9780122384523
    locator: Chapter 1
  - book: isbn:9781482237726
    locator: Chapter 1
---

## Definition

A propositional formula is a string of symbols that can be built from variables by the formation rules, and we define the set of all of them as the smallest set closed under those rules.

Let $P$ be a set of [[propositional variables|AC4HD34AXX]].
The alphabet over $P$ is the set $P \cup \{ \neg, \land, \lor, \to, \leftrightarrow, (, ) \}$, where the [[connectives|QS0XVAN9BG]] and the two brackets are symbols that are not in $P$.
A set $S$ of finite [[strings|1P6EP01HZF]] over this alphabet is closed when it has these three properties:

1. each variable $p \in P$, as a string of length $1$, is in $S$;
2. if $\varphi \in S$, then $(\neg \varphi) \in S$;
3. if $\varphi, \psi \in S$ and $\circ$ is one of $\land$, $\lor$, $\to$, $\leftrightarrow$, then $(\varphi \circ \psi) \in S$.

The set $\mathrm{Form}(P)$ of propositional formulas over $P$ is the intersection of all closed sets.
A propositional formula is an element of $\mathrm{Form}(P)$.

## Notation

We write $\mathrm{Form}$ for $\mathrm{Form}(P)$ when $P$ is fixed, and $\varphi$, $\psi$, $\chi$ for formulas.
In the string $(\varphi \circ \psi)$ the letters $\varphi$ and $\psi$ stand for the strings of the two formulas, and writing them side by side means concatenation.
The connective $\circ$ is the main connective of $(\varphi \circ \psi)$, and $\neg$ is the main connective of $(\neg \varphi)$.
The conventions for dropping brackets are on the [[concept page|TT7WT5HPN9]].

## Remarks

### Why the intersection is the smallest closed set

The set of all finite strings over the alphabet is closed, so at least one closed set exists and the intersection makes sense.
Each of the conditions 1 to 3 holds in every set of the family, so it holds in their intersection, and $\mathrm{Form}$ is closed.
By construction $\mathrm{Form}$ lies inside every closed set.
This minimality is what gives proofs by [[induction on formulas|EDRV3N0SA3]]: to show that all formulas have a property, show that the set of strings with the property is closed.

Each condition has a job.
Condition 1 gives the starting points; without it the empty set would be closed, and there would be no formulas.
Conditions 2 and 3 give the ways to build, and the brackets in them make the result readable in one way.
If we drop the brackets from condition 3, the string $p \land q \lor r$ becomes a formula with two different parses.

### Formation sequences

A formation sequence is a finite list $\varphi_1, \ldots, \varphi_n$ of strings in which each $\varphi_k$ is a variable, or $(\neg \varphi_i)$ for some $i < k$, or $(\varphi_i \circ \varphi_j)$ for some $i, j < k$ and a binary connective $\circ$.
A string is a formula if and only if it is the last entry of some formation sequence.
We show that the set $T$ of such last entries equals $\mathrm{Form}$.

1. Each variable is in $T$, by the sequence of length $1$.
2. If $\sigma$ ends with $\varphi$, then $\sigma$ followed by $(\neg \varphi)$ is a formation sequence, so $(\neg \varphi) \in T$.
3. If $\sigma$ ends with $\varphi$ and $\tau$ ends with $\psi$, then $\sigma$, then $\tau$, then $(\varphi \circ \psi)$ is a formation sequence, so $(\varphi \circ \psi) \in T$.
4. By steps 1 to 3 the set $T$ is closed, so $\mathrm{Form} \subseteq T$.
5. Conversely, in a formation sequence each $\varphi_k$ is in $\mathrm{Form}$, by [[strong induction|0KMVFSHFGZ]] on $k$.
   A variable is in $\mathrm{Form}$ by condition 1, and $(\neg \varphi_i)$ or $(\varphi_i \circ \varphi_j)$ with $i, j < k$ is in $\mathrm{Form}$ by the induction hypothesis and condition 2 or 3.
6. So $T \subseteq \mathrm{Form}$, and $T = \mathrm{Form}$.

### A small example and a failure

The string $\chi = ((p \lor q) \leftrightarrow (\neg r))$ is a formula, with the formation sequence
$$p, \quad q, \quad (p \lor q), \quad r, \quad (\neg r), \quad ((p \lor q) \leftrightarrow (\neg r)).$$
The third entry uses condition 3, the fifth uses condition 2, and the last uses condition 3 again.
The string $(p \land \land q)$ is not a formula, but a failed search for a formation sequence does not prove that.
A proof needs a property of all formulas that the string lacks, and [[strings that are not formulas|JFMDG89MTJ]] gives one.

### Variants

Some books add the constants $\top$ and $\bot$ to condition 1.
Some take only $\neg$ and $\to$ and define the other connectives as abbreviations.
Some write $\neg \varphi$ without brackets, and the [[unique readability theorem|6KBJX91N7G]] still holds for this variant.
Polish notation drops all brackets and writes connectives in front: $N\varphi$, $K\varphi\psi$, $A\varphi\psi$, $C\varphi\psi$, $E\varphi\psi$.

## Explanations

### L1 human

The definition says which strings of symbols count as formulas.
Single letters count.
If two strings count, then joining them with a connective and a pair of brackets gives a string that counts.
Nothing else counts.
So $((p \land q) \to r)$ counts, but $(p \land \land q)$ does not.

### L2 human

We show that $((\neg p) \to (q \land p))$ is a formula, by a formation sequence of five entries:
$$p, \quad (\neg p), \quad q, \quad (q \land p), \quad ((\neg p) \to (q \land p)).$$
The second entry uses condition 2 on the first, the fourth uses condition 3 on the third and the first, and the fifth uses condition 3 on the second and the fourth.
Check: the formula has $3$ connectives and $6$ brackets, as every formula must.
The typical use of a formation sequence is to show that a string is a formula, while induction on formulas shows that a string is not one.

### L3 human

The definition takes the least fixed point of the monotone operator that adds to a set $S$ the variables and all strings $(\neg \varphi)$ and $(\varphi \circ \psi)$ with $\varphi, \psi \in S$.
The formation sequences describe the same fixed point from below, as the union of the finite stages.
The top-down description by intersection and the bottom-up description by stages agree for every inductive definition with finitary rules.
The same scheme defines the terms and formulas of first-order logic and the theorems of a formal system.
