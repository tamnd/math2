---
tag: 6VHPVJ30KA
kind: example
name: The pigeonhole principle translates to the propositional pigeonhole formulas
msc: ["03F30", "03F20"]
topics: [RA380RWEC0]
audience: research
instance_of: [ZVD982MVST]
uses: [ZVD982MVST, 0HGVCWQGY3, 05006AJ7DZ, FYGWNXETVJ]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_arithmetic
    locator: Correspondence to propositional proof systems
  - url: https://en.wikipedia.org/wiki/Pigeonhole_principle
    locator: lead section
---

## Example

The statement "$n + 1$ pigeons do not fit into $n$ holes, one to a hole" translates into the most studied family of hard tautologies.
Let $R$ be a new binary relation symbol, read as "pigeon $u$ sits in hole $v$".
The pigeonhole principle for $R$ at $x$ is the $\Delta_0(R)$ formula $\mathrm{PHP}(R, x) := \neg (F(x) \land I(x))$, with $F$ and $I$ as follows.

$$F(x) := (\forall u \le x)(\exists v < x)\, R(u, v)$$

$$I(x) := (\forall u \le x)(\forall u' \le x)(\forall v < x)\big(u < u' \to \neg (R(u, v) \land R(u', v))\big)$$

So $F$ says that every pigeon sits in some hole, and $I$ says that no hole holds two pigeons.
We compute the [[Paris-Wilkie translation|ZVD982MVST]] at $x = n$, with $(\exists v < n)$ translated as a disjunction over $j = 0, \dots, n - 1$.

1. Atoms: $R(i, j)$ becomes the variable $p_{i, j}$.
   An atom $i < i'$ has no $R$, so it becomes $\top$ if $i < i'$ and $\bot$ otherwise; call this constant $c_{i, i'}$.
2. Each pigeon sits in some hole: $F(n)^{\mathrm{PW}} = \bigwedge_{i = 0}^{n} \bigvee_{j = 0}^{n - 1} p_{i, j}$.
3. No hole holds two pigeons: $I(n)^{\mathrm{PW}} = \bigwedge_{i, i' \le n} \bigwedge_{j < n} \big(c_{i, i'} \to \neg (p_{i, j} \land p_{i', j})\big)$.
4. A conjunct with $c_{i, i'} = \bot$ has the form $\bot \to \dots$, which is true.
   Removing these conjuncts leaves $\bigwedge_{i < i' \le n} \bigwedge_{j < n} \neg (p_{i, j} \land p_{i', j})$.
5. So, up to these constant conjuncts, $\mathrm{PHP}(R, n)^{\mathrm{PW}}$ is the formula $\mathrm{PHP}^{n+1}_n$ of propositional proof complexity, shown below.

$$\neg \Big( \bigwedge_{i \le n} \bigvee_{j < n} p_{i, j} \land \bigwedge_{i < i' \le n} \bigwedge_{j < n} \neg (p_{i, j} \land p_{i', j}) \Big)$$

6. Size: there are $n(n + 1)$ variables, and the second conjunction has $n \cdot n(n + 1)/2$ parts, so the size is of order $n^3$.
7. Truth: an assignment that makes the part inside $\neg$ true gives an injective map from $n + 1$ pigeons to $n$ holes.
   The finite [[pigeonhole principle|0HGVCWQGY3]] excludes this, so the formula is a [[tautology|05006AJ7DZ]].

For $n = 1$ the formula is $\neg \big(p_{0,0} \land p_{1,0} \land \neg (p_{0,0} \land p_{1,0})\big)$, an instance of $\neg (q \land \neg q)$.

## Remarks

The example connects a theorem of arithmetic with the hard tautologies of proof complexity.
[[Ajtai's theorem|Q0ERK64J78]] says that the formulas $\mathrm{PHP}^{n+1}_n$ have no bounded-depth Frege proofs of polynomial size.
By the contrapositive of the Paris-Wilkie theorem, [[$\mathsf{I}\Delta_0(R)$|FYGWNXETVJ]] does not prove $\forall x \, \mathrm{PHP}(R, x)$.
Later work improved the propositional lower bound to an exponential one, and this extends the unprovability to $T_2(R)$.

If the $n + 1$ pigeons are replaced by $2n$ or $n^2$ pigeons, the translations are the weak pigeonhole formulas.
These are easier: Paris, Wilkie and Woods found bounded-depth proofs of quasipolynomial size for the case of $2n$ pigeons, and their status in bounded arithmetic is part of the [[open problems on pigeonhole principles|NJ18EZ5JBC]].

Watch out: the symbol $R$ is what makes the formula hard.
For a $\Delta_0$ formula without $R$, every atom becomes $\top$ or $\bot$, and the translation is a variable-free formula with no proof-length content.

## Explanations

### L1 human

Three pigeons cannot sit in two holes with at most one pigeon in each hole.
Write "pigeon $i$ sits in hole $j$" as a switch, which gives $6$ switches for $3$ pigeons and $2$ holes.
The statement becomes a long formula about the switches, and it is true for every setting of the switches.
For large numbers this formula is hard to prove in some simple proof systems, even though the reason is easy.

### L2 human

We write out $\mathrm{PHP}^{3}_{2}$, the case $n = 2$, with variables $p_{i, j}$ for pigeons $i = 0, 1, 2$ and holes $j = 0, 1$.
That gives $6$ variables.
Each pigeon sits somewhere:

$$(p_{0,0} \lor p_{0,1}) \land (p_{1,0} \lor p_{1,1}) \land (p_{2,0} \lor p_{2,1}).$$

No hole holds two pigeons: for each of the $2$ holes and each of the $3$ pairs $i < i'$, we get $\neg (p_{i, j} \land p_{i', j})$, which makes $6$ conjuncts.
The formula $\mathrm{PHP}^3_2$ is the negation of the conjunction of these $3 + 6 = 9$ parts.
Check: if the $3$ clauses hold, two of the three pigeons choose the same hole among $2$ holes, and the conjunct for that pair and that hole fails.
The problem shows the typical use: a lower bound for $\mathrm{PHP}^{n+1}_n$ in a proof system becomes an unprovability result in bounded arithmetic.
