---
tag: TW6DDQ57CW
kind: proof
name: Proof that the Lindenbaum-Tarski algebra of classical logic is a free Boolean algebra
msc: ["03G05", "03B05"]
topics: [QYA4H5Y7VR]
audience: grad
proves: JVZ8APEV7A
uses: [Y060MF2NZ7, 9X08XK5RV2, 0XADJKM699, 0HM0HQCK6N, ZT47BK9Y6K]
methods: [0NTF6DMVAP, S3QADD13E9, 12MQ2NJ29A]
sources:
  - url: https://en.wikipedia.org/wiki/Lindenbaum–Tarski_algebra
    locator: lead section
  - url: https://plato.stanford.edu/entries/logic-algebraic-propositional/
    locator: "5. The algebraic counterparts of classical and intuitionistic logic"
  - book: isbn:9780387905785
---

## Proof

We use the [[basic theorems T1 to T8 and the rule HS of L|Y060MF2NZ7]], and the [[deduction theorem|9X08XK5RV2]] (DT).
DT says: $T \cup \set{\alpha} \vdash \beta$ implies $T \vdash \alpha \to \beta$.
Write $\varphi \le \psi$ for $T \vdash \varphi \to \psi$.

**Part A: a preorder and its equivalence.**

1. $\varphi \le \varphi$, by T1.
2. If $\varphi \le \psi$ and $\psi \le \chi$, then $\varphi \le \chi$, by HS.
3. So $\le$ is a preorder, and $\sim_T$, which is $\le$ in both directions, is an equivalence relation.

**Part B: $\sim_T$ is a congruence (part 1).**

4. Let $\varphi \sim_T \varphi'$ and $\psi \sim_T \psi'$.
5. From $T \vdash \varphi' \to \varphi$, T6 and MP give $T \vdash \neg \varphi \to \neg \varphi'$.
6. In the same way $T \vdash \neg \varphi' \to \neg \varphi$, so $\neg \varphi \sim_T \neg \varphi'$.
7. From $T \cup \set{\varphi \to \psi, \varphi'}$, MP with $\varphi' \to \varphi$ derives $\varphi$.
8. Then MP derives $\psi$, and MP with $\psi \to \psi'$ derives $\psi'$.
9. DT twice gives $T \vdash (\varphi \to \psi) \to (\varphi' \to \psi')$.
10. The other direction is the same with primed and unprimed formulas exchanged, so $\varphi \to \psi \sim_T \varphi' \to \psi'$.
11. So the operations on classes are well defined, also for $\land$, $\lor$, $\top$, $\bot$, which are defined from $\neg$ and $\to$.

**Part C: meets.**

12. T4 gives $\vdash \neg \varphi \to (\varphi \to \neg \psi)$.
13. T6 and MP give $\vdash \neg (\varphi \to \neg \psi) \to \neg \neg \varphi$.
14. HS with T2 gives $\vdash \neg(\varphi \to \neg \psi) \to \varphi$, that is $\varphi \land \psi \le \varphi$.
15. A1 gives $\vdash \neg \psi \to (\varphi \to \neg \psi)$.
16. T6, MP and then HS with T2 give $\vdash \neg (\varphi \to \neg \psi) \to \psi$, that is $\varphi \land \psi \le \psi$.
17. T7 with $\neg \psi$ for $\psi$ gives $\vdash \varphi \to (\neg \neg \psi \to \neg(\varphi \to \neg \psi))$.
18. So from $\varphi$ and $\psi$, T3, step 17 and MP derive $\varphi \land \psi$.
19. Let $\chi \le \varphi$ and $\chi \le \psi$. From $T \cup \set{\chi}$ we derive $\varphi$, $\psi$, and then $\varphi \land \psi$ by step 18.
20. DT gives $\chi \le \varphi \land \psi$, so $[\varphi \land \psi]$ is the greatest lower bound of $[\varphi]$ and $[\psi]$.

**Part D: joins.**

21. From $\varphi$ and $\neg \varphi$, T4 and MP twice derive $\psi$; DT twice gives $\vdash \varphi \to (\neg \varphi \to \psi)$.
22. So $\varphi \le \varphi \lor \psi$, since $\varphi \lor \psi$ is $\neg \varphi \to \psi$.
23. A1 gives $\vdash \psi \to (\neg \varphi \to \psi)$, so $\psi \le \varphi \lor \psi$.
24. Let $\varphi \le \chi$ and $\psi \le \chi$. From $T \cup \set{\neg \varphi \to \psi}$, HS derives $\neg \varphi \to \chi$.
25. T8 is $(\varphi \to \chi) \to ((\neg \varphi \to \chi) \to \chi)$, and MP twice derives $\chi$.
26. DT gives $\varphi \lor \psi \le \chi$, so $[\varphi \lor \psi]$ is the least upper bound.

**Part E: bounds (part 3).**

27. $\vdash \top$ by T1, since $\top$ is $p_0 \to p_0$.
28. A1 gives $\vdash \top \to (\varphi \to \top)$, and MP gives $\varphi \le \top$; so $[\top]$ is the top.
29. If $T \vdash \varphi$, then A1 and MP give $\top \le \varphi$, so $[\varphi] = 1$.
30. If $[\varphi] = 1$, then $T \vdash \top \to \varphi$, and MP with step 27 gives $T \vdash \varphi$.
31. From $\neg \top$, T4 and MP give $\top \to \varphi$, then step 27 and MP give $\varphi$.
32. DT gives $\bot \le \varphi$, so $[\bot]$ is the bottom.

**Part F: distributivity.**

33. Claim: $\varphi \land \chi \le \psi$ iff $\chi \le \varphi \to \psi$.
34. If $\chi \le \varphi \to \psi$: from $\varphi \land \chi$, steps 14 and 16 derive $\varphi$ and $\chi$, then MP derives $\varphi \to \psi$ and $\psi$.
35. DT gives $\varphi \land \chi \le \psi$.
36. If $\varphi \land \chi \le \psi$: from $\chi$ and $\varphi$, step 18 derives $\varphi \land \chi$, then MP derives $\psi$.
37. DT twice gives $\chi \le \varphi \to \psi$, which proves the claim.
38. Write $a = [\varphi]$, $b$, $c$ for classes, and $x = (a \land b) \lor (a \land c)$.
39. Then $a \land b \le x$ and $a \land c \le x$, so $b \le a \to x$ and $c \le a \to x$ by step 33.
40. So $b \lor c \le a \to x$ by step 26, and $a \land (b \lor c) \le x$ by step 33.
41. The inequality $x \le a \land (b \lor c)$ holds in every lattice, so the lattice is [[distributive|0HM0HQCK6N]].

**Part G: complements (part 2).**

42. $\varphi \lor \neg \varphi$ is $\neg \varphi \to \neg \varphi$, which is derivable by T1, so $[\varphi] \lor [\neg \varphi] = 1$ by step 29.
43. From $\varphi \land \neg \varphi$, steps 14 and 16 derive $\varphi$ and $\neg \varphi$; T4 and MP derive any $\psi$.
44. So $[\varphi] \land [\neg \varphi] = 0$, and $[\neg \varphi]$ is the [[complement|ZT47BK9Y6K]] of $[\varphi]$.
45. By Parts C to G, $\mathbf{L}_T$ is a complemented distributive lattice, that is a [[Boolean algebra|0XADJKM699]].
46. By T2, T3 and Part B, $[\varphi \to \psi] = [\neg \neg \varphi \to \psi] = \neg [\varphi] \lor [\psi]$.

**Part H: freeness (part 4).**

47. Let $T = \emptyset$, let $B$ be a Boolean algebra, and let $f \colon P \to B$.
48. Define $v(p) = f(p)$, $v(\neg \varphi) = \neg v(\varphi)$ and $v(\varphi \to \psi) = \neg v(\varphi) \lor v(\psi)$, by recursion on formulas.
49. A1 has the value $\neg a \lor \neg b \lor a = 1$, where $a = v(\varphi)$, $b = v(\psi)$.
50. For A2, put $u = \neg a \lor \neg b \lor c$; this is the value of $\varphi \to (\psi \to \chi)$.
51. The value of $(\varphi \to \psi) \to (\varphi \to \chi)$ is $(a \land \neg b) \lor \neg a \lor c = u$, by distributivity.
52. So A2 has the value $\neg u \lor u = 1$.
53. A3 has the value $(\neg b \land a) \lor (\neg b \land \neg a) \lor b = \neg b \lor b = 1$.
54. If $v(\varphi) = 1$ and $\neg v(\varphi) \lor v(\psi) = 1$, then $v(\psi) = 1$; so MP keeps the value $1$.
55. By induction on derivations, $\vdash \varphi$ implies $v(\varphi) = 1$.
56. In $B$, $\neg a \lor b = 1$ iff $a \le b$; so $\varphi \le \psi$ implies $v(\varphi) \le v(\psi)$.
57. So $\varphi \sim_\emptyset \psi$ implies $v(\varphi) = v(\psi)$, and $h([\varphi]) = v(\varphi)$ is well defined.
58. $h$ preserves $\neg$ and $\to$ by step 48, so it preserves $\land$, $\lor$, $0$, $1$ by their definitions.
59. $h([p]) = f(p)$ by step 48.
60. Let $h'$ be a second homomorphism with $h'([p]) = f(p)$.
61. By [[structural induction|12MQ2NJ29A]] with step 46, $h'([\varphi]) = h([\varphi])$ for every formula $\varphi$.
62. So $h$ is the only extension of $f$, and $\mathbf{L}_\emptyset$ is free over $p \mapsto [p]$. $\blacksquare$

## Idea

Every Boolean law that we need is a provable formula of L, and the basic theorems T1 to T8 give each of them.
The deduction theorem turns derivations from hypotheses into the inequalities of the order.
Residuation, $\varphi \land \chi \le \psi$ iff $\chi \le \varphi \to \psi$, gives distributivity without a long computation.
Freeness is soundness in an arbitrary Boolean algebra.

## Variants

1. One can first prove the [[completeness theorem|81ZNY1XKYJ]], and then compare formulas by their truth functions.
   That proof is shorter, but then the theorem cannot be used to prove completeness.
2. With $\land$, $\lor$, $\neg$, $\top$, $\bot$ as primitive connectives, the proof checks the Boolean axioms one by one for a calculus in these connectives.
3. The same proof with the axioms of intuitionistic logic, without T2, gives a Heyting algebra.
