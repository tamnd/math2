---
tag: PBQEYP9XTM
kind: proof
name: Proof of Karp's theorem
msc: ["03C75", "03C07"]
topics: [N64R1MGDBN]
audience: grad
proves: KAWWZ2DF0G
uses: [EWB8KXZMCV, 5HPW3GCJW3, PQG7VAZ1R2, 2RE7YAZK8R, 6F2DB4HTJR]
methods: [12MQ2NJ29A, 0J0XBKG64S, TFQ1845T84, 01XM7JEKHY]
sources:
  - url: https://en.wikipedia.org/wiki/Infinitary_logic
    locator: Concepts expressible in infinitary logic
  - book: isbn:9780521587136
    locator: Chapter 3
---

## Proof

We prove $1 \Rightarrow 2 \Rightarrow 1$ and $1 \Leftrightarrow 3$, and then the countable case.
For a finite map $p$ and a tuple $\bar a$ in its domain, $p\bar a$ is the tuple of images.

### From a system to infinitary equivalence

Let $I$ be a [[back-and-forth system|EWB8KXZMCV]].
By [[structural induction|12MQ2NJ29A]] on a formula $\varphi(\bar x)$ of $L_{\infty\omega}$ we show: for all $p \in I$ and $\bar a$ in $\operatorname{dom} p$, $\mathcal{A} \models \varphi[\bar a] \iff \mathcal{B} \models \varphi[p\bar a]$.

1. *Atomic.* $p$ is a partial isomorphism.
2. *Negation, and conjunction or disjunction of a set $\Phi$.* The claim for each member of $\Phi$ gives the claim for the whole.
3. *$\exists y \, \psi$.* Let $\mathcal{A} \models \psi[\bar a, a]$. Forth gives $q \supseteq p$ in $I$ with $a \in \operatorname{dom} q$. By the hypothesis for $\psi$ and $q$, $\mathcal{B} \models \psi[q\bar a, q(a)]$, and $q\bar a = p\bar a$. So $\mathcal{B} \models \exists y \, \psi[p\bar a]$.
4. The converse uses back, and $\forall y \, \psi$ is $\neg\exists y \, \neg\psi$.
5. For a sentence take any $p \in I$, which exists as $I \ne \emptyset$.

### From infinitary equivalence to a system

Let $\mathcal{A} \equiv_{\infty\omega} \mathcal{B}$.
Let $I$ be the set of finite maps $\bar a \mapsto \bar b$ such that $\mathcal{A} \models \varphi[\bar a] \iff \mathcal{B} \models \varphi[\bar b]$ for every $L_{\infty\omega}$ formula $\varphi(\bar x)$.

1. The empty map lies in $I$, by the hypothesis. Each member is a partial isomorphism, as atomic formulas, equations included, are preserved.
2. *Forth.* Let $\bar a \mapsto \bar b$ be in $I$ and $a \in A$. Suppose, for a [[contradiction|0J0XBKG64S]], that no $b \in B$ gives $\bar a a \mapsto \bar b b$ in $I$.
3. For each $b \in B$ choose $\psi_b(\bar x, y)$ with $\mathcal{A} \models \psi_b[\bar a, a]$ and $\mathcal{B} \not\models \psi_b[\bar b, b]$, negating a formula if needed.
4. $B$ is a set, and all $\psi_b$ have free variables among $\bar x, y$. So $\chi = \exists y \bigwedge_{b \in B} \psi_b$ is a formula of $L_{\infty\omega}$.
5. $\mathcal{A} \models \chi[\bar a]$, with witness $a$. So $\mathcal{B} \models \chi[\bar b]$, and some $b'$ satisfies every $\psi_b$, including $\psi_{b'}$, against step 3.
6. *Back* is the same with the roles of $\mathcal{A}$ and $\mathcal{B}$ exchanged.

### Games and the countable case

1. *$1 \Rightarrow 3$.* Duplicator keeps the current position inside some member of $I$ and answers a move by forth or back.
2. *$3 \Rightarrow 1$.* The finite positions reached in plays that follow a winning strategy form a back-and-forth system: the empty position is one, and the strategy extends each position in both directions.
3. *Countable case.* If $\mathcal{A}$ and $\mathcal{B}$ are countable and $I$ exists, the [[back-and-forth method|6F2DB4HTJR]] builds an isomorphism as the union of a chain in $I$. An isomorphism gives a system, its finite restrictions.

## Idea

Agreement on all infinitary formulas is itself a back-and-forth system.
Forth holds because a failure could be written down: a conjunction over all of $B$ of formulas that rule out each candidate $b$.
That conjunction is legal in $L_{\infty\omega}$, which is why the infinitary logic matches back-and-forth exactly.

## Variants

- The same argument with ordinal-indexed systems matches $L_{\infty\omega}$ sentences of each quantifier rank.
- In first-order logic the conjunction over $B$ is not allowed. For finite relational signatures, the [[Ehrenfeucht-Fraïssé theorem|72BMYXGFA8]] replaces it by a finite conjunction, at the price of bounding the number of rounds.
