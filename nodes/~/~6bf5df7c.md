---
tag: ~6bf5df7c
kind: definition
name: Propositional formula
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
defines: ~7139c138
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

Let $P$ be a set of [[propositional variables|AC4HD34AXX]].
The alphabet over $P$ is the set $P \cup \set{\neg, \land, \lor, \to, \leftrightarrow, (, )}$, where the [[connectives|QS0XVAN9BG]] and the two brackets are symbols that are not in $P$.
A set $S$ of finite [[strings|1P6EP01HZF]] over this alphabet is closed when it has these properties:

1. each variable $p \in P$, as a string of length $1$, is in $S$;
2. if $\varphi \in S$, then $(\neg \varphi) \in S$;
3. if $\varphi, \psi \in S$ and $\circ$ is one of $\land$, $\lor$, $\to$, $\leftrightarrow$, then $(\varphi \circ \psi) \in S$.

The set $\mathrm{Form}(P)$ of propositional formulas over $P$ is the intersection of all closed sets.
A propositional formula is an element of $\mathrm{Form}(P)$.

## Notation

We write $\mathrm{Form}$ for $\mathrm{Form}(P)$ when $P$ is fixed, and $\varphi$, $\psi$, $\chi$ for formulas.
In the string $(\varphi \circ \psi)$ the letters $\varphi$ and $\psi$ stand for the strings of the two formulas, and the juxtaposition is concatenation.
The connective $\circ$ is the main connective of $(\varphi \circ \psi)$, and $\neg$ is the main connective of $(\neg \varphi)$.
Outer brackets and the brackets that the precedence rules fix are often dropped; the conventions are on the [[concept page|~7139c138]].

## Remarks

### The intersection is the smallest closed set

The set of all finite strings over the alphabet is closed, so at least one closed set exists.
An intersection of closed sets is closed: each condition 1 to 3 holds in each set of the family, so it holds in their intersection.
So $\mathrm{Form}$ is closed, and it is a subset of every closed set.
This minimality gives proofs by [[induction on formulas|EDRV3N0SA3]]: to show that all formulas have a property, show that the set of strings with the property is closed.

### Formation sequences

A formation sequence is a finite list $\varphi_1, \ldots, \varphi_n$ of strings in which each $\varphi_k$ is a variable, or $(\neg \varphi_i)$ for some $i < k$, or $(\varphi_i \circ \varphi_j)$ for some $i, j < k$ and a binary connective $\circ$.
A string is a formula if and only if it is the last member of some formation sequence.
We prove both directions.

1. Let $T$ be the set of strings that are the last member of some formation sequence.
2. Each variable $p$ is in $T$, by the formation sequence $p$ of length $1$.
3. If $\varphi \in T$ by a sequence $\sigma$, then $\sigma$ followed by $(\neg \varphi)$ is a formation sequence, so $(\neg \varphi) \in T$.
4. If $\varphi \in T$ by $\sigma$ and $\psi \in T$ by $\tau$, then $\sigma$, then $\tau$, then $(\varphi \circ \psi)$ is a formation sequence, so $(\varphi \circ \psi) \in T$.
5. By steps 2 to 4 the set $T$ is closed, so $\mathrm{Form} \subseteq T$ by the definition of $\mathrm{Form}$.
6. Conversely, let $\varphi_1, \ldots, \varphi_n$ be a formation sequence; we show $\varphi_k \in \mathrm{Form}$ for each $k$, by [[strong induction|0KMVFSHFGZ]] on $k$.
7. If $\varphi_k$ is a variable, it is in $\mathrm{Form}$ by condition 1.
8. If $\varphi_k = (\neg \varphi_i)$ with $i < k$, then $\varphi_i \in \mathrm{Form}$ by the induction hypothesis, so $\varphi_k \in \mathrm{Form}$ by condition 2.
9. If $\varphi_k = (\varphi_i \circ \varphi_j)$ with $i, j < k$, then $\varphi_k \in \mathrm{Form}$ by the induction hypothesis and condition 3.
10. So $T \subseteq \mathrm{Form}$, and with step 5, $T = \mathrm{Form}$.

### Variants of the definition

Some books add the constants $\top$ and $\bot$ to condition 1.
Some books take fewer connectives, for example $\neg$ and $\to$ only, and define the others as abbreviations.
Some books write $\neg \varphi$ without brackets; the [[unique readability theorem|~26f00b05]] still holds for this variant.
Polish notation drops all brackets and writes connectives in front: $N\varphi$, $K\varphi\psi$, $A\varphi\psi$, $C\varphi\psi$, $E\varphi\psi$.

## Explanations

### L1 human

The definition says which strings of symbols count as formulas.
Single letters count.
If two strings count, then joining them with a connective and a pair of brackets gives a string that counts.
Nothing else counts.
So $((p \land q) \to r)$ counts, but $(p \land \land q)$ does not.

### L2 human

We show that $\chi = ((p \lor q) \leftrightarrow (\neg r))$ is a formula with a formation sequence.

1. $\varphi_1 = p$, a variable.
2. $\varphi_2 = q$, a variable.
3. $\varphi_3 = (p \lor q)$, by condition 3 from $\varphi_1$ and $\varphi_2$.
4. $\varphi_4 = r$, a variable.
5. $\varphi_5 = (\neg r)$, by condition 2 from $\varphi_4$.
6. $\varphi_6 = ((p \lor q) \leftrightarrow (\neg r)) = \chi$, by condition 3 from $\varphi_3$ and $\varphi_5$.

The typical use of a formation sequence is to show that a given string is a formula.
To show that a string is not a formula, we find a property that all formulas have and the string does not have, and we prove the property by induction.
A trap is to try to show "not a formula" by failing to find a formation sequence; a failed search is not a proof.

### L3 human

The definition takes the least fixed point of the monotone operator that adds to a set $S$ the variables and all strings $(\neg \varphi)$ and $(\varphi \circ \psi)$ with $\varphi, \psi \in S$.
The formation sequences describe the same fixed point from below, as the union of the finite stages.
The "top down" (intersection) and "bottom up" (stages) descriptions agree for every inductive definition with finitary rules.
The same scheme defines the terms and formulas of first-order logic and the theorems of a formal system.
