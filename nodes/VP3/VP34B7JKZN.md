---
tag: VP34B7JKZN
kind: proof
name: Proof that the one-sided group axioms define a group
topics: [BAZT8JJ70S]
audience: ug1
proves: FF2JMV4F9G
uses: [0K8F7PVDMX, 07WYQPB8E3, 0ZNZH0EXFX, D33V8HE0KY]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Group_(mathematics)
    locator: Elementary consequences of the group axioms
---

## Proof

We prove part 1 first.
Let $G$ have an associative operation, an element $e$ with $ea = a$ for all $a$, and for each $a$ an element $b$ with $ba = e$.

1. Fix $a \in G$, and choose $b \in G$ with $ba = e$. Reason: hypothesis on left inverses.
2. Choose $c \in G$ with $cb = e$. Reason: the same hypothesis, applied to the element $b$.
3. We have $ab = e(ab)$. Reason: $e$ is a left identity.
4. We have $e(ab) = (cb)(ab)$. Reason: $cb = e$ by step 2.
5. We have $(cb)(ab) = c(b(ab))$. Reason: associativity, with the three elements $c$, $b$ and $ab$.
6. We have $b(ab) = (ba)b$. Reason: associativity.
7. We have $(ba)b = eb = b$. Reason: $ba = e$ by step 1, and $e$ is a left identity.
8. By steps 5 to 7, $(cb)(ab) = cb$, and $cb = e$ by step 2.
9. By steps 3, 4 and 8, $ab = e$. So $b$ is also a right inverse of $a$, and $ab = e = ba$.
10. We have $ae = a(ba)$. Reason: $ba = e$ by step 1.
11. We have $a(ba) = (ab)a$. Reason: associativity.
12. We have $(ab)a = ea = a$. Reason: $ab = e$ by step 9, and $e$ is a left identity.
13. By steps 10 to 12, $ae = a$. So $e$ is also a right identity.
14. Step 13 holds for each $a \in G$, so $e$ is an identity element of $G$. Step 9 holds for each $a$, so each $a$ has the inverse $b$ with respect to $e$. With associativity, all three group axioms hold, and $G$ is a group.

Now we prove part 2.

15. Let $G$ have an associative operation with a right identity $e$ and right inverses. Define the [[opposite operation|D33V8HE0KY]] $a \ast b = ba$ on the same set.
16. The operation $\ast$ is associative. Reason: $(a \ast b) \ast c = c(ba)$ and $a \ast (b \ast c) = (cb)a$, and these are equal by associativity of the original operation.
17. For each $a$, $e \ast a = ae = a$, so $e$ is a left identity for $\ast$. If $ab = e$, then $b \ast a = ab = e$, so $b$ is a left inverse of $a$ for $\ast$.
18. By part 1, $(G, \ast)$ is a group with identity $e$, and $a \ast b = e = b \ast a$.
19. So $ea = a \ast e = a$ and $ae = e \ast a = a$, and $ab = ba = e$. Thus $e$ is a two-sided identity and $b$ is a two-sided inverse of $a$ for the original operation, and $G$ is a group. $\blacksquare$

## Idea

First we show that a left inverse is also a right inverse.
The trick is to write $e$ as $cb$, where $c$ is a left inverse of $b$, and then to move the parentheses.
Then $ae = a(ba) = (ab)a = ea = a$ shows that the left identity is also a right identity.
The right-sided case is the left-sided case for the reversed operation.
