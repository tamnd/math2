---
tag: TRXB894JMH
kind: proof
name: Proof of the Łoś–Tarski theorem by diagrams and compactness
aliases: [proof-of-los-tarski-theorem]
msc: ["03C40", "03C52"]
topics: [JYJHB4YBAH]
audience: grad
proves: 9RN0KYXNT1
uses: [EP5E317TNW, 1NR3HAWG9D, C9494XYEMN, SCRB74SWQN, CGH8C8EA9N, 676H7EGTKJ, 92SWXST1ZM]
methods: [0J0XBKG64S, TFQ1845T84, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Łoś–Tarski_preservation_theorem
    locator: Proof
  - book: isbn:9780521587136
---

## Proof

All structures have nonempty domains, and $\mathrm{Diag}$ and $\mathrm{ElDiag}$ are the atomic and elementary [[diagrams|EP5E317TNW]].

### Part 1

1. Suppose $T$ is equivalent to $T_\forall$. A universal sentence true in $B$ is true in each substructure of $B$, by [[this statement|C9494XYEMN]]. So the models of $T$ are closed under substructures.
2. Conversely, suppose the models of $T$ are closed under substructures, and let $A \models T_\forall$. We show $A \models T$.
3. Consider $T \cup \mathrm{Diag}(A)$, in $L$ with a new constant $c_a$ for each $a \in A$.
4. Suppose it has no model. By the [[compactness theorem|1NR3HAWG9D]], $T \cup \set{\delta_1, \dots, \delta_k}$ has no model for some $\delta_j \in \mathrm{Diag}(A)$. We may include $c_a = c_a$, so $k \ge 1$.
5. Write $\delta = \delta_1 \wedge \dots \wedge \delta_k$ as $\delta(\bar c)$ with $\delta(\bar x)$ quantifier-free. Then $T \models \neg\delta(\bar c)$.
6. The constants $\bar c$ do not occur in $T$, so $T \models \forall \bar x \, \neg\delta(\bar x)$. This sentence is universal, so it lies in $T_\forall$.
7. But $A \models \delta(\bar a)$, because each $\delta_j$ is true in $A$. So $A \not\models T_\forall$, a contradiction.
8. So $T \cup \mathrm{Diag}(A)$ has a model $B$. By the diagram lemma, $a \mapsto c_a^B$ is an [[embedding|SCRB74SWQN]] of $A$ into the $L$-reduct of $B$, which is a model of $T$.
9. The image of $A$ is a substructure of a model of $T$, so it is a model of $T$ by the hypothesis. Hence $A \models T$.

### Part 2

10. Existential sentences pass from a structure to its extensions, since a witness in $A$ is a witness in $B \supseteq A$. This is the easy direction.
11. Conversely, suppose the models of $T$ are closed under extensions, and let $B \models T_\exists$.
12. Let $\Sigma = T \cup \set{\neg\psi : \psi \text{ existential}, B \models \neg\psi}$. Suppose $\Sigma$ has no model.
13. By compactness, $T \models \psi_1 \vee \dots \vee \psi_k$ for some existential $\psi_j$ false in $B$. We may include $\exists x \, \neg(x = x)$, so $k \ge 1$. A disjunction of existential sentences is equivalent to an existential sentence, so it lies in $T_\exists$ and holds in $B$, a contradiction.
14. So $\Sigma$ has a model $A$; then $A \models T$, and every existential sentence true in $A$ is true in $B$.
15. Consider $\mathrm{Diag}(A) \cup \mathrm{ElDiag}(B)$, with disjoint sets of new constants. Suppose it has no model.
16. By compactness, $\mathrm{ElDiag}(B) \models \neg\delta(\bar c)$ for one quantifier-free $\delta(\bar c)$ in $\mathrm{Diag}(A)$. The $\bar c$ do not occur in $\mathrm{ElDiag}(B)$, so $B \models \neg\exists \bar x \, \delta(\bar x)$.
17. But $A \models \exists \bar x \, \delta(\bar x)$, so by step 14 $B \models \exists \bar x \, \delta(\bar x)$, a contradiction.
18. Let $C$ be a model. By the diagram lemmas, $A$ embeds in $C$ and $B$ has an [[elementary embedding|CGH8C8EA9N]] into $C$.
19. $C$ is an extension of a copy of $A \models T$, so $C \models T$. Then $B \models T$, because $B$ is elementarily embedded in $C$.

### Part 3

20. Let $\varphi$ be preserved by substructures, and apply part 1 to $T = \set{\varphi}$. Then $T_\forall \models \varphi$.
21. By compactness, finitely many $\forall\bar x_1 \, \theta_1, \dots, \forall\bar x_m \, \theta_m$ in $T_\forall$ imply $\varphi$. With disjoint variables, their conjunction is equivalent to the universal sentence $\forall \bar x_1 \cdots \forall \bar x_m \, (\theta_1 \wedge \dots \wedge \theta_m)$.
22. This sentence follows from $\varphi$ and implies $\varphi$, so it is equivalent to $\varphi$. The case of extensions is the same with part 2 and existential sentences.

## Idea

A model $A$ of the universal consequences of $T$ cannot be told apart from models of $T$ by finitely many facts about its elements.
Compactness turns this into an extension of $A$ that is a model of $T$, and closure under substructures brings $T$ back down to $A$.
The dual uses an elementary extension of $B$ that contains a model of $T$, and closure under extensions brings $T$ up.

## Variants

- For one sentence, the dual follows from part 1 by negation. The sentence $\varphi$ is preserved by extensions if and only if $\neg\varphi$ is preserved by substructures, and the negation of a universal sentence is equivalent to an existential one.
- The relative form for formulas has the same proof, with the free variables replaced by new constants.
