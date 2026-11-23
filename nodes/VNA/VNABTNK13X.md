---
tag: VNABTNK13X
kind: proof
name: Proof of Robinson's joint consistency theorem by a joint Henkin construction
msc: ["03C07", "03C40"]
topics: [FBWW4J1XWG]
audience: grad
proves: R6AN38DNBD
uses: [RY8KRKR097, FMZMD0GGYK, DCR0S91GYY, SC0BSJ3GT6, WQ1ZE255SF, AVD7T7J063, DKFGQTRYZE, 983GZBQYT4, 01TQB88H4C]
methods: [0J0XBKG64S, 0ASJVEFA9J, 0NTF6DMVAP]
sources:
  - url: https://builds.openlogicproject.org/
    locator: Interpolation
  - url: https://en.wikipedia.org/wiki/Robinson%27s_joint_consistency_theorem
    locator: lead section
---

## Proof

We run the Henkin construction on both sides at once, keep the two sides inseparable at every stage, and glue the two term models along an isomorphism of their common parts.

We prove part 1 for countable $L_1$ and $L_2$, and part 2 follows from part 1, as the statement shows.
We write $\varphi(c)$ for $\varphi^x_c$ when $x$ is clear.
By the [[soundness theorem|AVD7T7J063]] and [[Gödel's completeness theorem|WQ1ZE255SF]], $\Delta \vdash \sigma$ if and only if $\Delta \models \sigma$ for sets of sentences, and we use both forms.

**Step (a): inseparable pairs.**

1. Let $C = \{ c_0, c_1, \dots \}$ be new constants, and put $L_i(C) = L_i \cup C$ for $i = 0, 1, 2$.
   Then $L_1(C) \cap L_2(C) = L_0(C)$.
2. A pair $(\Gamma', \Sigma')$ of sets of sentences of $L_1(C)$ and $L_2(C)$ is inseparable when no sentence of $L_0(C)$ separates $\Gamma'$ from $\Sigma'$.
3. If $(\Gamma', \Sigma')$ is inseparable, then $\Gamma'$ is consistent.
   Otherwise $\Gamma' \vdash \neg \forall x \, (x = x)$, while $\Sigma' \vdash \neg \neg \forall x \, (x = x)$ always holds, so $\neg \forall x \, (x = x)$ would separate them.
4. In the same way $\Sigma'$ is consistent, with the separating sentence $\forall x \, (x = x)$.

**Step (b): the start pair $(\Gamma, \Sigma)$ is inseparable in $L_0(C)$.**

5. Suppose an $L_0(C)$-sentence separates $\Gamma$ from $\Sigma$.
   We write it as $\theta(c_{i_1}, \dots, c_{i_k})$, where $\theta(x_1, \dots, x_k)$ is an $L_0$-formula without symbols of $C$.
6. Let $\mathcal{A}$ be an $L_1(C)$-structure that is a model of $\Gamma$, and let $a_1, \dots, a_k$ be elements of $\mathcal{A}$.
   We change the interpretation of each $c_{i_j}$ to $a_j$, and the new structure is still a model of $\Gamma$, since $\Gamma$ has no symbols of $C$.
7. So the new structure satisfies $\theta(c_{i_1}, \dots, c_{i_k})$, and $\mathcal{A} \models \theta[a_1, \dots, a_k]$.
   Hence $\Gamma \models \forall x_1 \cdots \forall x_k \, \theta$.
8. By completeness, $\Gamma \vdash \forall \bar x \, \theta$.
   Axiom group 2, used $k$ times with Rule T, gives $\vdash \forall \bar x \, \theta \to \theta(c_{i_1}, \dots, c_{i_k})$, and with $\Sigma \vdash \neg \theta(c_{i_1}, \dots, c_{i_k})$ Rule T gives $\Sigma \vdash \neg \forall \bar x \, \theta$.
9. So the $L_0$-sentence $\forall \bar x \, \theta$ separates $\Gamma$ from $\Sigma$, which contradicts the hypothesis.

**Step (c): two lemmas.** Let $(\Gamma', \Sigma')$ be inseparable.

10. Lemma A: for each sentence $\alpha$ of $L_1(C)$, one of the pairs $(\Gamma' \cup \{ \alpha \}, \Sigma')$ and $(\Gamma' \cup \{ \neg \alpha \}, \Sigma')$ is inseparable.
11. To prove Lemma A, suppose $\theta_1$ separates the first pair and $\theta_2$ separates the second.
    The deduction theorem gives $\Gamma' \vdash \alpha \to \theta_1$ and $\Gamma' \vdash \neg \alpha \to \theta_2$.
12. Rule T gives $\Gamma' \vdash \theta_1 \lor \theta_2$ and $\Sigma' \vdash \neg (\theta_1 \lor \theta_2)$.
    So $\theta_1 \lor \theta_2$ separates $\Gamma'$ from $\Sigma'$, a contradiction.
13. Lemma B: let $\neg \forall x \, \varphi \in \Gamma'$, and let $c \in C$ occur neither in $\Gamma'$ nor in $\Sigma'$.
    Then $(\Gamma' \cup \{ \neg \varphi(c) \}, \Sigma')$ is inseparable.
14. To prove Lemma B, suppose $\theta(c)$ separates the new pair, where $\theta(y)$ is an $L_0(C)$-formula without $c$.
    We show that $\exists y \, \theta$ separates $\Gamma'$ from $\Sigma'$.
15. Let $\mathcal{A} \models \Gamma'$.
    Since $\mathcal{A} \models \neg \forall x \, \varphi$, some $a$ has $\mathcal{A} \models \neg \varphi[a]$, and we change the interpretation of $c$ to $a$.
16. The new structure satisfies $\Gamma' \cup \{ \neg \varphi(c) \}$, since $c$ is not in $\Gamma'$.
    So it satisfies $\theta(c)$, and $\mathcal{A} \models \exists y \, \theta$, which gives $\Gamma' \models \exists y \, \theta$.
17. Let $\mathcal{B} \models \Sigma'$ and $b \in \mathcal{B}$, and change the interpretation of $c$ to $b$.
    The new structure satisfies $\Sigma'$, so it satisfies $\neg \theta(c)$, and hence $\mathcal{B} \models \neg \exists y \, \theta$.
18. By completeness, $\Gamma' \vdash \exists y \, \theta$ and $\Sigma' \vdash \neg \exists y \, \theta$, a contradiction.
19. Lemmas A and B hold with the roles of $\Gamma'$ and $\Sigma'$ exchanged, by the same proofs.

**Step (d): the construction.**

20. The sentences of $L_1(C)$ and of $L_2(C)$ form [[countable|01TQB88H4C]] sets, and we list them as $\alpha_0, \alpha_1, \dots$ and $\beta_0, \beta_1, \dots$.
21. We put $\Gamma_0 = \Gamma$ and $\Sigma_0 = \Sigma$.
    At each stage only finitely many sentences have been added, so only finitely many constants of $C$ occur.
22. At stage $n$, on side 1, Lemma A lets us add $\alpha_n$ or $\neg \alpha_n$ to $\Gamma_n$ so that the pair stays inseparable.
    If the added sentence is $\neg \forall x \, \varphi$, we also add $\neg \varphi(c)$ for the first $c \in C$ that occurs in no sentence of the current pair, and Lemma B keeps the pair inseparable.
23. On side 2 we do the same with $\beta_n$ and $\Sigma_n$.
    The result is an inseparable pair $(\Gamma_{n+1}, \Sigma_{n+1})$.
24. We put $\Gamma^* = \bigcup_n \Gamma_n$ and $\Sigma^* = \bigcup_n \Sigma_n$.
    A separating sentence would have derivations from finitely many sentences, all in some $(\Gamma_n, \Sigma_n)$, so $(\Gamma^*, \Sigma^*)$ is inseparable.

**Step (e): properties of $\Gamma^*$ and $\Sigma^*$.**

25. By step 3, $\Gamma^*$ is consistent, and by step 22 it contains $\alpha$ or $\neg \alpha$ for each $L_1(C)$-sentence $\alpha$.
    So $\Gamma^*$ is maximal consistent in $L_1(C)$.
26. Let $\neg \forall x \, \varphi \in \Gamma^*$.
    It is some $\alpha_n$, and $\alpha_n$ was the sentence added at stage $n$, since $\neg \alpha_n \notin \Gamma^*$, so its witness was added too.
    Hence $\Gamma^*$ has the witness property of the [[Henkin construction|RY8KRKR097]], and in the same way $\Sigma^*$ has it in $L_2(C)$.
27. The two sets agree on $L_0(C)$.
    If an $L_0(C)$-sentence $\theta$ had $\theta \in \Gamma^*$ and $\theta \notin \Sigma^*$, then $\neg \theta \in \Sigma^*$, and $\theta$ would separate them.
28. Symmetrically, $\theta \in \Sigma^*$ with $\theta \notin \Gamma^*$ is impossible.
    So $\theta \in \Gamma^*$ if and only if $\theta \in \Sigma^*$.

**Step (f): the term models.**

29. Let $\mathcal{M}_1$ and $\mathcal{M}_2$ be the term models of $\Gamma^*$ and $\Sigma^*$, built as in the [[proof of model existence|FMZMD0GGYK]].
    By the truth lemma there, $\mathcal{M}_1 \models \Gamma^*$ and $\mathcal{M}_2 \models \Sigma^*$.
30. Every element of $\mathcal{M}_1$ is $[c]_1$ for some $c \in C$.
    Indeed, for a closed term $t$ we have $\vdash \neg \forall x \, \neg (x = t)$, so this sentence lies in $\Gamma^*$.
31. Its witness $c$ gives $\neg \neg (c = t) \in \Gamma^*$, so $(c = t) \in \Gamma^*$ by deductive closure, and $[t]_1 = [c]_1$.
    The same holds for $\mathcal{M}_2$.
32. We define $h([c]_1) = [c]_2$ for $c \in C$.
    By step 28 with $\theta = (c = d)$, $[c]_1 = [d]_1$ if and only if $[c]_2 = [d]_2$, so $h$ is well defined and injective.
33. By step 31 for $\mathcal{M}_2$, $h$ is onto, so $h$ is a bijection from $\mathcal{M}_1$ to $\mathcal{M}_2$.
34. For a relation symbol $R$ of $L_0$, step 28 gives $R^{\mathcal{M}_1}([c_1]_1, \dots)$ if and only if $R(c_1, \dots) \in \Gamma^*$, if and only if $R(c_1, \dots) \in \Sigma^*$, if and only if $R^{\mathcal{M}_2}([c_1]_2, \dots)$.
35. For a function symbol $f$ of $L_0$, step 31 gives $d \in C$ with $f(c_1, \dots, c_n) = d$ in $\Gamma^*$, and by step 28 it also lies in $\Sigma^*$.
    So $h$ sends $f^{\mathcal{M}_1}([c_1]_1, \dots)$ to $f^{\mathcal{M}_2}([c_1]_2, \dots)$.
36. Constant symbols of $L_0(C)$ are the case $n = 0$ of step 35.
    So $h$ is an isomorphism of the reducts of $\mathcal{M}_1$ and $\mathcal{M}_2$ to $L_0(C)$.

**Step (g): the joint model.**

37. We define a [[structure|983GZBQYT4]] $\mathcal{N}$ for $L_1 \cup L_2 \cup C$ with the universe of $\mathcal{M}_1$, and we interpret the symbols of $L_1(C)$ as in $\mathcal{M}_1$.
38. A symbol of $L_2$ outside $L_0$ is carried over from $\mathcal{M}_2$ by $h$.
    We put $R^{\mathcal{N}}(\bar a)$ if and only if $R^{\mathcal{M}_2}(h(\bar a))$, and $f^{\mathcal{N}}(\bar a) = h^{-1}(f^{\mathcal{M}_2}(h(\bar a)))$.
39. For symbols of $L_0(C)$ the two definitions agree, by step 36.
    So the reduct of $\mathcal{N}$ to $L_1(C)$ is $\mathcal{M}_1$, and $h$ is an isomorphism from the reduct to $L_2(C)$ onto $\mathcal{M}_2$.
40. Hence $\mathcal{N} \models \Gamma^* \supseteq \Gamma$.
    Isomorphic structures satisfy the same sentences, so $\mathcal{N} \models \Sigma^* \supseteq \Sigma$.
41. The reduct of $\mathcal{N}$ to $L_1 \cup L_2$ is a model of $\Gamma \cup \Sigma$, and by soundness $\Gamma \cup \Sigma$ is consistent.

## Idea

We run the Henkin construction on both sides at once, with one invariant: no sentence in the common language separates the two sides.
At the end both sides are Henkin sets, and they agree on every sentence in the common language with the new constants.
The new constants name every element on both sides, so this agreement gives an isomorphism of the common reducts.
Then the two term models glue into one structure for the joint language.
In the example with an order, a coloring $P$ on side 1 and a function $f$ on side 2, the glued model is one order whose points carry both the color and the function.

## Variants

For uncountable languages we list the sentences in a well-ordered sequence and use transfinite recursion.
Lemma B then needs a supply of unused constants at each stage, so we take $|C| = |L_1| + |L_2| + \aleph_0$.

A model-theoretic proof uses compactness and elementary chains.
It alternates between models of the two sides, with elementary embeddings in $L_0$, and the union of the chain is a model of $\Gamma \cup \Sigma$.

The [[proof from Craig's theorem|V36AHEN7ZE]] is short, but it uses interpolation, which is itself proved from Robinson's theorem or from cut elimination.
