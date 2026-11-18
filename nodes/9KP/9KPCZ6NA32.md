---
tag: 9KPCZ6NA32
kind: example
name: The arithmetical sets form the least ω-model of ACA0
msc: ["03B30", "03D55"]
topics: [BY8AAFN7C5]
audience: grad
instance_of: [NAASTN80QN, 7W9EG02T79]
not_instance_of:
  - target: MKB74TX3Z8
    note: the hierarchy of jumps along the well-ordering omega is not arithmetical
  - target: T21WETAHN5
    note: the set of indices of computable well-orderings is not arithmetical
uses: [K9XG0Z2N9V, TMJJSN9PDP, VPGQM418AG, 7CVJCQKY41, NYJX5QXX1T, 60P2XWY5QX, 3P2J5NWCM1]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: ω-models and β-models
  - url: https://en.wikipedia.org/wiki/Arithmetical_set
    locator: lead section
---

## Example

Let $\mathrm{ARITH}$ be the family of arithmetical sets: the sets $A \subseteq \N$ defined in $\N$ by a first-order formula of arithmetic without parameters.
By [[Post's theorem|NYJX5QXX1T]], $A \in \mathrm{ARITH}$ exactly when $A \le_T \emptyset^{(n)}$ for some $n$, where $\emptyset^{(n)}$ is the $n$-th [[Turing jump|60P2XWY5QX]] of $\emptyset$.
We check that $(\N, \mathrm{ARITH})$ is the least $\omega$-model of [[ACA0|K9XG0Z2N9V]], that it satisfies $\mathsf{WKL}_0$, and that it fails $\mathsf{ATR}_0$ and $\Pi^1_1\text{-}\mathsf{CA}_0$.

1. Let $\varphi(n)$ be an $L_2$-formula without set quantifiers, with set parameters $A_1, \ldots, A_k \in \mathrm{ARITH}$, where $A_i$ is defined by $\psi_i$.
2. Replace each atomic formula $t \in A_i$ in $\varphi$ by $\psi_i(t)$. The result is a first-order formula that defines $\set{n : \varphi(n)}$ in $\N$.
3. So this set is in $\mathrm{ARITH}$, and arithmetical comprehension holds. Induction holds in every $\omega$-model, so $(\N, \mathrm{ARITH})$ is a model of $\mathsf{ACA}_0$.
4. Every $\omega$-model of $\mathsf{ACA}_0$ contains each set given by arithmetical comprehension without parameters, that is, each arithmetical set. So $\mathrm{ARITH}$ is the least one.
5. $\mathsf{ACA}_0$ proves [[König's lemma|3P2J5NWCM1]], and every infinite binary tree is finitely branching. So $(\N, \mathrm{ARITH})$ is a model of $\mathsf{WKL}_0$.
6. For a set $H$ of pairs, write $H_j = \set{n : (n, j) \in H}$ and $H^j = \set{(n, i) \in H : i < j}$. Let $\theta(n, Y)$ say "$n \in Y'$", a $\Sigma^0_1$ formula.
7. Let $J(k, H)$ be the arithmetical formula $\forall j < k\, \forall n\, \big(n \in H_j \leftrightarrow \theta(n, H^j)\big)$. It says that $H$ is a jump hierarchy of length $k$.
8. By induction on $j$, any two sets with $J(k, H)$ have the same columns $H_j$ for $j < k$. Let $B_j$ be this common column. Then $B_0 = \emptyset'$, and $B_j \equiv_T \emptyset^{(j+1)}$.
9. For each $k$, a set $H$ with $J(k, H)$ is computable from $\emptyset^{(k)}$, so it is in $\mathrm{ARITH}$.
10. [[ATR0|TMJJSN9PDP]] fails. Its instance for $\theta$ along the well-ordering $(\N, <)$ asks for $H$ with $n \in H_j \leftrightarrow \theta(n, H^j)$ for all $j$. Then $H_j = B_j$ for all $j$.
11. Such an $H$ computes every $\emptyset^{(j+1)}$. If $H \le_T \emptyset^{(m)}$, then $\emptyset^{(m+1)} \le_T \emptyset^{(m)}$, which is false. So $H \notin \mathrm{ARITH}$.
12. [[Π¹₁-CA0|VPGQM418AG]] fails. Let $\psi(k, m) := \forall H\, \big(J(k + 1, H) \to m \in H_k\big)$, a $\Pi^1_1$ formula.
13. In $(\N, \mathrm{ARITH})$, $\psi(k, m)$ holds exactly when $m \in B_k$, by steps 8 and 9. So $\Pi^1_1$ comprehension asks for $\set{(m, k) : m \in B_k}$.
14. This set computes every $\emptyset^{(k+1)}$, so it is not arithmetical, by the argument of step 11.

## Remarks

The model shows that $\mathsf{ACA}_0$ does not prove $\mathsf{ATR}_0$.
Step 10 needs $(\N, <)$ to be a well-ordering in the model; it is, since $\N$ has no infinite descending sequence at all.
The set asked for in step 13 is essentially $\emptyset^{(\omega)}$, the first set beyond the arithmetical sets.

## Explanations

### L1 human

The arithmetical sets are those that can be described with quantifiers over numbers only.
They are closed under every arithmetical description, so they form a model of $\mathsf{ACA}_0$.
But they are not closed under iterating the jump infinitely often, so stronger systems fail.

### L2 human

The model separates $\mathsf{ACA}_0$ from $\mathsf{ATR}_0$.
The failing instance of $\mathsf{ATR}_0$ is the simplest one: the jump iterated along $\omega$.
A trap is to say that each $\emptyset^{(n)}$ is missing: each one is in the model, and only the sequence of all of them, as one set, is missing.
