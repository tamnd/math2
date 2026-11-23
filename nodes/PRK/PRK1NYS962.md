---
tag: PRK1NYS962
kind: proof
name: Proof of Solovay's arithmetical completeness theorem
msc: ["03F45", "03B45"]
topics: [3E7M66WW6Q]
audience: research
proves: 1ZRWVDYPX0
uses: [61THBNS8WE, 1DMFNR7FZT, NGHWZ9Y7ZV, HACXBCM7SS, NB2BCZR40F, F6H4STF9RG, 3HD30YG3DG, 3PRW76471J, 69234Z1V00, GE43CSZTS9, MFJXPAF0R0]
methods: [0NTF6DMVAP, 0J0XBKG64S, 12MQ2NJ29A, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: lead section
  - book: isbn:9780521701464
---

## Proof

We prove soundness by induction on derivations, and completeness by turning a finite countermodel into arithmetical sentences that behave like its worlds.
We write $\square \sigma$ for $\mathrm{Prov}_{\mathsf{PA}}(\ulcorner \sigma \urcorner)$ and use the [[derivability conditions|F6H4STF9RG]].
D1 says that if $\mathsf{PA} \vdash \sigma$, then $\mathsf{PA} \vdash \square \sigma$.
D2 says that $\mathsf{PA} \vdash \square(\sigma \to \tau) \to (\square \sigma \to \square \tau)$.
Formalized $\Sigma_1$-completeness says that $\mathsf{PA} \vdash \sigma \to \square \sigma$ for every $\Sigma_1$ sentence $\sigma$.
We also use one property of the proof coding: a sentence with a proof has proofs with arbitrarily large codes, for example by repeating an axiom line, and $\mathsf{PA}$ proves this fact.
The proof works for every $\Sigma_1$-sound $T$ as in part 3 of [[Solovay's theorem|1ZRWVDYPX0]] in place of $\mathsf{PA}$, as the last subsection explains.

### Soundness

We show that $\mathsf{GL} \vdash \varphi$ implies $\mathsf{PA} \vdash \varphi^*$ for every realization $*$, by induction on the derivation of $\varphi$ in $\mathsf{GL}$.

1. A realization of a tautology is a tautology, so $\mathsf{PA}$ proves it.
2. A realization of the axiom K is an instance of D2.
3. A realization of Löb's axiom is $\square(\square \sigma \to \sigma) \to \square \sigma$ with $\sigma = p^*$.
   $\mathsf{PA}$ proves it by the formalized form of [[Löb's theorem|3HD30YG3DG]].
4. Modus ponens is preserved, and necessitation is preserved by D1.
   A realization of a substitution instance of $\varphi$ is a realization of $\varphi$.

### The Solovay function

Let $(W, R, V)$ be a finite transitive irreflexive model with $W = \{ 1, \dots, n \}$ and with $1 R j$ for every $j \geq 2$.

5. Add a new world $0$.
   Let $W' = \{ 0, 1, \dots, n \}$ and $R' = R \cup \{ (0, i) : 1 \leq i \leq n \}$.
   Let $0 \in V'(p)$ exactly when $1 \in V(p)$, with $V'(p) \cap W = V(p)$.
6. $R'$ is transitive and irreflexive, and no world is $R'$-below $0$.
   The successors of each $i \geq 1$ are the same in both models, so each $i \geq 1$ satisfies the same formulas in both models, as in [[Kripke semantics|NGHWZ9Y7ZV]].
7. We cite a lemma of Solovay.
   There is a $\Sigma_1$ formula $H(x, y)$ such that $\mathsf{PA}$ proves that it defines a total function $h$ with the equations below.
   Here $S_j$ is the sentence "$\lim_m h(m) = j$", that is, $\exists m\, \forall k \geq m\, h(k) = j$.
   $$h(0) = 0, \qquad h(m + 1) = \begin{cases} j & \text{if } h(m) R' j \text{ and } m \text{ codes a } \mathsf{PA}\text{-proof of } \neg S_j, \\ h(m) & \text{otherwise.} \end{cases}$$
8. The existence of $H$ uses the [[diagonal lemma|3PRW76471J]], since the sentences $S_j$ mention $h$.
   The lemma also says that $\mathsf{PA}$ proves the facts of steps 9 to 14 below.
   Their formalization in $\mathsf{PA}$ is the part we cite without proof, and we give the informal argument for each.
9. If $h(m + 1) \neq h(m)$, then $h(m) R' h(m + 1)$.
   By transitivity, for $m < k$ either $h(k) = h(m)$ or $h(m) R' h(k)$.
   A code $m$ proves one sentence, and the $\neg S_j$ are different sentences, so $j$ in step 7 is unique.

### Facts (a) to (c)

10. Fact (a).
   The values of $h$ form an $R'$-chain, and $R'$ is a finite strict order, so $h$ changes at most $n$ times.
   Hence $\mathsf{PA} \vdash S_0 \vee \dots \vee S_n$, and $\mathsf{PA} \vdash \neg(S_i \wedge S_j)$ for $i \neq j$.
11. For each $i$, the formula $\exists m\, h(m) = i$ is a $\Sigma_1$ sentence.
   By step 9, $\mathsf{PA} \vdash \exists m\, h(m) = i \to S_i \vee \bigvee_{i R' j} S_j$.
12. For $i \geq 1$, $h$ reaches $i$ only at a step $m$ where $m$ codes a proof of $\neg S_i$.
   So $\mathsf{PA} \vdash \exists m\, h(m) = i \to \square \neg S_i$.
13. Fact (b): for $i R' j$, including $i = 0$, we have $\mathsf{PA} \vdash S_i \to \neg \square \neg S_j$.
   Assume $h(k) = i$ for all $k \geq m_0$ and $\neg S_j$ has a proof.
   Take a proof code $m \geq m_0$, and then $h(m + 1) = j \neq i$, a contradiction.
14. Fact (c): for $i \geq 1$, we have $\mathsf{PA} \vdash S_i \to \square \bigvee_{i R j} S_j$.
   From $S_i$ we get $\exists m\, h(m) = i$, so $\square \exists m\, h(m) = i$ by $\Sigma_1$-completeness.
   Step 11 with D1 and D2 gives $\square(S_i \vee \bigvee_{i R j} S_j)$, and step 12 gives $\square \neg S_i$.
   D2 combines the two.

### Facts (d) and (e): the walk stays at 0

15. Fact (d): $S_0$ is true in $\mathbb{N}$.
   Assume instead that $\lim h = i \geq 1$.
   Then $\exists m\, h(m) = i$ is a true $\Sigma_1$ sentence, so $\mathsf{PA}$ proves it, by [[Σ1-completeness|69234Z1V00]].
   Also $h$ moved to $i$ on a real proof of $\neg S_i$, so $\mathsf{PA} \vdash \neg S_i$.
16. By steps 11 and 15, $\mathsf{PA} \vdash \bigvee_{i R j} S_j$.
   By step 12 for each such $j$, $\mathsf{PA} \vdash \bigvee_{i R j} \square \neg S_j$.
   This is a $\Sigma_1$ sentence, and it is $0 = S0$ when $i$ has no successor.
17. $\mathsf{PA}$ is $\Sigma_1$-sound, so this sentence is true, and $\mathsf{PA} \vdash \neg S_j$ for some $j$ with $i R j$.
   That sentence has a proof code $m$ after $h$ has become constant $i$, and then $h(m + 1) = j \neq i$, a contradiction.
   So $\lim h = 0$.
18. Fact (e): for $i \geq 1$, $\mathsf{PA} \nvdash \neg S_i$.
   By step 9, once $h$ leaves $0$ it never returns, since no world is $R'$-below $0$.
   So step 17 gives $h(m) = 0$ for all $m$.
   If $m$ coded a proof of $\neg S_i$, then $0 R' i$ would give $h(m + 1) = i$.

### The realization and the main lemma

19. Define $p^* = \bigvee \{ S_k : 0 \leq k \leq n,\ k \in V'(p) \}$, where the empty disjunction is $0 = S0$.
20. Main lemma: for $i \geq 1$ and every modal formula $\psi$, if $i \models \psi$ then $\mathsf{PA} \vdash S_i \to \psi^*$, and if $i \not\models \psi$ then $\mathsf{PA} \vdash S_i \to \neg \psi^*$.
   We use [[structural induction|12MQ2NJ29A]] on $\psi$.
21. Variable $p$.
   If $i \models p$, then $S_i$ is a disjunct of $p^*$.
   If not, every disjunct is $S_k$ with $k \neq i$, and fact (a) gives $S_i \to \neg p^*$.
22. The case $\bot$ holds since $\mathsf{PA} \vdash \neg(0 = S0)$.
   For $\psi \to \chi$, use the induction hypothesis for $\psi$ and $\chi$ and the truth table of $\to$, by [[cases|0WCP0PVET6]].
23. Case $i \models \square \psi$.
   Every $j$ with $i R j$ has $j \models \psi$, so $\mathsf{PA} \vdash \bigvee_{i R j} S_j \to \psi^*$ by induction.
   D1 and D2 give $\mathsf{PA} \vdash \square \bigvee_{i R j} S_j \to \square \psi^*$, and fact (c) gives $\mathsf{PA} \vdash S_i \to \square \psi^*$.
24. Case $i \not\models \square \psi$.
   Some $j$ with $i R j$ has $j \not\models \psi$, so $\mathsf{PA} \vdash \psi^* \to \neg S_j$ by induction.
   D1 and D2 give $\mathsf{PA} \vdash \square \psi^* \to \square \neg S_j$, and fact (b) gives $\mathsf{PA} \vdash S_i \to \neg \square \psi^*$.

### Completeness, part 1 of the theorem

25. Assume $\mathsf{GL} \nvdash \varphi$.
   By the [[Kripke completeness of GL|1DMFNR7FZT]], $\varphi$ fails at a world $w$ of a finite transitive irreflexive model.
   Keep only $w$ and its successors, which does not change truth at these worlds.
   Number $w$ as $1$ and the other worlds as $2, \dots, n$.
26. Apply the construction above.
   By step 20, $1 \not\models \varphi$ gives $\mathsf{PA} \vdash S_1 \to \neg \varphi^*$.
27. If $\mathsf{PA} \vdash \varphi^*$, then $\mathsf{PA} \vdash \neg S_1$, against fact (e).
   So $\mathsf{PA} \nvdash \varphi^*$, and with soundness this proves part 1.

### Truth, part 2 of the theorem

Let $X = \bigwedge \{ \square \psi \to \psi : \square \psi \in \mathrm{Sub}(\varphi) \}$.

28. From 2 to 1: $\mathsf{GLS}$ contains $X \to \varphi$ and each conjunct of $X$, so modus ponens gives $\varphi$.
29. From 1 to 3, by induction on the derivation in $\mathsf{GLS}$.
   A theorem of $\mathsf{GL}$ has a realization provable in $\mathsf{PA}$ by soundness, hence true.
   If $\square \psi^*$ is true, then $\mathsf{PA} \vdash \psi^*$, so $\psi^*$ is true.
   Modus ponens preserves truth.
30. From 3 to 2, by contraposition.
   Assume $\mathsf{GL} \nvdash X \to \varphi$.
   As in step 25, get a model with root $1$, $1 \models X$ and $1 \not\models \varphi$, and apply the construction.
31. For $\psi \in \mathrm{Sub}(\varphi)$, $0 \models \psi$ if and only if $1 \models \psi$, by induction on $\psi$.
   Variables hold by step 5, and $\bot$ and $\to$ are direct.
32. For $\square \psi \in \mathrm{Sub}(\varphi)$, the successors of $0$ are $1$ and the successors of $1$.
   So $0 \models \square \psi$ if and only if $1 \models \psi$ and $1 \models \square \psi$.
   Since $1 \models \square \psi \to \psi$, this holds if and only if $1 \models \square \psi$.

### Truth at the new root

33. For $\psi \in \mathrm{Sub}(\varphi)$, if $0 \models \psi$ then $\mathsf{PA} \vdash S_0 \to \psi^*$, and if $0 \not\models \psi$ then $\mathsf{PA} \vdash S_0 \to \neg \psi^*$.
   The proof is by induction as in step 20, and only the case $\square \psi$ is new.
34. Case $0 \models \square \psi$.
   Every $j \geq 1$ has $j \models \psi$, so $\mathsf{PA} \vdash S_j \to \psi^*$ by step 20.
   Also $0 \models \psi$ by steps 32 and 31, so $\mathsf{PA} \vdash S_0 \to \psi^*$ by induction.
   Fact (a) gives $\mathsf{PA} \vdash \psi^*$, and D1 gives $\mathsf{PA} \vdash \square \psi^*$.
35. Case $0 \not\models \square \psi$.
   Some $j \geq 1$ has $j \not\models \psi$, and step 24 with $i = 0$ works, since fact (b) holds for $0 R' j$.
36. Since $1 \not\models \varphi$, step 31 gives $0 \not\models \varphi$, so $\mathsf{PA} \vdash S_0 \to \neg \varphi^*$.
   All theorems of $\mathsf{PA}$ are true and $S_0$ is true by fact (d), so $\varphi^*$ is false in $\mathbb{N}$.

### Other theories, part 3 of the theorem

37. Replace $\mathsf{PA}$ by $T$ in the definition of $h$ and in all steps.
   Steps 1 to 14 and 19 to 27 use only D1, D2, formalized $\Sigma_1$-completeness, the formalized Löb theorem and the cited lemma, and these hold in $T \supseteq \mathsf{PA}$.
   Steps 15 to 18 use only that $T$ is $\Sigma_1$-sound.

## Idea

The theorem reduces to one task: given a finite countermodel, find sentences $S_i$ that behave like its worlds.
Solovay's function $h$ walks up the frame, and it moves to a world $j$ only when it finds a proof that the walk does not end at $j$.
So the walk in fact never leaves $0$, but $\mathsf{PA}$ cannot prove this, and inside $\mathsf{PA}$ each $S_i$ "sees" exactly the $S_j$ with $i R j$.
The new root $0$ is needed because the true world must not prove its own falsity.
In part 2 the root $0$ copies the root $1$, and this works because $1$ satisfies the reflection formulas $\square \psi \to \psi$.

## Variants

A refinement of the construction, with one walk for several provability predicates, gives the arithmetical completeness of [[GLP|3EDRQJJHMT]].
The construction also bounds the complexity of the realization.
By step 9 and fact (a), each $S_i$ is equivalent in $\mathsf{PA}$ to "$h$ reaches $i$ and reaches no $R'$-successor of $i$", a Boolean combination of $\Sigma_1$ sentences.
So every non-theorem of $\mathsf{GL}$ is refuted by a realization whose values are such combinations.
