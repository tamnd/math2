---
tag: DQ2XRGXWP9
kind: proof
name: Proof of Gärdenfors's triviality theorem
msc: ["03B42", "03B45"]
topics: [CQM9SRN8PM]
audience: research
proves: WMZ1QP7KQY
uses: [Y05YQN7HGQ]
methods: [0J0XBKG64S, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Ramsey_test
    locator: Triviality theorem in belief revision
  - book: isbn:9780262071093
    locator: Gärdenfors, Knowledge in Flux
---

## Proof

We assume a nontrivial system with conditions 1 to 5 and show that one belief set must revise to an inconsistent set, against weak consistency.
We use the notation of [[the triviality theorem|WMZ1QP7KQY]].
Let $(\mathcal{K}, *)$ satisfy conditions 1 to 5, and let $K \in \mathcal{K}$ and $A, B, C$ witness nontriviality.

1. Revision is monotone in the belief set.
   Let $H, H' \in \mathcal{K}$ with $H \subseteq H'$, and let $\psi \in H * \varphi$; the Ramsey test gives $(\varphi > \psi) \in H \subseteq H'$, and the Ramsey test again gives $\psi \in H' * \varphi$.
2. Put $K_1 = K + (A \vee B)$, $K_2 = K + (A \vee C)$ and $H = K + A$.
   These lie in $\mathcal{K}$, since $\mathcal{K}$ is closed under expansion.
3. Since $A \vdash A \vee B$ and $A \vdash A \vee C$, we get $K_1 \subseteq H$ and $K_2 \subseteq H$.

### Two incompatible answers

4. Propositional logic gives $(A \vee B) \wedge (B \vee C) \equiv B \vee (A \wedge C)$, and $A \wedge C$ is refutable.
   So $K_1 + (B \vee C) = K + B$.
5. The set $K + B$ is consistent, because $\neg B \notin K$.
   By step 4, $\neg(B \vee C) \notin K_1$.
6. Preservation applied to step 5 gives $K_1 \subseteq K_1 * (B \vee C)$, so $A \vee B \in K_1 * (B \vee C)$.
7. Success gives $B \vee C \in K_1 * (B \vee C)$.
   By closure the set contains $(A \vee B) \wedge (B \vee C)$, which is equivalent to $B$ by step 4, so $B \in K_1 * (B \vee C)$.
8. Exchange the roles of $B$ and $C$ in steps 4 to 7.
   This gives $(A \vee C) \wedge (B \vee C) \equiv C$ and $\neg C \notin K$, so $C \in K_2 * (B \vee C)$.

### The contradiction

9. Steps 1 and 3 give $K_1 * (B \vee C) \subseteq H * (B \vee C)$ and $K_2 * (B \vee C) \subseteq H * (B \vee C)$.
   So $B$ and $C$ both lie in $H * (B \vee C)$.
10. Since $\vdash \neg(B \wedge C)$ and $H * (B \vee C)$ is a belief set, $H * (B \vee C)$ is inconsistent.
11. On the other hand, $H = K + A$ is consistent, because $\neg A \notin K$.
    Also $B \vee C$ is consistent, because $B$ is consistent with $K$.
12. Weak consistency applied to step 11 says that $H * (B \vee C)$ is consistent, and this contradicts step 10.

So no nontrivial belief revision system satisfies conditions 1 to 5.

## Idea

The Ramsey test turns the conditionals in a belief set into commitments about revision, so a larger belief set must revise to a larger result.
Preservation pushes the other way: two weaker belief sets revise by $B \vee C$ to two incompatible answers, $B$ and $C$.
The stronger belief set $K + A$ contains both weaker ones, so it inherits both answers and becomes inconsistent.

## Variants

Step 1 is the only use of the Ramsey test.
It uses the direction from revision to conditionals for $K_1$ and $K_2$, and the direction from conditionals to revision for $H$.
The proof applies preservation only to the formulas $A \vee B$ and $A \vee C$, which contain no $>$.
So a weaker preservation, restricted to formulas without $>$, does not escape the theorem.
