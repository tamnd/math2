---
tag: ERG3KAQWYF
kind: concept
name: Multimodal logic
msc: ["03B45", "03B42", "03B44"]
topics: [SKY7AQFG1V]
audience: grad
uses: [C3RZY20ETK, NGHWZ9Y7ZV, JS8W7PA6JK, VC3A2VWXND, FDFQFWPM4X, NM4CB7QAYT, 1HQ1W36J4V, 1P2B0C7CQ4]
sources:
  - url: https://en.wikipedia.org/wiki/Multimodal_logic
    locator: lead section
  - doi: 10.1016/0004-3702(92)90049-4
    locator: Halpern and Moses, A guide to completeness and complexity for modal logics of knowledge and belief, Artificial Intelligence 54 (1992), sections 2 and 3
  - url: https://en.wikipedia.org/wiki/Dynamic_logic_(modal_logic)
    locator: Axioms
  - url: https://en.wikipedia.org/wiki/Temporal_logic
    locator: History
---

## Summary

Deal one card each to Alice and Bob from three cards.
To say "Alice knows that Bob does not know her card" we need two boxes, $K_a$ for Alice and $K_b$ for Bob, each read by its own relation on the deals.
A multimodal logic has several boxes $\square_1, \dots, \square_n$ in this way, one for each agent, direction of time or program.
The [[Kripke semantics|NGHWZ9Y7ZV]] of [[modal logic|C3RZY20ETK]] carries over box by box, and the new questions come from axioms that link different boxes.

## Motivation

One box can express "agent $a$ knows $\varphi$", but not "agent $a$ knows that agent $b$ does not know $\varphi$".
One box can express "$\varphi$ will always hold", but not "$\varphi$ has always held".
Each such pair needs two boxes with two relations.
Often it also needs an axiom that links the relations, such as "the past relation is the converse of the future relation".

## Notation

The language has variables, $\bot$, $\to$, and one box $\square_i$ for each index $i$ in a set $I$ of modalities, with $\lozenge_i = \neg\square_i\neg$.
A frame is $(W, (R_i)_{i \in I})$, and $w \models \square_i\varphi$ when $\varphi$ holds at every $v$ with $w \mathrel{R_i} v$.
A normal multimodal logic contains the axiom $\mathrm{K}$ and is closed under necessitation for each box, and the smallest one with $n$ boxes is $\mathsf{K}_n$.
The *fusion* $\Lambda_1 \otimes \Lambda_2$ of two normal logics is the smallest normal bimodal logic that contains $\Lambda_1$ for $\square_1$ and $\Lambda_2$ for $\square_2$.
Epistemic logic writes $K_a$ for agents $a$, tense logic writes $G$ and $H$, and dynamic logic writes $[\alpha]$ for programs $\alpha$.

## Remarks

### Three standard examples

For knowledge of two agents, $\mathsf{S5}_2$ is the fusion of two copies of [[S5|VC3A2VWXND]], and each relation $R_a$ is an equivalence relation; see [[knowledge of two agents about a card deal|EM6M72T720]].
Tense logic $\mathsf{K}_t$ has boxes $G$ and $H$ and the axioms $p \to GPp$ and $p \to HFp$, which hold exactly when $R_H$ is the converse of $R_G$; see [[future and past in the basic tense logic|KXRMT4R9E8]].
[[Propositional dynamic logic|VJ78A0Q22R]] has a box $[\alpha]$ for each program $\alpha$, built from atomic programs by $;$, $\cup$ and ${}^*$.
Its axioms $[\alpha ; \beta]p \leftrightarrow [\alpha][\beta]p$ and $[\alpha \cup \beta]p \leftrightarrow ([\alpha]p \wedge [\beta]p)$ tie the boxes to the structure of programs.

### Everyone knows and common knowledge

For a group $G$ of agents, $E_G\varphi = \bigwedge_{a \in G} K_a\varphi$ says that everyone knows $\varphi$.
[[Common knowledge|7BCMKF2P7X]] $C_G\varphi$ is read by the transitive closure of $\bigcup_{a \in G} R_a$.
The two are different, since $E_G E_G\varphi$ need not follow from $E_G\varphi$; the L2 explanation gives a model.

### What is not multimodal

A logic with $\square$ and $\lozenge$ has only one modality, since $\lozenge$ is defined as $\neg\square\neg$.
A conditional logic with a binary connective $\varphi \mathrel{\square\!\!\to} \psi$ is not multimodal in this sense, since its modality has two arguments.

### Completeness and correspondence

$\mathsf{K}_n$ is sound and strongly complete for the class of all frames with $n$ relations.
The proof of [[the truth lemma|NM4CB7QAYT]] works with one canonical relation for each box: $\Gamma \mathrel{R_i} \Delta$ when $\square_i\varphi \in \Gamma$ implies $\varphi \in \Delta$.
Each axiom of [[the common schemata|FDFQFWPM4X]], written for $\square_i$, corresponds to the same condition on $R_i$, with the same proof.
The [[standard translation|1HQ1W36J4V]] uses one relation symbol $R_i$ for each box.

### Complexity

$\mathsf{K}_n$, $\mathsf{T}_n$ and $\mathsf{S4}_n$ are PSPACE-complete for $n \ge 1$, and $\mathsf{S5}_n$ is PSPACE-complete for $n \ge 2$, by Halpern and Moses.
With common knowledge and $n \ge 2$ they are EXPTIME-complete; see [[the complexity theorem|1P2B0C7CQ4]].
So a second agent changes the picture: $\mathsf{S5}$ alone is NP-complete, but $\mathsf{S5}_2$ is PSPACE-complete.

### Fusions

Completeness, the finite model property and decidability pass from $\Lambda_1$ and $\Lambda_2$ to $\Lambda_1 \otimes \Lambda_2$.
Kracht and Wolter proved this in 1991, and Fine and Schurz in 1996.
But a fusion has no interaction at all: $\mathsf{K} \otimes \mathsf{K}$ does not prove $\square_1\square_2 p \to \square_2\square_1 p$; see [[commutativity is not a theorem of the fusion|X2J9XQAP89]].

### History

Prior introduced the tense operators in "Time and Modality" (1957).
Hintikka gave the possible-worlds reading of knowledge and belief in "Knowledge and Belief" (1962).
Pratt introduced dynamic logic in 1976, and Fischer and Ladner defined its propositional version and proved it decidable in 1979.
Halpern and Moses classified the completeness and complexity of the logics of knowledge and belief for several agents in 1992.

### Watch out

Two boxes do not interact unless an axiom says so, and each link between boxes must be added as an axiom.
In particular, $\mathsf{K}_t$ is not $\mathsf{K} \otimes \mathsf{K}$, since its converse axioms are interaction axioms that the fusion does not prove.
And "everyone knows" is not common knowledge.

## Explanations

### L1 human

A multimodal logic talks about several kinds of necessity at once.
For example, it can say what Alice knows, what Bob knows, and what Alice knows about Bob's knowledge.
Each kind has its own arrows between worlds.
Extra laws can link the kinds, such as "what is true now will always have been true".

### L2 human

We show that $E_G p \to E_G E_G p$ can fail, with two agents $a$ and $b$.

1. Take $W = \{ u, v, t \}$ and $V(p) = \{ u, v \}$.
   Let $R_a$ have the classes $\{ u \}$ and $\{ v, t \}$, and let $R_b$ have the classes $\{ u, v \}$ and $\{ t \}$.
2. At $u$, the $R_a$-class $\{ u \}$ and the $R_b$-class $\{ u, v \}$ lie in $V(p)$, so $E_G p$ is true at $u$.
3. At $v$, the $R_a$-class is $\{ v, t \}$ and $p$ fails at $t$, so $K_a p$ and $E_G p$ are false at $v$.
4. Since $u \mathrel{R_b} v$, the formula $K_b E_G p$ is false at $u$, and so is $E_G E_G p$.

The typical use is to model several agents or several directions of time.
Watch out: each $K_a$ obeys $\mathsf{S5}$, but "everyone knows" does not, since it fails the axiom $\mathrm{4}$.

### L3 human

The fusion is the most neutral combination, and products and logics with interaction axioms are much harder.
The general theory is many-dimensional modal logic.
The product of two copies of $\mathsf{K}$ adds both commutativity formulas and the Church-Rosser formula $\lozenge_1\square_2 p \to \square_2\lozenge_1 p$, and its frames are products of two frames.
Common knowledge and the star of dynamic logic need a transitive closure, which is not first-order.
So the plain canonical model method fails for them, and completeness uses [[filtration|6ZZSHAKG5F]] instead.
