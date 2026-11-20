---
tag: 4F60HFVSA7
kind: proof
name: Proof that there are finitely many formulas of each quantifier rank
msc: ["03C07", "03B10"]
topics: [N64R1MGDBN]
audience: grad
proves: 3Q49RH1ZEK
uses: [FVEVRE5XNZ, MQ2KK8P8NT, HYJ10AF6RT, MCZRXR3SVB]
methods: [0ASJVEFA9J, 12MQ2NJ29A]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_rank
    locator: In first-order logic
  - book: isbn:9780521587136
    locator: Chapter 3
---

## Proof

We use one fact about propositional logic.
Let $\theta_1, \dots, \theta_N$ be formulas.
Every Boolean combination of them is equivalent to a disjunction of conjunctions $\bigwedge_{i} \pm\theta_i$, one for each truth assignment that makes it true.
So there are at most $2^{2^N}$ combinations up to equivalence, and each has rank at most $\max_i \operatorname{qr}(\theta_i)$.
We prove the statement for all $k$ at once, by [[induction|0ASJVEFA9J]] on $n$.

### Rank zero

1. *Case $n = 0$.* A formula of rank $0$ is quantifier-free, so it is a Boolean combination of [[atomic formulas|MCZRXR3SVB]].
2. An atomic formula with variables among $x_1, \dots, x_k$ is $x_i = x_j$ or $R(x_{i_1}, \dots, x_{i_r})$ for a relation symbol $R$ of arity $r$. There are $k^2$ equations and $k^r$ choices for each $R$. Since $L$ is finite and has no function symbols, the number $N$ of atomic formulas is finite.
3. By the fact above, the quantifier-free formulas in $x_1, \dots, x_k$ fall into at most $2^{2^N}$ classes, and we choose one representative of each for $\Phi_{0,k}$.

### From rank n to rank n + 1

1. *Step from $n$ to $n + 1$.* Every formula $\varphi$ of rank at most $n + 1$ is a Boolean combination of formulas of rank at most $n$ and formulas $\exists y \, \psi$ with $\operatorname{qr}(\psi) \le n$. This holds by [[structural induction|12MQ2NJ29A]] on $\varphi$, and $\forall y \, \psi$ is replaced by $\neg \exists y \, \neg\psi$, which has the same rank.
2. Let $\exists y \, \psi$ have free variables among $x_1, \dots, x_k$. Rename the bound variable to $x_{k+1}$, after renaming any bound occurrences of $x_{k+1}$ inside $\psi$. This gives an equivalent formula $\exists x_{k+1} \, \psi'$, with $\operatorname{qr}(\psi') = \operatorname{qr}(\psi) \le n$ and free variables of $\psi'$ among $x_1, \dots, x_{k+1}$.
3. By the induction hypothesis for $k + 1$, $\psi'$ is equivalent to some $\theta \in \Phi_{n,k+1}$. So $\exists y \, \psi$ is equivalent to $\exists x_{k+1} \, \theta$.
4. By the induction hypothesis for $k$, each formula of rank at most $n$ in $x_1, \dots, x_k$ is equivalent to a member of $\Phi_{n,k}$.
5. Replacing parts of a formula by equivalent formulas gives an equivalent formula. So $\varphi$ is equivalent to a Boolean combination of the finitely many formulas in $\Phi_{n,k} \cup \set{\exists x_{k+1} \, \theta : \theta \in \Phi_{n,k+1}}$.
6. These formulas have rank at most $n + 1$. By the fact above there are finitely many such combinations up to equivalence, and we choose one representative of each for $\Phi_{n+1,k}$.

### Classes of n-equivalence

1. *Classes of $\equiv_n$.* For $k = 0$, two structures are $n$-equivalent exactly when they satisfy the same members of the finite set $\Phi_{n,0}$. The class of $\mathcal{A}$ is defined by the conjunction of the members of $\Phi_{n,0}$ true in $\mathcal{A}$ and the negations of the others, and there are at most $2^{\abs{\Phi_{n,0}}}$ classes.

## Idea

A formula of rank $n + 1$ is built from rank $n$ pieces by Boolean operations and one more quantifier.
Finitely many pieces give finitely many Boolean combinations, and adding a quantifier to finitely many pieces gives finitely many new pieces.
The variable count grows by one at each level, which is why the induction runs over all $k$ at once.

## Variants

One can define the representatives directly as the Hintikka formulas, or rank $n$ characteristic formulas, of tuples, as in the [[proof of the Ehrenfeucht-Fraïssé theorem|GYEBFJM5FY]].
Then the finiteness follows from a count of the Hintikka formulas, by the same induction.
