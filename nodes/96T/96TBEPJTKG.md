---
tag: 96TBEPJTKG
kind: proof
name: Proof of the exponential model property of two-variable logic
msc: ["03B25", "03C13"]
topics: [E4AVTNWE9E]
audience: research
proves: S7C3C7DJRF
uses: [983GZBQYT4, 1WTCZB4DVB, 12MQ2NJ29A, ESPYW94XGR]
methods: [01XM7JEKHY, 0WCP0PVET6, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Two-variable_logic
    locator: lead section
---

## Proof

We first bring the sentence to Scott normal form, then we cut a model of the normal form down to an exponential size, and last we read off the decision procedure.
The construction of part 2 follows Grädel, Kolaitis and Vardi.
Parts 1, 2 and 3 refer to the [[statement|S7C3C7DJRF]].

### Part 1: naming the innermost quantifier

1. Let $\varphi_0 = \varphi$.
   While $\varphi_j$ contains a quantifier, choose an occurrence of a subformula $Q v \, \theta$ with $Q \in \{ \exists, \forall \}$ and $\theta$ quantifier-free.
   Let $w$ be the other variable, so that $\{ v, w \} = \{ x, y \}$.
2. Take a new unary symbol $P_j$.
   Let $\varphi_{j+1}$ be $\varphi_j$ with this occurrence replaced by $P_j(w)$, and let $\delta_j$ be $\forall w \, (P_j(w) \leftrightarrow Q v \, \theta)$.
3. The free variables of $Q v \, \theta$ are among $\{ w \}$.
   So in a structure that satisfies $\delta_j$, the formulas $P_j(w)$ and $Q v \, \theta$ have the same truth value under every assignment.
4. Hence, in a structure that satisfies $\delta_j$, the formulas $\varphi_j$ and $\varphi_{j+1}$ have the same truth value under every assignment.
   This follows by [[structural induction|12MQ2NJ29A]] on the context of the occurrence, with the clauses of [[satisfaction|1WTCZB4DVB]].
5. Each step removes one quantifier, so the process stops after $k$ steps with a quantifier-free $\varphi_k$, where $k$ is the number of quantifiers of $\varphi$.
6. Let $\mathcal{A}$ satisfy $\delta_0, \ldots, \delta_{k-1}$.
   By step 4, $\varphi_k$ has the truth value of the sentence $\varphi$ under every assignment.
   So $\mathcal{A} \models \varphi$ if and only if $\mathcal{A} \models \forall x \, \forall y \, \varphi_k$.

### Part 1: the shape of the normal form

7. For $Q = \exists$, $\delta_j$ is equivalent to $\forall w \, \forall v \, (\theta \to P_j(w)) \wedge \forall w \, \exists v \, (P_j(w) \to \theta)$.
   The second conjunct uses that the domain is nonempty: if $P_j(w)$ is false, every $v$ works.
8. For $Q = \forall$, $\delta_j$ is equivalent to $\forall w \, \forall v \, (P_j(w) \to \theta) \wedge \forall w \, \exists v \, (\theta \to P_j(w))$.
   The second conjunct says that $P_j(w)$ holds or some $v$ makes $\theta$ false.
9. If $w$ is $y$, we exchange the names $x$ and $y$ in the conjunct.
   This gives an equivalent sentence with prefix $\forall x \, \forall y$ or $\forall x \, \exists y$.
10. Let $\chi$ be the conjunction of $\varphi_k$ and of the matrices of the $\forall \forall$ conjuncts.
    Let $\chi_1, \ldots, \chi_m$ be the matrices of the $\forall \exists$ conjuncts, and add the conjunct $\forall x \, \exists y \, (x = y)$, so that $m \ge 1$.
11. Let $\psi = \forall x \, \forall y \, \chi \wedge \bigwedge_{i=1}^m \forall x \, \exists y \, \chi_i$.
    Each $\theta$ has length at most $\lvert \varphi \rvert$, so $\psi$ has length $O(\lvert \varphi \rvert^2)$, and it is computed in polynomial time.
12. A model of $\psi$ satisfies every $\delta_j$, by steps 7 and 8, and it satisfies $\forall x \, \forall y \, \varphi_k$.
    By step 6, it satisfies $\varphi$.
13. Let $\mathcal{A} \models \varphi$.
    Interpret $P_0, P_1, \ldots$ in this order, with $P_j$ the set of elements $a$ such that $Q v \, \theta$ holds when $w$ is $a$; this uses only symbols that are already interpreted.
    Then each $\delta_j$ holds, and by step 6 also $\forall x \, \forall y \, \varphi_k$ holds, so the expansion is a model of $\psi$.

### Part 2: types

Let $L'$ be the signature of $\psi$, and let $u$ be the number of its symbols.

14. The 1-type of an element $a$ is the set of atomic formulas $P(x)$ and $R(x, x)$ that hold at $a$.
    There are at most $2^u$ 1-types.
15. For $a \neq b$, the 2-type of $(a, b)$ is the set of atomic formulas in $x$ and $y$ that hold when $x$ is $a$ and $y$ is $b$.
    It contains the 1-type of $a$ written in $x$, the 1-type of $b$ written in $y$, and the facts $R(x, y)$ and $R(y, x)$ that hold.
16. For a quantifier-free $\chi(x, y)$, the truth of $\chi$ at $(a, b)$ with $a \neq b$ depends only on the 2-type of $(a, b)$.
    The truth of $\chi$ at $(a, a)$ depends only on the 1-type of $a$, since $x = y$ is then true.
17. Conversely, to define an $L'$-structure on a set $D$, it is enough to give a 1-type to each element and a 2-type to each pair $e \neq f$.
    The 2-type must agree with the 1-types, and the type of $(f, e)$ must come from that of $(e, f)$ by exchanging $x$ and $y$.
    This works because every atomic fact involves at most two elements.

### Part 2: kings, the court and the new domain

18. Let $\mathcal{A} \models \psi$.
    A 1-type is royal if exactly one element of $\mathcal{A}$ has it, and that element is a king.
    Let $K$ be the set of kings and $\Pi$ the set of non-royal 1-types that occur in $\mathcal{A}$.
19. For each king $a$ and each $i$, choose $w_i(a)$ in $\mathcal{A}$ with $\mathcal{A} \models \chi_i[a, w_i(a)]$.
    The court $C$ is $K$ together with all the $w_i(a)$, so $\lvert C \rvert \le (m + 1) \lvert K \rvert$.
20. For each $\pi \in \Pi$, choose $r_\pi$ of type $\pi$ in $\mathcal{A}$.
    For each $i$, choose $s_{\pi, i}$ with $\mathcal{A} \models \chi_i[r_\pi, s_{\pi, i}]$.
21. Let $D$ be the disjoint union of $C$ and the set of triples $(\pi, j, i)$ with $\pi \in \Pi$, $j \in \{ 0, 1, 2 \}$ and $1 \le i \le m$.
    Give each $c \in C$ its 1-type in $\mathcal{A}$, and give $(\pi, j, i)$ the 1-type $\pi$.
    A royal type is then still carried by one element of $D$ only, its king.

### Part 2: the rules for pairs

22. Rule (a).
    Pairs inside $C$ get their 2-types in $\mathcal{A}$.
23. Rule (b).
    Let $e = (\pi, j, i')$ and $1 \le i \le m$, and put $s = s_{\pi, i}$.
    If $s = r_\pi$, nothing is assigned.
    If $s$ is a king, the pair $(e, s)$ gets the 2-type of $(r_\pi, s)$.
24. Otherwise $s$ has a type $\pi' \in \Pi$.
    Then the pair $(e, (\pi', j + 1 \bmod 3, i))$ gets the 2-type of $(r_\pi, s)$.
25. Rule (c).
    Let $c \in C \setminus K$ and $1 \le i \le m$, and choose $b$ with $\mathcal{A} \models \chi_i[c, b]$.
    If $b \in C$, nothing is assigned.
    Otherwise $b$ is not a king, so it has a type $\pi' \in \Pi$, and the pair $(c, (\pi', 0, i))$ gets the 2-type of $(c, b)$.
26. No pair gets two different 2-types.
    Rule (a) uses pairs inside $C$, rule (b) uses pairs of a triple with a king or with a triple, and rule (c) uses pairs of a non-king of $C$ with a triple.
27. Within rule (b), a pair $(e, s)$ with a king $s$ always gets the type of $(r_\pi, s)$, whatever $i$ is.
    A triple of level $j$ points only to level $j + 1 \bmod 3$, so two triples never point to each other.
    Different values of $i$ give targets with different last coordinates.
28. Within rule (c), different values of $i$ give different targets $(\pi', 0, i)$.
29. Rule (d).
    Every other pair $e \neq f$ gets the 2-type of some pair $a \neq b$ in $\mathcal{A}$ with the 1-types of $e$ and $f$.
    Such a pair exists, because $e$ or $f$ is a triple, whose 1-type is non-royal and so belongs to two elements of $\mathcal{A}$.
30. Each assigned 2-type is the 2-type of a pair in $\mathcal{A}$ whose 1-types match, so step 17 defines a structure $\mathcal{D}$ on $D$.

### Part 2: the small structure is a model

31. $\mathcal{D} \models \forall x \, \forall y \, \chi$.
    A pair $e \neq f$ has the 2-type of a pair $a \neq b$ of $\mathcal{A}$, and $\mathcal{A} \models \chi[a, b]$, so step 16 applies.
    The pair $(e, e)$ has the 1-type of some $a$, and $\mathcal{A} \models \chi[a, a]$.
32. Each king $a$ has a witness for $\chi_i$ in $\mathcal{D}$.
    The witness $w_i(a)$ lies in $C$, and rule (a) copies the 2-type from $\mathcal{A}$; if $w_i(a) = a$, step 16 applies to the 1-type.
33. Each $c \in C \setminus K$ has a witness by rule (c).
    It is $b$ itself if $b \in C$, and otherwise the triple $(\pi', 0, i)$, which has the 2-type of $(c, b)$ with $c$.
34. Each triple $e = (\pi, j, i')$ has a witness by rule (b).
    It is $e$ itself if $s = r_\pi$, the king $s$, or a triple with the 2-type of $(r_\pi, s)$, and in each case $\chi_i$ holds by step 16.
35. So $\mathcal{D} \models \psi$, and by step 12, $\mathcal{D} \models \varphi$.
    Since $\lvert K \rvert + \lvert \Pi \rvert \le 2^u$, the size is $\lvert D \rvert \le (m + 1) \lvert K \rvert + 3 m \lvert \Pi \rvert \le (4m + 1) 2^u$.
36. Here $u$ is at most the number of symbols of $\varphi$ plus $k$, and $m \le k + 1$, so $u$ and $m$ are at most $2 \lvert \varphi \rvert$.
    Hence $\lvert D \rvert \le (8 \lvert \varphi \rvert + 1) \cdot 4^{\lvert \varphi \rvert} \le 2^{c \lvert \varphi \rvert}$ for a constant $c$, and this proves part 2.

### Part 3: decidability and the upper bound

37. To decide whether $\varphi$ is satisfiable, compute $N = 2^{c \lvert \varphi \rvert}$ and test all structures for the symbols of $\varphi$ with at most $N$ elements.
    By part 2 this test is correct, and it always stops.
38. A nondeterministic algorithm guesses one structure with at most $N$ elements and checks $\varphi$ in it.
    The check of a formula with two variables takes time polynomial in $N$ and $\lvert \varphi \rvert$, so satisfiability is in NEXPTIME.
    This proves part 3.

## Idea

The Scott normal form turns every two-variable sentence into universal conditions on pairs plus one witness demand for each element.
Because only two variables occur, a structure is fixed by the 1-types of its elements and the 2-types of its pairs.
A small model keeps the elements whose 1-type is unique, with their witnesses, and adds three levels of copies of one representative of each other 1-type.
The copies in level $j$ take their witnesses from level $j + 1$, so no pair is asked to carry two different types.

## Variants

Mortimer's original proof of 1975 gave the finite model property with a larger bound.

Scott's reduction of 1962 shows that satisfiability of $\mathrm{FO}^2$ without equality reduces to the Gödel-Kalmár-Schütte class, which is decidable by the theorem on [[decidable prefix classes|ZF79MZRQ8V]].

For the counting extension $\mathrm{C}^2$ the small model method fails, since some satisfiable sentences have only infinite models.
Pratt-Hartmann's procedure instead uses integer programming on the numbers of elements of each type.
