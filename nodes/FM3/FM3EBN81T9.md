---
tag: FM3EBN81T9
kind: example
name: The inclusion atom is not definable in dependence logic
msc: ["03B60"]
topics: [MDHDYV8QZW]
audience: research
uses: [DNAPTJ98WD]
not_instance_of:
  - target: DNAPTJ98WD
    note: the inclusion atom is not closed under subteams, while every formula of dependence logic is
sources:
  - url: https://en.wikipedia.org/wiki/Dependence_logic
    locator: Inclusion/exclusion logic
  - url: https://en.wikipedia.org/wiki/Dependence_logic
    locator: Properties
---

## Example

The inclusion atom $x \subseteq y$ holds in a team $X$ when every value of $x$ in $X$ is also a value of $y$ in $X$:

$$\mathcal{M} \models_X x \subseteq y \iff \text{for every } s \in X \text{ there is } s' \in X \text{ with } s'(y) = s(x).$$

We show that no formula of [[dependence logic|DNAPTJ98WD]] defines this atom in a structure $\mathcal{M}$ with at least two elements $0$ and $1$.
So the inclusion atom is a team property outside dependence logic.

1. Let $s_1$ be the assignment with $s_1(x) = 0$, $s_1(y) = 1$, and $s_2$ the assignment with $s_2(x) = 1$, $s_2(y) = 0$. Let $X = \{ s_1, s_2 \}$.
2. The values of $x$ in $X$ are $0$ and $1$, and the values of $y$ in $X$ are $1$ and $0$. So $\mathcal{M} \models_X x \subseteq y$.
3. Let $Y = \{ s_1 \}$, a subteam of $X$. The only value of $x$ in $Y$ is $0$, and the only value of $y$ in $Y$ is $1$. So $x \subseteq y$ fails in $Y$.
4. Every dependence logic formula $\varphi$ is downward closed: if $\mathcal{M} \models_X \varphi$ and $Y \subseteq X$, then $\mathcal{M} \models_Y \varphi$.
5. Suppose that a dependence logic formula $\varphi(x, y)$ held in exactly the teams that satisfy $x \subseteq y$. By step 2, $\varphi$ holds in $X$.
6. By step 4, $\varphi$ holds in $Y$, and by the assumption, $x \subseteq y$ holds in $Y$. This contradicts step 3.

## Remarks

The example shows the failure of the closure property that marks dependence logic.
The inclusion atom has a different closure property: if $x \subseteq y$ holds in $X$ and in $Z$, it holds in $X \cup Z$.
The reason is that each value of $x$ in $X \cup Z$ finds a matching value of $y$ in the same part.
Inclusion logic, first-order logic with inclusion atoms, has this closure under unions for all its formulas.
In a structure with one element, $x \subseteq y$ holds in every team, so the hypothesis "at least two elements" is needed.
The same argument shows that $x \subseteq y$ is not equivalent to a first-order formula.
A first-order formula holds in a team when it holds in each assignment of the team, so it would hold in $Y$.
The empty team satisfies $x \subseteq y$, because it has no value of $x$ that needs a match.

## Explanations

### L1 human

In a table with columns $x$ and $y$, the inclusion statement says: every entry of column $x$ also appears somewhere in column $y$.
The table with rows $(0, 1)$ and $(1, 0)$ passes the test.
The smaller table with only the row $(0, 1)$ fails, because $0$ is not in column $y$ any more.
Every statement of dependence logic stays true when we delete rows, so dependence logic cannot express this test.

### L2 human

We compare the inclusion atom with the dependence atom $=\!(x, y)$ on the same teams.

1. In $X = \{ s_1, s_2 \}$ the two assignments have different values of $x$, so $=\!(x, y)$ holds.
2. In $Y = \{ s_1 \}$ there is one assignment, so $=\!(x, y)$ holds again.
3. Add $s_3$ with $s_3(x) = 0$, $s_3(y) = 0$. In $X \cup \{ s_3 \}$ the atom $=\!(x, y)$ fails, because $s_1$ and $s_3$ agree on $x$ and not on $y$.
4. In $X \cup \{ s_3 \}$ the atom $x \subseteq y$ still holds, because the values of $x$ are $0, 1$ and the values of $y$ are $1, 0, 0$.

So adding rows can break a dependence atom and keep an inclusion atom.
Deleting rows can break an inclusion atom and keep a dependence atom.
A trap is to think that every team property that a database theorist uses is downward closed: inclusion dependencies, such as foreign keys, are not.
