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

Let $\mathrm{ARITH}$ be the family of arithmetical sets: the sets $A \subseteq \mathbb{N}$ that a first-order formula of arithmetic without parameters defines in $\mathbb{N}$.
By [[Post's theorem|NYJX5QXX1T]], $A \in \mathrm{ARITH}$ exactly when $A \le_T \emptyset^{(n)}$ for some $n$, where $\emptyset^{(n)}$ is the $n$-th [[Turing jump|60P2XWY5QX]] of $\emptyset$.
We check that $(\mathbb{N}, \mathrm{ARITH})$ is the least $\omega$-model of [[ACA0|K9XG0Z2N9V]], that it satisfies $\mathsf{WKL}_0$, and that it fails $\mathsf{ATR}_0$ and $\Pi^1_1\text{-}\mathsf{CA}_0$.

### A model of ACA0 and WKL0

1. Let $\varphi(n)$ be an $L_2$ formula without set quantifiers, with parameters $A_1, \ldots, A_k \in \mathrm{ARITH}$, where $\psi_i$ defines $A_i$.
2. Replace each atomic formula $t \in A_i$ in $\varphi$ by $\psi_i(t)$.
   The result is a first-order formula that defines $\{ n : \varphi(n) \}$ in $\mathbb{N}$, so this set is in $\mathrm{ARITH}$, and arithmetical comprehension holds.
3. Induction holds in every $\omega$-model, because its numbers are the true natural numbers.
   So $(\mathbb{N}, \mathrm{ARITH})$ is a model of $\mathsf{ACA}_0$.
4. Every $\omega$-model of $\mathsf{ACA}_0$ contains each set that arithmetical comprehension gives without parameters, that is, each arithmetical set.
   So $\mathrm{ARITH}$ is the least $\omega$-model.
5. $\mathsf{ACA}_0$ proves [[König's lemma|3P2J5NWCM1]], and every binary tree is finitely branching, so $(\mathbb{N}, \mathrm{ARITH})$ is a model of $\mathsf{WKL}_0$.

### Jump hierarchies of finite length

6. For a set $H$ of pairs, write $H_j = \{ n : (n, j) \in H \}$ and $H^j = \{ (n, i) \in H : i < j \}$.
   Let $\theta(n, Y)$ say "$n \in Y'$", a $\Sigma^0_1$ formula.
7. Let $J(k, H)$ be the arithmetical formula $\forall j < k\, \forall n\, \big(n \in H_j \leftrightarrow \theta(n, H^j)\big)$, which says that $H$ is a jump hierarchy of length $k$.
8. By induction on $j$, any two sets with $J(k, H)$ have the same columns $H_j$ for $j < k$.
   Call this common column $B_j$.
   Then $B_0 = \emptyset'$, because $H^0$ is empty.
   Since $B_j$ computes $H^j$ and hence $H^{j+1}$, and $H^{j+1}$ computes $B_j$, we get $B_{j+1} = (H^{j+1})' \equiv_T B_j'$, so $B_j \equiv_T \emptyset^{(j+1)}$ by induction.
9. For each $k$, the set with columns $B_0, \ldots, B_{k-1}$ and no other elements satisfies $J(k, H)$, and it is computable from $\emptyset^{(k)}$.
   So for each $k$ some $H$ with $J(k, H)$ lies in $\mathrm{ARITH}$.

### The failures

10. [[ATR0|TMJJSN9PDP]] fails.
    Its instance for $\theta$ along the well-ordering $(\mathbb{N}, <)$ asks for $H$ with $n \in H_j \leftrightarrow \theta(n, H^j)$ for all $j$, and then $H_j = B_j$ for all $j$ by step 8.
11. Such an $H$ computes every $\emptyset^{(j+1)}$.
    If $H \le_T \emptyset^{(m)}$, then $\emptyset^{(m+1)} \le_T \emptyset^{(m)}$, which is false, so $H \notin \mathrm{ARITH}$.
12. [[Π¹₁-CA0|VPGQM418AG]] fails.
    Let $\psi(k, m)$ be the $\Pi^1_1$ formula $\forall H\, \big(J(k + 1, H) \to m \in H_k\big)$.
13. In $(\mathbb{N}, \mathrm{ARITH})$, $\psi(k, m)$ holds exactly when $m \in B_k$.
    Step 9 gives an $H$ in the model with $J(k + 1, H)$, so the formula is not true for an empty reason, and step 8 fixes column $k$ of every such $H$.
14. So $\Pi^1_1$ comprehension asks for $\{ (m, k) : m \in B_k \}$, which computes every $\emptyset^{(k+1)}$ and is not arithmetical, by the argument of step 11.

## Remarks

The model shows that $\mathsf{ACA}_0$ does not prove $\mathsf{ATR}_0$.
Step 10 needs $(\mathbb{N}, <)$ to be a well-ordering in the model, and it is, because $\mathbb{N}$ has no infinite descending sequence at all.
The set asked for in steps 10 and 14 is, up to Turing equivalence, $\emptyset^{(\omega)}$, the first set beyond the arithmetical sets.

If we start from a set $X$ instead of $\emptyset$, the same argument shows that the sets arithmetical in $X$ form the least $\omega$-model of $\mathsf{ACA}_0$ that contains $X$.
Adding $\emptyset^{(\omega)}$ and closing again under arithmetical definitions gives a larger $\omega$-model of $\mathsf{ACA}_0$, and that model contains the hierarchy along $\omega$ but not the hierarchy along $\omega + \omega$.

Watch out: each $\emptyset^{(n)}$ is in the model.
Only the sequence of all of them, as one set, is missing.

## Explanations

### L1 human

The arithmetical sets are the sets that can be described with quantifiers over numbers only.
Any description of this kind that uses arithmetical sets as parameters again gives an arithmetical set, so they form a model of $\mathsf{ACA}_0$.
But no single arithmetical set lists the halting problem, the halting problem relative to it, and so on forever.
So systems that build this list fail in the model.

### L2 human

The model separates $\mathsf{ACA}_0$ from $\mathsf{ATR}_0$.
The failing instance of $\mathsf{ATR}_0$ is the simplest one, the jump iterated along $\omega$.
Look at the first columns: $B_0 = \emptyset'$ is $\Sigma^0_1$, $B_1 \equiv_T \emptyset''$ is $\Sigma^0_2$, and in general $B_j$ is $\Sigma^0_{j+1}$ but not $\Sigma^0_j$, by Post's theorem.
A single arithmetical set is $\Sigma^0_m$ for some fixed $m$, so it is computable from $\emptyset^{(m)}$ and cannot compute the column $B_m \equiv_T \emptyset^{(m+1)}$.
This is the typical way to show that an $\omega$-model fails a principle: find an instance whose solutions must climb past every level of the model.
