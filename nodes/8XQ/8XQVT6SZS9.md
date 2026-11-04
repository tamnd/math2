---
tag: 8XQVT6SZS9
kind: proof
name: Proof of Stone's representation theorem for finite Boolean algebras
msc: ["06E05", "06E15"]
proves: 0DYS9C3HH5
uses: [06GKBTAA5E, 004J7ZEFAT, 011C29Q1S1, 0XYVDWGQX2]
sources:
  - url: https://www.macs.hw.ac.uk/~markl/1-stone-duality.pdf
    locator: Lemma 2.1, Lemma 2.2 and Theorem 2.3
---

## Proof

Let $B$ be a finite [[Boolean algebra|06GKBTAA5E]], with order $a \le b$ meaning $a \wedge b = a$.
Write $\varphi(b) = \set{x \in \operatorname{At}(B) : x \le b}$ for $b \in B$.
An isomorphism here is a bijection $B \to \mathcal{P}(\operatorname{At}(B))$ that sends $\wedge, \vee, \neg, 0, 1$ to $\cap, \cup$, complement in $\operatorname{At}(B)$, $\varnothing$ and $\operatorname{At}(B)$.
We first derive basic facts on the order, then on atoms.

1. For $u \in B$, absorption gives $u \wedge u = u \wedge (u \vee (u \wedge u)) = u$, since $u \vee (u \wedge u) = u$. In the same way $u \vee u = u$.
2. For $u \in B$, $0 \wedge u = 0$: absorption gives $0 \wedge (0 \vee u) = 0$, and $0 \vee u = u \vee 0 = u$. Also $u \wedge 1 = u$, so $u \le 1$.
3. The relation $\le$ is a [[partial order|011C29Q1S1]]. Reflexivity is step 1. If $a \le b$ and $b \le a$, then $a = a \wedge b = b \wedge a = b$.
4. Transitivity: if $a \le b$ and $b \le c$, then $a \wedge c = (a \wedge b) \wedge c = a \wedge (b \wedge c) = a \wedge b = a$.
5. If $a \le b$, then $a \vee b = (b \wedge a) \vee b = b \vee (b \wedge a) = b$ by absorption.
6. For $a, b \in B$, $a \wedge b \le a$, since $(a \wedge b) \wedge a = (a \wedge a) \wedge b = a \wedge b$ by step 1. Also $a \le a \vee b$, since $a \wedge (a \vee b) = a$ by absorption.
7. If $c \le a$ and $c \le b$, then $c \le a \wedge b$, since $c \wedge (a \wedge b) = (c \wedge a) \wedge b = c \wedge b = c$.
8. By steps 4, 6 and 7, for all $c, a, b \in B$: $c \le a \wedge b$ if and only if $c \le a$ and $c \le b$.
9. If $c \le 0$, then $c = c \wedge 0 = 0 \wedge c = 0$ by commutativity and step 2. So no atom lies below $0$, and $\varphi(0) = \varnothing$. By step 2, $\varphi(1) = \operatorname{At}(B)$.
10. Let $x$ be an atom and $b \in B$. We claim that exactly one of $x \le b$ and $x \le \neg b$ holds.
11. By step 6, $x \wedge b \le x$. If $x \wedge b \ne 0$, then $x \wedge b = x$ because $x$ is minimal in $B \setminus \set{0}$. So $x \le b$.
12. If $x \wedge b = 0$, then $x = x \wedge (b \vee \neg b) = (x \wedge b) \vee (x \wedge \neg b) = 0 \vee (x \wedge \neg b) = x \wedge \neg b$. So $x \le \neg b$.
13. If both held, step 8 would give $x \le b \wedge \neg b = 0$, so $x = 0$ by step 9. This is false for an atom, which proves the claim of step 10.
14. By step 10, $\varphi(\neg b) = \operatorname{At}(B) \setminus \varphi(b)$. By step 8, $\varphi(a \wedge b) = \varphi(a) \cap \varphi(b)$.
15. Let $x$ be an atom and $a, b \in B$. If $x \le a$ or $x \le b$, then $x \le a \vee b$ by steps 6 and 4.
16. Conversely, let $x \not\le a$ and $x \not\le b$. By step 10, $x \le \neg a$ and $x \le \neg b$. By step 8 and [[De Morgan's law|0XYVDWGQX2]], $x \le \neg a \wedge \neg b = \neg(a \vee b)$.
17. Then step 10 gives $x \not\le a \vee b$. With step 15, $\varphi(a \vee b) = \varphi(a) \cup \varphi(b)$.
18. Every nonzero $b \in B$ has an atom below it. Let $S = \set{y \in B \setminus \set{0} : y \le b}$. It contains $b$ and is finite.
19. Choose $y \in S$ for which the set $D(y) = \set{z \in B : z \le y}$ has the fewest elements. Let $z \ne 0$ with $z \le y$.
20. Then $z \le b$ by step 4, so $z \in S$, and $D(z) \subseteq D(y)$ by step 4. If $z \ne y$, then $y \notin D(z)$ by step 3, while $y \in D(y)$.
21. So $z \ne y$ would give $\abs{D(z)} < \abs{D(y)}$, against the choice of $y$. Hence $z = y$, so $y$ is an atom, and $y \le b$.
22. The map $\varphi$ is injective. Let $\varphi(a) = \varphi(b)$, and suppose $a \not\le b$. Put $c = a \wedge \neg b$.
23. If $c = 0$, then $a = a \wedge (b \vee \neg b) = (a \wedge b) \vee (a \wedge \neg b) = (a \wedge b) \vee 0 = a \wedge b$, so $a \le b$. Hence $c \ne 0$.
24. By step 18, some atom $x$ satisfies $x \le c$. By step 8, $x \le a$ and $x \le \neg b$.
25. So $x \in \varphi(a)$, and $x \notin \varphi(b)$ by step 10. This contradicts $\varphi(a) = \varphi(b)$, so $a \le b$.
26. By symmetry $b \le a$, so $a = b$ by step 3.
27. The map $\varphi$ is surjective. Let $T \subseteq \operatorname{At}(B)$, and list its elements as $t_1, \dots, t_k$. Put $s_0 = 0$ and $s_i = s_{i-1} \vee t_i$ for $1 \le i \le k$.
28. By step 9 and step 17, $\varphi(s_k) = \varphi(t_1) \cup \dots \cup \varphi(t_k)$, by induction on $k$.
29. For atoms $x$ and $t$, $x \le t$ holds if and only if $x = t$. Indeed $x \ne 0$ and $x \le t$ give $x = t$, by minimality of $t$.
30. So $\varphi(t_i) = \set{t_i}$ for each $i$, and $\varphi(s_k) = T$ by step 28.
31. By steps 22 to 30, $\varphi$ is a bijection from $B$ to $\mathcal{P}(\operatorname{At}(B))$. By steps 9, 14 and 17, it preserves $0$, $1$, $\neg$, $\wedge$ and $\vee$.
32. Hence $\varphi$ is an isomorphism from $B$ to the [[power set Boolean algebra|004J7ZEFAT]] of $\operatorname{At}(B)$.

## Idea

An atom is so small that for each element $b$ it lies either below $b$ or below $\neg b$, never both.
This makes "the set of atoms below $b$" respect and, or and not.
Finiteness gives an atom below every nonzero element, so two different elements are told apart by some atom, and every set of atoms is reached by its join.
