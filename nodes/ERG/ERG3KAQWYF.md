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

A multimodal logic has several boxes $\square_1, \dots, \square_n$ instead of one, each read by its own accessibility relation.
It is the language of [[modal logic|C3RZY20ETK]] for knowledge of several agents, for time with past and future, and for programs.
Each agent, direction or program has its own box.
The basic theory of [[Kripke semantics|NGHWZ9Y7ZV]] carries over box by box; new questions come from the axioms that connect different boxes.

## Motivation

One box can express "agent $a$ knows $\varphi$", but not "agent $a$ knows that agent $b$ does not know $\varphi$".
One box can express "$\varphi$ will always hold", but not "$\varphi$ has always held".
For each such pair we need two boxes with two relations.
Often we also need an axiom that says how the relations are linked, such as "the past relation is the converse of the future relation".
The study of these combinations is the theory of multimodal logic.

## Notation

1. The language has variables, $\bot$, $\to$ and one box $\square_i$ for each index $i$ in a set $I$ of *modalities*; $\lozenge_i = \neg\square_i\neg$.
2. A frame is $(W, (R_i)_{i \in I})$, and $w \models \square_i\varphi$ if and only if $\varphi$ holds at every $v$ with $w \mathrel{R_i} v$.
3. A normal multimodal logic contains axiom $\mathrm{K}$ and is closed under necessitation for each box. The smallest one with $n$ boxes is $\mathsf{K}_n$.
4. The *fusion* $\Lambda_1 \otimes \Lambda_2$ of two normal monomodal logics is the smallest normal bimodal logic that contains $\Lambda_1$ for $\square_1$ and $\Lambda_2$ for $\square_2$.
5. In epistemic logic the boxes are written $K_a$ for agents $a$. In tense logic they are $G$ and $H$. In dynamic logic they are $[\alpha]$ for programs $\alpha$.

## Remarks

### Examples

1. Knowledge of two agents. $\mathsf{S5}_2$ is the fusion of two copies of [[S5|VC3A2VWXND]]; each $R_a$ is an equivalence relation, see [[knowledge of two agents about a card deal|EM6M72T720]].
2. Tense logic. $\mathsf{K}_t$ has boxes $G$ and $H$ and the interaction axioms $p \to GPp$ and $p \to HFp$. These axioms hold exactly when $R_H$ is the converse of $R_G$, see [[future and past in the basic tense logic|KXRMT4R9E8]].
3. Propositional dynamic logic. There is a box $[\alpha]$ for each program $\alpha$, built from atomic programs by $;$, $\cup$ and ${}^*$. The axioms $[\alpha ; \beta]p \leftrightarrow [\alpha][\beta]p$ and $[\alpha \cup \beta]p \leftrightarrow [\alpha]p \wedge [\beta]p$ tie the boxes to the program structure.
4. Common knowledge. With agents in a group $G$, $E_G\varphi = \bigwedge_{a \in G} K_a\varphi$ means "everyone knows", and [[common knowledge|7BCMKF2P7X]] $C_G\varphi$ is read by the transitive closure of $\bigcup_{a \in G} R_a$.

### Non-examples

1. A logic with $\square$ and $\lozenge$ is not multimodal: $\lozenge$ is defined as $\neg\square\neg$, so there is only one modality.
2. The fusion $\mathsf{K} \otimes \mathsf{K}$ does not prove the commutativity axiom $\square_1\square_2 p \to \square_2\square_1 p$, see [[commutativity is not a theorem of the fusion|X2J9XQAP89]]. So a fusion has no interaction between its boxes, and commutativity is an extra axiom, not a consequence.
3. A conditional logic with a binary connective $\varphi \mathrel{\square\!\!\to} \psi$ is not multimodal in this sense: its modality has two arguments, not one.

### Basic properties

1. Completeness of $\mathsf{K}_n$. $\mathsf{K}_n$ is sound and strongly complete for the class of all frames with $n$ relations. The proof of [[the truth lemma|NM4CB7QAYT]] works with one canonical relation for each box: $\Gamma \mathrel{R_i} \Delta$ if and only if $\square_i\varphi \in \Gamma$ implies $\varphi \in \Delta$.
2. Correspondence box by box. Each axiom of [[the common schemata|FDFQFWPM4X]] written for $\square_i$ corresponds to the same condition on $R_i$, with the same proof.
3. The [[standard translation|1HQ1W36J4V]] uses one relation symbol $R_i$ for each box, and the correctness proof is the same.
4. Complexity. $\mathsf{K}_n$, $\mathsf{T}_n$ and $\mathsf{S4}_n$ are PSPACE-complete for $n \ge 1$, and $\mathsf{S5}_n$ is PSPACE-complete for $n \ge 2$, by Halpern and Moses. With common knowledge, and $n \ge 2$, they are EXPTIME-complete, see [[the complexity theorem|1P2B0C7CQ4]].
5. Transfer for fusions. Completeness, the finite model property and decidability pass from $\Lambda_1$ and $\Lambda_2$ to $\Lambda_1 \otimes \Lambda_2$. This was proved by Kracht and Wolter in 1991 and by Fine and Schurz in 1996.
6. Interaction can change the logic sharply. For two agents, $\mathsf{S5}$ for each agent is NP-complete, but $\mathsf{S5}_2$ is PSPACE-complete, by property 4 and [[the complexity theorem|1P2B0C7CQ4]].

### History

Prior introduced the tense operators in "Time and Modality" (1957).
Hintikka gave the possible-worlds reading of knowledge and belief in "Knowledge and Belief" (1962).
Pratt introduced dynamic logic in 1976, and Fischer and Ladner defined its propositional version and proved it decidable in 1979.
Halpern and Moses classified the completeness and complexity of the multi-agent logics of knowledge and belief in 1992.

### Common errors

1. Assuming that two boxes interact without an axiom. The fusion proves no interaction formula such as commutativity, see non-example 2; each link between boxes must be added as an axiom.
2. Confusing "everyone knows" $E_G\varphi$ with common knowledge $C_G\varphi$. $E_G E_G \varphi$ need not follow from $E_G \varphi$.
3. Reading the tense logic $\mathsf{K}_t$ as $\mathsf{K} \otimes \mathsf{K}$. The converse axioms of $\mathsf{K}_t$ are interaction axioms, and the fusion does not prove them.

## Explanations

### L1 human

A multimodal logic talks about several kinds of necessity at once.
For example, it can say what Alice knows, what Bob knows, and what Alice knows about Bob's knowledge.
Each kind has its own arrows between worlds.
Extra laws can link the kinds, such as "what was true will always have been true".

### L2 human

We show that $E_G p \to E_G E_G p$ can fail, with agents $a$ and $b$.

1. Take $W = \set{u, v, t}$. Let $R_a$ have the classes $\set{u}$ and $\set{v, t}$, and $R_b$ have the classes $\set{u, v}$ and $\set{t}$. Put $V(p) = \set{u, v}$.
2. At $u$: the $R_a$-class is $\set{u}$, and the $R_b$-class is $\set{u, v}$. Both lie in $V(p)$, so $E_G p$ is true at $u$.
3. At $v$: the $R_a$-class is $\set{v, t}$, and $p$ fails at $t$. So $K_a p$ and $E_G p$ are false at $v$.
4. $u \mathrel{R_b} v$, so $K_b E_G p$ is false at $u$, and $E_G E_G p$ is false at $u$.

The typical use is to model several agents or several directions of time.
A trap: each $K_a$ obeys $\mathsf{S5}$, but "everyone knows" does not, since it fails axiom 4.

### L3 human

The fusion is the most neutral combination; products and logics with interaction axioms are much harder.
The general theory is the subject of many-dimensional modal logic.
Products of two copies of $\mathsf{K}$ have commutativity and the Church-Rosser property $\lozenge_1\square_2 p \to \square_2\lozenge_1 p$ as axioms, and their frames are the products of two frames.
Common knowledge and the star of dynamic logic need a transitive closure, which is not first-order.
So the canonical model method fails for them, and completeness uses filtration instead, see [[filtration|6ZZSHAKG5F]].
