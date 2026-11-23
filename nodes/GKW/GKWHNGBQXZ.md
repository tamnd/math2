---
tag: GKWHNGBQXZ
kind: example
name: A Nullstellensatz refutation of three clauses
msc: ["03F20"]
topics: [CBAF7J051K]
audience: research
instance_of: [ZERBQSTZB5]
uses: [ZERBQSTZB5, T3SXVH3ZZC]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Proof systems
---

## Example

Let $F$ be the CNF with the three [[clauses|T3SXVH3ZZC]] $x \vee y$, $\neg x$ and $\neg y$.
The clauses $\neg x$ and $\neg y$ force $x = y = 0$, and then $x \vee y$ is false, so $F$ is unsatisfiable.
We give a [[Nullstellensatz refutation|ZERBQSTZB5]] of $F$ over an arbitrary field $\mathbb{F}$, with $1$ read as true.

1. The translation of $x \vee y$ is $f_1 = (1 - x)(1 - y)$, since both literals are positive.
2. The translation of $\neg x$ is $f_2 = x$, and the translation of $\neg y$ is $f_3 = y$.
3. Take $g_1 = 1$, $g_2 = 1 - y$ and $g_3 = 1$, and take $h_x = h_y = 0$ for the Boolean axioms.
4. Then $g_1 f_1 = 1 - x - y + xy$.
5. Also $g_2 f_2 = (1 - y) x = x - xy$.
6. Also $g_3 f_3 = y$.
7. The sum of the three products is $1 - x - y + xy + x - xy + y = 1$.

So $g_1 f_1 + g_2 f_2 + g_3 f_3 = 1$ holds as an identity of polynomials, and the list $g_1, g_2, g_3$ is a Nullstellensatz refutation of $F$.
The products $g_1 f_1$ and $g_2 f_2$ have degree $2$ and $g_3 f_3$ has degree $1$, so the degree of the refutation is $2$.
The size is $4 + 2 + 1 = 7$ monomials.

## Remarks

### Why degree 2 is needed

The degree $2$ is the least possible.
In a refutation of degree $1$, the product $g_1 f_1$ must be $0$, because $f_1$ has degree $2$, and every $h_j (x_j^2 - x_j)$ must be $0$ for the same reason.
Then $g_2$ and $g_3$ are constants $b, c$, and $b x + c y = 1$ has no solution, since the constant term of the left side is $0$.

### The link with resolution

The certificate does not use the Boolean axioms.
It follows the [[resolution refutation|6JSH907W5R]] that resolves $x \vee y$ with $\neg x$ to get $y$, and then $y$ with $\neg y$.
The factor $1 - y$ in $g_2$ corresponds to the literal $y$ that stays in the resolvent of the first step.

## Explanations

### L1 human

The three rules are "$x$ or $y$", "not $x$" and "not $y$", and they cannot all hold.
With $1$ for true, each rule becomes a polynomial that is $0$ exactly when the rule holds.
We multiply these polynomials by other polynomials and add them, and the result is the number $1$.
If all three rules held, every polynomial would be $0$, so the sum would be $0$, and not $1$.

### L2 human

The method is to guess the multipliers $g_i$ and to check the identity by expansion.

1. Start with $g_1 = 1$, so that the sum contains $1 - x - y + xy$.
2. Choose $g_2 = 1 - y$ to cancel the terms $-x$ and $xy$.
3. Choose $g_3 = 1$ to cancel the term $-y$.

A trap is to read the translation with the opposite convention: with $0$ for true, the clause $x \vee y$ becomes $xy$ and the certificate changes.
