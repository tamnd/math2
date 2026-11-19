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

Take three worlds $w, u, v$ and the centered system of spheres around $w$:
$$\$_w = \set{\set{w}, \set{w, u}, \set{w, u, v}}.$$
The atoms $p, q, r, s$ have these truth values:

| world | $p$ | $q$ | $r$ | $s$ |
|---|---|---|---|---|
| $w$ | false | true | false | true |
| $u$ | true | true | false | false |
| $v$ | true | false | true | false |

We use the sphere clause of [[conditional logic|ZGYG7WN7EC]]: $\varphi > \psi$ is true at $w$ when the smallest sphere with a $\varphi$-world satisfies $\varphi \to \psi$ everywhere, or when no sphere has a $\varphi$-world.
Since the spheres are nested and finite, the smallest sphere with a $\varphi$-world exists whenever some sphere has one.

1. The $p$-worlds are $u$ and $v$, so the smallest sphere with a $p$-world is $\set{w, u}$.
2. In $\set{w, u}$, $p \to q$ holds at $w$, since $p$ is false there, and at $u$, since $q$ is true there. So $p > q$ is true at $w$.
3. Strengthening fails. The only $(p \wedge r)$-world is $v$, so the smallest sphere with one is $\set{w, u, v}$.
4. At $v$, $p \wedge r$ is true and $q$ is false. So $(p \wedge r) > q$ is false at $w$, although $p > q$ is true.
5. Contraposition fails. The only $\neg q$-world is $v$, so the smallest sphere with one is $\set{w, u, v}$.
6. At $v$, $\neg q$ is true and $\neg p$ is false. So $\neg q > \neg p$ is false at $w$, although $p > q$ is true.
7. Transitivity fails. The world $w$ is a $q$-world, so the smallest sphere with a $q$-world is $\set{w}$.
8. At $w$, $s$ is true, so $q > s$ is true at $w$.
9. In $\set{w, u}$, $p \to s$ fails at $u$, where $p$ is true and $s$ is false. So $p > s$ is false at $w$.
10. So $p > q$ and $q > s$ are true at $w$, and $p > s$ is false.

## Remarks

All three inferences are valid for the material conditional and for the strict conditional, see [[the strict conditional|5F6H9XXMVN]].
They fail here because different antecedents select different spheres.
In step 4, the extra conjunct $r$ forces us out to the far world $v$.
If we delete $v$, every conditional with a satisfiable antecedent is decided inside $\set{w, u}$, and strengthening holds for $p$ and $r$ in the vacuous way: no sphere has a $(p \wedge r)$-world, so $(p \wedge r) > q$ is true.
The weak forms that survive in $\mathsf{VC}$ are rational monotonicity and the rule "from $\varphi > \psi$ and $(\varphi \wedge \psi) > \chi$ infer $\varphi > \chi$".

## Explanations

### L1 human

Read $p$ as "the match is struck", $q$ as "it lights" and $r$ as "it is wet".
In the nearest situations where the match is struck, it is dry and lights.
So "if it had been struck, it would have lit" is true.
But the nearest situation where it is struck and wet is a farther one, and there it does not light.
So adding "and it is wet" changes the answer.

### L2 human

1. List the spheres from small to large: $\set{w}$, $\set{w, u}$, $\set{w, u, v}$.
2. For each antecedent, find the first sphere that meets it: $p$ meets $\set{w, u}$; $p \wedge r$ and $\neg q$ meet only the last sphere; $q$ meets $\set{w}$.
3. Check the material conditional on that sphere only.

The typical use of such a model is to show that a proposed rule for counterfactuals is invalid.
A trap: checking $\varphi \to \psi$ on the whole set of worlds gives the strict conditional, not the counterfactual.
