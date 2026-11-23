---
tag: 17C5DRFAW7
kind: proof
name: Proof of the properties of Löb's axiom
msc: ["03F45", "03B45"]
topics: [3E7M66WW6Q]
audience: research
proves: QQ6PZFGGB3
uses: [C3RZY20ETK, NGHWZ9Y7ZV, G989VP2NGP, 0GJZW9JFZQ, 0DQPNJNPYK]
methods: [0NTF6DMVAP, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Proof

We prove parts 1 and 2 by derivations in $\mathsf{K} + \mathrm{L}$, and part 3 by building a refuting valuation from each defect of the frame.
We use the notation of [[Löb's axiom in provability logic|QQ6PZFGGB3]].

### A derived rule of K

Rule (RM) says: if $\mathsf{K} \vdash A \to B$, then $\mathsf{K} \vdash \square A \to \square B$.

1. The [[necessitation rule|G989VP2NGP]] applied to $A \to B$ gives $\square(A \to B)$.
2. The axiom K, with $A$ and $B$ substituted, is $\square(A \to B) \to (\square A \to \square B)$.
3. Modus ponens with steps 1 and 2 gives $\square A \to \square B$.

### Part 1: axiom 4 from Löb's axiom

We show $\mathsf{K} + \mathrm{L} \vdash \square p \to \square \square p$.
Let $q$ be the formula $p \wedge \square p$.

4. The tautologies $q \to p$ and $q \to \square p$ and rule (RM) give $\vdash \square q \to \square p$ and $\vdash \square q \to \square \square p$.
5. From $\vdash \square q \to \square p$, propositional logic gives $\vdash p \to (\square q \to q)$.
   Indeed, if $p$ and $\square q$ hold, then $\square p$ holds by step 4, so $q = p \wedge \square p$ holds.
6. Rule (RM) applied to step 5 gives $\vdash \square p \to \square(\square q \to q)$.
7. Löb's axiom with $q$ substituted for $p$ is $\square(\square q \to q) \to \square q$.
8. Steps 6 and 7 give $\vdash \square p \to \square q$.
9. Steps 8 and 4 give $\vdash \square p \to \square \square p$.

### Part 2: Löb's rule

10. Assume $\mathsf{GL} \vdash \square \varphi \to \varphi$.
11. Necessitation gives $\mathsf{GL} \vdash \square(\square \varphi \to \varphi)$.
12. Löb's axiom with $\varphi$ substituted for $p$ and modus ponens give $\mathsf{GL} \vdash \square \varphi$.
13. Steps 10 and 12 and modus ponens give $\mathsf{GL} \vdash \varphi$.

### Part 3: good frames validate L

We assume that $R$ is transitive and conversely well-founded, and we show that $\mathrm{L}$ is valid on $(W, R)$.

14. Fix a valuation and a world $w$, and assume $w \not\models \square p$.
   We show $w \not\models \square(\square p \to p)$, which proves $w \models \mathrm{L}$.
15. Let $X = \{ v \in W : w R v \text{ and } v \not\models p \}$.
   By step 14 and the truth clause for $\square$, $X$ is nonempty.
16. By converse well-foundedness, $X$ has an $R$-maximal element $v$.
   So $w R v$, $v \not\models p$, and no $u \in X$ has $v R u$.
17. Let $u$ be any world with $v R u$.
   By [[transitivity|0GJZW9JFZQ]], $w R v$ and $v R u$ give $w R u$.
   If $u \not\models p$, then $u \in X$, against step 16, so $u \models p$.
18. Step 17 holds for every successor $u$ of $v$, so $v \models \square p$.
   With $v \not\models p$, we get $v \not\models \square p \to p$.
19. Since $w R v$, step 18 gives $w \not\models \square(\square p \to p)$.

### Part 3: frames that validate L are good

We assume that $\mathrm{L}$ is valid on $(W, R)$, and we show transitivity first.

20. Assume, for a contradiction, that $w R v$ and $v R u$ but not $w R u$.
   Then $u \neq v$, since $u = v$ would give $w R u$.
21. Put $p$ true exactly at the worlds outside $\{ v, u \}$.
22. Since $w R v$ and $v \not\models p$, we get $w \not\models \square p$.
23. Let $x$ be a successor of $w$, so $x \neq u$ because $w R u$ fails.
   If $x \neq v$, then $x \models p$, so $x \models \square p \to p$.
   If $x = v$, then $v R u$ and $u \not\models p$ give $v \not\models \square p$, so $v \models \square p \to p$.
24. By step 23, $w \models \square(\square p \to p)$.
   With step 22, $\mathrm{L}$ fails at $w$, against validity, so $R$ is transitive.

Next we show converse well-foundedness.

25. Assume, for a contradiction, that a nonempty $X \subseteq W$ has no $R$-maximal element.
   So every $y \in X$ has some $z \in X$ with $y R z$.
26. Put $p$ true exactly at the worlds outside $X$.
27. Let $y$ be any world.
   If $y \notin X$, then $y \models p$, so $y \models \square p \to p$.
   If $y \in X$, then $y$ has a successor $z \in X$, where $p$ fails, so $y \not\models \square p$ and $y \models \square p \to p$.
28. By step 27, $\square p \to p$ is true at every world, so $\square(\square p \to p)$ is true at every world.
29. Validity of $\mathrm{L}$ and step 28 give $y \models \square p$ for every world $y$.
30. Take $y \in X$, which exists since $X$ is nonempty.
   By step 25 it has a successor $z \in X$, and $z \not\models p$, so $y \not\models \square p$, against step 29.
   Hence $R$ is conversely [[well-founded|0DQPNJNPYK]].

Steps 9, 13, 19, 24 and 30 prove the three parts of the statement.

## Idea

Part 1 applies Löb's axiom to the stronger formula $p \wedge \square p$, because a proof of $p$ already gives the hypothesis of Löb's axiom for $p \wedge \square p$.
Part 3 is a correspondence argument.
A world that refutes $\square p$ sees a maximal world that refutes $p$, and that maximal world refutes $\square p \to p$.
Conversely, a bad configuration of the frame, either a missing transitive edge or a set without a maximal element, gives a valuation that refutes $\mathrm{L}$.

## Variants

Part 1 also follows from part 3 and the [[Kripke completeness of GL|1DMFNR7FZT]], since axiom 4 is valid on every transitive frame.
That proof is not independent, because the completeness proof uses axiom 4.
For part 3, some books state converse well-foundedness as "there is no infinite chain $w_0 R w_1 R w_2 R \cdots$".
A set without a maximal element contains such a chain by the axiom of dependent choice, and the set of points of such a chain has no maximal element.
So the two forms agree in the presence of dependent choice.
