---
tag: 6T82THKX5M
kind: proof
name: Proof of the de Jongh-Sambin fixed-point theorem
msc: ["03F45", "03B45"]
topics: [3E7M66WW6Q]
audience: research
proves: TDDX1NHG8D
uses: [61THBNS8WE, QQ6PZFGGB3, 17C5DRFAW7, G989VP2NGP, 1ZRWVDYPX0]
methods: [0NTF6DMVAP, 12MQ2NJ29A, 01XM7JEKHY]
sources:
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: History
  - book: isbn:9780521701464
---

## Proof

We prove two replacement lemmas, use them with Löb's axiom for uniqueness, and then check the one-box recipe with Löb's rule.

We use axiom 4, $\square X \to \square \square X$, and Löb's rule from [[Löb's axiom in provability logic|QQ6PZFGGB3]].
We also use rule (RM) from [[its proof|17C5DRFAW7]]: if $\vdash X \to Y$ then $\vdash \square X \to \square Y$.
All derivations are in $\mathsf{GL}$, and $\boxdot X := X \wedge \square X$.
For a formula $B(x)$ with a variable $x$, $B(X)$ is the result of replacing every $x$ by $X$.

### Lemma 1: replacement under a dotted box

Lemma 1: for every formula $B(x)$ and all formulas $X$, $Y$, we have $\vdash \boxdot(X \leftrightarrow Y) \to (B(X) \leftrightarrow B(Y))$.

1. We use [[structural induction|12MQ2NJ29A]] on $B$.
   If $B$ is $x$, the claim follows from the first conjunct of $\boxdot$.
   If $B$ is another variable or $\bot$, then $B(X) = B(Y)$.
2. If $B = B_1 \to B_2$, the induction hypotheses for $B_1$ and $B_2$ give the claim by propositional logic.
3. Let $B = \square B_1$.
   The induction hypothesis and (RM) give $\vdash \square \boxdot(X \leftrightarrow Y) \to \square(B_1(X) \leftrightarrow B_1(Y))$.
   The axiom $\mathrm{K}$ gives $\vdash \square(B_1(X) \leftrightarrow B_1(Y)) \to (\square B_1(X) \leftrightarrow \square B_1(Y))$.
4. By axiom 4, $\square(X \leftrightarrow Y) \to \square \square(X \leftrightarrow Y)$.
   Since $\square$ commutes with $\wedge$, this gives $\vdash \boxdot(X \leftrightarrow Y) \to \square \boxdot(X \leftrightarrow Y)$.
   Steps 3 and 4 give the claim for $\square B_1$.
5. Replacement: if $\vdash X \leftrightarrow Y$, then necessitation gives $\vdash \boxdot(X \leftrightarrow Y)$, so $\vdash B(X) \leftrightarrow B(Y)$.

### Lemma 2: replacement under a box

Lemma 2: if $x$ is modalized in $B(x)$, then $\vdash \square(X \leftrightarrow Y) \to (B(X) \leftrightarrow B(Y))$.

6. Such a $B$ is built with $\to$ from $\bot$, variables other than $x$, and formulas $\square B_1$ with $B_1$ arbitrary.
   By induction on this build, it suffices to treat $\square B_1$.
7. By step 4, $\vdash \square(X \leftrightarrow Y) \to \square \boxdot(X \leftrightarrow Y)$.
   By Lemma 1 for $B_1$ and step 3, $\vdash \square \boxdot(X \leftrightarrow Y) \to (\square B_1(X) \leftrightarrow \square B_1(Y))$.

### Part 2: uniqueness

Let $D := \boxdot(p \leftrightarrow A(p)) \wedge \boxdot(r \leftrightarrow A(r))$.

8. By Lemma 2 with $B = A$, $\vdash \square(p \leftrightarrow r) \to (A(p) \leftrightarrow A(r))$.
9. With the first conjuncts of $D$, step 8 gives $\vdash D \to (\square(p \leftrightarrow r) \to (p \leftrightarrow r))$.
10. By step 4, $\vdash D \to \square D$.
11. (RM) on step 9 gives $\vdash \square D \to \square(\square(p \leftrightarrow r) \to (p \leftrightarrow r))$.
    Löb's axiom then gives $\vdash \square D \to \square(p \leftrightarrow r)$.
12. Steps 10, 11 and 9 give $\vdash D \to (p \leftrightarrow r)$.
13. Let $\vdash H \leftrightarrow A(H)$ and $\vdash H' \leftrightarrow A(H')$.
    Necessitation gives the boxed forms.
    So the substitution $p := H$, $r := H'$ in step 12 gives $\vdash H \leftrightarrow H'$.

### Part 3: existence for one box

Let $A(p) = B(\square C(p))$ with $p$ not in $B(x)$.
Let $d := \square C(B(\top))$, let $H := B(d)$, and let $e := \square C(H)$.
Then $A(H) = B(e)$, so we must show $\vdash d \leftrightarrow e$.

14. Propositional logic gives $\vdash d \to (d \leftrightarrow \top)$, and (RM) gives $\vdash \square d \to \square(d \leftrightarrow \top)$.
    With axiom 4, $\vdash d \to \boxdot(d \leftrightarrow \top)$.
15. Lemma 1 with $X = d$ and $Y = \top$ gives $\vdash d \to (H \leftrightarrow B(\top))$.
16. (RM) on step 15 gives $\vdash \square d \to \square(H \leftrightarrow B(\top))$.
17. Lemma 2 for the formula $\square C(y)$, which is modalized in $y$, gives $\vdash \square(H \leftrightarrow B(\top)) \to (e \leftrightarrow d)$.
18. By axiom 4, $d$ gives $\square d$, so steps 16 and 17 give $\vdash d \to (e \leftrightarrow d)$, hence $\vdash d \to e$.
19. For $e \to d$ we use Löb's rule.
    Assume $\square(e \to d)$ and $e$.
    By axiom 4, $e$ gives $\square e$, so $\square d$ by axiom $\mathrm{K}$.
20. By steps 16 and 17, $\square d$ gives $e \leftrightarrow d$, and $e$ gives $d$.
    So $\vdash \square(e \to d) \to (e \to d)$, and Löb's rule gives $\vdash e \to d$.
21. So $\vdash d \leftrightarrow e$.
    By replacement (step 5), $\vdash B(d) \leftrightarrow B(e)$, that is, $\vdash H \leftrightarrow A(H)$.

### Part 1: existence in general

22. Write $A(p) = B(\square C_1(p), \dots, \square C_m(p))$ with $p$ not in $B(x_1, \dots, x_m)$.
    For $m = 0$, $H = A$.
    For $m = 1$, this is Part 3.
23. For $m \geq 2$ one uses induction on $m$, and each step applies a one-box argument like Part 3 with extra parameters.
    We cite this reduction without proof.

### Part 4: arithmetical form

24. Choose a fixed point $H$ by part 1.
    Let $\mathsf{PA} \vdash \sigma \leftrightarrow A^*(\sigma)$, and extend $*$ by $p^* = \sigma$ and $r^* = H^*$.
25. The realization of step 12 is provable in $\mathsf{PA}$, by the arithmetical soundness half of [[Solovay's theorem|1ZRWVDYPX0]].
    The realization of $\boxdot(H \leftrightarrow A(H))$ is provable, as the realization of a theorem.
26. The first derivability condition turns $\mathsf{PA} \vdash \sigma \leftrightarrow A^*(\sigma)$ into $\mathsf{PA} \vdash \mathrm{Prov}(\ulcorner \sigma \leftrightarrow A^*(\sigma) \urcorner)$.
    So the realization of $D$ is provable, and $\mathsf{PA} \vdash \sigma \leftrightarrow H^*$.

### Check of Part 3 on one formula

We test the recipe on $A(p) = \square p \to q$.

27. Here $B(x) = x \to q$ and $C(p) = p$, so $B(\top) = \top \to q$ and $H = \square(\top \to q) \to q$.
    By replacement, $H$ is equivalent to $\square q \to q$.
28. We check $\vdash (\square q \to q) \leftrightarrow (\square(\square q \to q) \to q)$ directly.
29. From left to right, Löb's axiom gives $\square(\square q \to q) \to \square q$, and then $\square q \to q$ gives $q$.
30. From right to left, the tautology $q \to (\square q \to q)$ and (RM) give $\square q \to \square(\square q \to q)$.
    So $\square q$ gives $\square(\square q \to q)$, and then $q$.

The L2 explanation of the [[statement|TDDX1NHG8D]] checks the case $A(p) = \neg \square p$ in the same way.

## Idea

Uniqueness is a Löb argument.
Two fixed points agree at all later worlds, and so they agree now.
For one box, the guess $B(\square C(B(\top)))$ comes from a case split.
When $\square C(\dots)$ holds, the box can be replaced by $\top$ inside, and axiom 4 makes this replacement stable under $\square$.
Löb's rule then shows that the guess and the true box agree, and the general case nests the one-box case.

## Variants

There is a semantic proof on finite transitive irreflexive frames.
There the truth value of a fixed point at a world is fixed by its values at the later worlds.
This gives uniqueness by induction along the converse well-founded order, and it gives existence by computing $H$ depth by depth.

In arithmetic, existence also follows from the [[diagonal lemma|3PRW76471J]].
That fixed point is not given by a modal formula, but part 4 shows that it is equivalent to one.
