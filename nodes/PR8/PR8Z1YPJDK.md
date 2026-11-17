---
tag: PR8Z1YPJDK
kind: example
name: A model of Robinson arithmetic in which addition is not commutative
msc: ["03F30", "03C62"]
topics: [QHCRN4JVG0]
audience: grad
instance_of: [3K1AKGXF8A]
uses: [TT8MXRTVBM, MVCH6N9SNW, 4A84VHDTHV]
sources:
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
  - book: isbn:9780521857840
---

## Example

We build a structure $\mathfrak{M}$ for $L_A$ that satisfies all axioms of [[Robinson arithmetic|TT8MXRTVBM]] but in which $0 + x = x$ fails.
The domain is $M = \N \cup \set{a, b}$, where $a$ and $b$ are two new elements.
On $\N$, the symbols $0$, $S$, $+$ and $\cdot$ have their usual meaning.
On the new elements, let $S(a) = a$ and $S(b) = b$.
For addition, let $x + n = x$ for $x \in \set{a, b}$ and $n \in \N$, and for every $x \in M$ let $x + a = b$ and $x + b = a$.
For multiplication, let $x \cdot 0 = 0$ for every $x$, and for $n \ge 1$ let $a \cdot n = b$ and $b \cdot n = a$.
Further, let $0 \cdot a = 0 \cdot b = 0$, and for $n \ge 1$ let $n \cdot a = a$ and $n \cdot b = b$.
Finally, let $a \cdot a = b$, $b \cdot a = a$, $a \cdot b = b$ and $b \cdot b = a$.
Interpret $<$ by $\mathsf{Q}8$: $x < y$ holds when $v + S x = y$ for some $v \in M$.

We check $\mathsf{Q}1$ to $\mathsf{Q}7$; $\mathsf{Q}8$ holds by the choice of $<$.
On $\N$ every axiom holds, as in [[the standard model|WXHVSE066S]], so we check only the cases that involve $a$ or $b$.

1. $\mathsf{Q}1$ and $\mathsf{Q}2$: $S$ maps $\N$ injectively onto $\N \setminus \set{0}$ and fixes $a$ and $b$. So $S$ is injective and never takes the value $0$.
2. $\mathsf{Q}3$: $a = S(a)$ and $b = S(b)$, so $a$ and $b$ have predecessors.
3. $\mathsf{Q}4$: $a + 0 = a$ and $b + 0 = b$, by the rule $x + n = x$.
4. $\mathsf{Q}5$ with $y = n \in \N$ and $x \in \set{a, b}$: both $x + (n + 1)$ and $S(x + n) = S(x)$ equal $x$.
5. $\mathsf{Q}5$ with $y = a$: $S y = a$, so $x + S y = b$, and $S(x + a) = S(b) = b$.
6. $\mathsf{Q}5$ with $y = b$: $x + S y = x + b = a$, and $S(x + b) = S(a) = a$.
7. $\mathsf{Q}6$ holds by definition.
8. $\mathsf{Q}7$ with $x = a$ and $y = n$: $a \cdot (n + 1) = b$. The right side $a \cdot n + a$ is $0 + a = b$ if $n = 0$, and $b + a = b$ if $n \ge 1$.
9. $\mathsf{Q}7$ with $x = b$ and $y = n$: $b \cdot (n + 1) = a$. The right side $b \cdot n + b$ is $0 + b = a$ if $n = 0$, and $a + b = a$ if $n \ge 1$.
10. $\mathsf{Q}7$ with $y = a$, so $S y = a$: we need $x \cdot a = x \cdot a + x$. For $x = 0$ both sides are $0$. For $x = n \ge 1$, $a + n = a$. For $x = a$, $b + a = b$. For $x = b$, $a + b = a$.
11. $\mathsf{Q}7$ with $y = b$: we need $x \cdot b = x \cdot b + x$. For $x = 0$ both sides are $0$. For $x = n \ge 1$, $b + n = b$. For $x = a$, $b + a = b$. For $x = b$, $a + b = a$.

So $\mathfrak{M} \models \mathsf{Q}$.
In $\mathfrak{M}$ we have $0 + a = b \ne a$, while $a + 0 = a$.

## Remarks

By [[soundness|4A84VHDTHV]], a sentence false in a model of $\mathsf{Q}$ is not a theorem of $\mathsf{Q}$.
So $\mathsf{Q}$ proves none of the following sentences, each false in $\mathfrak{M}$:

- $\forall x\,(0 + x = x)$, since $0 + a = b$;
- $\forall x\, \forall y\,(x + y = y + x)$, since $a + 0 = a$ and $0 + a = b$;
- $\forall x\, \forall y\, \forall z\,((x + y) + z = x + (y + z))$, since $(0 + a) + a = b + a = b$ and $0 + (a + a) = 0 + b = a$;
- $\forall x\, \forall y\,(x \cdot y = y \cdot x)$, since $a \cdot \overline{2} = b$ and $\overline{2} \cdot a = a$;
- $\forall x\,(S x \ne x)$, since $S(a) = a$;
- $\forall x\, \forall y\, \neg(x < y \land y < x)$, since $a < b$ and $b < a$.

For the last item: $a + S a = a + a = b$, so $a < b$, and $b + S b = b + b = a$, so $b < a$.
All six sentences are true in $\N$, and [[Peano arithmetic|HACXBCM7SS]] proves each of them by induction.
The elements $a$ and $b$ are non-standard: they are not values of numerals.

## Explanations

### L1 human

Robinson arithmetic has rules for adding a number on the right, but no rule for adding on the left.
So we can invent two extra "numbers" $a$ and $b$ that behave strangely when added on the left.
In this world, $a + 0 = a$ but $0 + a = b$.
All eight rules still hold, so the rules alone cannot prove that $0 + x = x$.

### L2 human

We check one axiom instance by hand, $\mathsf{Q}7$ with $x = \overline{2}$ and $y = a$.

1. $\mathsf{Q}7$ says $\overline{2} \cdot S a = \overline{2} \cdot a + \overline{2}$.
2. The left side is $\overline{2} \cdot a = a$, because $S a = a$ and $n \cdot a = a$ for $n \ge 1$.
3. The right side is $a + \overline{2} = a$, because $x + n = x$ for $x \in \set{a, b}$.
4. Both sides equal $a$, so this instance holds.

The typical use of such a model is to show that a sentence is independent of $\mathsf{Q}$.
A trap is to define the new elements so that only the addition axioms hold; each multiplication case must also be checked.
