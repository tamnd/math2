---
tag: GJ9KW45F3C
kind: example
name: Open induction proves the commutativity of addition
msc: ["03F30"]
topics: [QHCRN4JVG0]
audience: research
instance_of: [T70PYM1F36]
uses: [T70PYM1F36, 3K1AKGXF8A, 4EQPCHKEBH, PR8Z1YPJDK]
sources:
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
  - book: isbn:9780521857840
---

## Example

The law $x + y = y + x$ needs induction only on plain equations.
We show that $\mathsf{IOpen}$, the [[fragment|T70PYM1F36]] of $\mathsf{PA}$ with induction for quantifier-free formulas, proves $\forall x \, \forall y \, (x + y = y + x)$.
We use the axioms $\mathsf{Q}4$, $x + 0 = x$, and $\mathsf{Q}5$, $x + Sy = S(x + y)$, of [[Robinson arithmetic|3K1AKGXF8A]].
Each induction below is on an equation, possibly with a parameter, so each is an axiom of $\mathsf{IOpen}$.

1. Lemma A is $0 + x = x$, by induction on $x$.
   The base $0 + 0 = 0$ is $\mathsf{Q}4$, and if $0 + x = x$, then $0 + Sx = S(0 + x) = Sx$ by $\mathsf{Q}5$.
2. Lemma B is $Sy + x = S(y + x)$, by induction on $x$ with parameter $y$.
   The base is $Sy + 0 = Sy = S(y + 0)$, by $\mathsf{Q}4$ twice.
3. For the step of Lemma B, assume $Sy + x = S(y + x)$.
   Then $Sy + Sx = S(Sy + x) = SS(y + x) = S(y + Sx)$, by $\mathsf{Q}5$, the hypothesis and $\mathsf{Q}5$ again.
4. Commutativity is by induction on $y$ in $x + y = y + x$, with parameter $x$.
   The base $x + 0 = x = 0 + x$ holds by $\mathsf{Q}4$ and Lemma A.
5. For the step, assume $x + y = y + x$.
   Then $x + Sy = S(x + y) = S(y + x) = Sy + x$, by $\mathsf{Q}5$, the hypothesis and Lemma B.

So $\mathsf{IOpen} \vdash \forall x \, \forall y \, (x + y = y + x)$, with three instances of open induction.

## Remarks

The informal argument is the [[usual proof by induction|4EQPCHKEBH]]; the example checks that each induction is on a quantifier-free formula.
[[Robinson arithmetic|3K1AKGXF8A]] does not prove the law, since [[a model of Q|PR8Z1YPJDK]] has elements $a$ and $b$ with $a + b \ne b + a$.
So the law separates $\mathsf{Q}$ from $\mathsf{IOpen}$.

The associativity of $+$, the commutativity and associativity of $\cdot$, and distributivity follow by open induction in the same way.
Not all simple number theory follows, though.
By Shepherdson's theorem, $\mathsf{IOpen}$ does not prove that $\sqrt 2$ is irrational.

## Explanations

### L1 human

Commutativity says that $x + y = y + x$, for example $2 + 5 = 5 + 2$.
The starting rules only say how to add $0$ or a successor on the right.
Three short inductions move the successor from the right to the left.
Each induction is about a plain equation, so the weakest form of induction is enough.

### L2 human

We check Lemma B for $y = 1$ and $x = 2$ by unfolding the equations.
The left side is
$$S1 + 2 = S(S1 + 1) = SS(S1 + 0) = SS(S1) = 4.$$
The right side is
$$S(1 + 2) = S(S(1 + 1)) = SSS(1 + 0) = SSS1 = 4.$$
Check: both sides equal $4$, as Lemma B predicts.

The typical use is as the first step toward showing that every model of $\mathsf{IOpen}$ is a commutative discretely ordered semiring.
Watch out for the order of the lemmas.
The step of commutativity needs Lemma B, and its base needs Lemma A, so they must come first.
