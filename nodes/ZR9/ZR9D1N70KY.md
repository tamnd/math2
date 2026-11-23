---
tag: ZR9D1N70KY
kind: proof
name: Proof of the first incompleteness theorem by the halting problem
msc: ["03F40", "03D35"]
topics: [HXHHWY3328]
audience: grad
proves: X9WYNYE29C
uses: [Z7TN2B35B0, EZ6Z9V91C2, TN9G24VABN, 6M12VR1GT6, 4S29X1GTV4]
methods: [0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Halting_problem
    locator: Gödel's incompleteness theorems
  - book: isbn:9780521857840
---

## Proof

Suppose a theory $T$ proved every true sentence "program $e$ does not halt on input $e$".
Then we could decide halting: run $e$ on $e$ and search the theorems of $T$ for a non-halting proof, side by side, and one search ends.
The halting problem is undecidable, so $T$ misses some true non-halting sentence.
The steps below make this exact, and they give parts 1 and 2 of the theorem with a different undecided sentence.

1. Let $K := \{e \in \mathbb{N} : \text{the program with code } e \text{ halts on input } e\}$.
   The set $K$ is [[computably enumerable|TN9G24VABN]] and, by the [[undecidability of the halting problem|Z7TN2B35B0]], not decidable.
2. A set is decidable exactly when it and its complement are computably enumerable, by [[Post's complement theorem|EZ6Z9V91C2]].
   So the complement $\overline{K}$ is not computably enumerable.
3. The relation "program $e$ on input $e$ halts within $s$ steps" is decidable.
   Let $C(x, z)$ be a $\Sigma_1$ formula that represents it in $\mathsf{Q}$, and let $H(x) := \exists z \, C(x, z)$.
4. In $\mathbb{N}$, $H$ defines $K$, since $C$ defines its relation in the model $\mathbb{N}$ of $\mathsf{Q}$.
   So $\mathbb{N} \models H(\underline{e})$ exactly when $e \in K$.
5. If $e \in K$, choose $s$ such that $e$ halts within $s$ steps.
   By representability, $\mathsf{Q} \vdash C(\underline{e}, \underline{s})$, so $T \vdash H(\underline{e})$.
6. Let $S := \{e : T \vdash \neg H(\underline{e})\}$.
   A program can list the theorems of $T$ and keep those of the form $\neg H(\underline{e})$, so $S$ is computably enumerable.
7. Assume $T$ is consistent.
   If $e \in S \cap K$, then $T$ proves $\neg H(\underline{e})$ and, by step 5, $H(\underline{e})$.
   So $S \cap K$ is empty, and $S \subseteq \overline{K}$.
8. By steps 2 and 6, $S \ne \overline{K}$, so we can choose $e_0 \in \overline{K}$ with $e_0 \notin S$.
9. By step 4, the $\Pi_1$ sentence $\neg H(\underline{e_0})$ is true in $\mathbb{N}$, and by the choice of $e_0$, $T \nvdash \neg H(\underline{e_0})$.
10. Now assume that $T$ is $1$-consistent, so every $\Sigma_1$ sentence provable in $T$ is true.
    If $T \vdash H(\underline{e_0})$, then $H(\underline{e_0})$ is true, and $e_0 \in K$ by step 4, which contradicts step 8.
11. So $T$ proves neither $H(\underline{e_0})$ nor $\neg H(\underline{e_0})$, and $T$ is not negation complete.

## Idea

Provability in $T$ is computably enumerable, so a consistent $T$ can prove non-halting only for a computably enumerable set of programs.
The programs that do not halt do not form such a set, so some program that never halts has no proof that it never halts.
The undecided sentence is "program $e_0$ does not halt on input $e_0$".
No self-reference appears in the argument, and all of it is hidden inside the undecidability of the halting problem.

Watch out: step 9 needs only consistency, but step 10 needs $1$-consistency.
A consistent but false theory can prove $H(\underline{e_0})$, a false claim that $e_0$ halts.

## Variants

An explicit $e_0$ can be read off.
Let $s$ be a program that halts on exactly the inputs in $S$.
If $s \in S$, then $s$ halts on $s$, so $s \in K$, against step 7.
So $s \notin S$, and then $s$ does not halt on $s$, so $s \in \overline{K} \setminus S$.

A refinement uses two disjoint computably enumerable sets that no decidable set separates, and it needs only consistency, as in [[Rosser's theorem|DH9RQ61GVD]].
The [[diagonal proof|XYHTQH2TGB]] also gives an explicit sentence.
Replace $K$ by any computably enumerable set whose complement is not computably enumerable, such as the set of solvable Diophantine equations.
The undecided sentence then reads "this equation has no solution".
