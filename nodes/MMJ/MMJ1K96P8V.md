---
tag: MMJ1K96P8V
kind: proof
name: Proof of De Morgan's laws in a Boolean algebra
msc: ["06E05"]
proves: 0XYVDWGQX2
uses: [06GKBTAA5E]
sources:
  - url: https://proofwiki.org/wiki/De_Morgan's_Laws_(Boolean_Algebras)
---

## Proof

We show that $\neg a \wedge \neg b$ is a complement of $a \vee b$, and then use that complements are unique.
All axioms quoted are those of the definition of a [[Boolean algebra|06GKBTAA5E]] $A$.

1. Let $u \in A$. By commutativity and the identity axiom, $0 \vee u = u$ and $1 \wedge u = u$.
2. Let $u \in A$. Absorption gives $0 \wedge (0 \vee u) = 0$. By step 1, $0 \vee u = u$, so $0 \wedge u = 0$.
3. In the same way, absorption gives $1 \vee (1 \wedge u) = 1$. By step 1, $1 \wedge u = u$, so $1 \vee u = 1$.
4. Uniqueness of complements. Let $u, x \in A$ with $u \vee x = 1$ and $u \wedge x = 0$. We claim $x = \neg u$.
5. By the identity, complement and distributive axioms, $x = x \wedge 1 = x \wedge (u \vee \neg u) = (x \wedge u) \vee (x \wedge \neg u)$.
6. By commutativity, $x \wedge u = u \wedge x = 0$. So by step 1, step 5 gives $x = x \wedge \neg u$.
7. In the same way, $\neg u = \neg u \wedge (u \vee x) = (\neg u \wedge u) \vee (\neg u \wedge x) = 0 \vee (\neg u \wedge x) = \neg u \wedge x$. Here $\neg u \wedge u = u \wedge \neg u = 0$.
8. By commutativity, $x \wedge \neg u = \neg u \wedge x$. So steps 6 and 7 give $x = \neg u$, which proves the claim of step 4.
9. Now fix $a, b \in A$. By associativity and commutativity of $\vee$, $(a \vee b) \vee \neg a = (a \vee \neg a) \vee b = 1 \vee b$. By step 3 this is $1$.
10. In the same way, $(a \vee b) \vee \neg b = a \vee (b \vee \neg b) = a \vee 1 = 1 \vee a = 1$.
11. By distributivity, $(a \vee b) \vee (\neg a \wedge \neg b) = ((a \vee b) \vee \neg a) \wedge ((a \vee b) \vee \neg b)$. By steps 9 and 10 this is $1 \wedge 1 = 1$.
12. By associativity and commutativity of $\wedge$, $(\neg a \wedge \neg b) \wedge a = (a \wedge \neg a) \wedge \neg b = 0 \wedge \neg b$. By step 2 this is $0$.
13. In the same way, $(\neg a \wedge \neg b) \wedge b = \neg a \wedge (b \wedge \neg b) = \neg a \wedge 0 = 0 \wedge \neg a = 0$.
14. By commutativity and distributivity, $(a \vee b) \wedge (\neg a \wedge \neg b) = ((\neg a \wedge \neg b) \wedge a) \vee ((\neg a \wedge \neg b) \wedge b)$. By steps 12 and 13 this is $0 \vee 0 = 0$.
15. By steps 11 and 14, the element $x = \neg a \wedge \neg b$ satisfies the hypotheses of step 4 with $u = a \vee b$. So $\neg(a \vee b) = \neg a \wedge \neg b$.
16. For the second law, we check that $\neg a \vee \neg b$ is a complement of $a \wedge b$. By commutativity and distributivity, $(a \wedge b) \vee (\neg a \vee \neg b) = ((\neg a \vee \neg b) \vee a) \wedge ((\neg a \vee \neg b) \vee b)$.
17. By associativity and commutativity, $(\neg a \vee \neg b) \vee a = (a \vee \neg a) \vee \neg b = 1 \vee \neg b = 1$, using step 3.
18. In the same way, $(\neg a \vee \neg b) \vee b = \neg a \vee (b \vee \neg b) = \neg a \vee 1 = 1 \vee \neg a = 1$.
19. By steps 16 to 18, $(a \wedge b) \vee (\neg a \vee \neg b) = 1 \wedge 1 = 1$.
20. By distributivity, $(a \wedge b) \wedge (\neg a \vee \neg b) = ((a \wedge b) \wedge \neg a) \vee ((a \wedge b) \wedge \neg b)$.
21. By associativity and commutativity, $(a \wedge b) \wedge \neg a = (a \wedge \neg a) \wedge b = 0 \wedge b = 0$, using step 2.
22. In the same way, $(a \wedge b) \wedge \neg b = a \wedge (b \wedge \neg b) = a \wedge 0 = 0 \wedge a = 0$.
23. By steps 20 to 22, $(a \wedge b) \wedge (\neg a \vee \neg b) = 0 \vee 0 = 0$.
24. By steps 19 and 23 and step 4 with $u = a \wedge b$, we get $\neg(a \wedge b) = \neg a \vee \neg b$. This proves both laws for all $a, b \in A$.

## Idea

An element has only one complement: one element that joins with it to $1$ and meets it in $0$.
So to find $\neg(a \vee b)$ it is enough to guess a candidate and check the two complement equations.
The candidate $\neg a \wedge \neg b$ passes both checks by distributivity, and the second law works the same way with the roles of $\wedge$ and $\vee$ swapped.
