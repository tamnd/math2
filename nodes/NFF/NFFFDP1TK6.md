---
tag: NFFFDP1TK6
kind: proof
name: Proof of the soundness of the reduction axioms of public announcement logic
msc: ["03B42", "03B45"]
topics: [CQM9SRN8PM]
audience: research
proves: MFGHDHGV1D
uses: [9465T2PWZT, EA34W4ERRE, 12MQ2NJ29A]
methods: [0NTF6DMVAP, 12MQ2NJ29A]
sources:
  - book: isbn:9781402058387
    locator: van Ditmarsch, van der Hoek and Kooi, Dynamic Epistemic Logic, chapter on public announcements
  - url: https://en.wikipedia.org/wiki/Dynamic_epistemic_logic
    locator: section Public Events
---

## Proof

We use the notation of [[the theorem|MFGHDHGV1D]], check the five axioms one at a time, and then build the translation into [[epistemic logic|EA34W4ERRE]].
Fix a model $M$ and a world $w$.
If $\varphi$ is false at $w$, then every formula $[!\varphi]\theta$ is true at $w$.
So is every right-hand side of parts 1 to 4, since each has the form $\varphi \to \cdots$.
So for parts 1 to 4 we assume $M, w \models \varphi$, which means $w \in W'$.

### Atoms, negation and conjunction

1. $M|\varphi, w \models p$ holds iff $w \in V'(p) = V(p) \cap W'$.
2. Since $w \in W'$, this holds iff $w \in V(p)$, that is, iff $M, w \models p$, which proves part 1.
3. For part 2, the left side holds iff $M|\varphi, w \not\models \psi$.
4. Since $\varphi$ holds at $w$, we have $M, w \models [!\varphi]\psi$ iff $M|\varphi, w \models \psi$.
5. So the right side $\neg[!\varphi]\psi$ holds iff $M|\varphi, w \not\models \psi$, and the two sides agree.
6. For part 3, $M|\varphi, w \models \psi \wedge \chi$ iff $M|\varphi, w \models \psi$ and $M|\varphi, w \models \chi$.
7. By step 4 for $\psi$ and for $\chi$, this is $M, w \models [!\varphi]\psi \wedge [!\varphi]\chi$.

### Knowledge

8. $M|\varphi, w \models K_a\psi$ iff $M|\varphi, v \models \psi$ for every $v \in W'$ with $w R_a v$, by the definition of $R'_a$.
9. Take any $v$ with $w R_a v$.
   If $v \notin W'$, then $[!\varphi]\psi$ is true at $v$ in $M$, vacuously.
10. If $v \in W'$, then $M, v \models [!\varphi]\psi$ iff $M|\varphi, v \models \psi$, by the definition of $[!\varphi]$.
11. So the condition of step 8 holds iff $M, v \models [!\varphi]\psi$ for every $v$ with $w R_a v$.
12. That is $M, w \models K_a[!\varphi]\psi$, which is the right side of part 4 when $\varphi$ holds at $w$.

### Composition

13. Let $\theta = \varphi \wedge [!\varphi]\psi$.
    We claim that $(M|\varphi)|\psi = M|\theta$.
14. The worlds of $(M|\varphi)|\psi$ are the $v \in W'$ with $M|\varphi, v \models \psi$.
15. For $v \in W'$, $M, v \models [!\varphi]\psi$ iff $M|\varphi, v \models \psi$.
    So these are exactly the $v$ with $M, v \models \theta$.
16. Both models restrict the relations and the valuation of $M$ to this same set, which proves the claim.
17. Now $M, w \models [!\varphi][!\psi]\chi$ says: if $M, w \models \varphi$ and $M|\varphi, w \models \psi$, then $(M|\varphi)|\psi, w \models \chi$.
18. By step 15 at $w$, the hypothesis says $M, w \models \theta$.
    By the claim, the conclusion says $M|\theta, w \models \chi$.
19. That is the clause for $M, w \models [!\theta]\chi$, which proves part 5.

### Reduction to epistemic logic

20. Call two formulas equivalent, written $\equiv$, when they are true at the same worlds of every model.
21. If $\varphi \equiv \varphi'$ and $\psi \equiv \psi'$, then $[!\varphi]\psi \equiv [!\varphi']\psi'$.
    Indeed $M|\varphi = M|\varphi'$, and $\psi$ and $\psi'$ agree in that model.
22. For epistemic formulas $\alpha$ and $\beta$, define $r(\alpha, \beta)$ by recursion on $\beta$.
    Put $r(\alpha, p) = \alpha \to p$ and $r(\alpha, \neg\beta) = \alpha \to \neg r(\alpha, \beta)$.
    Put $r(\alpha, \beta \wedge \gamma) = r(\alpha, \beta) \wedge r(\alpha, \gamma)$ and $r(\alpha, K_a\beta) = \alpha \to K_a r(\alpha, \beta)$.
23. By [[structural induction|12MQ2NJ29A]] on $\beta$, $r(\alpha, \beta) \equiv [!\alpha]\beta$.
    Each case is one of parts 1 to 4, with the induction hypothesis substituted inside.
24. Define $t$ on all formulas so that $t$ commutes with atoms, $\neg$, $\wedge$ and $K_a$, and $t([!\varphi]\psi) = r(t(\varphi), t(\psi))$.
25. By structural induction, $t(\chi)$ has no announcements and $t(\chi) \equiv \chi$.
    The announcement case uses step 23 and then step 21 with $\varphi \equiv t(\varphi)$ and $\psi \equiv t(\psi)$.

This proves the five axioms and the reduction.

## Idea

An announcement deletes worlds and changes nothing else.
So atoms keep their values, Boolean connectives commute with the update, and knowledge after the update is knowledge before, restricted to the surviving worlds.
The only care is the precondition: where $\varphi$ is false, every $[!\varphi]$ statement is vacuously true.

## Variants

The same clause-by-clause argument proves the reduction axioms for action models, with the product update in place of restriction.

The translation $t$ can blow up exponentially, because $r(\alpha, \beta)$ copies $\alpha$ once for each operator of $\beta$.
Lutz showed in 2006 that this blow-up cannot be avoided in general.
