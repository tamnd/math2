---
tag: 4EQPCHKEBH
kind: proof
name: Proof of the commutativity of addition by induction
msc: [03F30]
proves: 0DFZNHJ0S2
uses: [0W5DSDFQ4G, 0832XVR512, 0ASJVEFA9J]
methods: [0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Proofs_involving_the_addition_of_natural_numbers
    locator: Proof of commutativity
---

## Proof

We argue by [[induction|0ASJVEFA9J]], first for two lemmas and then for the statement.
Let $S$ be the [[successor function|0832XVR512]].
The [[addition|0W5DSDFQ4G]] satisfies $a + 0 = a$ and $a + S(b) = S(a + b)$ for all natural numbers $a$ and $b$.
Write $1 = S(0)$. Then $n + 1 = n + S(0) = S(n + 0) = S(n)$ for each natural number $n$.

1. Lemma 1: $0 + a = a$ for every natural number $a$. We use induction on $a$.
2. For $a = 0$, the definition gives $0 + 0 = 0$.
3. Suppose that $0 + a = a$. Then $0 + S(a) = S(0 + a) = S(a)$, by the definition and the hypothesis. This proves Lemma 1.
4. Lemma 2: $S(a) + b = S(a + b)$ for all natural numbers $a$ and $b$. Fix $a$ and use induction on $b$.
5. For $b = 0$, we have $S(a) + 0 = S(a)$ and $S(a + 0) = S(a)$, so both sides are equal.
6. Suppose that $S(a) + b = S(a + b)$. Then $S(a) + S(b) = S(S(a) + b) = S(S(a + b))$, by the definition and the hypothesis.
7. Also $S(a + S(b)) = S(S(a + b))$ by the definition. So $S(a) + S(b) = S(a + S(b))$, which proves Lemma 2.
8. Now fix $a$. We prove $a + b = b + a$ by induction on $b$.
9. For $b = 0$, we have $a + 0 = a$ by the definition and $0 + a = a$ by Lemma 1. So $a + 0 = 0 + a$.
10. Suppose that $a + b = b + a$. Then $a + S(b) = S(a + b) = S(b + a)$, by the definition and the hypothesis.
11. By Lemma 2, $S(b) + a = S(b + a)$. So $a + S(b) = S(b) + a$.
12. By induction, $a + b = b + a$ for every natural number $b$. Since $a$ was arbitrary, this holds for all natural numbers $a$ and $b$.

## Idea

The definition of addition only tells us how to add $0$ or a successor on the right.
The two lemmas show that $0$ and successors behave in the same way on the left.
With them, an induction on the second number moves each successor from one side to the other.
