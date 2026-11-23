---
tag: PTQNQF2K3T
kind: example
name: Failure of strengthening, transitivity and contraposition for counterfactuals
msc: ["03B45"]
topics: [CQM9SRN8PM]
audience: research
instance_of: [ZGYG7WN7EC]
uses: [ZGYG7WN7EC]
sources:
  - url: https://en.wikipedia.org/wiki/Counterfactual_conditional
    locator: Non-monotonicity
  - url: https://en.wikipedia.org/wiki/Conditional_logic
    locator: Logical principles and their failure
---

## Example

Take three worlds $w, u, v$ and the following centered system of spheres around $w$.
$$\$_w = \{\{w\}, \{w, u\}, \{w, u, v\}\}$$
The atoms $p, q, r, s$ have these truth values.

| world | $p$ | $q$ | $r$ | $s$ |
|---|---|---|---|---|
| $w$ | false | true | false | true |
| $u$ | true | true | false | false |
| $v$ | true | false | true | false |

We use the sphere clause of [[conditional logic|ZGYG7WN7EC]].
The conditional $\varphi > \psi$ is true at $w$ when no sphere has a $\varphi$-world, or when the smallest sphere with a $\varphi$-world satisfies $\varphi \to \psi$ everywhere.
The spheres are nested and finite, so the smallest sphere with a $\varphi$-world exists whenever some sphere has one.

1. The $p$-worlds are $u$ and $v$, so the smallest sphere with a $p$-world is $\{w, u\}$.
2. In $\{w, u\}$, $p \to q$ holds at $w$, where $p$ is false, and at $u$, where $q$ is true.
   So $p > q$ is true at $w$.
3. Strengthening fails.
   The only $(p \wedge r)$-world is $v$, so the smallest sphere with one is $\{w, u, v\}$.
4. At $v$, $p \wedge r$ is true and $q$ is false.
   So $(p \wedge r) > q$ is false at $w$, although $p > q$ is true.
5. Contraposition fails.
   The only $\neg q$-world is $v$, so the smallest sphere with one is $\{w, u, v\}$.
6. At $v$, $\neg q$ is true and $\neg p$ is false.
   So $\neg q > \neg p$ is false at $w$, although $p > q$ is true.
7. Transitivity fails.
   The world $w$ is a $q$-world, so the smallest sphere with a $q$-world is $\{w\}$.
8. At $w$, $s$ is true, so $q > s$ is true at $w$.
9. In $\{w, u\}$, $p \to s$ fails at $u$, where $p$ is true and $s$ is false.
   So $p > s$ is false at $w$.
10. So $p > q$ and $q > s$ are true at $w$, and $p > s$ is false.

## Remarks

All three inferences are valid for the material conditional and for the strict conditional, as [[the strict conditional|5F6H9XXMVN]] shows.
They fail here because different antecedents select different spheres.
In step 4 the extra conjunct $r$ forces us out to the far world $v$.
If we delete $v$, no world satisfies $p \wedge r$, and $(p \wedge r) > q$ becomes true in the vacuous way.

Weak forms of the three rules survive in $\mathsf{VC}$.
Rational monotonicity infers $(\varphi \wedge \chi) > \psi$ from $\varphi > \psi$ and $\neg(\varphi > \neg\chi)$.
In our model $p > \neg r$ is true, because $r$ fails at $w$ and $u$, so rational monotonicity does not apply to $r$, as it should not.
Cumulative transitivity infers $\varphi > \chi$ from $\varphi > \psi$ and $(\varphi \wedge \psi) > \chi$.

## Explanations

### L1 human

Read $p$ as "the match is struck", $q$ as "it lights" and $r$ as "it is wet".
In the nearest situations where the match is struck, it is dry and lights.
So "if it had been struck, it would have lit" is true.
But the nearest situation where it is struck and wet is farther away, and there it does not light.
So adding "and it is wet" changes the answer.

### L2 human

List the spheres from small to large: $\{w\}$, $\{w, u\}$, $\{w, u, v\}$.
For each antecedent, find the first sphere that meets it.
Here $p$ meets $\{w, u\}$, both $p \wedge r$ and $\neg q$ meet only the last sphere, and $q$ meets $\{w\}$.
Then check the material conditional on that sphere only.
This is the typical use of such a model: it shows that a proposed rule for counterfactuals is invalid.
Watch out: if you check $\varphi \to \psi$ on the whole set of worlds, you compute the strict conditional, not the counterfactual.
