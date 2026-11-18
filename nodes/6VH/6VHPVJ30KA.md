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

Let $R$ be a new binary relation symbol, read as "pigeon $u$ sits in hole $v$".
The pigeonhole principle for $R$ at $x$ is the $\Delta_0(R)$ formula $\mathrm{PHP}(R, x) := \neg (F(x) \land I(x))$, where
$$F(x) := (\forall u \le x)(\exists v < x) R(u, v), \qquad I(x) := (\forall u \le x)(\forall u' \le x)(\forall v < x)\big(u < u' \to \neg (R(u, v) \land R(u', v))\big).$$
It says that $x + 1$ pigeons cannot sit in $x$ holes with at most one pigeon in each hole.
We compute the [[Paris-Wilkie translation|ZVD982MVST]] at $x = n$, with $(\exists v < n)$ translated as a disjunction over $j = 0, \dots, n - 1$.

1. Atoms. $R(i, j)$ becomes the variable $p_{i, j}$. An atom $i < i'$ is a closed atom without $R$, so it becomes $\top$ if $i < i'$ and $\bot$ otherwise.
2. $F(n)^{\mathrm{PW}} = \bigwedge_{i = 0}^{n} \bigvee_{j = 0}^{n - 1} p_{i, j}$. Each pigeon sits in some hole.
3. $I(n)^{\mathrm{PW}} = \bigwedge_{i, i' \le n} \bigwedge_{j < n} \big(c_{i, i'} \to \neg (p_{i, j} \land p_{i', j})\big)$, where $c_{i, i'}$ is $\top$ for $i < i'$ and $\bot$ otherwise.
4. A conjunct with $c_{i, i'} = \bot$ is the formula $\bot \to \dots$, which is true. Removing these conjuncts leaves $\bigwedge_{i < i' \le n} \bigwedge_{j < n} \neg (p_{i, j} \land p_{i', j})$.
5. So $\mathrm{PHP}(R, n)^{\mathrm{PW}}$ is, up to these constant conjuncts, the formula $\mathrm{PHP}^{n+1}_n$ of propositional proof complexity: $\neg \big( \bigwedge_{i \le n} \bigvee_{j < n} p_{i, j} \land \bigwedge_{i < i' \le n} \bigwedge_{j < n} \neg (p_{i, j} \land p_{i', j}) \big)$.
6. Size. There are $n(n + 1)$ variables. The second conjunction has $n \cdot n(n + 1)/2$ parts, so the size is of order $n^3$.
7. Truth. An assignment that makes the part inside $\neg$ true gives an injective map from $n + 1$ pigeons to $n$ holes. The finite [[pigeonhole principle|0HGVCWQGY3]] excludes this, so the formula is a [[tautology|05006AJ7DZ]].
8. For $n = 1$ the formula is $\neg \big(p_{0,0} \land p_{1,0} \land \neg (p_{0,0} \land p_{1,0})\big)$, an instance of $\neg (q \land \neg q)$.

## Remarks

The example connects a theorem of bounded arithmetic with the best-known family of hard tautologies.
Ajtai proved that the formulas $\mathrm{PHP}^{n+1}_n$ have no constant-depth Frege proofs of polynomial size.
By the contrapositive of the Paris-Wilkie theorem, [[$\mathsf{I}\Delta_0(R)$|FYGWNXETVJ]] does not prove $\forall x \, \mathrm{PHP}(R, x)$.
Ajtai's theorem also covers the stronger theory $T_2(R)$, and later work improved the propositional lower bound to an exponential one.
If $n + 1$ pigeons are replaced by $2n$ or $n^2$ pigeons, the translations are the weak pigeonhole formulas, and their status is part of the [[open problems on pigeonhole principles|NJ18EZ5JBC]].

## Explanations

### L1 human

Three pigeons cannot sit in two holes with at most one pigeon in each hole.
Write "pigeon $i$ sits in hole $j$" as a switch, which gives $6$ switches for $3$ pigeons and $2$ holes.
The statement becomes a long formula about the switches, and it is true for every setting of the switches.
For large numbers this formula is hard to prove in some simple proof systems, even though the reason is easy.

### L2 human

We write out $\mathrm{PHP}^{3}_{2}$, the case $n = 2$.

1. Variables: $p_{i, j}$ for pigeons $i = 0, 1, 2$ and holes $j = 0, 1$, which gives $6$ variables.
2. Each pigeon sits somewhere: $(p_{0,0} \lor p_{0,1}) \land (p_{1,0} \lor p_{1,1}) \land (p_{2,0} \lor p_{2,1})$.
3. No hole has two pigeons: for each hole $j$ and each pair $i < i'$ among $3$ pairs, $\neg (p_{i, j} \land p_{i', j})$. This gives $2 \cdot 3 = 6$ conjuncts.
4. The formula $\mathrm{PHP}^3_2$ is the negation of the conjunction of the $3 + 6 = 9$ parts.
5. Check: if the $3$ clauses of step 2 hold, two pigeons choose the same hole among $2$ holes. A conjunct of step 3 then fails.

The typical use is to transfer lower bounds for $\mathrm{PHP}^{n+1}_n$ in proof complexity into unprovability results in bounded arithmetic.
A trap is to forget the new symbol $R$: for a $\Delta_0$ formula without $R$, every atom is $\top$ or $\bot$, and the translation gives no hard tautology.
