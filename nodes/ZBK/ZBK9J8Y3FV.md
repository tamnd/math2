---
tag: ZBK9J8Y3FV
kind: proof
name: Proof of the knower paradox
msc: ["03A05", "03B42"]
topics: [6Q4JJ2MMV8]
audience: grad
proves: N3BWQRFQCC
uses: [3PRW76471J, G989VP2NGP, 0Y0MQYST0M]
methods: [0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Knower_paradox
    locator: Formulation
  - url: https://plato.stanford.edu/entries/epistemic-paradoxes/
    locator: "Epistemic Paradoxes, 5.1 The Knower Paradox"
---

## Proof

We use the notation of the [[statement|N3BWQRFQCC]].

*Part 1.*

1. The [[diagonal lemma|3PRW76471J]] for $\neg K(x)$ gives a sentence $\kappa$ with $\kappa \leftrightarrow \neg K(\ulcorner \kappa \urcorner)$ in $S$.
2. Factivity for $\kappa$ gives $K(\ulcorner \kappa \urcorner) \to \kappa$ in $S$.
3. Steps 1 and 2 give $K(\ulcorner \kappa \urcorner) \to \neg K(\ulcorner \kappa \urcorner)$ in $S$, by transitivity of $\to$.
4. A sentence $p \to \neg p$ implies $\neg p$ in classical and intuitionistic logic. So $\neg K(\ulcorner \kappa \urcorner) \in S$.
5. Step 1, from right to left, and step 4 give $\kappa \in S$, by [[modus ponens|0Y0MQYST0M]].
6. [[Necessitation|G989VP2NGP]] applied to step 5 gives $K(\ulcorner \kappa \urcorner) \in S$.
7. Steps 4 and 6 give a sentence and its negation in $S$. So $S$ is inconsistent.

*Part 2.* Write $\Box \varphi$ for $B(\ulcorner \varphi \urcorner)$.

8. The diagonal lemma for $\neg B(x)$ gives $\delta$ with $\delta \leftrightarrow \neg \Box \delta$ in $S$.
9. Step 8 gives $\delta \to \neg \Box \delta$. Necessitation and closure give $\Box \delta \to \Box \neg \Box \delta$.
10. Positive introspection for $\delta$ gives $\Box \delta \to \Box \Box \delta$.
11. The tautology $\Box \delta \to (\neg \Box \delta \to \bot)$ is in $S$. Necessitation gives $\Box(\Box \delta \to (\neg \Box \delta \to \bot))$.
12. Closure twice gives $\Box \Box \delta \to (\Box \neg \Box \delta \to \Box \bot)$.
13. Steps 9, 10 and 12 give $\Box \delta \to \Box \bot$ in $S$.
14. By step 8, $\neg \Box \delta \to \delta$. With the tautology $(p \to q) \to ((\neg p \to q) \to q)$, $(\Box \delta \to \delta) \to \delta$ is in $S$.
15. Necessitation and closure give $\Box(\Box \delta \to \delta) \to \Box \delta$.
16. Belief in accuracy gives $\Box(\Box \delta \to \delta)$. By step 15, $\Box \delta \in S$.
17. Steps 13 and 16 give $\Box \bot \in S$.
18. Let $\psi$ be any sentence. Necessitation for the tautology $\bot \to \psi$ and closure give $\Box \bot \to \Box \psi$.
19. Steps 17 and 18 give $\Box \psi \in S$, which is $B(\ulcorner \psi \urcorner) \in S$.

## Idea

Part 1 is the liar argument with "known" in place of "true".
Factivity gives one direction of the truth schema, and the proof of $\neg K(\ulcorner \kappa \urcorner)$ gives the other direction through necessitation.
Part 2 uses introspection and belief in accuracy in place of factivity, in the style of the proof of Löb's theorem.

## Variants

1. In part 1, closure under derivability can be weakened. The proof uses only modus ponens, transitivity of $\to$, and the rule from $p \to \neg p$ to $\neg p$.
2. The SEP entry gives the original version with "this sentence is known to be false". Its proof uses factivity for the negation of the sentence in the same way.
