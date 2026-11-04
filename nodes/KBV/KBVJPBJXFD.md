---
tag: KBVJPBJXFD
kind: proof
name: Proof of the associativity of addition by induction
msc: [03F30]
proves: 0C32J27WQC
uses: [0W5DSDFQ4G, 0832XVR512, 0ASJVEFA9J]
methods: [0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Proofs_involving_the_addition_of_natural_numbers
    locator: Proof of associativity
---

## Proof

We argue by [[induction|0ASJVEFA9J]] on $c$.
Let $S$ be the [[successor function|0832XVR512]].
The [[addition|0W5DSDFQ4G]] satisfies $x + 0 = x$ and $x + S(y) = S(x + y)$ for all natural numbers $x$ and $y$.
Fix natural numbers $a$ and $b$.

1. For $c = 0$: the definition gives $(a + b) + 0 = a + b$.
2. Also $b + 0 = b$, so $a + (b + 0) = a + b$. Thus $(a + b) + 0 = a + (b + 0)$.
3. Suppose that $(a + b) + c = a + (b + c)$ for some natural number $c$.
4. By the definition, $(a + b) + S(c) = S((a + b) + c)$.
5. By the hypothesis of step 3, $S((a + b) + c) = S(a + (b + c))$.
6. By the definition, $S(a + (b + c)) = a + S(b + c)$.
7. By the definition again, $S(b + c) = b + S(c)$, so $a + S(b + c) = a + (b + S(c))$.
8. Steps 4 to 7 give $(a + b) + S(c) = a + (b + S(c))$.
9. Since $S(c) = c + 1$, induction gives $(a + b) + c = a + (b + c)$ for every natural number $c$. As $a$ and $b$ were arbitrary, the law holds for all $a$, $b$ and $c$.

## Idea

The recursive definition of addition peels one successor off the last number at a time.
On both sides, this successor moves to the outside in the same way.
So the case $S(c)$ reduces to the case $c$.
