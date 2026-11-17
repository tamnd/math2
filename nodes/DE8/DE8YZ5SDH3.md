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
The proof uses three instances of the [[induction schema|G55NMADJ6G]] and the axioms $\mathsf{Q}4$ and $\mathsf{Q}5$ of [[Robinson arithmetic|TT8MXRTVBM]].

Lemma A: $\mathsf{PA} \vdash \forall x\,(0 + x = x)$.

1. Use induction on $x$ for $\varphi_A(x) := 0 + x = x$.
2. Base: $0 + 0 = 0$ is an instance of $\mathsf{Q}4$.
3. Step: assume $0 + x = x$. By $\mathsf{Q}5$, $0 + S x = S(0 + x)$, and the assumption gives $S(0 + x) = S x$.

Lemma B: $\mathsf{PA} \vdash \forall x\, \forall y\,(S x + y = S(x + y))$.

4. Fix $x$ as a parameter, and use induction on $y$ for $\varphi_B(y, x) := S x + y = S(x + y)$.
5. Base: $S x + 0 = S x$ by $\mathsf{Q}4$, and $S(x + 0) = S x$ by $\mathsf{Q}4$ inside $S$.
6. Step: assume $S x + y = S(x + y)$. By $\mathsf{Q}5$, $S x + S y = S(S x + y)$.
7. By the assumption, $S(S x + y) = S(S(x + y))$, and by $\mathsf{Q}5$, $S(x + y) = x + S y$. So $S x + S y = S(x + S y)$.

Commutativity: $\mathsf{PA} \vdash \forall y\, \forall x\,(x + y = y + x)$.

8. Fix $y$ as a parameter, and use induction on $x$ for $\varphi_C(x, y) := x + y = y + x$.
9. Base: $0 + y = y$ by Lemma A, and $y = y + 0$ by $\mathsf{Q}4$. So $0 + y = y + 0$.
10. Step: assume $x + y = y + x$. By Lemma B, $S x + y = S(x + y)$.
11. By the assumption, $S(x + y) = S(y + x)$, and by $\mathsf{Q}5$, $S(y + x) = y + S x$. So $S x + y = y + S x$.
12. The induction axiom for $\varphi_C$ gives $\forall x\,(x + y = y + x)$, and generalization over $y$ gives the claim.

## Remarks

The example shows the typical pattern of a proof in $\mathsf{PA}$: lemmas proved by induction feed the step of a later induction.
Each of the three formulas $\varphi_A$, $\varphi_B$ and $\varphi_C$ is quantifier-free, so the proof works already in the fragment with open induction.
In [[this model of Q|PR8Z1YPJDK]] Lemma A and commutativity fail, since $0 + a = b$ and $a + 0 = a$.
So the inductions for $\varphi_A$ and $\varphi_C$ cannot be replaced by the axioms of $\mathsf{Q}$ alone.
Lemma B happens to hold in that model, so the model says nothing about whether $\mathsf{Q}$ proves it.

## Explanations

### L1 human

We want to show that $x + y = y + x$ for all numbers.
The axioms only say how to add on the right: $x + 0 = x$ and $x + (y + 1) = (x + y) + 1$.
So we first show, by induction, how adding works on the left: $0 + x = x$ and $(x + 1) + y = (x + y) + 1$.
Then a third induction turns the left rules and the right rules into the swap $x + y = y + x$.

### L2 human

We trace one induction step of the main proof, with $y = \overline{3}$, from $x = \overline{1}$ to $x = \overline{2}$.

1. The assumption of the step is $\overline{1} + \overline{3} = \overline{3} + \overline{1}$.
2. Lemma B with $x = \overline{1}$ and $y = \overline{3}$ gives $\overline{2} + \overline{3} = S(\overline{1} + \overline{3})$.
3. The assumption turns this into $S(\overline{3} + \overline{1})$.
4. $\mathsf{Q}5$ gives $S(\overline{3} + \overline{1}) = \overline{3} + S\,\overline{1} = \overline{3} + \overline{2}$.
5. So $\overline{2} + \overline{3} = \overline{3} + \overline{2}$, the statement at $x = \overline{2}$.

The typical use of this example is as the first lemma of formal number theory, since nearly every later proof reorders a sum.
A trap is to induct on $y$ in the main step without Lemma B: the step then needs $x + S y = S y + x$, which needs the left rule again.
