---
tag: CQ0QCQK5JT
kind: statement
role: theorem
name: Kamp's theorem
msc: ["03B44", "03C07"]
topics: [CQM9SRN8PM]
audience: research
uses: [8XB117FKKV, RMJ56ZPA63, 086QKPF0A6, 0FRXBVVR03, 0R3H5PANRQ, 0MWKJ44V5A, 08J2M1JYAG, YW6YGBMVQY]
about: [8XB117FKKV, RMJ56ZPA63]
proofs: [~7ebae795]
sources:
  - url: https://en.wikipedia.org/wiki/Kamp%27s_theorem
    locator: section Formal statement, section Other expressive completeness results
  - book: isbn:9780198537694
    locator: Gabbay, Hodkinson and Reynolds, Temporal Logic, volume 1
  - doi: 10.2168/LMCS-10(1:14)2014
    locator: Rabinovich, A proof of Kamp's theorem, Logical Methods in Computer Science 10 (2014)
  - wikipedia: en:83795911@r1373516405
    locator: Kamp's theorem
    note: adopted
    mention: wikipedia://en/83795911
    sections: [Statement]
same_as:
  wikidata: Q141285148
  wikipedia: Kamp's theorem
inventory: [AB8THS9G4H]
---

## Statement

Let $\mathcal{P}$ be a finite set of unary predicate symbols.
A *structure* is a [[linear order|0FRXBVVR03]] $(T, <)$ with a subset $P^T \subseteq T$ for each $P \in \mathcal{P}$.
Let $\mathrm{FOMLO}$ be the [[first-order logic|086QKPF0A6]] with the relations $<$, $=$ and the predicates of $\mathcal{P}$.
Let $\mathrm{TL}(U, S)$ be the [[temporal logic|8XB117FKKV]] with an atom $p$ for each $P \in \mathcal{P}$, the Boolean connectives, and the binary operators $U$ and $S$.
Their meaning is strict: $A \, U \, B$ holds at $t$ when some $u > t$ has $B$ and every $v$ with $t < v < u$ has $A$, and $S$ is the mirror image.

**Theorem (Kamp).**
Let $(T, <)$ be a Dedekind complete linear order: every nonempty subset with an upper bound has a [[least upper bound|0R3H5PANRQ]].
For every $\mathrm{FOMLO}$ formula $\varphi(x)$ with one free variable $x$, there is a $\mathrm{TL}(U, S)$ formula $A$ with the following property.
For every structure on $(T, <)$ and every $t \in T$, $\varphi(t)$ holds if and only if $A$ is true at $t$.

The formula $A$ depends only on $\varphi$, not on the order.
So the statement holds uniformly over the class of all Dedekind complete linear orders.
It includes the [[natural numbers|0MWKJ44V5A]], the integers and the [[real numbers|08J2M1JYAG]].
Conversely, every $\mathrm{TL}(U, S)$ formula is equivalent to an $\mathrm{FOMLO}$ formula with one free variable, by the [[standard translation|YW6YGBMVQY]].

## Remarks

### Why each hypothesis is needed

1. Dedekind completeness is needed. Over the rationals $(\mathbb{Q}, <)$, $U$ and $S$ are not expressively complete. Stavi found two further connectives that give expressive completeness over all linear orders.
2. Both $U$ and $S$ are needed on orders with a past, such as $\mathbb{Z}$ or $\mathbb{R}$: a formula with only $U$, evaluated at $t$, depends only on $t$ and the points after $t$. Over $\mathbb{N}$ with the initial point as reference, $X$ and $U$ alone suffice for sentences, by Gabbay, Pnueli, Shelah and Stavi.
3. The binary operators are needed. With only $F$ and $P$, the logic cannot express $U$ over $\mathbb{R}$. Over $\mathbb{N}$, the logic with $X$, $F$ and their past versions equals two-variable first-order logic, by Etessami, Vardi and Wilke, and it misses $U$.

### Consequences

1. Over $(\mathbb{N}, <)$, LTL with $X$ and $U$ has the expressive power of first-order logic on infinite words. So [[LTL|RMJ56ZPA63]] defines exactly the star-free $\omega$-regular languages.
2. Every first-order property of a time line can be checked with a temporal formula whose size depends only on the first-order formula. The size of $A$ is in general nonelementary in the size of $\varphi$. Otherwise first-order satisfiability over $(\mathbb{N}, <)$, which is nonelementary, would be elementary through LTL.
3. First-order logic over $(\mathbb{N}, <)$ needs only three variables, since $\mathrm{TL}(U, S)$ translates into its three-variable fragment.

### Generalizations

1. Gabbay's separation theorem: over a class of linear orders, expressive completeness of a temporal logic is equivalent to the separation property. Kamp's theorem follows from separation over Dedekind complete orders, see [[the proof|~7ebae795]].
2. Stavi's theorem: with the two Stavi connectives added, the logic is expressively complete over all linear orders.
3. Metric temporal logic is expressively complete for first-order logic over the reals with order and the functions $t \mapsto t + q$ for rational $q$, by Hunter, Ouaknine and Worrell (2013).

## History

Arthur Prior introduced the operators $F$, $P$, $G$ and $H$ in Time and Modality (1957).
Hans Kamp introduced $U$ and $S$, and proved the theorem, in his UCLA doctoral thesis "Tense Logic and the Theory of Linear Order" (1968).
Gabbay, Pnueli, Shelah and Stavi proved the version for $(\mathbb{N}, <)$ with future operators only in 1980.
Gabbay gave the proof by separation, and Rabinovich published a short self-contained proof in 2014.

## Explanations

### L1 human

First-order logic can say anything about a time line with variables for moments: "there is a later moment where it rains, and no earlier one where it snows".
Temporal logic has no variables, only words like "until" and "since".
Kamp's theorem says that, on time lines without gaps, "until" and "since" can say everything that the variable language can say about one moment.

### L2 human

We translate the first-order formula $\varphi(x) = \exists y\,\big(x < y \wedge Q(y) \wedge \forall z\,(x < z < y \to P(z))\big)$.

1. It says: some later $y$ has $Q$, and every point strictly between $x$ and $y$ has $P$.
2. This is the strict until at $x$: $\varphi(x)$ is equivalent to $p \, U \, q$.
3. Now take $\psi(x) = \exists y\,(y < x \wedge Q(y))$. This is $\top \, S \, q$, the past diamond $Pq$.
4. A formula such as $\exists y\,\exists y'\,(x < y < y' \wedge Q(y) \wedge Q(y'))$ is $\top \, U \, (q \wedge (\top \, U \, q))$.

The typical use is to show that a specification language based on $U$ and $S$ loses nothing against first-order logic.
A trap: the theorem is about one free variable; a first-order formula with two free variables has no direct temporal counterpart.

### L3 human

The proof goes through separation: every temporal formula is a Boolean combination of pure past, present and pure future formulas.
Then a quantifier $\exists y$ over a point is split into the cases $y < x$, $y = x$ and $y > x$, and each case is a temporal formula at $x$.
Separation holds over Dedekind complete orders but fails over $\mathbb{Q}$, where a formula can refer to a gap.
Other proofs use Ehrenfeucht and Fraïssé games, or purely syntactic rewriting as in Rabinovich's paper.
