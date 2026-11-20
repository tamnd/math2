---
tag: QJJ5J1AJQT
kind: proof
name: Proof of McGee's theorem
msc: ["03F25", "03A05"]
topics: [6Q4JJ2MMV8]
audience: research
proves: GQW8RQVZJ4
uses: [P3XFQC6ACX, BJF29XET83, 3K1AKGXF8A, 4S29X1GTV4]
methods: [0ASJVEFA9J, 0J0XBKG64S]
sources:
  - url: https://plato.stanford.edu/entries/truth-axiomatic/
    locator: "Axiomatic Theories of Truth, 4.3 The Friedman-Sheard theory and revision semantics"
  - book: isbn:9780521115810
---

## Proof

We use the notation and the hypotheses NEC, (D) and (U) of the [[statement|GQW8RQVZJ4]].

*Step A: the formula $\theta$.*

1. By [[representability in Q|BJF29XET83]], there is a formula $\mathrm{Ng}(a, v)$ for the map from a code $\ulcorner \chi \urcorner$ to $\ulcorner \neg \forall x\, \chi \urcorner$.
2. So $\mathsf{Q} \vdash \forall v\, (\mathrm{Ng}(\underline{n}, v) \leftrightarrow v = \underline{g(n)})$ for each $n$, where $g$ is this map.
3. In the same way, $\mathsf{Q} \vdash \forall u\, (\mathrm{Sb}(\underline{n}, \underline{m}, u) \leftrightarrow u = \underline{h(n, m)})$, where $h(\ulcorner \chi \urcorner, m) = \ulcorner \chi(\underline{m}) \urcorner$.
4. Let $\psi(a, x) := (x = 0 \wedge \exists v\, (\mathrm{Ng}(a, v) \wedge T(v))) \vee \exists y\, (x = Sy \wedge \exists u\, (\mathrm{Sb}(a, y, u) \wedge T(u)))$.
5. The [[diagonal lemma with parameters|P3XFQC6ACX]] gives a formula $\theta(x)$ with $\mathsf{Q} \vdash \theta(x) \leftrightarrow \psi(\ulcorner \theta \urcorner, x)$.
6. Here $\ulcorner \theta \urcorner$ is the code of $\theta(x)$, a formula with only $x$ free.

*Step B: the two equivalences.*

7. Put $x := 0$ in step 5. In $\mathsf{Q}$, $0 \neq Sy$ for all $y$, so the second disjunct of $\psi$ is false.
8. So $\mathsf{Q} \vdash \theta(0) \leftrightarrow \exists v\, (\mathrm{Ng}(\ulcorner \theta \urcorner, v) \wedge T(v))$.
9. By step 2, the right side is equivalent in $\mathsf{Q}$ to $T\ulcorner \neg \forall x\, \theta(x) \urcorner$. Call this equivalence (E0).
10. Put $x := Sy$ in step 5. In $\mathsf{Q}$, $Sy \neq 0$, so the first disjunct is false.
11. In $\mathsf{Q}$, $Sy = Sy'$ implies $y = y'$. So the second disjunct is equivalent to $\exists u\, (\mathrm{Sb}(\ulcorner \theta \urcorner, y, u) \wedge T(u))$.
12. This is $T\ulcorner \theta(\dot y) \urcorner$ by the definition of the dot notation. So $\mathsf{Q} \vdash \theta(Sy) \leftrightarrow T\ulcorner \theta(\dot y) \urcorner$. Call this (E1).

*Step C: $S$ refutes $\forall x\, \theta(x)$.*

13. We argue in $S$, and assume $\forall x\, \theta(x)$.
14. Then $\theta(Sy)$ for every $y$. By (E1), $\forall y\, T\ulcorner \theta(\dot y) \urcorner$.
15. By (U) for $\chi := \theta$, this gives $T\ulcorner \forall x\, \theta(x) \urcorner$.
16. Also $\theta(0)$, by the assumption. By (E0), $T\ulcorner \neg \forall x\, \theta(x) \urcorner$.
17. By (D) for $\varphi := \forall x\, \theta(x)$, this gives $\neg T\ulcorner \forall x\, \theta(x) \urcorner$.
18. Steps 15 and 17 contradict each other. So $S \vdash \neg \forall x\, \theta(x)$, which is equivalent to $\exists x\, \neg \theta(x)$.

*Step D: $S$ proves every instance.*

19. NEC applied to step 18 gives $S \vdash T\ulcorner \neg \forall x\, \theta(x) \urcorner$. By (E0), $S \vdash \theta(0)$.
20. Assume $S \vdash \theta(\underline{n})$. NEC gives $S \vdash T\ulcorner \theta(\underline{n}) \urcorner$.
21. By step 3, $\mathsf{Q} \vdash \exists u\, (\mathrm{Sb}(\ulcorner \theta \urcorner, \underline{n}, u) \wedge T(u)) \leftrightarrow T\ulcorner \theta(\underline{n}) \urcorner$.
22. The left side is the right side of (E1) with $y := \underline{n}$. So $S \vdash \theta(S\underline{n})$, and $S\underline{n}$ is the numeral $\underline{n + 1}$.
23. By [[induction|0ASJVEFA9J]] on $n$, outside $S$, steps 19 to 22 give $S \vdash \theta(\underline{n})$ for every $n \in \mathbb{N}$.
24. Steps 18 and 23 show that $S$ is [[ω-inconsistent|4S29X1GTV4]], with the formula $\theta(x)$.

## Idea

The formula $\theta(x)$ says, at $0$, "not all numbers have $\theta$ is true", and, at $n + 1$, "$\theta(n)$ is true".
If all numbers had $\theta$, then (U) would make "all have $\theta$" true, and (D) with the value at $0$ would make it not true.
So $S$ refutes the universal claim, and NEC then proves each instance, one number at a time.
The induction in step 23 is outside the theory, so it cannot be turned into a proof of the universal claim.

## Variants

1. The SEP entry states that the $\omega$-inconsistency of FS follows from results of McGee (1985). The proof above uses only NEC, (D) and (U), and no induction inside $S$.
2. The [[Yablo paradox|6FJXAN1ND9]] gives a related $\omega$-inconsistency from T-sentences alone; see [[its proof|4C40VGJHDD]].
