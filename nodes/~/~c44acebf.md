---
tag: ~c44acebf
kind: statement
role: theorem
name: Solution of Tarski's problems for free groups
aliases: [sela-theorem-on-free-groups, kharlampovich-myasnikov-theorem]
msc: ["20E05", "03C60", "20F10"]
topics: [BAZT8JJ70S]
audience: research
about: [0KTW26C80J, P3B1V182N4]
uses: [3TZW7W8N6A, ~0757d1ee, 0KTW26C80J, P3B1V182N4, CGH8C8EA9N, HWC687ES0Q]
history:
  first_stated: "around 1945"
  posed_by: "Alfred Tarski"
  notes: "Answered by Zlil Sela (Geometric and Functional Analysis 16, 2006) and by Olga Kharlampovich and Alexei Myasnikov (Journal of Algebra 302, 2006)."
sources:
  - url: https://en.wikipedia.org/wiki/Free_group
    locator: Tarski's problems
  - url: https://en.wikipedia.org/wiki/Elementary_equivalence
    locator: Elementary embeddings
---

## Statement

For $n \ge 1$, let $F_n$ be the [[free group|0KTW26C80J]] with basis $a_1, \ldots, a_n$.
[[Tarski asked two questions|3TZW7W8N6A]] about the [[elementary theory|~0757d1ee]] of these groups: whether all $F_n$ with $n \ge 2$ have the same elementary theory, and whether this theory is decidable.
The answer to both questions is yes.

**Theorem (Sela; Kharlampovich-Myasnikov).**

1. For all $m, n \ge 2$, the groups $F_m$ and $F_n$ are [[elementarily equivalent|P3B1V182N4]].
2. For $2 \le k \le n$, the inclusion $F_k \to F_n$ with $a_i \mapsto a_i$ for $1 \le i \le k$ is an [[elementary embedding|CGH8C8EA9N]].
3. The common elementary theory of the groups $F_n$ with $n \ge 2$ is [[decidable|HWC687ES0Q]].

Part 1 follows from part 2, since an elementary embedding $F_2 \to F_n$ gives $F_2 \equiv F_n$ for each $n \ge 2$.

## Remarks

### Why each hypothesis is needed

1. The rank must be at least $2$. The group $F_1 \cong \mathbb{Z}$ satisfies $\forall x \forall y \, (x y = y x)$, and $F_2$ does not, because $a_1 a_2$ and $a_2 a_1$ are different [[reduced words|0KBTP8Q2FS]]. The group $F_0$ is trivial, so it satisfies $\forall x \, (x = e)$.
2. The groups must be free. The [[free abelian group|0WJX8MGG37]] $\mathbb{Z}^2$ has two generators, but it is abelian, so $\mathbb{Z}^2 \not\equiv F_2$. In contrast with part 1, $\mathbb{Z}^m \equiv \mathbb{Z}^n$ only for $m = n$, by [[Szmielew's theorem|~efe20356]], because $\mathbb{Z}^n / p\mathbb{Z}^n$ has dimension $n$ over $\mathbb{F}_p$.
3. In part 2 the embedding must be the standard one. The map $F_2 \to F_2$ with $a_1 \mapsto a_1^2$ and $a_2 \mapsto a_2$ is injective, but it is not elementary: see the L2 explanation.

### Consequences

1. Each first-order sentence that is true in $F_2$ is true in every $F_n$ with $n \ge 2$, and conversely.
2. The groups $F_2 \subseteq F_3 \subseteq \cdots$ form an elementary chain by part 2. The union of an elementary chain is an elementary extension of each member, so the free group of countably infinite rank is also elementarily equivalent to $F_2$.
3. The elementary theory of a non-abelian free group can be decided by an algorithm, by part 3.
4. Sela also proved that this theory is [[stable|T7JW5QY6KR]].

### Converse

The converse question asks whether every group elementarily equivalent to $F_2$ is free.
The answer is no.
For a closed orientable [[surface|VGJJVBZ1MQ]] of [[genus|NJ787GZS1N]] at least $2$, the [[fundamental group|S1XK3HXHFX]] is elementarily equivalent to $F_2$, but it is not a free group.
The finitely generated groups that are elementarily equivalent to $F_2$ are called elementary free groups, and the work on Tarski's problems describes them.

### Generalizations

Sela extended the methods to torsion-free [[hyperbolic groups|JWJ8YPR7EB]] and classified them up to elementary equivalence.
The methods also give a theory of equations over free groups, often called algebraic geometry over groups.

## History

Alfred Tarski asked the two questions around 1945.
Makanin proved that the solvability of a system of equations over a free group is decidable, and Razborov described the set of all solutions of such a system.
Zlil Sela answered the first question in a series of papers; the final paper, "Diophantine geometry over groups VI: The elementary theory of a free group", appeared in Geometric and Functional Analysis 16 in 2006.
Olga Kharlampovich and Alexei Myasnikov answered both questions in "Elementary theory of free non-abelian groups", Journal of Algebra 302, 2006.

## Explanations

### L1 human

A free group on two letters $a$ and $b$ consists of all words in $a$, $b$ and their inverses, such as $a b a^{-1}$, where we cancel $a a^{-1}$ and $b b^{-1}$.
A free group on three letters is larger and has more words.
Tarski asked whether a sentence of the language of groups can ever tell the two groups apart.
For example, the sentence "there are two elements $x$ and $y$ with $xy \ne yx$" is true in both groups.
Many decades later, Sela and, independently, Kharlampovich and Myasnikov proved that no sentence tells them apart.
They also showed that there is an algorithm that decides whether a sentence is true in a free group on two letters.

### L2 human

We check two of the claims of the remarks: that $F_1 \not\equiv F_2$, and that a non-standard embedding of $F_2$ in itself is not elementary.
We write $a = a_1$ and $b = a_2$.

1. Let $\varphi$ be $\forall x \forall y \, (x y = y x)$. The group $F_1 = \langle a \rangle$ is cyclic, so $F_1 \models \varphi$.
2. In $F_2$ the reduced words $ab$ and $ba$ are different, so $F_2 \models \neg \varphi$. Hence $F_1 \not\equiv F_2$.
3. Let $f \colon F_2 \to F_2$ be the homomorphism with $f(a) = a^2$ and $f(b) = b$. A nonempty reduced word in $a, b$ goes to a word with nonzero powers $a^{2k}$ and $b^{l}$ in turn, which is again nonempty and reduced. So $f$ is injective.
4. Let $\psi(x)$ be the formula $\exists y \, (y y = x)$. In $F_2$, the element $f(a) = a^2$ satisfies $\psi$, with $y = a$.
5. The element $a$ does not satisfy $\psi$ in $F_2$. The [[group homomorphism|0JYTG5K9Y4]] $F_2 \to \mathbb{Z}^2$ with $a \mapsto (1, 0)$ and $b \mapsto (0, 1)$ would map $y$ with $y^2 = a$ to an element $v$ with $2v = (1, 0)$, and no such $v$ exists in $\mathbb{Z}^2$.
6. An elementary embedding $f$ must satisfy: $F_2 \models \psi(a)$ if and only if $F_2 \models \psi(f(a))$. Steps 4 and 5 show that this fails, so $f$ is not elementary.

The typical use of this kind of check is to separate groups or embeddings by one formula.
The trap is that part 2 of the theorem is about the standard embedding only, where each basis element goes to a basis element.

### L3 human

The theorem places the non-abelian free groups among the structures with a tame model theory: one complete, decidable and stable theory is shared by all of them.
The proofs pass through the study of equations over free groups.
Makanin-Razborov diagrams describe the solution sets of systems of equations, and limit groups, also called finitely generated fully residually free groups, play the role of the irreducible varieties of algebraic geometry.
Sela's approach uses actions of groups on real trees, and the approach of Kharlampovich and Myasnikov is combinatorial and algebraic.
In the later sub-areas, [[presentations|0JGEQXQ4AC]], [[free groups|0KTW26C80J]] and [[hyperbolic groups|JWJ8YPR7EB]] provide the group-theoretic background of these methods.
In contrast with the theory of all groups, which is undecidable, and with [[Szmielew's theorem|~efe20356]] for abelian groups, this result shows a decidable theory for a class of groups that are far from abelian.
