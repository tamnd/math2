---
tag: DE8YZ5SDH3
kind: example
name: Peano arithmetic proves that addition is commutative
msc: ["03F30"]
topics: [QHCRN4JVG0]
audience: grad
illustrates: [HACXBCM7SS, 1QD0KDDGYJ]
uses: [Z8YDBW2857, TT8MXRTVBM, G55NMADJ6G]
sources:
  - url: https://en.wikipedia.org/wiki/Peano_axioms
    locator: Addition
  - book: isbn:9780521857840
---

## Example

We prove $\forall x\, \forall y\,(x + y = y + x)$ in [[Peano arithmetic|Z8YDBW2857]].
The axioms $\mathsf{Q}4$ and $\mathsf{Q}5$ of [[Robinson arithmetic|TT8MXRTVBM]] only say how a sum behaves in its right argument.
So we first prove two rules for the left argument, each by one instance of the [[induction schema|G55NMADJ6G]], and then a third induction swaps the arguments.

Lemma A: $\mathsf{PA} \vdash \forall x\,(0 + x = x)$.

1. We use induction on $x$ for $\varphi_A(x) := 0 + x = x$.
2. The base $0 + 0 = 0$ is an instance of $\mathsf{Q}4$.
3. For the step, assume $0 + x = x$.
   Then $0 + S x = S(0 + x)$ by $\mathsf{Q}5$, and $S(0 + x) = S x$ by the assumption.

Lemma B: $\mathsf{PA} \vdash \forall x\, \forall y\,(S x + y = S(x + y))$.

4. We keep $x$ as a parameter and use induction on $y$ for $\varphi_B(y, x) := S x + y = S(x + y)$.
5. For the base, $S x + 0 = S x$ by $\mathsf{Q}4$, and $S(x + 0) = S x$ by $\mathsf{Q}4$ inside $S$.
6. For the step, assume $S x + y = S(x + y)$.
   Then $\mathsf{Q}5$, the assumption and $\mathsf{Q}5$ again give the chain below.

$$S x + S y = S(S x + y) = S(S(x + y)) = S(x + S y).$$

Commutativity: $\mathsf{PA} \vdash \forall y\, \forall x\,(x + y = y + x)$.

7. We keep $y$ as a parameter and use induction on $x$ for $\varphi_C(x, y) := x + y = y + x$.
8. For the base, $0 + y = y$ by Lemma A, and $y = y + 0$ by $\mathsf{Q}4$, so $0 + y = y + 0$.
9. For the step, assume $x + y = y + x$.
   Then Lemma B, the assumption and $\mathsf{Q}5$ give the chain below.

$$S x + y = S(x + y) = S(y + x) = y + S x.$$

10. The induction axiom for $\varphi_C$ gives $\forall x\,(x + y = y + x)$, and generalization over $y$ gives the claim.

## Remarks

The example shows the typical pattern of a proof in $\mathsf{PA}$: lemmas proved by induction feed the step of a later induction.
All three formulas $\varphi_A$, $\varphi_B$ and $\varphi_C$ are quantifier-free, so the proof works already with [[open induction|GJ9KW45F3C]].

Induction cannot be dropped.
In [[this model of Q|PR8Z1YPJDK]], with two extra elements $a$ and $b$, we have $0 + a = b$ and $a + 0 = a$.
So Lemma A and commutativity both fail there, and $\mathsf{Q}$ alone proves neither.
Lemma B holds in that model, for example $S a + a = a + a = b$ and $S(a + a) = S b = b$, so the model does not decide whether $\mathsf{Q}$ proves Lemma B.

What changes for multiplication?
The same plan works, with more lemmas: first $0 \cdot x = 0$ and $S x \cdot y = x \cdot y + y$, then commutativity of $\cdot$, and these use associativity and commutativity of $+$.

## Explanations

### L1 human

We want to show that $x + y = y + x$ for all numbers.
The axioms only say how to add on the right: $x + 0 = x$ and $x + (y + 1) = (x + y) + 1$.
So we first show, by induction, how adding works on the left: $0 + x = x$ and $(x + 1) + y = (x + y) + 1$.
Then a third induction turns the left rules and the right rules into the swap $x + y = y + x$.

### L2 human

We trace one step of the main induction with $y = \overline{3}$, from $x = \overline{1}$ to $x = \overline{2}$.
The hypothesis of the step is $\overline{1} + \overline{3} = \overline{3} + \overline{1}$.
Lemma B with $x = \overline{1}$ gives $\overline{2} + \overline{3} = S(\overline{1} + \overline{3})$, and the hypothesis turns the right side into $S(\overline{3} + \overline{1})$.
Then $\mathsf{Q}5$ finishes the step:
$$S(\overline{3} + \overline{1}) = \overline{3} + S\,\overline{1} = \overline{3} + \overline{2}.$$
Check: both sides have the value $5$ in the standard model.
The typical use of this example is as the first lemma of formal number theory, since nearly every later proof reorders a sum.
The trap is to induct on $y$ in the main proof without Lemma B, because the step then needs $x + S y = S y + x$, which again needs a rule for the left argument.
