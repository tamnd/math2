---
tag: BAV2SAADQT
kind: example
name: In S5, □(p ∨ □q) is equivalent to □p ∨ □q
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [VC3A2VWXND]
uses: [VC3A2VWXND, FXTCKYR3AQ, E87G6ZTMTN, 0G8VEZ3WTK, 0VABYWJWH9, N60RVXSA5W]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Example

In general a box does not pass through a disjunction, but in $\mathsf{S5}$ it does when one side is itself boxed.
We prove the following law of the [[modal logic S5|VC3A2VWXND]] by a semantic argument, and then show that $\mathsf{S4}$ does not prove it:
$$\mathsf{S5} \vdash \square(p \vee \square q) \leftrightarrow (\square p \vee \square q).$$
By [[completeness of K, T, D, K4, S4, B and S5|FXTCKYR3AQ]], it is enough to check the formula at every world of every model whose relation is an [[equivalence relation|0G8VEZ3WTK]].

1. Truth at $w$ depends only on the worlds that $w$ can reach.
   In an equivalence relation these form the class of $w$, and on that class $R$ is universal.
2. So it is enough to check models with $R = W \times W$.
   There $\square\varphi$ is true at one world exactly when $\varphi$ is true at all worlds, so $\square q$ is true at all worlds or at none.
3. Case 1: $\square q$ is true at all worlds.
   Then $p \vee \square q$ is true everywhere, so $\square(p \vee \square q)$ is true everywhere, and $\square p \vee \square q$ is true everywhere too.
4. Case 2: $\square q$ is false at all worlds.
   Then $p \vee \square q$ has the same truth set as $p$, so $\square(p \vee \square q)$ agrees with $\square p$, and so does $\square p \vee \square q$.
5. In both cases the two sides agree at every world, so the equivalence is valid on universal frames and is a theorem of $\mathsf{S5}$.

Now we refute one direction on a [[preorder|0VABYWJWH9]]: take $W = \{ r, a \}$ and $R = \{ (r, r), (a, a), (r, a) \}$, with $V(p) = \{ r \}$ and $V(q) = \{ a \}$.

6. $\square q$ is true at $a$, because $a$ sees only $a$, and false at $r$, because $r$ sees itself and $q$ is false at $r$.
7. $p \vee \square q$ is true at $r$ by $p$ and at $a$ by $\square q$, so $\square(p \vee \square q)$ is true at $r$.
8. $\square p$ is false at $r$, because $a$ lacks $p$, and with step 6, $\square p \vee \square q$ is false at $r$.
9. So $\square(p \vee \square q) \to (\square p \vee \square q)$ fails at $r$, and by [[soundness|E87G6ZTMTN]] it is not a theorem of the [[modal logic S4|N60RVXSA5W]].

## Remarks

The other direction, $(\square p \vee \square q) \to \square(p \vee \square q)$, already holds in $\mathsf{K4}$.
RM gives $\square p \to \square(p \vee \square q)$, and $\mathrm{4}$ with RM gives $\square q \to \square\square q \to \square(p \vee \square q)$.

The failing direction needs symmetry.
In the preorder above, $a$ does not see back to $r$, so $\square q$ is not constant, and the case split of step 2 breaks.
Together with the [[reduction of iterated modalities|GHPPQ19J6B]], this law is what lets you rewrite every formula of $\mathsf{S5}$ to modal depth at most $1$.

What if you replace $\square q$ by $q$?
Then the law fails even in $\mathsf{S5}$.
On a universal frame with two worlds, $p$ at one and $q$ at the other, $\square(p \vee q)$ is true and $\square p \vee \square q$ is false.

## Explanations

### L1 human

In $\mathsf{S5}$, "box" means "in every world", and all worlds see all worlds.
So "box $q$" is a fixed fact: it is true in every world or in none.
If it is true, both sides of the law are true.
If it is false, both sides say "$p$ in every world".
In a picture where one world cannot look back, this case split breaks.

### L2 human

We check case 2 on a small universal model, with $W = \{ 1, 2 \}$, $V(p) = \{ 1 \}$ and $V(q) = \{ 2 \}$.
$\square q$ is false at both worlds, because world $1$ lacks $q$.
So $p \vee \square q$ has the truth set $\{ 1 \}$, the same as $p$, and $\square(p \vee \square q)$ is false at both worlds because world $2$ lacks it.
$\square p$ is false too, so $\square p \vee \square q$ is false at both worlds.
Both sides are false at both worlds, as the case analysis predicts.
The idea "a boxed formula has a constant value" is the standard way to prove $\mathsf{S5}$ laws on universal frames.
Watch out: the method needs completeness for universal frames, and in weaker logics a boxed formula need not have a constant value.
