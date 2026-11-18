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

Work in $\mathsf{RCA}_0$.
We prove $1 \Rightarrow 3 \Rightarrow 2 \Rightarrow 1$.

1. ($1 \Rightarrow 3$) The range of $f$ is defined by $\exists i\, f(i) = m$, an arithmetical formula with parameter $f$.
2. ($3 \Rightarrow 2$) Let $\varphi(n) = \exists j\, \theta(n, j)$ with $\theta$ in $\Sigma^0_0$.
3. Let $D$ be the set of pairs $(n, j)$ with $\theta(n, j)$ and $\neg\theta(n, j')$ for all $j' < j$. It exists by $\Delta^0_1$ comprehension.
4. Define $f(m) = 2n + 1$ if $m = (n, j) \in D$, and $f(m) = 2m$ otherwise. Its graph is $\Sigma^0_0$ in $D$, so $f$ exists.
5. $f$ is one-to-one. Even values come from one $m$ each. If $f(m) = f(m') = 2n + 1$, then $m = (n, j)$ and $m' = (n, j')$ lie in $D$.
6. By the definition of $D$, neither $j < j'$ nor $j' < j$ is possible. So $j = j'$ and $m = m'$.
7. By 3, the range $R$ of $f$ exists. Claim: $\varphi(n) \leftrightarrow 2n + 1 \in R$.
8. If $\theta(n, j)$ for some $j$, then there is a least such $j$, by the least number principle for $\Sigma^0_0$ formulas, which $\mathsf{RCA}_0$ proves. Then $(n, j) \in D$ and $f((n, j)) = 2n + 1$.
9. If $2n + 1 = f(m)$, then $m = (n, j) \in D$ for some $j$, so $\theta(n, j)$.
10. So $\set{n : 2n + 1 \in R}$ exists by $\Delta^0_1$ comprehension, and it is $\set{n : \varphi(n)}$.
11. ($2 \Rightarrow 1$) By induction on $k$ outside the system, we show comprehension for $\Sigma^0_k$ and $\Pi^0_k$ formulas. The case $k = 0$ is $\Delta^0_1$ comprehension.
12. Let $\varphi(n)$ be $\Pi^0_k$. Its negation is equivalent to a $\Sigma^0_k$ formula, which defines a set $Y$. Then $\N \setminus Y$ exists by $\Delta^0_1$ comprehension.
13. Let $\varphi(n) = \exists j\, \psi(n, j)$ with $\psi$ in $\Pi^0_k$. The set $Z = \set{(n, j) : \psi(n, j)}$ exists by the previous step.
14. Then $\varphi(n) \leftrightarrow \exists j\, ((n, j) \in Z)$, a $\Sigma^0_1$ formula with parameter $Z$. By 2, $\set{n : \varphi(n)}$ exists.
15. Every arithmetical formula is equivalent to a formula in [[prenex normal form|CS82V969DE]] with a $\Sigma^0_0$ matrix. Merging like quantifiers by pairing gives a $\Sigma^0_k$ formula for some $k$. So arithmetical comprehension holds.

## Idea

The function $f$ lists the elements of a $\Sigma^0_1$ set without repetition, using the least witness of each element.
Then one quantifier at a time, $\Sigma^0_1$ comprehension builds every arithmetical set.

## Variants

For the version of 3 with arbitrary functions, step 4 can take $f(m) = n + 1$ when $m = (n, j)$ with $\theta(n, j)$, and $f(m) = 0$ otherwise.
Then $\varphi(n)$ holds exactly when $n + 1$ is in the range, and the set $D$ is not needed.
