---
tag: EW0QB5XZS9
kind: proof
name: Proof that arithmetical comprehension is equivalent to the existence of ranges of one-to-one functions
msc: ["03B30", "03F35"]
topics: [BY8AAFN7C5]
audience: grad
proves: 3MQ39PRCYJ
uses: [DNXCKXZZ08, K9XG0Z2N9V, CS82V969DE]
methods: [0NTF6DMVAP, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Arithmetical comprehension ACA0
---

## Proof

We work in [[RCA0|DNXCKXZZ08]] and prove $1 \Rightarrow 3 \Rightarrow 2 \Rightarrow 1$; the middle step lists a $\Sigma^0_1$ set without repeats by its least witnesses.

### From comprehension to ranges

1. The range of $f$ is defined by the formula $\exists i\, f(i) = m$, which is arithmetical with parameter $f$.
   So [[arithmetical comprehension|K9XG0Z2N9V]] gives the range.

### From ranges to Σ⁰₁ comprehension

2. Let $\varphi(n) \equiv \exists j\, \theta(n, j)$ with $\theta$ a $\Sigma^0_0$ formula.
3. Let $D$ be the set of pairs $(n, j)$ such that $\theta(n, j)$ holds and $\theta(n, j')$ fails for all $j' < j$.
   The condition is $\Sigma^0_0$, so $D$ exists by $\Delta^0_1$ comprehension.
4. Define $f(m) = 2n + 1$ if $m = (n, j) \in D$, and $f(m) = 2m$ otherwise.
   Its graph is $\Sigma^0_0$ in $D$, so $f$ exists.
5. The function $f$ is one-to-one.
   Each even value $2m$ comes from $m$ alone, and if $f(m) = f(m') = 2n + 1$, then $m = (n, j)$ and $m' = (n, j')$ are both in $D$.
   Both $j$ and $j'$ are the least witness for $n$, so $j = j'$ and $m = m'$.
6. By statement 3, the range $R$ of $f$ exists.
7. If $\theta(n, j)$ holds for some $j$, then there is a least such $j$, by the least number principle for $\Sigma^0_0$ formulas, which $\mathsf{RCA}_0$ proves.
   Then $(n, j) \in D$ and $2n + 1 = f((n, j)) \in R$.
8. Conversely, if $2n + 1 = f(m)$, then $m = (n, j) \in D$ for some $j$, so $\theta(n, j)$ holds.
9. So $\{ n : 2n + 1 \in R \}$, which exists by $\Delta^0_1$ comprehension, is $\{ n : \varphi(n) \}$.

### From Σ⁰₁ comprehension to arithmetical comprehension

10. By induction on $k$ outside the system, we show comprehension for $\Sigma^0_k$ and for $\Pi^0_k$ formulas.
    The case $k = 0$ is $\Delta^0_1$ comprehension.
11. Let $\varphi(n)$ be $\Pi^0_k$ with $k \ge 1$.
    Its negation is equivalent to a $\Sigma^0_k$ formula, which defines a set $Y$ by the case $k$, and the complement of $Y$ exists by $\Delta^0_1$ comprehension.
12. Let $\varphi(n) \equiv \exists j\, \psi(n, j)$ with $\psi$ a $\Pi^0_k$ formula.
    The set $Z = \{ (n, j) : \psi(n, j) \}$ exists by step 11.
13. Then $\varphi(n) \leftrightarrow \exists j\, ((n, j) \in Z)$, a $\Sigma^0_1$ formula with parameter $Z$, so $\{ n : \varphi(n) \}$ exists by statement 2.
14. Every arithmetical formula is equivalent to one in [[prenex normal form|CS82V969DE]] with a $\Sigma^0_0$ matrix.
    Merging adjacent quantifiers of the same kind by pairing gives a $\Sigma^0_k$ formula for some $k$, so arithmetical comprehension holds.

## Idea

The function $f$ lists the elements of a $\Sigma^0_1$ set without repetition.
It does so by sending each element $n$ to the odd number $2n + 1$ only at its least witness, and sending everything else to distinct even numbers, so nothing is ever listed twice.
Once one $\Sigma^0_1$ quantifier can be removed, the arithmetical hierarchy falls one level at a time: each new quantifier is a $\Sigma^0_1$ question about a set we have already built.
For example, the set of indices of total programs is $\Pi^0_2$, and two steps of this kind build it from the halting set.

## Variants

For the version of statement 3 with arbitrary functions, step 4 can take $f(m) = n + 1$ when $m = (n, j)$ with $\theta(n, j)$, and $f(m) = 0$ otherwise.
Then $\varphi(n)$ holds exactly when $n + 1$ is in the range, and the set $D$ of least witnesses is not needed.
The induction in step 10 is in the metatheory, so it gives one proof for each $k$, and not a single proof of "$\Sigma^0_k$ comprehension for all $k$".
