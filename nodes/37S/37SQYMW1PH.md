---
tag: 37SQYMW1PH
kind: statement
role: lemma
name: Zorn's lemma implies the axiom of choice
msc: ["03E25"]
sources:
  - wikipedia: en:51442@r1364256157
    locator: Zorn's lemma, section Zorn's lemma implies the axiom of choice
    note: adopted
    mention: wikipedia://en/51442#2CLB
    sections: [Statement]
inventory: [MGRA4BD4T6]
---

## Statement

A proof that Zorn's lemma implies the axiom of choice illustrates a typical application of Zorn's lemma. (The structure of the proof is exactly the same as the one for the Hahn–Banach theorem.)

Given a set $X$ of nonempty sets and its union $U := \bigcup X$ (which exists by the axiom of union), we want to show there is a function

$$f : X \to U$$

such that $f(S) \in S$ for each $S \in X$. For that end, consider the set

$$P = \{ f : Y \to U \mid Y \subset X, f(S) \in S\text{ for each }S \in Y \}.$$

It is partially ordered by extension; i.e., $f \le g$ if and only if $f$ is the restriction of $g$. If $f_i : Y_i \to U$ is a chain in $P$, then we can define the function $f$ on the union $Y = \cup_i Y_i$ by setting $f(x) = f_i(x)$ when $x \in Y_i$. This is well-defined since if $i < j$, then $f_i$ is the restriction of $f_j$. The function $f$ is also an element of $P$ and is a common extension of all $f_i$'s. Thus, we have shown that each chain in $P$ has an upper bound in $P$. Hence, by Zorn's lemma, there is a maximal element $f$ in $P$ that is defined on some $Y \subset X$. We want to show $Y = X$. Suppose otherwise; then there is a set $S \in X - Y$. As $S$ is nonempty, it contains an element $s$. We can then extend $f$ to a function $g$ on $Y \cup \{ S \}$ by setting $g|_{Y} = f$ and $g(S) = s$. (Note this step does not need the axiom of choice.) The function $g$ is in $P$ and $f < g$, a contradiction to the maximality of $f$. $\square$

Essentially the same proof also shows that Zorn's lemma implies the [[well-ordering theorem|0N109NG5ZX]]: take $P$ to be the set of all well-ordered subsets of a given set $X$, ordered by initial segments, and then shows a maximal element of $P$ is $X$. For a proof of the converse (in the form of the maximal principle), see Hausdorff maximal principle#Proof from the well-ordering theorem.
