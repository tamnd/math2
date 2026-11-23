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

We cite part 1, outline the short derivation of part 2(a), prove part 2(b) by building a small model, and derive part 3 from part 2.

### Part 1

Part 1 is part 3 of the [[cut-elimination theorem|AYRZ98Y0NW]], and [[the proof by rank reduction|Q1799WJA0W]] proves it.

### Part 2(a): the short derivation with cuts

Let $T$ consist of the universal closures of $x + 0 = x$, $x + S y = S(x + y)$, $0 + x = x$, $(x + y) + z = x + (y + z)$, $e(0) = S 0$ and $e(S x) = e(x) + e(x)$, with the equality axioms.
All of them are true in the natural numbers.
Define $\psi_0(x) = I(x)$ and $\psi_{i+1}(x) = \forall y\, (\psi_i(y) \to \psi_i(y + e(x)))$, so $\psi_{i+1}(a)$ says that $\psi_i$ is closed under adding $2^a$.
We give the structure of the derivation and cite its length bound.

1. For each $i$, derive $\psi_i(a), a = b \Rightarrow \psi_i(b)$ from the equality axioms, by induction on $i$.
2. For each $i$, derive $\psi_i(a) \Rightarrow \psi_i(S a)$.
   For $i = 0$ this is an instance of $\forall x\, (I(x) \to I(Sx))$.
3. For $i + 1$, assume $\psi_{i+1}(a)$ and $\psi_i(y)$.
   Two uses of $\psi_{i+1}(a)$ give $\psi_i((y + e(a)) + e(a))$.
4. Associativity and the axiom $e(S a) = e(a) + e(a)$ give $(y + e(a)) + e(a) = y + e(S a)$.
   Step 1 turns step 3 into $\psi_i(y + e(S a))$, so $\psi_{i+1}(S a)$ holds.
5. For each $i$, derive $\Rightarrow \psi_i(0)$.
   For $i = 0$ this is $I(0)$.
6. For $i + 1$, the formula $\psi_{i+1}(0)$ says that $\psi_i$ is closed under adding $e(0) = S 0$.
   Since $y + S 0 = S y$, this is step 2 together with step 1.
7. From $\psi_{i+1}(a)$ and $\psi_i(0)$ we get $\psi_i(0 + e(a))$, and $0 + e(a) = e(a)$ gives $\psi_i(e(a))$.
8. Start from $\psi_\ell(s_0)$, given by step 5.
   Step 7 with step 5 gives $\psi_{\ell - 1}(s_1)$, then $\psi_{\ell - 2}(s_2)$, and finally $\psi_0(s_\ell) = I(s_\ell)$.
9. The steps are joined by cuts on the formulas $\psi_i$.
   Since $\psi_i$ contains two copies of $\psi_{i-1}$, its length is exponential in $i$.
10. Cited lemma: when the derivation is assembled with care, its length is at most $2^{c \ell}$ for a constant $c$.

### Part 2(b): the shape of a cut-free derivation

Let $D$ be a cut-free derivation of $S_\ell$ with $N$ sequents.
Call a formula *universal* if it has the form $\forall x_1 \cdots \forall x_k\, M$ with $M$ quantifier-free.

11. By the [[subformula property|Z2NXKDK06G]], every formula of $D$ is a subformula of $S_\ell$ up to substitution of terms.
12. The quantifiers of $S_\ell$ stand at the front of antecedent formulas, with no connective above them.
    So a quantified formula of $D$ occurs only in antecedents, and it is universal.
13. Hence $D$ has no ${\forall}$R, ${\exists}$L or ${\exists}$R steps, and each axiom $A \Rightarrow A$ has a quantifier-free $A$.
14. For a sequent $S$ of $D$, let $H_S$ list the quantifier-free active formulas $A[t/x]$ of the ${\forall}$L steps above $S$.
15. Claim: for each sequent $S$ of $D$, the sequent $H_S, S^\circ_L \Rightarrow S^\circ_R$ is valid.
    Here $S^\circ_L$ and $S^\circ_R$ are the quantifier-free formulas of the two sides of $S$.
16. We prove the claim by induction on the derivation.
    For an axiom, the claim is the axiom itself.
    At a ${\forall}$L step with a quantifier-free active formula, that formula moves from $S^\circ_L$ into $H_S$.
17. At a ${\forall}$L step whose active formula has a quantifier, nothing changes, and structural steps keep validity.
18. A propositional step acts only on quantifier-free formulas, by step 12.
    It stays sound when extra formulas are added to the antecedent, so validity passes down.

### Part 2(b), continued: a model with a gap

19. Let $H$ be the list for the end sequent.
    Each ${\forall}$L step has its own conclusion, so $H$ has at most $N - 1$ formulas.
20. Let $I(t_1) \to I(S t_1), \dots, I(t_m) \to I(S t_m)$ be the instances in $H$ of the axiom for $I$, so $m \leq N - 1$.
21. Evaluate all terms with every variable sent to $0$.
    Let $n_0$ be the least natural number that is not the value of any $t_j$.
    The $m$ terms have at most $m$ values, so $n_0 \leq m$.
22. Take the natural numbers with the usual $0$, $S$, $+$, $e$ and equality, and let $I(n)$ hold exactly when $n \leq n_0$.
23. The instances of $T$ in $H$ are true, since $T$ is true and its equality axioms hold for real equality.
    Also $I(0)$ is true.
24. Each $I(t_j) \to I(S t_j)$ is true.
    If the value $v$ of $t_j$ is less than $n_0$, then $v + 1 \leq n_0$.
    Otherwise $v > n_0$, because $v \neq n_0$, and then $I(t_j)$ is false.
25. By the claim of step 15 for the end sequent, $I(s_\ell)$ is true in this model.
    So $2_\ell(0) \leq n_0 \leq m \leq N - 1$, and hence $N > 2_\ell(0)$.

### Part 3

26. Suppose that an elementary $f$ is such a bound.
    Every elementary function is bounded by a fixed tower, so there is a $k$ with $f(n) \leq 2_k(n)$ for all $n$.
27. By part 2(a), $S_\ell$ has a derivation of length $n \leq 2^{c \ell}$.
    By part 2(b), every cut-free derivation of $S_\ell$ has size, and so length, greater than $2_\ell(0)$.
28. Since $2_k$ is increasing, the bound gives the following:
    $$2_\ell(0) < f(n) \leq 2_k(n) \leq 2_k(2^{c \ell}) = 2_{k+1}(c \ell).$$
29. But $2_\ell(0) = 2_{k+1}(2_{\ell - k - 1}(0))$, and $2_{\ell - k - 1}(0) > c \ell$ for all large $\ell$.
    Since $2_{k+1}$ is increasing, $2_\ell(0) > 2_{k+1}(c \ell)$, which contradicts step 28.
    So no elementary $f$ is a bound.

## Idea

With cuts, a short derivation proves that $I$ is closed under adding $2^{2^{\cdots}}$, one quantifier level at a time, and each level is a lemma used twice.
Without cuts there are no lemmas, so every use of a universal axiom is an explicit instance.
The instances of $I(x) \to I(Sx)$ must then climb to $2_\ell(0)$ one by one.
Step 21 is a pigeonhole argument: if the list of instances is too short, it misses some number, and a model that makes $I$ true only up to that gap refutes the end sequent.

## Variants

Statman and Orevkov gave the first lower bounds of this kind, and Orevkov's examples use no function symbols.
Statman's route goes through Herbrand's theorem: a cut-free proof yields a Herbrand disjunction, and the same counting bounds its size from below.
Buss's sharpened lower bounds use the same kind of counting, with a closer match between the degree of the cut formulas and the height of the tower.
