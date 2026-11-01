---
tag: RH2EZGYGAW
kind: statement
role: theorem
name: Whitney extension theorem
msc: [26B05, "26E10", 54C20]
uses: [0ZCK8DQYN1, 0PJXBR6QA3, 0TCBZMEYGN, 0J8T4K4YTE]
about: [0TCBZMEYGN]
sources:
  - url: https://en.wikipedia.org/wiki/Whitney_extension_theorem
same_as:
  wikidata: Q7996766
  wikipedia: Whitney extension theorem
---

## Statement

Let $n \ge 1$ and $m \ge 0$ be integers and let $A \subseteq \R^n$ be a [[closed set|0ZCK8DQYN1]].
For each [[multi-index|0PJXBR6QA3]] $\alpha$ with $\abs{\alpha} \le m$, let $f_\alpha \colon A \to \R$ be continuous.
For $x, y \in A$ and $\abs{\alpha} \le m$, set
$$R_\alpha(x, y) = f_\alpha(x) - \sum_{\abs{\beta} \le m - \abs{\alpha}} \frac{f_{\alpha + \beta}(y)}{\beta!} (x - y)^\beta.$$
Assume that for every compact set $K \subseteq A$ and every $\abs{\alpha} \le m$,
$$\frac{\abs{R_\alpha(x, y)}}{\norm{x - y}^{m - \abs{\alpha}}} \to 0 \quad \text{as } \norm{x - y} \to 0,$$
uniformly for $x, y \in K$ with $x \ne y$.
Then there is a function $F \colon \R^n \to \R$ of [[class $C^m$|0TCBZMEYGN]] such that $D^\alpha F = f_\alpha$ on $A$ for every $\abs{\alpha} \le m$.
Moreover, $F$ can be chosen of class $C^\infty$ on $\R^n \setminus A$.

## Remarks

The family $(f_\alpha)$ is a list of candidate derivatives of $F$ on $A$, called a jet.
The condition says that the candidate values obey [[Taylor's theorem|0J8T4K4YTE]] uniformly on compact parts of $A$.
It is necessary: if $F$ is of class $C^m$ on $\R^n$, then the restrictions of $D^\alpha F$ to $A$ satisfy it, by Taylor's theorem.
For $m = 0$ the condition holds automatically, because a continuous function is uniformly continuous on compact sets, and the theorem gives a continuous extension, as the Tietze extension theorem does.
The proof covers $\R^n \setminus A$ by cubes whose size is comparable to their distance to $A$.
It then glues Taylor polynomials taken at nearby points of $A$ with a partition of unity subordinate to these cubes.

## Explanations

### L1 human

Suppose the values of a function and of its derivatives are prescribed only on a closed set.
The question is whether a smooth function on all of space has exactly these values and derivatives there.
Whitney's theorem says yes, as soon as the prescribed values fit together the way Taylor expansions of a smooth function would.

### L2 human

The theorem turns questions about functions on arbitrary closed sets into questions about jets, which are easier to handle.
It is used to define smooth functions on closed subsets, and in the study of ideals of smooth functions.
For $n = 1$ and $m = 1$ the condition says that $f_0$ is differentiable along $A$ with derivative $f_1$, uniformly on compact sets.
The related [[Borel's lemma|KZHNA19FSS]] extends a jet given at a single point.
