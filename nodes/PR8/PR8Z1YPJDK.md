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

[[Robinson arithmetic|TT8MXRTVBM]] proves $0 + \overline{n} = \overline{n}$ for every numeral, yet it does not prove $\forall x\,(0 + x = x)$.
To show this, we build a structure $\mathfrak{M}$ for $L_A$ that satisfies every axiom of $\mathsf{Q}$ and in which $0 + x = x$ fails.

The domain is $M = \mathbb{N} \cup \{a, b\}$, where $a$ and $b$ are two new elements.
On $\mathbb{N}$, the symbols $0$, $S$, $+$ and $\cdot$ have their usual meaning, and $S(a) = a$, $S(b) = b$.
For addition, let $x + n = x$ for $x \in \{a, b\}$ and $n \in \mathbb{N}$, and for every $x \in M$ let $x + a = b$ and $x + b = a$.
For multiplication, let $x \cdot 0 = 0$ for every $x$, and for $n \ge 1$ let $a \cdot n = b$ and $b \cdot n = a$.
Let $0 \cdot a = 0 \cdot b = 0$, and for $n \ge 1$ let $n \cdot a = a$ and $n \cdot b = b$.
Finally, let $a \cdot a = b$, $b \cdot a = a$, $a \cdot b = b$ and $b \cdot b = a$.
Interpret $<$ by $\mathsf{Q}8$: $x < y$ holds when $v + S x = y$ for some $v \in M$.

We check $\mathsf{Q}1$ to $\mathsf{Q}7$, since $\mathsf{Q}8$ holds by the choice of $<$.
On $\mathbb{N}$ every axiom holds, as in [[the standard model|WXHVSE066S]], so only the cases with $a$ or $b$ remain.

1. $\mathsf{Q}1$ and $\mathsf{Q}2$: $S$ maps $\mathbb{N}$ injectively onto $\mathbb{N} \setminus \{0\}$ and fixes $a$ and $b$, so $S$ is injective and never takes the value $0$.
2. $\mathsf{Q}3$: $a = S(a)$ and $b = S(b)$, so $a$ and $b$ have predecessors.
3. $\mathsf{Q}4$: $a + 0 = a$ and $b + 0 = b$, by the rule $x + n = x$.
4. $\mathsf{Q}5$ with $y = n \in \mathbb{N}$ and $x \in \{a, b\}$: both $x + (n + 1)$ and $S(x + n) = S(x)$ equal $x$.
5. $\mathsf{Q}5$ with $y = a$: since $S a = a$, the left side is $x + a = b$, and the right side is $S(x + a) = S(b) = b$.
6. $\mathsf{Q}5$ with $y = b$: the left side is $x + b = a$, and the right side is $S(x + b) = S(a) = a$.
7. $\mathsf{Q}6$ holds by definition.
8. $\mathsf{Q}7$ with $x = a$ and $y = n$: the left side is $a \cdot (n + 1) = b$.
   The right side $a \cdot n + a$ is $0 + a = b$ if $n = 0$, and $b + a = b$ if $n \ge 1$.
9. $\mathsf{Q}7$ with $x = b$ and $y = n$: the left side is $b \cdot (n + 1) = a$.
   The right side $b \cdot n + b$ is $0 + b = a$ if $n = 0$, and $a + b = a$ if $n \ge 1$.
10. $\mathsf{Q}7$ with $y = a$: since $S a = a$, we need $x \cdot a = x \cdot a + x$.
    For $x = 0$ both sides are $0$, for $x = n \ge 1$ we get $a + n = a$, for $x = a$ we get $b + a = b$, and for $x = b$ we get $a + b = a$.
11. $\mathsf{Q}7$ with $y = b$: we need $x \cdot b = x \cdot b + x$.
    For $x = 0$ both sides are $0$, for $x = n \ge 1$ we get $b + n = b$, for $x = a$ we get $b + a = b$, and for $x = b$ we get $a + b = a$.

So $\mathfrak{M} \models \mathsf{Q}$.
In $\mathfrak{M}$ we have $0 + a = b \ne a$, while $a + 0 = a$.

## Remarks

By [[soundness|4A84VHDTHV]], a sentence that is false in one model of $\mathsf{Q}$ is not a theorem of $\mathsf{Q}$.
So $\mathsf{Q}$ does not prove $\forall x\,(0 + x = x)$, since $0 + a = b$.
It does not prove the commutativity of addition, since $a + 0 = a$ and $0 + a = b$.
It does not prove the commutativity of multiplication, since $a \cdot \overline{2} = b$ and $\overline{2} \cdot a = a$.

Associativity fails too.
Compute both groupings of $0 + a + a$:
$$(0 + a) + a = b + a = b, \qquad 0 + (a + a) = 0 + b = a.$$
The model also has $S a = a$, so $\mathsf{Q}$ does not prove $\forall x\,(S x \ne x)$.
Even the order misbehaves: $a + S a = a + a = b$ gives $a < b$, and $b + S b = b + b = a$ gives $b < a$.

All these sentences are true in $\mathbb{N}$, and [[Peano arithmetic|HACXBCM7SS]] proves each of them by induction.
The elements $a$ and $b$ are non-standard, because they are not values of numerals.
That is why the numerical instances survive: every instance $0 + \overline{n} = \overline{n}$ talks only about standard elements.

## Explanations

### L1 human

Robinson arithmetic has a rule for adding a number on the right, but no rule for adding on the left.
So we can invent two extra "numbers" $a$ and $b$ that behave strangely when they are added on the left.
In this world, $a + 0 = a$ but $0 + a = b$.
All the rules still hold, so the rules alone cannot prove that $0 + x = x$.

### L2 human

We check one axiom instance by hand: $\mathsf{Q}7$ with $x = \overline{2}$ and $y = a$, which says $\overline{2} \cdot S a = \overline{2} \cdot a + \overline{2}$.
The left side is $\overline{2} \cdot a = a$, because $S a = a$ and $n \cdot a = a$ for $n \ge 1$.
The right side is $a + \overline{2} = a$, because $x + n = x$ for $x \in \{a, b\}$.
Both sides equal $a$, so the instance holds.

A model like this is the standard way to show that a sentence is independent of $\mathsf{Q}$.
Watch out: it is easy to define the new elements so that only the addition axioms hold.
Each multiplication case must be checked as well, as steps 8 to 11 do.
