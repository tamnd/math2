---
tag: DCR0S91GYY
kind: proof
name: Proof of Lindenbaum's lemma by enumeration of sentences
msc: ["03B10", "03C07"]
topics: [FBWW4J1XWG]
audience: ug2
proves: SC0BSJ3GT6
uses: [AVD7T7J063, VM8TQ70CVJ, DKFGQTRYZE, 05006AJ7DZ, 9X08XK5RV2, 01TQB88H4C, 0Y0MQYST0M]
methods: [0ASJVEFA9J, 0J0XBKG64S, 0WCP0PVET6]
sources:
  - book: isbn:9780122384523
    locator: Section 2.4
  - book: isbn:9780122384523
    locator: Section 2.5
  - url: https://builds.openlogicproject.org/
    locator: The Completeness Theorem
---

## Proof

We list all sentences, decide them one at a time, and check that no stage and no union of stages becomes inconsistent.
We use the system $H$ of the [[soundness theorem|AVD7T7J063]] and the definitions of [[Lindenbaum's lemma|SC0BSJ3GT6]].
All sets below are sets of [[sentences|DKFGQTRYZE]] of $L$.

**Step (a): five facts about $H$.**

1. (P1) Finiteness: if $\Gamma \vdash \varphi$, then $\Gamma_0 \vdash \varphi$ for some finite $\Gamma_0 \subseteq \Gamma$.
   A derivation is a finite list, so it uses finitely many members of $\Gamma$.
2. (P2) Monotonicity: if $\Gamma \vdash \varphi$ and $\Gamma \subseteq \Gamma'$, then $\Gamma' \vdash \varphi$.
   A derivation from $\Gamma$ is also a derivation from $\Gamma'$.
3. (P3) Rule T: if $\Gamma \vdash \alpha_1, \dots, \Gamma \vdash \alpha_n$, and every truth assignment that makes $\alpha_1, \dots, \alpha_n$ true makes $\beta$ true, then $\Gamma \vdash \beta$.
   The formula $\alpha_1 \to (\alpha_2 \to \cdots (\alpha_n \to \beta) \cdots)$ is a [[tautology|05006AJ7DZ]], so it is an axiom of group 1, and $n$ uses of [[modus ponens|0Y0MQYST0M]] give $\beta$.
4. (P4) Deduction theorem: if $\Gamma \cup \{ \alpha \} \vdash \beta$, then $\Gamma \vdash \alpha \to \beta$.
   The proof is the induction on derivations of the [[propositional deduction theorem|9X08XK5RV2]].
   It works for $H$ because MP is the only rule of $H$, and the formulas that the induction needs are tautologies, so axioms of group 1.
5. (P5) $\Gamma \cup \{ \neg \sigma \}$ is inconsistent if and only if $\Gamma \vdash \sigma$, and $\Gamma \cup \{ \sigma \}$ is inconsistent if and only if $\Gamma \vdash \neg \sigma$.
6. We prove the first part of (P5).
   Let $\Gamma \cup \{ \neg \sigma \} \vdash \psi$ and $\Gamma \cup \{ \neg \sigma \} \vdash \neg \psi$, so (P4) gives $\Gamma \vdash \neg \sigma \to \psi$ and $\Gamma \vdash \neg \sigma \to \neg \psi$.
7. Every truth assignment that makes $\neg \sigma \to \psi$ and $\neg \sigma \to \neg \psi$ true makes $\sigma$ true, because if $\sigma$ were false then $\psi$ and $\neg \psi$ would both be true.
   So (P3) gives $\Gamma \vdash \sigma$.
8. Conversely, if $\Gamma \vdash \sigma$, then $\Gamma \cup \{ \neg \sigma \}$ derives $\sigma$ by (P2) and $\neg \sigma$ by a one-line derivation, so it is inconsistent.
9. The second part of (P5) is the first part applied to $\neg \sigma$, together with (P3) for the tautologies $\neg \neg \sigma \to \sigma$ and $\sigma \to \neg\neg\sigma$, which show that $\Gamma \cup \{ \sigma \}$ and $\Gamma \cup \{ \neg \neg \sigma \}$ derive the same formulas.

**Step (b): the construction, for a countable $L$.**

10. $L$ has countably many symbols, and each sentence is a finite string of symbols.
    So the set of sentences is [[countable|01TQB88H4C]], and we fix a list $\sigma_0, \sigma_1, \sigma_2, \dots$ of all sentences of $L$.
11. We put $\Delta_0 = \Gamma$.
    For $n \ge 0$, we put $\Delta_{n+1} = \Delta_n \cup \{ \sigma_n \}$ if this set is consistent, and $\Delta_{n+1} = \Delta_n \cup \{ \neg \sigma_n \}$ otherwise.
12. We show by induction on $n$ that each $\Delta_n$ is consistent.
    The set $\Delta_0 = \Gamma$ is consistent by hypothesis.
13. Let $\Delta_n$ be consistent.
    If $\Delta_n \cup \{ \sigma_n \}$ is consistent, then $\Delta_{n+1}$ is this set, and we are done.
    Otherwise (P5) gives $\Delta_n \vdash \neg \sigma_n$.
14. In that second case, suppose $\Delta_n \cup \{ \neg \sigma_n \}$ were inconsistent.
    Then (P5) gives $\Delta_n \vdash \sigma_n$, and with step 13 the set $\Delta_n$ is inconsistent, against the induction hypothesis.
    So $\Delta_{n+1} = \Delta_n \cup \{ \neg \sigma_n \}$ is consistent.
15. We put $\Delta = \bigcup_{n} \Delta_n$, so that $\Gamma = \Delta_0 \subseteq \Delta$.
16. To see that $\Delta$ is consistent, suppose $\Delta \vdash \psi$ and $\Delta \vdash \neg \psi$.
    By (P1) the two derivations use only a finite set $\Delta' \subseteq \Delta$.
17. Each member of $\Delta'$ lies in some $\Delta_n$, and $\Delta_0 \subseteq \Delta_1 \subseteq \cdots$, so $\Delta' \subseteq \Delta_N$ for the largest such index $N$.
    Then (P2) makes $\Delta_N$ inconsistent, against step 12.
18. $\Delta$ is maximal, because each sentence is some $\sigma_n$, and $\sigma_n$ or $\neg \sigma_n$ lies in $\Delta_{n+1} \subseteq \Delta$.

**Step (c): the properties of a maximal consistent set $\Delta$.**
These steps do not use the countability of $L$.

19. Property 1: let $\Delta \vdash \sigma$ and suppose $\sigma \notin \Delta$.
    Maximality gives $\neg \sigma \in \Delta$, so $\Delta \vdash \neg \sigma$ and $\Delta$ is inconsistent, which is impossible.
    Hence $\sigma \in \Delta$.
20. Property 2: maximality gives at least one of $\sigma$ and $\neg \sigma$.
    If both lay in $\Delta$, then $\Delta$ would derive both and be inconsistent.
21. Property 3, the case $\sigma \notin \Delta$: then $\neg \sigma \in \Delta$ by property 2.
    Every truth assignment that makes $\neg \sigma$ true makes $\sigma \to \tau$ true, so (P3) gives $\Delta \vdash \sigma \to \tau$, and property 1 gives $(\sigma \to \tau) \in \Delta$.
22. Property 3, the case $\tau \in \Delta$: every truth assignment that makes $\tau$ true makes $\sigma \to \tau$ true, so (P3) and property 1 give $(\sigma \to \tau) \in \Delta$.
23. Property 3, the remaining case $\sigma \in \Delta$ and $\tau \notin \Delta$: if $(\sigma \to \tau) \in \Delta$, then MP gives $\Delta \vdash \tau$, and property 1 gives $\tau \in \Delta$, a contradiction.
    So $(\sigma \to \tau) \notin \Delta$, and steps 21 to 23 prove property 3.
24. Property 4: let $\forall x \, \varphi \in \Delta$ and let $t$ be a closed term.
    A closed term has no variables, so it is substitutable for $x$ in $\varphi$, and $\forall x \, \varphi \to \varphi^x_t$ is an axiom of group 2.
25. MP gives $\Delta \vdash \varphi^x_t$.
    The formula $\varphi^x_t$ is a sentence, because $x$ is the only variable that can be free in $\varphi$ and $t$ is closed, so property 1 gives $\varphi^x_t \in \Delta$.
26. Property 5, first part: let $\Delta \subsetneq \Delta''$, and pick a sentence $\sigma \in \Delta'' \setminus \Delta$.
    Property 2 gives $\neg \sigma \in \Delta \subseteq \Delta''$, so $\Delta''$ contains $\sigma$ and $\neg \sigma$ and is inconsistent.
27. Property 5, second part: let $\Delta$ be consistent with no consistent proper superset, and suppose $\sigma \notin \Delta$ and $\neg \sigma \notin \Delta$.
    Then $\Delta \cup \{ \sigma \}$ and $\Delta \cup \{ \neg \sigma \}$ are proper supersets, so both are inconsistent.
28. By (P5), $\Delta \vdash \neg \sigma$ and $\Delta \vdash \sigma$, so $\Delta$ is inconsistent.
    This contradiction shows that $\Delta$ is maximal consistent.

## Idea

We walk through a list of all sentences and decide each one in turn.
A sentence goes in when it keeps the set consistent, and otherwise its negation goes in.
Fact (P5) is what makes this safe: if both choices failed, the set before the step would already be inconsistent.
At the end, a contradiction in the union would use only finitely many sentences, so it would already appear at a finite stage, and no finite stage has one.

## Variants

For an uncountable $L$, the [[proof by Zorn's lemma|6F5F3GN6SJ]] replaces the list by a maximality argument.
We can also well-order the sentences and run the same construction by transfinite recursion, taking unions at limit stages.
The [[propositional version|GNPVCQC55C]] is the same construction for propositional formulas.
The construction is not effective: whether $\Delta_n \cup \{ \sigma_n \}$ is consistent is not a computable question in first-order logic, by [[Church's theorem|VA6BNNY2YC]].
