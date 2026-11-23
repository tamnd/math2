---
tag: FMZMD0GGYK
kind: proof
name: Proof of the model existence theorem by the Henkin construction
msc: ["03B10", "03C07"]
topics: [FBWW4J1XWG]
audience: ug2
proves: G0DTR159RN
uses: [AVD7T7J063, SC0BSJ3GT6, DCR0S91GYY, RY8KRKR097, VM8TQ70CVJ, DKFGQTRYZE, 6D3WA7N2W4, 983GZBQYT4, 2RBQPV02AS, 01TQB88H4C, NCDZ969V7X, A7S460KHBM]
methods: [0J0XBKG64S, 12MQ2NJ29A, 0KMVFSHFGZ, 0WCP0PVET6, RGNF33GVHX]
sources:
  - book: isbn:9780122384523
    locator: Section 2.4
  - book: isbn:9780122384523
    locator: Section 2.5
  - url: https://builds.openlogicproject.org/
    locator: The Completeness Theorem
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_completeness_theorem
    locator: Model existence theorem
---

## Proof

We add witness constants, extend to a maximal consistent set, build the term model, and prove the truth lemma by induction on sentences.
Let $L$ be a countable first-order language with equality, and let $\Gamma$ be a [[consistent|VM8TQ70CVJ]] set of [[sentences|DKFGQTRYZE]] of $L$.
We build a model of $\Gamma$ with a countable universe, by the [[Henkin construction|RY8KRKR097]].
Derivability $\vdash$ is in the Hilbert system $H$ of the [[soundness theorem|AVD7T7J063]], for the language named in each step.
For a formula $\varphi$, we write $n(\varphi)$ for the number of occurrences of $\neg$, $\to$ and $\forall$ in $\varphi$.

**Step (a): facts about $H$.**
We use the facts (P1) to (P5) of the [[proof of Lindenbaum's lemma|DCR0S91GYY]] and four more facts, (P6) to (P9).
The proofs of (P6) and (P7) are inductions on derivations, as in Enderton, Section 2.4.

1. (P6) Generalization theorem: if $\Sigma \vdash \varphi$ and the variable $x$ is not free in any member of $\Sigma$, then $\Sigma \vdash \forall x \, \varphi$.
   The induction uses the axioms of groups 3 and 4, and the fact that a generalization of an axiom is an axiom.
2. (P7) Constant replacement: let $D$ be a derivation of $\varphi$ from $\Sigma$, where the constant $c$ does not occur in $\Sigma$, and let $y$ be a variable that does not occur in $D$.
   Replacing $c$ by $y$ everywhere in $D$ gives a derivation of $\varphi^c_y$ from $\Sigma$, because each axiom becomes an axiom of the same group and the members of $\Sigma$ do not change.
3. (P8) Generalization on constants: let $\Sigma$ be a set of sentences, and let $c$ be a constant that occurs neither in $\Sigma$ nor in $\varphi$.
   If $\Sigma \vdash \varphi^x_c$, then $\Sigma \vdash \forall x \, \varphi$.
4. To prove (P8), take a derivation of $\varphi^x_c$ and a variable $y$ that does not occur in it.
   By (P7), $\Sigma \vdash \varphi^x_y$, since $c$ does not occur in $\varphi$.
5. The members of $\Sigma$ are sentences, so (P6) gives $\Sigma \vdash \forall y \, \varphi^x_y$.
6. The variable $y$ does not occur in $\varphi$, so $(\varphi^x_y)^y_x = \varphi$, and $x$ is substitutable for $y$ in $\varphi^x_y$, because the occurrences of $y$ stand where $x$ was free.
   So group 2 gives the axiom $\forall y \, \varphi^x_y \to \varphi$, and MP gives $\Sigma \vdash \varphi$.
7. Then (P6) gives $\Sigma \vdash \forall x \, \varphi$, since $x$ is not free in the sentences of $\Sigma$.
8. (P9) Equality: let $t, u, w, t_i, u_i$ be closed terms, $f$ an $n$-ary function symbol and $P$ an $n$-ary relation symbol.
   Then (i) $\vdash t = t$, (ii) $t = u \vdash u = t$, (iii) $t = u, u = w \vdash t = w$, (iv) $t_1 = u_1, \dots, t_n = u_n \vdash f t_1 \dots t_n = f u_1 \dots u_n$, and (v) $t_1 = u_1, \dots, t_n = u_n, P t_1 \dots t_n \vdash P u_1 \dots u_n$.
9. In the proof of (P9) we instantiate generalized axioms with closed terms.
   A closed term has no variables, so it is substitutable for every variable, and group 2 with MP removes one quantifier $\forall x$ at a time.
10. For (i): $\forall x \, (x = x)$ is a generalization of an axiom of group 5, so it is an axiom, and we instantiate $x$ by $t$.
11. For (ii): take the axiom of group 6 with $\alpha = (x = x)$ and $\alpha' = (y = x)$, where only the first occurrence of $x$ is replaced.
    Its generalization over $x, y$, instantiated with $t, u$, gives $\vdash t = u \to (t = t \to u = t)$, and (i) with MP twice gives $t = u \vdash u = t$.
12. For (iii): take the axiom of group 6 with $\alpha = (x = z)$ and $\alpha' = (y = z)$, and instantiate $x, y, z$ by $u, t, w$ to get $\vdash u = t \to (u = w \to t = w)$.
    From $t = u$, (ii) gives $u = t$, and MP twice gives $t = w$.
13. For (iv): for $i = 1, \dots, n$, take the axiom of group 6 with $\alpha = (z = f v_1 \dots v_{i-1} x v_{i+1} \dots v_n)$, and $\alpha'$ the same with this $x$ replaced by $y$.
    Instantiate $z$ by $f t_1 \dots t_n$, $v_j$ by $u_j$ for $j < i$, $v_j$ by $t_j$ for $j > i$, $x$ by $t_i$ and $y$ by $u_i$.
14. With MP and $t_i = u_i$, step 13 turns $f t_1 \dots t_n = f u_1 \dots u_{i-1} t_i \dots t_n$ into $f t_1 \dots t_n = f u_1 \dots u_i t_{i+1} \dots t_n$.
    We start from (i) and apply this for $i = 1, \dots, n$, and the last formula is (iv).
15. For (v): in the same way, the axiom of group 6 with $\alpha = P v_1 \dots v_{i-1} x v_{i+1} \dots v_n$ replaces $t_i$ by $u_i$ in one place.
    Starting from $P t_1 \dots t_n$, $n$ such steps give $P u_1 \dots u_n$.

**Step (b): new constants keep consistency.**

16. Let $C = \{ c_0, c_1, c_2, \dots \}$ be countably many new constant symbols, and let $L^+ = L \cup C$.
17. We claim that $\Gamma$ is consistent in $L^+$.
    Suppose not; then $\Gamma \vdash \neg \forall x \, (x = x)$ in $L^+$, since an inconsistent set derives every formula by (P3).
18. Take such a derivation $D$.
    It uses finitely many constants $c_{i_1}, \dots, c_{i_k}$ of $C$, and we replace them by distinct variables that do not occur in $D$.
19. The sentences of $\Gamma$ and the sentence $\neg \forall x \, (x = x)$ contain no symbol of $C$.
    So by (P7), used $k$ times, the result is a derivation in $L$ of $\neg \forall x \, (x = x)$ from $\Gamma$.
20. Also $\vdash \forall x \, (x = x)$ in $L$, by step 10, so $\Gamma$ is inconsistent in $L$, against the hypothesis.

**Step (c): the witness sentences.**

21. Consider the pairs $(\varphi, x)$ of a formula $\varphi$ of $L^+$ and a variable $x$ such that no variable other than $x$ is free in $\varphi$.
    Since $L^+$ is countable, these pairs form a countable set, and we list them as $(\varphi_0, x_0), (\varphi_1, x_1), \dots$.
22. Let $d_n$ be the first constant in the list $c_0, c_1, \dots$ that occurs in none of $\varphi_0, \dots, \varphi_n$ and differs from $d_0, \dots, d_{n-1}$.
    It exists, because these finitely many formulas contain finitely many constants of $C$.
23. Let $\theta_n$ be the sentence $\neg \forall x_n \, \varphi_n \to \neg (\varphi_n)^{x_n}_{d_n}$, and let $\Theta = \{ \theta_0, \theta_1, \dots \}$.
24. The constant $d_m$ does not occur in $\theta_0, \dots, \theta_{m-1}$.
    Indeed, $\theta_k$ contains only the symbols of $\varphi_k$ and $d_k$, and step 22 gives $d_m \notin \varphi_k$ and $d_m \ne d_k$ for $k < m$.

**Step (d): $\Gamma \cup \Theta$ is consistent in $L^+$.**

25. Suppose not.
    By (P1) and (P2), some set $\Gamma \cup \{ \theta_0, \dots, \theta_m \}$ is inconsistent, and we take the least such $m$.
26. Put $\Gamma' = \Gamma \cup \{ \theta_0, \dots, \theta_{m-1} \}$.
    It is consistent, by step (b) when $m = 0$ and by the choice of $m$ when $m > 0$.
27. Write $\varphi, x, d$ for $\varphi_m, x_m, d_m$.
    Since $\Gamma' \cup \{ \theta_m \}$ is inconsistent, (P5) gives $\Gamma' \vdash \neg \theta_m$.
28. Every truth assignment that makes $\neg(A \to B)$ true makes $A$ true and $B$ false.
    So (P3) gives $\Gamma' \vdash \neg \forall x \, \varphi$ and $\Gamma' \vdash \neg \neg \varphi^x_d$, and then $\Gamma' \vdash \varphi^x_d$.
29. The constant $d$ occurs neither in $\Gamma$, whose sentences are in $L$, nor in $\theta_0, \dots, \theta_{m-1}$, by step 24, nor in $\varphi$, by step 22.
    The members of $\Gamma'$ are sentences.
30. So (P8) gives $\Gamma' \vdash \forall x \, \varphi$, and with step 28 the set $\Gamma'$ is inconsistent, which contradicts step 26.

**Step (e): a maximal consistent Henkin set.**

31. [[Lindenbaum's lemma|SC0BSJ3GT6]] for the countable language $L^+$ gives a maximal consistent set $\Delta$ of sentences of $L^+$ with $\Gamma \cup \Theta \subseteq \Delta$.
32. For the witness property, let $\neg \forall x \, \varphi \in \Delta$, where no variable other than $x$ is free in $\varphi$.
    Then $(\varphi, x) = (\varphi_n, x_n)$ for some $n$, and $\theta_n \in \Delta$.
33. Property 3 of Lindenbaum's lemma, applied to $\theta_n$, gives $\neg \varphi^x_{d_n} \in \Delta$.
    So every sentence $\neg \forall x \, \varphi$ in $\Delta$ has a witness constant in $\Delta$.

**Step (f): the term model.**

34. Let $T$ be the set of closed [[terms|6D3WA7N2W4]] of $L^+$, which is not empty since $c_0 \in T$.
    For $t, u \in T$, we put $t \sim u$ when $(t = u) \in \Delta$.
35. The relation $\sim$ is an equivalence relation.
    By (P9)(i), (ii), (iii) and the deductive closure of $\Delta$ (property 1 of Lindenbaum's lemma), $\Delta$ contains $t = t$, contains $u = t$ when it contains $t = u$, and contains $t = w$ when it contains $t = u$ and $u = w$.
36. The relation $\sim$ is a congruence: if $t_i \sim u_i$ for $i = 1, \dots, n$, then (P9)(iv) and deductive closure give $f t_1 \dots t_n \sim f u_1 \dots u_n$.
37. Also, if $t_i \sim u_i$ for all $i$, then $P t_1 \dots t_n \in \Delta$ if and only if $P u_1 \dots u_n \in \Delta$.
    This follows from (P9)(v), used in both directions with (P9)(ii), and deductive closure.
38. We write $[t]$ for the class of $t$ and $M = T / {\sim}$, and we define a [[structure|983GZBQYT4]] $\mathcal{M}$ for $L^+$ with universe $M$ as follows.
39. For a constant symbol $c$, we put $c^{\mathcal{M}} = [c]$.
    For a function symbol $f$, we put $f^{\mathcal{M}}([t_1], \dots, [t_n]) = [f t_1 \dots t_n]$, which does not depend on the representatives by step 36.
40. For a relation symbol $P$, we let $P^{\mathcal{M}}$ be the set of tuples $([t_1], \dots, [t_n])$ with $P t_1 \dots t_n \in \Delta$, which does not depend on the representatives by step 37.
    The symbol $=$ means identity on $M$, as in every structure.
41. Every closed term $t$ has the value $t^{\mathcal{M}} = [t]$, by induction on $t$.
    For a constant this is step 39, and for $t = f t_1 \dots t_n$ the induction hypothesis and step 39 give $t^{\mathcal{M}} = f^{\mathcal{M}}([t_1], \dots, [t_n]) = [t]$.
42. So every element of $M$ is the value of a closed term.

**Step (g): the truth lemma.**
For every sentence $\sigma$ of $L^+$, we show that $\mathcal{M} \models \sigma$ if and only if $\sigma \in \Delta$.

43. We use [[strong induction|0KMVFSHFGZ]] on $n(\sigma)$, for all sentences at once.
    The substitution of a closed term does not change $n$, that is, $n(\varphi^x_t) = n(\varphi)$.
44. Case $\sigma = (t = u)$: by step 41 and the definition of satisfaction, $\mathcal{M} \models t = u$ iff $[t] = [u]$ iff $t \sim u$ iff $(t = u) \in \Delta$.
45. Case $\sigma = P t_1 \dots t_n$: by step 41, $\mathcal{M} \models \sigma$ iff $([t_1], \dots, [t_n]) \in P^{\mathcal{M}}$, iff $P t_1 \dots t_n \in \Delta$ by step 40.
46. Case $\sigma = \neg \tau$: $\mathcal{M} \models \neg \tau$ iff $\mathcal{M} \not\models \tau$, iff $\tau \notin \Delta$ by the induction hypothesis, iff $\neg \tau \in \Delta$ by property 2 of Lindenbaum's lemma.
47. Case $\sigma = (\tau \to \rho)$: $\mathcal{M} \models \sigma$ iff $\mathcal{M} \not\models \tau$ or $\mathcal{M} \models \rho$, iff $\tau \notin \Delta$ or $\rho \in \Delta$ by the induction hypothesis, iff $\sigma \in \Delta$ by property 3.
48. Case $\sigma = \forall x \, \varphi$, where no variable other than $x$ is free in $\varphi$.
    By the definition of [[satisfaction|2RBQPV02AS]], $\mathcal{M} \models \sigma$ iff $\mathcal{M} \models \varphi[x \mapsto a]$ for every $a \in M$.
49. By step 42, each $a$ is $t^{\mathcal{M}}$ for a closed $t$.
    The [[substitution lemma|A7S460KHBM]] gives $\mathcal{M} \models \varphi[x \mapsto t^{\mathcal{M}}]$ iff $\mathcal{M} \models \varphi^x_t$, because a closed $t$ is substitutable.
50. So $\mathcal{M} \models \sigma$ iff $\mathcal{M} \models \varphi^x_t$ for every closed $t$.
    Since $n(\varphi^x_t) < n(\sigma)$, the induction hypothesis turns this into "$\varphi^x_t \in \Delta$ for every closed term $t$".
51. If $\forall x \, \varphi \in \Delta$, then $\varphi^x_t \in \Delta$ for every closed $t$, by property 4 of Lindenbaum's lemma.
52. If $\forall x \, \varphi \notin \Delta$, then $\neg \forall x \, \varphi \in \Delta$ by property 2.
    The witness property of step 33 gives a constant $d$ with $\neg \varphi^x_d \in \Delta$, so $\varphi^x_d \notin \Delta$ by property 2.
53. Steps 51 and 52 show that $\forall x \, \varphi \in \Delta$ iff $\varphi^x_t \in \Delta$ for every closed $t$.
    With step 50, $\mathcal{M} \models \sigma$ iff $\sigma \in \Delta$, which ends the induction.

**Step (h): the conclusion.**

54. Let $\mathcal{M}_0$ be the reduct of $\mathcal{M}$ to $L$: the same universe and the same interpretations of the symbols of $L$, with the constants of $C$ forgotten.
55. Satisfaction of an $L$-sentence uses only the symbols of $L$, so $\mathcal{M}_0 \models \sigma$ iff $\mathcal{M} \models \sigma$ for every sentence $\sigma$ of $L$, by induction on formulas.
56. Every $\gamma \in \Gamma$ lies in $\Delta$, so $\mathcal{M} \models \gamma$ by the truth lemma, and $\mathcal{M}_0 \models \gamma$ by step 55.
    Hence $\mathcal{M}_0$ is a model of $\Gamma$.
57. The set $T$ consists of finite strings over the countable alphabet of $L^+$, so it is [[countable|01TQB88H4C]].
    The map $t \mapsto [t]$ sends $T$ onto $M$, so $M$ is finite or countably infinite.
58. Hence every consistent set of sentences of a countable language has a model with a countable universe, which proves the theorem for countable $L$.

## Idea

A model must be built from syntax alone, so its elements are the closed terms, and two terms name the same element when the theory says that they are equal.
For this to work, the theory must decide every sentence, which Lindenbaum's lemma arranges, and it must name a witness for every existential sentence, which the Henkin constants arrange.
Then the truth lemma, an induction on sentences, shows that the term model makes true exactly the sentences of the theory.
The witnesses are used in one place only, the case $\forall x \, \varphi$ of the truth lemma, and step 52 is where they do their work.

## Variants

For an uncountable language of cardinality $\kappa$, we add $\kappa$ new constants, well-order the pairs $(\varphi, x)$ in type $\kappa$, and choose the witnesses by transfinite recursion.
Lindenbaum's lemma in the form of the [[proof by Zorn's lemma|6F5F3GN6SJ]] finishes the proof, the model has at most $\kappa$ elements, and the axiom of choice is used.

In an interleaved form, we decide the sentences one at a time and add a witness $\neg \varphi^x_d$ right after each $\neg \forall x \, \varphi$ that goes in.
The [[joint Henkin proof of Robinson's joint consistency theorem|VNABTNK13X]] uses this form.
In a language without equality the relation $\sim$ is not needed, and the universe is the set $T$ itself.
Hasenjaeger gave a simplified form of the argument in 1953, and Rasiowa and Sikorski gave an algebraic form with ultrafilters of the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]].
