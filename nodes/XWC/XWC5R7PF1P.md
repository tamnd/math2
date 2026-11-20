---
tag: XWC5R7PF1P
kind: example
name: Mixed theorems of the fusion of K and T
msc: ["03B62", "03B45"]
topics: [NJB94B39QK]
audience: research
instance_of: [HP1N0MBTDJ]
uses: [HP1N0MBTDJ, ERG3KAQWYF, NGHWZ9Y7ZV, E87G6ZTMTN]
sources:
  - url: https://plato.stanford.edu/entries/logic-combining/
    locator: Combining Logics (SEP entry), section 4.1
---

## Example

Let $\mathsf{K} \otimes \mathsf{T}$ be the fusion of $\mathsf{K}$, for the box $\square_1$, and $\mathsf{T}$, for the box $\square_2$, as in [[combining logics|HP1N0MBTDJ]].
Its axioms are all instances of classical tautologies in the bimodal language, the axiom $\mathsf{K}$ for each box, and $\square_2 \varphi \to \varphi$.
Its rules are modus ponens and necessitation for each box.
Schemas range over all bimodal formulas.

Claim 1: $\vdash \square_1(\square_2 p \to p)$.

1. The formula $\square_2 p \to p$ is an instance of the axiom of $\mathsf{T}$.
2. Necessitation for $\square_1$ gives $\square_1(\square_2 p \to p)$.

This is a mixed theorem: it uses the axiom of one component inside the box of the other.

Claim 2: $\nvdash \square_2(\square_1 p \to p)$ and $\nvdash \square_1 p \to p$.

3. Every theorem is valid on every [[Kripke frame|NGHWZ9Y7ZV]] $(W, R_1, R_2)$ with $R_2$ reflexive. Tautologies and the $\mathsf{K}$ axioms are valid on all such frames, and $\square_2 \varphi \to \varphi$ is valid when $R_2$ is reflexive. Modus ponens and necessitation keep validity, as in [[soundness of normal modal logics|E87G6ZTMTN]].
4. Take $W = \set{w}$, $R_1 = \emptyset$, $R_2 = \set{(w, w)}$ and $V(p) = \emptyset$.
5. The world $w$ has no $R_1$-successor, so $\square_1 p$ is true at $w$. The atom $p$ is false at $w$, so $\square_1 p \to p$ is false at $w$.
6. The only $R_2$-successor of $w$ is $w$ itself, so $\square_2(\square_1 p \to p)$ is false at $w$.
7. The frame has $R_2$ reflexive, so by step 3 neither formula is a theorem.

## Remarks

Claim 2 shows that the axiom $\mathsf{T}$ for $\square_2$ does not pass to $\square_1$.
In a fusion, each box keeps only the axioms of its own component; there is no axiom that links the two boxes.
Claim 1 shows that the fusion is still more than the two components side by side: the rules of one component act on formulas of the other.
For the absence of interaction, compare [[commutativity is not a theorem of the fusion of K with K|X2J9XQAP89]] and [[multimodal logic|ERG3KAQWYF]].

## Explanations

### L1 human

We join a logic with box 1, where nothing special holds, and a logic with box 2, where "box 2 of $p$" implies $p$.
The joined logic can say "box 1 of (box 2 of $p$ implies $p$)", because the rules of logic 1 apply to any formula.
But it cannot say that box 1 of $p$ implies $p$.

### L2 human

The frames of the fusion have one relation for each box, and each relation obeys only the conditions of its own logic.
A one-world frame with an empty $R_1$ and a reflexive $R_2$ shows that the reflexivity of $R_2$ says nothing about $R_1$.
A trap is to think that the fusion is the union of the theorems of the components; it also has mixed theorems.
