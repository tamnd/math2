---
tag: GNPVCQC55C
kind: proof
name: Proof of the strong completeness theorem by maximal consistent sets
msc: ["03B05", "03F03"]
topics: [JDK63589SA]
audience: ug2
proves: 81ZNY1XKYJ
uses: [1MGMQX43B8, Y060MF2NZ7, 9X08XK5RV2, VM8TQ70CVJ, H31CS3HK5P, QN7M1JCGT9, 1HK0VYWTV7, 01TQB88H4C, TT7WT5HPN9]
methods: [0J0XBKG64S, 12MQ2NJ29A, 0ASJVEFA9J, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Completeness_(logic)
    locator: Semantic completeness
  - book: isbn:9781447145578
    locator: Chapter 1
---

## Proof

We prove the strong form for a [[countable|01TQB88H4C]] set $P$ of variables.
A set $\Gamma$ is [[consistent|VM8TQ70CVJ]] when there is no $\psi$ with $\Gamma \vdash \psi$ and $\Gamma \vdash \neg \psi$.
A set $\Delta$ is maximal consistent when it is consistent and, for every formula $\varphi$, $\varphi \in \Delta$ or $\neg \varphi \in \Delta$.
We use the theorems (T4) $\neg \varphi \to (\varphi \to \psi)$ and (T7) $\varphi \to (\neg \psi \to \neg (\varphi \to \psi))$ of the [[basic theorems of the Hilbert system L|Y060MF2NZ7]].

Step (a): if $\Gamma \not\vdash \varphi$, then $\Gamma \cup \set{\neg \varphi}$ is consistent.

1. Suppose $\Gamma \cup \set{\neg \varphi} \vdash \psi$ and $\Gamma \cup \set{\neg \varphi} \vdash \neg \psi$ for some $\psi$.
2. The [[deduction theorem|9X08XK5RV2]], used twice, gives $\Gamma \vdash \neg \varphi \to \psi$ and $\Gamma \vdash \neg \varphi \to \neg \psi$.
3. The instance $(\neg \varphi \to \neg \psi) \to ((\neg \varphi \to \psi) \to \varphi)$ of (A3) and two applications of MP give $\Gamma \vdash \varphi$. This contradicts $\Gamma \not\vdash \varphi$.

Step (b): if $\Delta \cup \set{\varphi}$ and $\Delta \cup \set{\neg \varphi}$ are both inconsistent, then $\Delta$ is inconsistent.

4. Since $\Delta \cup \set{\neg \varphi}$ is inconsistent, step (a) gives $\Delta \vdash \varphi$.
5. Since $\Delta \cup \set{\varphi}$ is inconsistent, there is $\psi$ with $\Delta \cup \set{\varphi} \vdash \psi$ and $\Delta \cup \set{\varphi} \vdash \neg \psi$.
6. The deduction theorem gives $\Delta \vdash \varphi \to \psi$ and $\Delta \vdash \varphi \to \neg \psi$. MP with step 4 gives $\Delta \vdash \psi$ and $\Delta \vdash \neg \psi$.

Step (c), Lindenbaum's lemma: every consistent set $\Gamma$ is contained in a maximal consistent set $\Delta$.

7. The [[formulas|TT7WT5HPN9]] are finite strings over a countable alphabet, so they form a countable set. List them as $\varphi_0, \varphi_1, \varphi_2, \dots$.
8. Put $\Delta_0 = \Gamma$. Put $\Delta_{n+1} = \Delta_n \cup \set{\varphi_n}$ if this set is consistent, and $\Delta_{n+1} = \Delta_n \cup \set{\neg \varphi_n}$ otherwise.
9. Each $\Delta_n$ is consistent, by induction on $n$. $\Delta_0 = \Gamma$ is consistent. If $\Delta_n$ is consistent, then step (b) shows that $\Delta_n \cup \set{\varphi_n}$ or $\Delta_n \cup \set{\neg \varphi_n}$ is consistent, and step 8 takes a consistent one.
10. Put $\Delta = \bigcup_n \Delta_n$. Suppose $\Delta \vdash \psi$ and $\Delta \vdash \neg \psi$. The two derivations are finite, so they use finitely many members of $\Delta$.
11. These members lie in one $\Delta_n$, because $\Delta_0 \subseteq \Delta_1 \subseteq \cdots$. Then $\Delta_n$ is inconsistent, which contradicts step 9. So $\Delta$ is consistent.
12. Every formula is some $\varphi_n$, and $\varphi_n$ or $\neg \varphi_n$ lies in $\Delta_{n+1} \subseteq \Delta$. So $\Delta$ is maximal consistent.

Step (d): a maximal consistent set $\Delta$ is closed under $\vdash$, and contains exactly one of $\varphi$, $\neg \varphi$.

13. Let $\Delta \vdash \varphi$. If $\varphi \notin \Delta$, then $\neg \varphi \in \Delta$ by maximality, so $\Delta \vdash \neg \varphi$ and $\Delta$ is inconsistent. Hence $\varphi \in \Delta$.
14. If $\varphi \in \Delta$ and $\neg \varphi \in \Delta$, then $\Delta$ derives both, which contradicts consistency. With maximality, exactly one of $\varphi$, $\neg \varphi$ lies in $\Delta$.

Step (e), the truth lemma: let $\Delta$ be maximal consistent, and define the [[truth assignment|H31CS3HK5P]] $v$ by $v(p) = 1$ if $p \in \Delta$ and $v(p) = 0$ otherwise.
Then $v(\varphi) = 1$ if and only if $\varphi \in \Delta$, for every formula $\varphi$.

15. We use [[structural induction|12MQ2NJ29A]] on $\varphi$. For a variable $p$ the claim is the definition of $v$.
16. Case $\neg \psi$: $v(\neg \psi) = 1$ iff $v(\psi) = 0$ iff $\psi \notin \Delta$ (induction hypothesis) iff $\neg \psi \in \Delta$ (step 14).
17. Case $\psi \to \chi$ with $v(\psi) = 0$: then $v(\psi \to \chi) = 1$. The induction hypothesis and step 14 give $\neg \psi \in \Delta$. Then (T4) and MP give $\Delta \vdash \psi \to \chi$, so $\psi \to \chi \in \Delta$ by step 13.
18. Case $\psi \to \chi$ with $v(\chi) = 1$: then $v(\psi \to \chi) = 1$. The induction hypothesis gives $\chi \in \Delta$. Then (A1) $\chi \to (\psi \to \chi)$ and MP give $\Delta \vdash \psi \to \chi$, so $\psi \to \chi \in \Delta$ by step 13.
19. Case $\psi \to \chi$ with $v(\psi) = 1$ and $v(\chi) = 0$: then $v(\psi \to \chi) = 0$. The induction hypothesis and step 14 give $\psi \in \Delta$ and $\neg \chi \in \Delta$.
20. In the case of step 19, (T7) and two applications of MP give $\Delta \vdash \neg (\psi \to \chi)$. Steps 13 and 14 give $\psi \to \chi \notin \Delta$.
21. Steps 17 to 20 cover all cases, and in each case $v(\psi \to \chi) = 1$ iff $\psi \to \chi \in \Delta$.

Step (f), the conclusion.

22. Every consistent set $\Gamma$ is [[satisfiable|QN7M1JCGT9]]. Step (c) gives a maximal consistent $\Delta \supseteq \Gamma$, and the assignment $v$ of step (e) makes every member of $\Delta$ true.
23. Now let $\Gamma \models \varphi$, and suppose $\Gamma \not\vdash \varphi$. Step (a) shows that $\Gamma \cup \set{\neg \varphi}$ is consistent.
24. By step 22, some $v$ makes all of $\Gamma$ true and $v(\neg \varphi) = 1$, so $v(\varphi) = 0$. This contradicts $\Gamma \models \varphi$.
25. Hence $\Gamma \vdash \varphi$, which is the strong form. The weak form is the case $\Gamma = \emptyset$.

## Idea

The proof shows that every consistent set has a model.
It first extends the consistent set to a maximal consistent set, one formula at a time.
A maximal consistent set decides every formula, so it defines a truth assignment: a variable is true when it lies in the set.
The truth lemma then shows that this assignment makes exactly the members of the set true.

## Variants

- Uncountable $P$: the list of step 7 does not exist in general. Apply [[Zorn's lemma|04RXTQA5ZA]] to the consistent sets that contain $\Gamma$, ordered by inclusion; the union of a chain is consistent by the argument of steps 10 and 11. A maximal element $\Delta$ is maximal consistent: if $\varphi \notin \Delta$ and $\neg \varphi \notin \Delta$, both extensions are inconsistent, and step (b) makes $\Delta$ inconsistent.
- Algebraic form: maximal consistent sets are the ultrafilters of the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]], and the truth lemma says that an ultrafilter gives a homomorphism onto $\set{0, 1}$.
- First-order logic: the same plan, with witnesses added for existential formulas, proves [[Gödel's completeness theorem|WQ1ZE255SF]]. This is the method of Leon Henkin.
- [[Kalmár's proof|KD3Q8XH8A3]] gives the weak form by a direct construction of derivations.
