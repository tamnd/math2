---
tag: GYEBFJM5FY
kind: proof
name: Proof of the Ehrenfeucht-Fraïssé theorem
msc: ["03C07", "03C13"]
topics: [N64R1MGDBN]
audience: grad
proves: 72BMYXGFA8
uses: [2RE7YAZK8R, 1DVRN1T2Z0, FVEVRE5XNZ, MQ2KK8P8NT, HYJ10AF6RT, MCZRXR3SVB]
methods: [12MQ2NJ29A, 0ASJVEFA9J, TFQ1845T84, 01XM7JEKHY]
sources:
  - url: https://en.wikipedia.org/wiki/Ehrenfeucht%E2%80%93Fra%C3%AFss%C3%A9_game
    locator: Equivalence and inexpressibility
  - book: isbn:9780521587136
    locator: Chapter 3
---

## Proof

We prove both implications, with the starting tuples $\bar a \in A^k$ and $\bar b \in B^k$.
We write $\mathcal{A} \models \varphi[\bar a]$ for satisfaction and $\bar a a$ for the tuple $\bar a$ extended by $a$.

### From a winning strategy to n-equivalence

Let $L$ be relational.
By [[structural induction|12MQ2NJ29A]] on a formula $\varphi(x_1, \dots, x_k)$, for all $k$, $n \ge \operatorname{qr}(\varphi)$ and tuples at once, we show: if Duplicator wins $G_n(\mathcal{A}, \bar a, \mathcal{B}, \bar b)$, then $\mathcal{A} \models \varphi[\bar a] \iff \mathcal{B} \models \varphi[\bar b]$.

1. *$\varphi$ atomic.* Any play of $G_n$ that follows the strategy ends in a partial isomorphism that contains $a_i \mapsto b_i$. Its restriction to $\bar a$ is a partial isomorphism, so $\bar a$ and $\bar b$ satisfy the same [[atomic formulas|MCZRXR3SVB]].
2. *$\neg\varphi$, $\varphi \wedge \psi$.* These follow from the claim for the parts, since the rank of the parts is at most $n$.
3. *$\exists y \, \psi$, with $\operatorname{qr}(\psi) \le n - 1$.* Let $\mathcal{A} \models \psi[\bar a a]$ for some $a \in A$. Let Spoiler pick $a$ in round 1, and let $b$ be Duplicator's answer.
4. The rest of the strategy wins $G_{n-1}(\mathcal{A}, \bar a a, \mathcal{B}, \bar b b)$. By the induction hypothesis for $\psi$, $\mathcal{B} \models \psi[\bar b b]$, so $\mathcal{B} \models \exists y \, \psi[\bar b]$.
5. The converse is the same with Spoiler picking in $\mathcal{B}$. The case $\forall y \, \psi$ follows from $\neg\exists y \, \neg\psi$.

### Hintikka formulas

Now let $L$ be finite and relational.
For an $L$-structure $\mathcal{A}$, a tuple $\bar a \in A^k$ and $m \ge 0$, define $\varphi^m_{\bar a}(x_1, \dots, x_k)$ by recursion on $m$.

1. $\varphi^0_{\bar a}$ is the conjunction of the atomic and negated atomic formulas in $x_1, \dots, x_k$ that $\bar a$ satisfies. There are finitely many atomic formulas, as $L$ is finite and has no function symbols.
2. $\varphi^{m+1}_{\bar a} = \bigwedge_{a \in A} \exists x_{k+1} \, \varphi^m_{\bar a a} \wedge \forall x_{k+1} \bigvee_{a \in A} \varphi^m_{\bar a a}$.
3. By [[induction|0ASJVEFA9J]] on $m$, for fixed $k$ only finitely many formulas $\varphi^m_{\bar a}$ occur, over all structures and tuples. For $m = 0$ there are finitely many sets of literals. For $m + 1$, $\varphi^{m+1}_{\bar a}$ is fixed by the set $\set{\varphi^m_{\bar a a} : a \in A}$, a subset of a finite set. So the conjunction and disjunction in step 2 are finite after removing repeats.
4. $\operatorname{qr}(\varphi^m_{\bar a}) = m$ for $m \ge 1$, and $0$ for $m = 0$, by the [[rules of rank|MQ2KK8P8NT]].
5. $\mathcal{A} \models \varphi^m_{\bar a}[\bar a]$, by induction on $m$: each $\exists$ is witnessed by $a$, and each $b \in A$ satisfies the disjunct for $a = b$.

### From n-equivalence to a winning strategy

We show by induction on $m$, for all $k$ and tuples: if $\mathcal{B} \models \varphi^m_{\bar a}[\bar b]$, then Duplicator wins $G_m(\mathcal{A}, \bar a, \mathcal{B}, \bar b)$.

1. *$m = 0$.* Then $\bar b$ satisfies exactly the atomic formulas that $\bar a$ satisfies. With the equations $x_i = x_j$ among them, $a_i \mapsto b_i$ is well defined and injective, so it is a partial isomorphism, and Duplicator wins.
2. *$m + 1$, Spoiler picks $a \in A$.* The conjunct $\exists x_{k+1} \, \varphi^m_{\bar a a}$ holds at $\bar b$, so some $b \in B$ has $\mathcal{B} \models \varphi^m_{\bar a a}[\bar b b]$. Duplicator answers $b$.
3. *$m + 1$, Spoiler picks $b \in B$.* The conjunct $\forall x_{k+1} \bigvee_a \varphi^m_{\bar a a}$ gives some $a \in A$ with $\mathcal{B} \models \varphi^m_{\bar a a}[\bar b b]$. Duplicator answers $a$.
4. In both cases the induction hypothesis gives a winning strategy for the remaining $m$ rounds in $G_m(\mathcal{A}, \bar a a, \mathcal{B}, \bar b b)$.
5. Now let $(\mathcal{A}, \bar a) \equiv_n (\mathcal{B}, \bar b)$. By step 5 of the previous part, $\mathcal{A} \models \varphi^n_{\bar a}[\bar a]$, and its rank is at most $n$. So $\mathcal{B} \models \varphi^n_{\bar a}[\bar b]$, and Duplicator wins $G_n(\mathcal{A}, \bar a, \mathcal{B}, \bar b)$.

## Idea

A quantifier is a move, and its witness is the element chosen.
The Hintikka formula $\varphi^m_{\bar a}$ lists, for each possible next move, the formula of rank $m - 1$ that the extended tuple satisfies.
It is a complete description of $\bar a$ up to rank $m$, and it is a strategy for Duplicator written as a sentence.

## Variants

- The second implication can also be proved by contraposition: if Spoiler wins, an induction on $n$ turns Spoiler's strategy into a separating formula.
- For the infinite game, the same proof with conjunctions of any size gives [[Karp's theorem|KAWWZ2DF0G]]; the finiteness step is then not needed.
- With the [[finiteness lemma|3Q49RH1ZEK]] one can replace $\varphi^m_{\bar a}$ by the conjunction of all formulas of rank at most $m$ in $\Phi_{m,k}$ that $\bar a$ satisfies.
