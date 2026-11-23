---
tag: B6QKEXDEPM
kind: example
name: Formation sequence and parse tree of a propositional formula
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
instance_of: [TT7WT5HPN9]
uses: [TFDYXS3K1N, 0Y0JGC2K9T]
sources:
  - url: https://en.wikipedia.org/wiki/Well-formed_formula
    locator: Propositional calculus
  - book: isbn:9780122384523
    locator: Chapter 1
---

## Example

One formula can be seen in three ways: as a string, as a list of building steps, and as a tree.
We take
$$\varphi = ((p \land q) \to (\neg r)),$$
a string of $12$ symbols, and look at it in all three ways.

1. The list
   $$p, \quad q, \quad r, \quad (p \land q), \quad (\neg r), \quad ((p \land q) \to (\neg r))$$
   is a formation sequence.
   The first three entries are variables, and each later entry comes from earlier ones by one rule of the [[definition|TFDYXS3K1N]].
   Its last entry is $\varphi$, so $\varphi$ is a [[propositional formula|TT7WT5HPN9]].
2. The main connective of $\varphi$ is $\to$, with left part $(p \land q)$ and right part $(\neg r)$.
3. By the recursive definition of subformulas,
   $$\mathrm{Sub}(\varphi) = \{ \varphi, (p \land q), (\neg r), p, q, r \},$$
   a set with $6$ elements.
4. The parse tree has the root $\to$.
   Its left child is $\land$, with the leaves $p$ and $q$, and its right child is $\neg$, with the leaf $r$.
   The tree has $6$ nodes, one for each subformula, and depth $2$.
5. The string has $3$ connectives and $6$ brackets, so it has twice as many brackets as connectives, as every formula must.

## Remarks

The formation sequence is not unique: the order $r$, $(\neg r)$, $p$, $q$, $(p \land q)$, $\varphi$ also works.
The tree, on the other hand, is unique, by the [[unique readability theorem|6KBJX91N7G]].
So the tree is the true identity of the formula, and the sequence is only one way to build it.

The initial segment $((p \land q)$ has $2$ left brackets and $1$ right bracket, so it is not a formula.
This is a small case of a general fact: no proper initial segment of a formula is a formula.
With the precedence rules we can write $\varphi$ as $p \land q \to \neg r$, because $\land$ binds more strongly than $\to$.

Change one variable and the count changes.
The formula $((p \land q) \to (\neg p))$ has only $5$ subformulas, because $p$ occurs twice but counts once in the set.

## Explanations

### L1 human

The formula says "if $p$ and $q$, then not $r$".
We build it in steps: first the letters $p$, $q$ and $r$, then "$p$ and $q$", then "not $r$", and last the whole "if ... then".
Each step uses only the pieces of earlier steps.
Drawn as a tree, the "if ... then" sits at the top, with "and" and "not" below it, and the letters at the bottom.

### L2 human

A machine finds the main connective by counting brackets.
Remove the outer brackets of $\varphi$ to get $(p \land q) \to (\neg r)$, then read from the left and keep the number of open brackets:
$$\underset{1}{(}\ \underset{1}{p}\ \underset{1}{\land}\ \underset{1}{q}\ \underset{0}{)}\ \underset{0}{\to}\ \cdots$$
The count first returns to $0$ after the fifth symbol, so the left part is $(p \land q)$, the next symbol $\to$ is the main connective, and the rest $(\neg r)$ is the right part.
This is how the parser of a programming language builds a tree.

Watch out.
Do not split at the first connective you see, here $\land$.
It lies inside a bracket, so it is not the main connective.
