---
tag: ~4b1ecd4c
kind: proof
name: Proof of the Chang-Łoś-Suszko theorem by a sandwich chain
aliases: [proof-of-chang-los-suszko-theorem]
msc: ["03C40", "03C52"]
topics: [JYJHB4YBAH]
audience: grad
proves: ~99a892b2
uses: [NHCRZ74JHH, EP5E317TNW, 1NR3HAWG9D, 8WZF9SBP39, CGH8C8EA9N, SCRB74SWQN, 92SWXST1ZM]
methods: [0J0XBKG64S, 01XM7JEKHY, 0ASJVEFA9J]
sources:
  - book: isbn:9780521587136
---

## Proof

For a structure $B$, let $L_B$ be $L$ with a constant for each element of $B$, as in the [[diagram lemmas|EP5E317TNW]].

### The easy implications

1. Suppose 3. Then the models of $T$ are the models of the $\forall\exists$ theory $T_{\forall\exists}$. By part 2 of the [[elementary chain theorem|NHCRZ74JHH]], a union of a chain of such models is a model. This gives 1.
2. Statement 2 is a special case of statement 1.

### From 2 to 3: two lemmas

3. Assume 2, and let $B \models T_{\forall\exists}$. We must show $B \models T$.
4. Lemma 1: if $C \models T_{\forall\exists}$, there is $A \models T$ with $C \subseteq A$ such that every universal $L_C$-sentence true in $C$ is true in $A$.
5. Proof of lemma 1. Let $\Gamma$ be $T$ together with all universal $L_C$-sentences true in $C$; this includes $\mathrm{Diag}(C)$.
6. Suppose $\Gamma$ has no model. By the [[compactness theorem|1NR3HAWG9D]] and closure of universal sentences under $\wedge$, $T \models \neg\forall \bar z \, \theta(\bar c, \bar z)$ for one universal sentence $\forall \bar z \, \theta(\bar c, \bar z)$ true in $C$.
7. The constants $\bar c$ do not occur in $T$, so $T \models \forall \bar y \, \exists \bar z \, \neg\theta(\bar y, \bar z)$. This is a $\forall\exists$ sentence, so it holds in $C$, and then $C \models \exists \bar z \, \neg\theta(\bar c, \bar z)$, a contradiction.
8. So $\Gamma$ has a model $A$. It satisfies $\mathrm{Diag}(C)$, so $C$ [[embeds|SCRB74SWQN]] in $A$, and we identify $C$ with its image.
9. Lemma 2: if $C \subseteq A$ and every universal $L_C$-sentence true in $C$ is true in $A$, there is $C' $ with $C \preceq C'$ and $A \subseteq C'$.
10. Proof of lemma 2. Consider $\mathrm{ElDiag}(C) \cup \mathrm{Diag}(A)$, where the elements of $C$ have the same constants in both parts. Suppose it has no model.
11. By compactness, $\mathrm{ElDiag}(C) \models \neg\delta(\bar c, \bar d)$ for one quantifier-free $\delta(\bar c, \bar d) \in \mathrm{Diag}(A)$, where $\bar d$ are constants for elements of $A \setminus C$.
12. The $\bar d$ do not occur in $\mathrm{ElDiag}(C)$, so $C \models \forall \bar x \, \neg\delta(\bar c, \bar x)$. This universal $L_C$-sentence then holds in $A$, but $\bar d$ witnesses $\delta$ in $A$, a contradiction.
13. A model of the union gives an [[elementary embedding|CGH8C8EA9N]] of $C$ and an embedding of $A$ that agree on $C$. After renaming, $C \preceq C'$ and $A \subseteq C'$.

### From 2 to 3: the chain

14. Put $B_0 = B$. Suppose $B_n$ is built with $B \preceq B_n$. Then $B_n \models T_{\forall\exists}$, since $B_n$ and $B$ satisfy the same sentences.
15. Lemma 1 for $C = B_n$ gives $A_n \models T$ with $B_n \subseteq A_n$. Lemma 2 gives $B_{n+1}$ with $B_n \preceq B_{n+1}$ and $A_n \subseteq B_{n+1}$.
16. Then $B \preceq B_{n+1}$, since a composite of elementary embeddings is elementary. By [[induction|0ASJVEFA9J]] we get $B_0 \subseteq A_0 \subseteq B_1 \subseteq A_1 \subseteq \cdots$.
17. Let $U$ be the union. Each element of $U$ lies in some $A_n$ and in some $B_n$, so $U$ is the union of the chain $(A_n)$ and also of the chain $(B_n)$.
18. The $A_n$ are models of $T$ indexed by $\mathbb{N}$, so $U \models T$ by statement 2.
19. The $B_n$ form an elementary chain, so $B \preceq U$ by part 1 of the elementary chain theorem.
20. Hence $B \models T$. This proves that $T_{\forall\exists}$ has the same models as $T$.

### The sentence form

21. Let $\varphi$ be preserved by unions of chains, and apply the theorem to $T = \set{\varphi}$. Then $T_{\forall\exists} \models \varphi$.
22. By compactness, finitely many sentences $\forall \bar x_k \, \exists \bar y_k \, \theta_k$ of $T_{\forall\exists}$ imply $\varphi$, for $k = 1$ to $m$.
23. With disjoint variables, their conjunction is equivalent to $\forall \bar x_1 \cdots \forall \bar x_m \, \exists \bar y_1 \cdots \exists \bar y_m \, (\theta_1 \wedge \dots \wedge \theta_m)$. This sentence is equivalent to $\varphi$.

## Idea

A model $B$ of $T_{\forall\exists}$ sits between models of $T$ and elementary extensions of itself, in an alternating chain.
The union of the chain is a union of models of $T$, so it is a model of $T$.
It is also an elementary extension of $B$, so $B$ is a model of $T$.

## Variants

- One can replace lemmas 1 and 2 by a single compactness argument that gives a model $A$ of $T$ with $B \subseteq A \subseteq B'$ and $B \preceq B'$, and then iterate.
- With $\kappa$-saturated models, lemma 2 becomes an embedding of $A$ over $B$ into a saturated elementary extension of $B$.
- Keisler's sandwich theorem refines the chain argument and characterizes the theories whose models are closed under unions of elementary chains of a given kind.
