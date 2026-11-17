---
tag: FZF2NPMSKS
kind: proof
name: Proof structure of the complexity bounds for cut elimination
msc: ["03F05", "03F20"]
topics: [R10RMQCJQX]
audience: research
proves: B5F5HB4YK7
uses: [Q1799WJA0W, PZX9J3VEMT, RJ3MCAAZSV]
methods: [0ASJVEFA9J, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Cut-elimination_theorem
    locator: Cut elimination
---

## Proof

**Part 1.**
Part 1 is part 3 of the cut-elimination theorem, proved in [[the proof by rank reduction|Q1799WJA0W]].

**Part 2(a), cited.**
Let $T$ contain these universal sentences, all true in the natural numbers, together with the equality axioms.
They are $x + 0 = x$, $x + S y = S(x + y)$, $0 + x = x$, $(x + y) + z = x + (y + z)$, $e(0) = S 0$ and $e(S x) = e(x) + e(x)$.
Define $\psi_0(x) = I(x)$ and $\psi_{i+1}(x) = \forall y\, (\psi_i(y) \to \psi_i(y + e(x)))$.
So $\psi_{i+1}(a)$ says that $\psi_i$ is closed under adding $2^a$.
The derivation has the following structure, and its length bound is the lemma cited without proof.

1. For each $i$, derive $\psi_i(a), a = b \Rightarrow \psi_i(b)$ from the equality axioms, using the case $i - 1$ inside $\psi_i$.
2. For each $i$, derive $\psi_i(a) \Rightarrow \psi_i(S a)$. For $i = 0$ this is an instance of $\forall x\, (I(x) \to I(Sx))$.
3. For $i + 1$: from $\psi_{i+1}(a)$ and $\psi_i(y)$, apply $\psi_{i+1}(a)$ twice to get $\psi_i((y + e(a)) + e(a))$.
4. By the axioms for $e$ and associativity, $(y + e(a)) + e(a) = y + e(S a)$. Step 1 gives $\psi_i(y + e(S a))$, so $\psi_{i+1}(S a)$.
5. For each $i$, derive $\Rightarrow \psi_i(0)$. For $i = 0$ this is $I(0)$.
6. For $i + 1$, the claim $\psi_{i+1}(0)$ says that $\psi_i$ is closed under adding $e(0) = S 0$. Since $y + S 0 = S y$, this is step 2.
7. From $\psi_{i+1}(a)$ and $\psi_i(0)$ we get $\psi_i(0 + e(a))$, and $0 + e(a) = e(a)$ gives $\psi_i(e(a))$.
8. Start from $\psi_\ell(s_0)$, which is step 5. Step 7 gives $\psi_{\ell - 1}(s_1)$, then $\psi_{\ell - 2}(s_2)$, and finally $\psi_0(s_\ell) = I(s_\ell)$.
9. Each step uses cuts on the formulas $\psi_i$. The formula $\psi_i$ has two copies of $\psi_{i-1}$, so its length is exponential in $i$.
10. Cited lemma: assembled with care, the whole derivation of $S_\ell$ has length at most $2^{c \ell}$ for a constant $c$.

**Part 2(b).**
Let $D$ be a cut-free derivation of $S_\ell$ with $N$ sequents.
Call a formula *universal* if it is $\forall x_1 \cdots \forall x_k\, M$ with $M$ quantifier-free.

11. Every formula of $D$ is a subformula of $S_\ell$ up to substitution of terms, since $D$ is cut-free.
12. The quantifiers of $S_\ell$ stand in front of formulas in its antecedent, and no connective is above them. So a quantified formula of $D$ occurs only in antecedents, and it is universal.
13. Hence $D$ has no ${\forall}$R, ${\exists}$L or ${\exists}$R steps, and its axioms $A \Rightarrow A$ have quantifier-free $A$.
14. Let $H_S$ be the list of quantifier-free active formulas $A[t/x]$ of the ${\forall}$L steps in the derivation of a sequent $S$ of $D$.
15. Claim: for every sequent $S$ of $D$, the sequent $H_S, S^\circ_L \Rightarrow S^\circ_R$ is valid, where $S^\circ_L$ and $S^\circ_R$ are the quantifier-free formulas of $S$.
16. For an axiom, the claim is the axiom itself. For a ${\forall}$L step with quantifier-free active formula, the formula moves from $S^\circ_L$ into $H_S$.
17. For a ${\forall}$L step whose active formula has a quantifier, nothing changes. Structural steps keep validity.
18. A propositional step acts on quantifier-free formulas by step 12. It is sound with any extra antecedent formulas, so validity passes from the premises to the conclusion.
19. Let $H$ be the list for $D$. Each ${\forall}$L step has its own conclusion, so $H$ has at most $N - 1$ formulas.
    By the claim, every model of $H$ and of the quantifier-free formulas of the antecedent of $S_\ell$ satisfies $I(s_\ell)$.
20. Let $I(t_1) \to I(S t_1), \dots, I(t_m) \to I(S t_m)$ be the instances in $H$ of the axiom for $I$. Then $m \leq N - 1$.
21. Evaluate terms with every variable sent to $0$. Let $n_0$ be the least natural number that is not the value of any $t_j$. Then $n_0 \leq m$.
22. Take the natural numbers with the usual $0$, $S$, $+$, $e$ and equality, and let $I(n)$ be true exactly when $n \leq n_0$.
23. The instances of $T$ in $H$ and the quantifier-free members of $T$ are true, since $T$ is true and its equality axiom for $I$ holds for real equality. Also $I(0)$ is true.
24. Each $I(t_j) \to I(S t_j)$ is true. If the value $v$ of $t_j$ is less than $n_0$, then $v + 1 \leq n_0$. Otherwise $v > n_0$, and $I(t_j)$ is false.
25. By step 19, $I(s_\ell)$ is true, so $2_\ell(0) \leq n_0 \leq m \leq N - 1$. Hence $N > 2_\ell(0)$.

**Part 3.**

26. Suppose $f$ is elementary. Then there is a $k$ with $f(n) \leq 2_k(n)$ for all $n$.
27. By parts 2(a) and 2(b), the sequent $S_\ell$ has a derivation of length $n \leq 2^{c \ell}$, and every cut-free derivation has length greater than $2_\ell(0)$.
28. If $f$ were a bound, then $2_\ell(0) < f(n) \leq 2_k(n) \leq 2_k(2^{c \ell}) = 2_{k+1}(c \ell)$, since $2_k$ is increasing.
29. But $2_\ell(0) = 2_{k+1}(2_{\ell - k - 1}(0))$, and $2_{\ell - k - 1}(0) > c \ell$ for all large $\ell$. Since $2_{k+1}$ is increasing, this is a contradiction.

## Idea

With cuts, a short derivation proves that $I$ is closed under $x \mapsto x + 2^{2^{\cdots}}$, one quantifier level at a time.
Without cuts, every use of a universal axiom is an explicit instance, and the instances of $I(x) \to I(Sx)$ must reach $2_\ell(0)$ one by one.
The count in step 21 is a pigeonhole argument: a model that makes $I$ true only up to the first gap refutes too short a list of instances.

## Variants

Statman and Orevkov gave the first lower bounds of this kind, and Orevkov's examples use no function symbols.
Pudlák modified the construction so that the derivations with cuts have polynomial length.
Buss's sharpened lower bounds use the same kind of counting, with a closer match between the depth of the cut formulas and the height of the tower.
