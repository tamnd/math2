---
tag: 2PZM6JSNN2
kind: proof
name: Proof of the distributive law by induction
msc: [03F30]
proves: 0KBEMAJAYA
uses: [0W5DSDFQ4G, 0JRC32D6K2, 0832XVR512, 0C32J27WQC, 0ASJVEFA9J]
methods: [0ASJVEFA9J]
sources:
  - url: https://proofwiki.org/wiki/Natural_Number_Multiplication_Distributes_over_Addition
---

## Proof

We argue by [[induction|0ASJVEFA9J]] on $c$.
Let $S$ be the [[successor function|0832XVR512]].
The [[addition|0W5DSDFQ4G]] satisfies $x + 0 = x$ and $x + S(y) = S(x + y)$.
The [[multiplication|0JRC32D6K2]] satisfies $x \cdot 0 = 0$ and $x \cdot S(y) = x \cdot y + x$.
Fix natural numbers $a$ and $b$.

1. For $c = 0$: since $b + 0 = b$, we get $a \cdot (b + 0) = a \cdot b$.
2. Also $a \cdot 0 = 0$, so $a \cdot b + a \cdot 0 = a \cdot b + 0 = a \cdot b$. Thus the law holds for $c = 0$.
3. Suppose that $a \cdot (b + c) = a \cdot b + a \cdot c$ for some natural number $c$.
4. By the definition of addition, $b + S(c) = S(b + c)$. So $a \cdot (b + S(c)) = a \cdot S(b + c)$.
5. By the definition of multiplication, $a \cdot S(b + c) = a \cdot (b + c) + a$.
6. By the hypothesis of step 3, $a \cdot (b + c) + a = (a \cdot b + a \cdot c) + a$.
7. By the [[associativity of addition|0C32J27WQC]], $(a \cdot b + a \cdot c) + a = a \cdot b + (a \cdot c + a)$.
8. By the definition of multiplication, $a \cdot c + a = a \cdot S(c)$.
9. Steps 4 to 8 give $a \cdot (b + S(c)) = a \cdot b + a \cdot S(c)$.
10. Since $S(c) = c + 1$, induction gives the law for every natural number $c$. As $a$ and $b$ were arbitrary, it holds for all $a$, $b$ and $c$.

## Idea

Both recursive definitions work on the last argument, so we induct on $c$.
Going from $c$ to $c + 1$ adds one more copy of $a$ on each side.
Associativity of addition lets us put that copy next to $a \cdot c$.
