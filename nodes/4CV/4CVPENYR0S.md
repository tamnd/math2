---
tag: 4CVPENYR0S
kind: proof
name: Proof of Russell's paradox
msc: ["03E30"]
proves: 0HESMMSYEG
uses: [0SJ3RX9TXA, 0EZ758XE73]
methods: [0J0XBKG64S]
sources:
  - url: https://proofwiki.org/wiki/Russell%27s_Paradox
---

## Proof

We argue by contradiction.

1. Suppose that there is a [[set|0SJ3RX9TXA]] $R$ such that, for each set $x$, $x \in R$ if and only if $x \notin x$.
2. The object $R$ is itself a set. So we may take $x = R$ in step 1. This gives: $R \in R$ if and only if $R \notin R$.
3. Suppose $R \in R$. By step 2, $R \notin R$. This contradicts the assumption $R \in R$.
4. So $R \in R$ is false, that is, $R$ is not an [[element|0EZ758XE73]] of $R$. In symbols, $R \notin R$.
5. By step 2 and step 4, $R \in R$.
6. Steps 4 and 5 give both $R \notin R$ and $R \in R$, a contradiction.
7. So the assumption of step 1 is false. There is no set $R$ such that, for each set $x$, $x \in R$ if and only if $x \notin x$.

## Idea

Ask whether $R$ contains itself. The defining property of $R$ says that $R \in R$ exactly when $R \notin R$. No statement can be equivalent to its own negation, so no such $R$ exists.
