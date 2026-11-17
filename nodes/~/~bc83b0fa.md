---
tag: ~bc83b0fa
kind: proof
name: Proof of Lindenbaum's lemma by enumeration of sentences
msc: ["03B10", "03C07"]
topics: [FBWW4J1XWG]
audience: ug2
proves: ~8ecc8dc7
uses: [~331f6430, VM8TQ70CVJ, DKFGQTRYZE, 05006AJ7DZ, 9X08XK5RV2, 01TQB88H4C, 0Y0MQYST0M]
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

We use the system $H$ of the [[soundness theorem|~331f6430]] and the definitions of the [[statement|~8ecc8dc7]].
All sets below are sets of [[sentences|DKFGQTRYZE]] of $L$.

Step (a): five facts about $H$.

1. (P1) Finiteness: if $\Gamma \vdash \varphi$, then $\Gamma_0 \vdash \varphi$ for some finite $\Gamma_0 \subseteq \Gamma$. A derivation is a finite list, so it uses finitely many members of $\Gamma$.
2. (P2) Monotonicity: if $\Gamma \vdash \varphi$ and $\Gamma \subseteq \Gamma'$, then $\Gamma' \vdash \varphi$. A derivation from $\Gamma$ is a derivation from $\Gamma'$.
3. (P3) Rule T: if $\Gamma \vdash \alpha_1, \dots, \Gamma \vdash \alpha_n$, and every truth assignment that makes $\alpha_1, \dots, \alpha_n$ true makes $\beta$ true, then $\Gamma \vdash \beta$. The formula $\alpha_1 \to (\alpha_2 \to \cdots (\alpha_n \to \beta) \cdots)$ is a [[tautology|05006AJ7DZ]], so it is an axiom of group 1, and $n$ uses of [[modus ponens|0Y0MQYST0M]] give $\beta$.
4. (P4) Deduction theorem: if $\Gamma \cup \set{\alpha} \vdash \beta$, then $\Gamma \vdash \alpha \to \beta$. The proof is the induction on derivations of the [[propositional deduction theorem|9X08XK5RV2]]. It works for $H$ because MP is the only rule of $H$ and the formulas it needs are tautologies, so axioms of group 1.
5. (P5) $\Gamma \cup \set{\neg \sigma}$ is inconsistent if and only if $\Gamma \vdash \sigma$. Also, $\Gamma \cup \set{\sigma}$ is inconsistent if and only if $\Gamma \vdash \neg \sigma$.
6. Proof of the first part of (P5). Let $\Gamma \cup \set{\neg \sigma} \vdash \psi$ and $\Gamma \cup \set{\neg \sigma} \vdash \neg \psi$. By (P4), $\Gamma \vdash \neg \sigma \to \psi$ and $\Gamma \vdash \neg \sigma \to \neg \psi$.
7. Every assignment that makes $\neg \sigma \to \psi$ and $\neg \sigma \to \neg \psi$ true makes $\sigma$ true: if $\sigma$ were false, $\psi$ and $\neg \psi$ would both be true. So (P3) gives $\Gamma \vdash \sigma$.
8. Conversely, if $\Gamma \vdash \sigma$, then $\Gamma \cup \set{\neg \sigma}$ derives $\sigma$ by (P2) and $\neg \sigma$ by a one-line derivation, so it is inconsistent.
9. The second part of (P5) is the same argument with $\neg \sigma$ in place of $\sigma$. It uses that $\neg \neg \sigma \to \sigma$ and $\sigma \to \neg\neg\sigma$ are tautologies, with (P3).

Step (b): the construction, for a countable $L$.

10. $L$ has countably many symbols, and each sentence is a finite string of symbols. So the set of sentences is [[countable|01TQB88H4C]], and we fix a list $\sigma_0, \sigma_1, \sigma_2, \dots$ of all sentences of $L$.
11. Put $\Delta_0 = \Gamma$. For $n \ge 0$, put $\Delta_{n+1} = \Delta_n \cup \set{\sigma_n}$ if this set is consistent, and $\Delta_{n+1} = \Delta_n \cup \set{\neg \sigma_n}$ otherwise.
12. Each $\Delta_n$ is consistent, by induction on $n$. $\Delta_0 = \Gamma$ is consistent by hypothesis.
13. Let $\Delta_n$ be consistent. If $\Delta_n \cup \set{\sigma_n}$ is consistent, then $\Delta_{n+1}$ is this set. Otherwise (P5) gives $\Delta_n \vdash \neg \sigma_n$.
14. In the second case, suppose $\Delta_n \cup \set{\neg \sigma_n}$ were inconsistent. Then (P5) gives $\Delta_n \vdash \sigma_n$, and with step 13 the set $\Delta_n$ is inconsistent. This contradicts the induction hypothesis, so $\Delta_{n+1} = \Delta_n \cup \set{\neg \sigma_n}$ is consistent.
15. Put $\Delta = \bigcup_{n} \Delta_n$. Then $\Gamma = \Delta_0 \subseteq \Delta$.
16. $\Delta$ is consistent. Suppose $\Delta \vdash \psi$ and $\Delta \vdash \neg \psi$. By (P1) the two derivations use a finite set $\Delta' \subseteq \Delta$.
17. Each member of $\Delta'$ lies in some $\Delta_n$, and $\Delta_0 \subseteq \Delta_1 \subseteq \cdots$. So $\Delta' \subseteq \Delta_N$ for the largest such $n = N$, and (P2) makes $\Delta_N$ inconsistent. This contradicts step 12.
18. $\Delta$ is maximal: each sentence is some $\sigma_n$, and $\sigma_n$ or $\neg \sigma_n$ lies in $\Delta_{n+1} \subseteq \Delta$.

Step (c): the properties of a maximal consistent set $\Delta$.
These steps hold for every $L$.

19. Property 1. Let $\Delta \vdash \sigma$ and suppose $\sigma \notin \Delta$. Maximality gives $\neg \sigma \in \Delta$, so $\Delta \vdash \neg \sigma$, and $\Delta$ is inconsistent. Hence $\sigma \in \Delta$.
20. Property 2. Maximality gives at least one of $\sigma$, $\neg \sigma$. If both lie in $\Delta$, then $\Delta$ derives both and is inconsistent. So exactly one lies in $\Delta$.
21. Property 3, the case $\sigma \notin \Delta$. Then $\neg \sigma \in \Delta$ by property 2. Every assignment that makes $\neg \sigma$ true makes $\sigma \to \tau$ true, so (P3) gives $\Delta \vdash \sigma \to \tau$, and property 1 gives $(\sigma \to \tau) \in \Delta$.
22. Property 3, the case $\tau \in \Delta$. Every assignment that makes $\tau$ true makes $\sigma \to \tau$ true, so (P3) and property 1 give $(\sigma \to \tau) \in \Delta$.
23. Property 3, the remaining case $\sigma \in \Delta$ and $\tau \notin \Delta$. If $(\sigma \to \tau) \in \Delta$, then MP gives $\Delta \vdash \tau$, and property 1 gives $\tau \in \Delta$, a contradiction. So $(\sigma \to \tau) \notin \Delta$. Steps 21 to 23 prove property 3.
24. Property 4. Let $\forall x \, \varphi \in \Delta$ and let $t$ be a closed term. A closed term has no variables, so it is substitutable for $x$ in $\varphi$, and $\forall x \, \varphi \to \varphi^x_t$ is an axiom of group 2.
25. MP gives $\Delta \vdash \varphi^x_t$. The formula $\varphi^x_t$ is a sentence, because $x$ is the only variable that can be free in $\varphi$ and $t$ is closed. Property 1 gives $\varphi^x_t \in \Delta$.
26. Property 5, first part. Let $\Delta \subsetneq \Delta''$ with some sentence $\sigma \in \Delta'' \setminus \Delta$. Property 2 gives $\neg \sigma \in \Delta \subseteq \Delta''$, so $\Delta''$ contains $\sigma$ and $\neg \sigma$ and is inconsistent.
27. Property 5, second part. Let $\Delta$ be consistent with no consistent proper superset, and let $\sigma$ be a sentence with $\sigma \notin \Delta$ and $\neg \sigma \notin \Delta$. Then $\Delta \cup \set{\sigma}$ and $\Delta \cup \set{\neg \sigma}$ are proper supersets, so both are inconsistent.
28. By (P5), $\Delta \vdash \neg \sigma$ and $\Delta \vdash \sigma$, so $\Delta$ is inconsistent. This contradiction shows that $\Delta$ is maximal consistent.

## Idea

We go through a list of all sentences and decide each one in turn.
A sentence goes in when it keeps the set consistent, and otherwise its negation goes in; fact (P5) shows that one of the two choices is always safe.
Since derivations are finite, any contradiction in the union would already appear at a finite stage, so the union is consistent.

## Variants

- For an uncountable $L$, see the [[proof by Zorn's lemma|~08168ab3]]. One can also well-order the sentences and run the same construction by transfinite recursion, taking unions at limit stages.
- The [[propositional version|GNPVCQC55C]] is the same construction for formulas of propositional logic.
- The construction is not effective in general: deciding whether $\Delta_n \cup \set{\sigma_n}$ is consistent is not a computable test for first-order logic, by [[Church's theorem|VA6BNNY2YC]].
