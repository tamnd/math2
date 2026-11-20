---
tag: S1X1BYWD3G
kind: example
name: Boethius' theses in Wansing's C
msc: ["03B60", "03B53"]
topics: [NJB94B39QK]
audience: grad
instance_of: [NQFYY76BSM]
uses: [NQFYY76BSM, 22K4GWJ0WM, 0Y0MQYST0M]
sources:
  - url: https://plato.stanford.edu/entries/logic-connexive/
    locator: Connexive Logic (SEP entry), sections 1, 2 and 4.5.1
---

## Example

We derive [[Boethius' theses|22K4GWJ0WM]] BT and BT′ in Wansing's system $\mathbf{C}$ of [[connexive logic|NQFYY76BSM]], and we show that its implication is not symmetric.
The axioms we use are a2 $\sim\sim A \leftrightarrow A$ and a5 $\sim(A \to B) \leftrightarrow (A \to \sim B)$, with positive intuitionistic logic and [[modus ponens|0Y0MQYST0M]].

BT′: $(A \to \sim B) \to \sim(A \to B)$.

1. $\sim(A \to B) \leftrightarrow (A \to \sim B)$. Axiom a5.
2. $(A \to \sim B) \to \sim(A \to B)$. From 1, by the elimination of $\land$.

BT: $(A \to B) \to \sim(A \to \sim B)$.

3. $B \to \sim\sim B$. From axiom a2, by the elimination of $\land$.
4. $(B \to \sim\sim B) \to ((A \to B) \to (A \to \sim\sim B))$. A theorem of positive intuitionistic logic.
5. $(A \to B) \to (A \to \sim\sim B)$. Modus ponens on 3 and 4.
6. $\sim(A \to \sim B) \leftrightarrow (A \to \sim\sim B)$. Axiom a5, with $\sim B$ for $B$.
7. $(A \to \sim\sim B) \to \sim(A \to \sim B)$. From 6, by the elimination of $\land$.
8. $(A \to B) \to \sim(A \to \sim B)$. From 5 and 7, by transitivity of $\to$ in positive intuitionistic logic.

Non-symmetry: $(p \to q) \to (q \to p)$ is not a theorem.

9. Take a model of $\mathbf{C}$ with one state $t$, where $t$ supports the truth of $q$ and not the truth of $p$.
10. Then $t$ supports the truth of $p \to q$, since the only state $u \geq t$ is $t$ and $t$ supports $q$.
11. $t$ does not support the truth of $q \to p$, since $t$ supports $q$ and not $p$.
12. So $t$ does not support the truth of $(p \to q) \to (q \to p)$.
13. $\mathbf{C}$ is sound for its models, so the formula is not a theorem.

## Remarks

Steps 5 to 8 give the strong form $(A \to B) \to \sim(A \to \sim B)$, and the converse also holds in $\mathbf{C}$.
So $\mathbf{C}$ proves $(A \to B) \leftrightarrow \sim(A \to \sim B)$, the hyperconnexive principle BTe of the SEP entry.
The non-symmetry argument uses only the positive part of the semantics, where $\mathbf{C}$ agrees with intuitionistic logic.

## Explanations

### L1 human

Boethius' thesis says: if $A$ implies $B$, then $A$ does not imply not-$B$.
In $\mathbf{C}$, "$A$ does not imply not-$B$" is read as "$A$ implies not-not-$B$", that is, "$A$ implies $B$".
So the thesis says that "$A$ implies $B$" implies itself.

### L2 human

BT′ is half of axiom a5, and BT is a5 combined with double negation in the consequent.
Non-symmetry needs a model; one state with $q$ true and $p$ not true is enough.
A trap is to think that BT holds classically; it fails when $A$ is false.
