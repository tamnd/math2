---
tag: SX43GZ9RD1
kind: proof
name: Proof of the number of permutations by counting injections
msc: [05A05]
proves: 0CEBCS0E0E
uses: [0BQMWCNS8S, 0SNQEF7Z53, 0PVG1CRAJN, 0X0N833FF8, 0GV2573FP4, 03QC59M99B, 0N5M924N3P, 0WFCGVMRRC]
sources:
  - url: https://proofwiki.org/wiki/Number_of_Permutations
    locator: Proof 2
---

## Proof

We show that the permutations of $X$ are exactly the injections from $X$ to $X$, and then count injections.

1. A [[permutation|0BQMWCNS8S]] of $X$ is a [[bijection|0SNQEF7Z53]] $\sigma : X \to X$. In particular it is [[injective|0PVG1CRAJN]].
2. Conversely, let $\sigma : X \to X$ be injective, and put $C = \sigma(X)$. Then $\sigma$ is a bijection from $X$ onto $C$.
3. Composing a numbering of $X$ with $\sigma$ numbers $C$. So $|C| = |X| = n$, as in the [[bijection principle|0GV2573FP4]].
4. By the [[complement principle|03QC59M99B]], $|X \setminus C| = n - n = 0$. So $X \setminus C$ is empty and $C = X$.
5. So $\sigma$ is surjective, hence a bijection of $X$, that is, a permutation.
6. By steps 1 to 5, the permutations of $X$ are exactly the injections from $X$ to $X$.
7. By the [[number of injections|0X0N833FF8]], there are $(n)_n$ of them, where $(n)_n$ is the [[falling factorial|0N5M924N3P]].
8. For $n = 0$, $(0)_0 = 1 = 0!$. For $n \ge 1$, $(n)_n = n (n-1) \cdots 1$, which is $n!$ by the definition of the [[factorial|0WFCGVMRRC]].
9. Hence $X$ has exactly $n!$ permutations.

## Idea

On a finite set, a map from the set to itself that never repeats a value must hit every element.
So permutations are just injections from $X$ to itself, and the injection count $n (n-1) \cdots 1$ is $n!$.
