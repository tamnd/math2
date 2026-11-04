---
tag: 65R6J4MXZA
kind: proof
name: Proof that every infinite set has a countably infinite subset
msc: ["03E10"]
proves: 0RWQ5VZ6VQ
uses: [0HTGB13FE2, 0YXEQWRGP0, 01MKW4R283, 0BBTH3YSZA, 0DSHAVH45F, 0PVG1CRAJN, 0SEZ3JGZP7, 0SNQEF7Z53]
sources:
  - url: https://proofwiki.org/wiki/Infinite_Set_has_Countably_Infinite_Subset
    locator: Proof 3
---

## Proof

We define the subset by recursion, with a choice function.

1. Let $A$ be an [[infinite set|01MKW4R283]]. Let $X$ be the set of nonempty subsets of $A$.
2. By the [[axiom of choice|0HTGB13FE2]], there is a [[choice function|0YXEQWRGP0]] $c$ on $X$. So $c(S) \in S$ for each nonempty $S \subseteq A$.
3. Let $F \subseteq A$ be a [[finite set|0BBTH3YSZA]]. Then $A \setminus F$ is nonempty. Otherwise $A = F$, and $A$ would be finite.
4. Let $\Phi$ be the set of finite subsets of $A$. Define $g \colon \N \times \Phi \to \Phi$ by $g(n, F) = F \cup \{c(A \setminus F)\}$. This set is finite, since it adds one element to $F$. So $g$ is well defined.
5. By [[definition by recursion|0DSHAVH45F]], there is a function $n \mapsto F_n$ from $\N$ to $\Phi$ with $F_0 = \emptyset$ and $F_{n+1} = g(n, F_n)$.
6. Define $f \colon \N \to A$ by $f(n) = c(A \setminus F_n)$. Then $f(n) \in A \setminus F_n$ and $F_{n+1} = F_n \cup \{f(n)\}$.
7. By induction on $n$, $F_n = \{f(0), \dots, f(n-1)\}$. This holds for $n = 0$, and step 6 gives the inductive step.
8. Let $m < n$ be natural numbers. Then $f(m) \in F_n$ by step 7. But $f(n) \notin F_n$ by step 6. So $f(m) \neq f(n)$.
9. Hence $f$ is [[injective|0PVG1CRAJN]].
10. As a function onto its image, $f \colon \N \to f(\N)$ is injective and surjective, so it is a [[bijection|0SNQEF7Z53]].
11. Thus $f(\N) \subseteq A$ is [[countably infinite|0SEZ3JGZP7]], which proves the statement.

## Idea

Pick elements of $A$ one at a time, each different from the ones already picked. The supply never runs out, because only finitely many elements are used at each stage and $A$ is infinite. A single choice function makes all the picks at once, and recursion strings them into a sequence.
