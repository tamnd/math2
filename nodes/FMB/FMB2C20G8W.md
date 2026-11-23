---
tag: FMB2C20G8W
kind: statement
role: theorem
name: Transfer theorem for undecidability
aliases: [undecidability-by-interpretation, tarski-mostowski-robinson-transfer-theorem]
msc: ["03B25", "03D35", "03C07"]
topics: [E4AVTNWE9E]
audience: grad
about: [9JDDFN8PT7]
uses: [9JDDFN8PT7, HWC687ES0Q, 92SWXST1ZM, 3K1AKGXF8A, RZ42PP37MD, 0KYYSMEVHH]
history:
  first_stated: "1953"
  notes: Stated and used by Alfred Tarski, Andrzej Mostowski and Raphael Robinson in the book Undecidable Theories (1953).
sources:
  - url: https://en.wikipedia.org/wiki/Decidability_(logic)
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Undecidability
---

## Statement

The theorem says that a theory which can define a copy of an essentially undecidable theory inside its models is undecidable too.

Let $L_1$ be a finite signature and $L_2$ a signature, both with a computable coding of sentences.
An interpretation $I$ of $L_1$ in $L_2$ consists of $L_2$-formulas $\delta(x)$, $\rho_R(x_1, \ldots, x_n)$ for each $n$-ary relation symbol $R$ of $L_1$, and $\gamma_f(x_1, \ldots, x_n, y)$ for each $n$-ary function symbol $f$ of $L_1$, with constants as $0$-ary functions.
Let $\varepsilon_I$ be the $L_2$-sentence saying that $\delta$ is nonempty and that each $\gamma_f$ defines a function from $\delta^n$ to $\delta$.
For an $L_2$-structure $\mathcal{M}$ with $\mathcal{M} \models \varepsilon_I$, the $L_1$-structure $\mathcal{M}^I$ has universe $\delta(\mathcal{M})$, relations $\rho_R(\mathcal{M}) \cap \delta(\mathcal{M})^n$, and the functions defined by the $\gamma_f$.
There is a computable map $\sigma \mapsto \sigma^I$ from $L_1$-sentences to $L_2$-sentences with $\mathcal{M} \models \sigma^I$ exactly when $\mathcal{M}^I \models \sigma$, for every $\mathcal{M} \models \varepsilon_I$.

An $L_1$-theory $T_1$ is interpretable in an $L_2$-theory $T_2$ when, for some $I$, $T_2 \models \varepsilon_I$ and $T_2 \models \sigma^I$ for every $\sigma \in T_1$.
$T_1$ is interpretable in an $L_2$-structure $\mathcal{M}$ when, for some $I$, $\mathcal{M} \models \varepsilon_I$ and $\mathcal{M}^I \models T_1$.

1. If $T_1$ is [[essentially undecidable|9JDDFN8PT7]] and interpretable in a consistent $L_2$-theory $T_2$, then $T_2$ is essentially undecidable.
2. If $T_1$ is essentially undecidable, finitely axiomatizable, and interpretable in an $L_2$-structure $\mathcal{M}$, then every $L_2$-theory $T$ with $\mathcal{M} \models T$ is undecidable.
   In particular $\operatorname{Th}(\mathcal{M})$ is hereditarily undecidable.

## Remarks

### Why each hypothesis is needed

Essential undecidability of $T_1$ is needed, not only undecidability.
The theory $T_1$ with no axioms in one binary relation symbol $R$ is undecidable, and it is interpretable in the decidable theory $\operatorname{Th}(\mathbb{N}, <)$ by $\rho_R = (x_1 < x_2)$.

Consistency of $T_2$ is needed, because the inconsistent theory interprets every theory and is decidable.

Finite axiomatizability in part 2 is used to replace $T_1$ by one sentence $\beta$, so that $\operatorname{Cn}(T \cup \{\beta\})$ is decidable when $T$ is.
Without it, part 1 still gives the essential undecidability of $\operatorname{Th}(\mathcal{M})$, but not the undecidability of the weaker theories $T$.

### What it gives you

By [[Lagrange's four-square theorem|0KYYSMEVHH]], $\mathbb{N}$ is defined in the ring $\mathbb{Z}$ by $\exists a \, \exists b \, \exists c \, \exists d \, (x = a^2 + b^2 + c^2 + d^2)$.
So [[Robinson arithmetic|3K1AKGXF8A]] is interpretable in $\mathbb{Z}$, and the theories of rings, of commutative rings and of integral domains are undecidable.

Julia Robinson proved in 1949 that $\mathbb{Z}$ is definable in the field $\mathbb{Q}$.
So $\mathsf{Q}$ is interpretable in the field $\mathbb{Q}$, and the theory of fields is undecidable.

Tarski proved by this method that the theory of groups is undecidable.
That theory is still not essentially undecidable, as [[the theory of groups is not essentially undecidable|8FYX4VNRW8]] shows.

Addition is definable in $(\mathbb{N}, S, \cdot)$, so $\operatorname{Th}(\mathbb{N}, S, \cdot)$ is undecidable, while [[Skolem arithmetic|X86G2FXTPC]] without the successor is decidable.

### The converse

The converse direction fails: if $T_1$ is interpretable in an essentially undecidable theory $T_2$, then $T_1$ need not be undecidable.
[[Presburger arithmetic|4W0E9G7PPV]] is decidable, and it is interpretable in true arithmetic, which is essentially undecidable, by interpreting $0$ and $+$ as themselves and $1$ as $S 0$.

### Generalizations

The interpretation may use parameters.
Then $\beta$ also quantifies the parameters existentially, and part 2 still holds.

The interpretation may define the universe as a quotient of $\delta^k$ by a definable equivalence relation.
The proof is the same, with $\varepsilon_I$ also saying that the formula defines an equivalence relation that respects the $\rho_R$ and $\gamma_f$.

Part 2 with $T = \operatorname{Cn}(\emptyset)$ gives Church's theorem for every signature $L_2$ in which some structure interprets $\mathsf{Q}$.

### Watch out

Do not use a formula $\delta$ with parameters and then apply the theorem as stated without the generalization above.
For example, in the field $\mathbb{Q}$ the formula $x = p$ with a parameter $p$ defines a single point, and its truth depends on the choice of $p$.
Also check $\varepsilon_I$: if $\delta(\mathcal{M})$ is not closed under the defined functions, $\mathcal{M}^I$ is not a structure at all.

### Try it

Is the theory of fields of characteristic $0$ undecidable?
Yes: the field $\mathbb{Q}$ is a model of it and interprets $\mathsf{Q}$, so part 2 applies.

Can part 2 show that $\operatorname{Th}(\mathbb{N}, <)$ is undecidable?
No: that theory is decidable, so by part 2 no interpretation of $\mathsf{Q}$ in $(\mathbb{N}, <)$ exists.

## History

Tarski, Mostowski and Robinson developed the method of interpretations in their book Undecidable Theories of 1953.
They used it to show the undecidability of the theories of groups, rings and fields, among others.
Julia Robinson's definition of the integers in the rational field, from 1949, gave the case of fields.

## Explanations

### L1 human

Suppose a hard puzzle can be rewritten, piece by piece, as a puzzle of another kind.
Then the second kind of puzzle is at least as hard as the first.
The transfer theorem uses this idea: if the hard theory of whole numbers can be rewritten inside a theory about rings or groups, then that theory is also beyond the reach of a computer.
For example, the whole numbers sit inside the integers as the sums of four squares.

### L2 human

We interpret $\mathsf{Q}$ in the ring $\mathcal{M} = (\mathbb{Z}, 0, 1, +, \cdot)$.

1. Let $\delta(x)$ be $\exists a \, \exists b \, \exists c \, \exists d \, (x = a \cdot a + b \cdot b + c \cdot c + d \cdot d)$.
   By Lagrange's theorem, $\delta(\mathcal{M}) = \mathbb{N}$.
2. Let $\gamma_0(y)$ be $y = 0$, let $\gamma_S(x, y)$ be $y = x + 1$, and let $\gamma_+$ and $\gamma_\cdot$ be the graphs of $+$ and $\cdot$.
3. The sentence $\varepsilon_I$ holds in $\mathcal{M}$, because $\mathbb{N}$ is nonempty and closed under $0$, $x \mapsto x + 1$, $+$ and $\cdot$.
4. $\mathcal{M}^I$ is the standard model $(\mathbb{N}, 0, S, +, \cdot)$, so $\mathcal{M}^I \models \mathsf{Q}$.
5. Axiom 1 of $\mathsf{Q}$ becomes $\forall x \, (\delta(x) \to \forall y \, (\delta(y) \wedge y = x + 1 \to \neg (y = 0)))$, which is true in $\mathbb{Z}$.
6. By part 2, every theory true in $\mathbb{Z}$, such as the theory of commutative rings, is undecidable.

The typical use of the theorem is this pattern: define a copy of the natural numbers inside a structure, then conclude undecidability.

### L3 human

Interpretations are the morphisms between theories, and the transfer theorem says that essential undecidability is closed upward along them.
The same notion of interpretation underlies the study of interpretability degrees of arithmetic theories, the bi-interpretability of structures in model theory, and the reductions between decision problems in computability.
On the positive side, interpretations transfer decidability downward, as in the interpretation of many structures in the monadic second-order theory of the binary tree.
