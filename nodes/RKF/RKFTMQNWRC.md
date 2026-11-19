---
tag: RKFTMQNWRC
kind: statement
role: theorem
name: Topological semantics of intuitionistic logic
msc: ["03B20", "54A05"]
topics: [38EQ20GR7M]
audience: research
uses: [0CQHFPGJ45, 02BH3MCBQB, 0RZH6W98HK, NG943XNQWH, BXVNEN55MR, 2VF0546VXK, 08J2M1JYAG, W9VYJRBF9N]
about: [Q11N8X99FK, 0CQHFPGJ45]
proofs: [J4PPJCF09K]
history:
  first_stated: "Tarski, 1938, Der Aussagenkalkül und die Topologie"
sources:
  - url: https://en.wikipedia.org/wiki/Intuitionistic_logic
    locator: Tarski-like semantics
  - url: https://en.wikipedia.org/wiki/Heyting_algebra
    locator: Examples
---

## Statement

Let $X$ be a [[topological space|0CQHFPGJ45]].
A *topological valuation* assigns to each propositional variable $p$ an [[open set|02BH3MCBQB]] $V(p) \subseteq X$.
It extends to all formulas by the following clauses, where $\mathrm{Int}$ is the [[interior|0RZH6W98HK]]:

- $[\![\bot]\!] = \emptyset$, $[\![\varphi \wedge \psi]\!] = [\![\varphi]\!] \cap [\![\psi]\!]$, and $[\![\varphi \vee \psi]\!] = [\![\varphi]\!] \cup [\![\psi]\!]$;
- $[\![\varphi \to \psi]\!] = \mathrm{Int}\big((X \setminus [\![\varphi]\!]) \cup [\![\psi]\!]\big)$.

So $[\![\neg \varphi]\!] = \mathrm{Int}(X \setminus [\![\varphi]\!])$.
A formula is *valid in* $X$ if $[\![\varphi]\!] = X$ for every topological valuation.

**Theorem.**

1. The open sets of $X$, ordered by inclusion, form a [[Heyting algebra|NG943XNQWH]], with $U \to W = \mathrm{Int}((X \setminus U) \cup W)$.
2. Soundness: every theorem of [[intuitionistic propositional logic|Q11N8X99FK]] is valid in every topological space.
3. Completeness for the [[real line|08J2M1JYAG]]: if $\varphi$ is valid in $\R$, then $\mathsf{IPC} \vdash \varphi$.
4. Completeness for the [[Cantor space|W9VYJRBF9N]]: if $\varphi$ is valid in the Cantor space, then $\mathsf{IPC} \vdash \varphi$.
5. Hence $\mathsf{IPC}$ is the logic of all topological spaces, of $\R$, and of the Cantor space.

The proof is in [[the proof by the Gödel-McKinsey-Tarski translation|J4PPJCF09K]].

## Remarks

### Why each hypothesis is needed

1. Truth values must be open. If $V(p)$ may be any set and implication uses complements without interior, the semantics is classical.
2. The interior in the clause for $\to$ is needed. Without it, $[\![p \vee \neg p]\!] = X$ for every $V$.
3. Completeness needs a space with enough points that are not isolated. A discrete space has the power set as its algebra of opens, so it validates $p \vee \neg p$.
4. A finite space never suffices for item 3: by [[Gödel's theorem on finite matrices|CFCPJA1QF5]], no finite Heyting algebra characterizes $\mathsf{IPC}$.

### Consequences

1. On $\R$ with $V(p) = (0, \infty)$, the formulas $p \vee \neg p$ and $\neg p \vee \neg \neg p$ fail at $0$; see [[the countermodels on the real line|QEV38QKN22]].
2. Every Kripke frame gives a topological space, its [[Alexandrov topology|CWZ1K5AN1N]] of up-sets, and the two semantics agree.
3. Every Beth model is a topological model on its space of paths; this gives [[Beth completeness|BTG0J9V3H4]] on the full binary tree.

### Converse

Items 2 to 4 together form a biconditional for $\R$ and for the Cantor space.
Item 1 has a converse in the form of a representation theorem.
Every Heyting algebra embeds in the up-sets of its prime filters, which are the opens of an Alexandrov space.

### Generalizations

1. The argument works for every space $X$ with $\mathrm{Log}(X) = \mathsf{S4}$, for example every dense-in-itself separable metric space such as $\R^n$ or $\mathbb{Q}$.
2. The [[Heyting algebra semantics|JM1XJXWZYH]] replaces the algebra of opens by an arbitrary Heyting algebra.
3. Intuitionistic predicate logic has a topological semantics too, with $\exists$ read as a union and $\forall$ read as the interior of an intersection.

## History

Tarski gave the topological interpretation of intuitionistic propositional logic in 1938.
McKinsey and Tarski later connected it with the logic $\mathsf{S4}$ through the Gödel translation.

## Explanations

### L1 human

The theorem gives a picture for each formula: a region of space with no edge points counted in it.
"Not $p$" is the inside of the region outside $p$.
On the number line, take "$p$" to be the positive numbers.
Then "not $p$" is the negative numbers, and the point $0$ belongs to neither, so "$p$ or not $p$" leaves out $0$.
The theorem says that the laws of intuitionistic logic are exactly the formulas that always cover the whole line.

### L2 human

1. Take $V(p) = (0, \infty)$ in $\R$.
2. Then $[\![\neg p]\!] = \mathrm{Int}((-\infty, 0]) = (-\infty, 0)$.
3. So $[\![p \vee \neg p]\!] = \R \setminus \set{0}$, and excluded middle is not valid in $\R$.
4. By item 2 of the theorem, $\mathsf{IPC} \nvdash p \vee \neg p$.

The typical use of the theorem is to refute a formula by a picture on the line.
A trap: the boundary points do the work; at $0$ the formula fails, while it holds everywhere else.

### L3 human

The algebra of opens of a space is a complete Heyting algebra, and every complete Heyting algebra is a frame in the sense of pointfree topology.
The completeness for $\R$ is the open-set shadow of the McKinsey-Tarski theorem for $\mathsf{S4}$.
The proof of that theorem maps $\R$ onto finite rooted posets by continuous open maps, which carry a refutation on the poset back to $\R$.
