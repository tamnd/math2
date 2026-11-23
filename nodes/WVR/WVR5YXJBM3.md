---
tag: WVR5YXJBM3
kind: example
name: A formula with a free variable is neither true nor false
msc: ["03B10"]
topics: [NJDME6F845]
audience: ug2
not_instance_of:
  - target: K7XDVK5854
    note: the formula x < 1 has a free variable, and some assignments satisfy it while others do not
uses: [71X7TB3F98, 1WTCZB4DVB, 983GZBQYT4, DKFGQTRYZE]
sources:
  - book: isbn:9780122384523
    locator: Section 2.2
  - url: https://builds.openlogicproject.org/
    locator: Syntax and Semantics
---

## Example

Let $\mathcal{N} = (\mathbb{N}, <, 1)$ be the natural numbers with the usual order and a constant symbol $1$ interpreted as the number $1$.
Let $\varphi$ be the formula $x < 1$.
We show that neither $\varphi$ nor $\neg \varphi$ is [[true|71X7TB3F98]] in $\mathcal{N}$.

1. A formula is true in $\mathcal{N}$ when every assignment satisfies it.
2. Let $s_0$ be an assignment with $s_0(x) = 0$.
   Then $0 < 1$, so $\mathcal{N} \models \varphi[s_0]$, by the atomic clause of [[satisfaction|1WTCZB4DVB]].
3. Let $s_5$ be an assignment with $s_5(x) = 5$.
   Then $5 < 1$ is false, so $\mathcal{N} \not\models \varphi[s_5]$.
4. By step 3, not every assignment satisfies $\varphi$, so $\varphi$ is not true in $\mathcal{N}$.
5. By step 2 and the clause for $\neg$, $\mathcal{N} \not\models \neg \varphi[s_0]$, so $\neg \varphi$ is not true in $\mathcal{N}$ either.

The condition that fails is that $\varphi$ is not a [[sentence|DKFGQTRYZE]], so its satisfaction depends on the assignment.

## Remarks

Bivalence, "exactly one of $\psi$ and $\neg \psi$ is true", holds for sentences but not for formulas.
That is also why "$\mathcal{M} \not\models \varphi$" and "$\mathcal{M} \models \neg \varphi$" mean different things when $\varphi$ has a free variable.

The two sentences built from $\varphi$ behave as expected.
The universal closure $\forall x \, (x < 1)$ is false in $\mathcal{N}$, by step 3.
The existential closure $\exists x \, (x < 1)$ is true in $\mathcal{N}$, by step 2.

A formula with a free variable can still be true, when every assignment satisfies it.
The formula $x < 1 \vee \neg (x < 1)$ is true in $\mathcal{N}$, because each assignment satisfies one of the two disjuncts.

## Explanations

### L1 human

"$x$ is less than $1$" is not a full statement, because we do not know $x$.
If $x$ is $0$ it is true, and if $x$ is $5$ it is false.
So we cannot call it true, and we cannot call it false.
The statement "every $x$ is less than $1$" is false, and "some $x$ is less than $1$" is true, because they have no unknown left.

### L2 human

We compare three readings of $x < 1$ in $\mathcal{N}$.
Under one assignment, it holds when $s(x) = 0$ and fails otherwise.
As a formula that is true in $\mathcal{N}$, it would need all assignments, and $s(x) = 5$ fails, so it is not true.
As a formula that defines a set, it defines
$$\{ a \in \mathbb{N} : a < 1 \} = \{0\}.$$
The third reading is the typical use: formulas with free variables define sets and relations.
Watch out: from "$x < 1$ is not true in $\mathbb{N}$" you may not conclude that $\neg (x < 1)$ is true, and the assignment $x \mapsto 0$ shows why.
