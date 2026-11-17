---
tag: VHQXG9TYGE
kind: example
name: Unification without the occurs check gives an unsound resolution step
msc: ["03B10", "03B35"]
topics: [TTCRX3NFNY]
audience: grad
not_instance_of:
  - target: DEB3CF4Z2D
    note: the step uses a substitution that is not a unifier, because the unification of y with h(g(y)) skips the occurs check, and it derives the empty clause from a satisfiable set
uses: [DEB3CF4Z2D, RJJ9D0WF53, GCPQGMJYEV, 983GZBQYT4, QN7M1JCGT9]
sources:
  - url: https://en.wikipedia.org/wiki/Unification_(computer_science)
    locator: Occurs check
  - url: https://en.wikipedia.org/wiki/Resolution_(logic)
    locator: Resolution in first-order logic
---

## Example

Consider the invalid sentence $\forall y\,\exists x\, R(x,y) \to \exists x\,\forall y\, R(x,y)$.
Its negation is equivalent to $\forall y\,\exists x\, R(x,y) \land \forall x\,\exists y\, \neg R(x,y)$.
[[Skolem normal form|GCPQGMJYEV]] with new function symbols $g$ and $h$ gives the two clauses
$$C_1 = \{R(g(y), y)\}, \qquad C_2 = \{\neg R(x, h(x))\}.$$
A faulty prover "resolves" them to $\square$, and we show that this step is not a step of [[first-order resolution|DEB3CF4Z2D]].

1. The set $\{C_1, C_2\}$ is [[satisfiable|QN7M1JCGT9]]. Take the [[structure|983GZBQYT4]] $\mathcal{M}$ with domain $\mathbb{N}$, $R^{\mathcal{M}}(m, n)$ if and only if $m = n + 1$, $g(n) = n + 1$ and $h(n) = n$.
2. Check $C_1$. For every $n$, $R(g(n), n)$ means $n + 1 = n + 1$, which is true.
3. Check $C_2$. For every $m$, $R(m, h(m))$ means $m = m + 1$, which is false, so $\neg R(m, h(m))$ is true.
4. The faulty unification. The [[unification|RJJ9D0WF53]] of $R(g(y), y)$ and $R(x, h(x))$ starts with $g(y) = x$ and $y = h(x)$. The first equation gives $x \mapsto g(y)$, and the second becomes $y = h(g(y))$.
5. The occurs check fails here, since $y$ occurs in $h(g(y))$. The faulty prover skips the check, binds $y \mapsto h(g(y))$, and uses $\sigma = \{x \mapsto g(y), y \mapsto h(g(y))\}$.
6. $\sigma$ is not a unifier. We get $R(g(y), y)\sigma = R(g(h(g(y))), h(g(y)))$ and $R(x, h(x))\sigma = R(g(y), h(g(y)))$, and the first arguments differ.
7. No unifier exists. If $\tau$ unifies the atoms, then $x\tau = g(y\tau)$ and $y\tau = h(x\tau) = h(g(y\tau))$. The right side has two more symbols than $y\tau$, so this is impossible.
8. Conclusion. The faulty step derives $\square$ from a satisfiable set, so it is unsound. The correct calculus finds no resolvent and no factor of $C_1$ and $C_2$, so it derives nothing.

## Remarks

The example shows that the occurs check is what keeps resolution sound.
Without it, a "unifier" can stand for an infinite term such as $h(g(h(g(\cdots))))$, which is not a term of first-order logic.
The same clauses also show that the invalid formula above has no resolution proof, as soundness and completeness require.

The same error appears with a wrong Skolemization.
If $\forall x\,\exists y\, R(x,y)$ is turned into $\{R(x, c)\}$ instead of $\{R(x, f(x))\}$, the clause unifies with $R(z, z)$ through $\{x \mapsto c, z \mapsto c\}$.
The correct clause does not unify with $R(z,z)$, again by the occurs check on $z = f(z)$.

Logic programming systems often omit the occurs check for speed.
They then accept some "proofs" that are not valid in first-order logic, for the reason shown here.

## Explanations

### L1 human

"Everyone has a parent" does not imply "someone is the parent of everyone".
A careless proof machine can still "prove" this implication.
To do so, it must make $y$ equal to an expression that contains $y$ itself, which leads to an endless chain.
A correct machine checks whether a letter occurs inside the expression it is matched with, and it refuses the match.
This small check, the occurs check, separates a correct proof from a false one.

### L2 human

To test a unification step by hand, apply the proposed substitution to both atoms and compare.

1. The proposed $\sigma$ maps $x$ to $g(y)$ and $y$ to $h(g(y))$.
2. Applied to $R(g(y), y)$, it gives $R(g(h(g(y))), h(g(y)))$.
3. Applied to $R(x, h(x))$, it gives $R(g(y), h(g(y)))$.
4. The first arguments $g(h(g(y)))$ and $g(y)$ differ, so $\sigma$ is not a unifier.

The typical use of this check: every mgu in a hand-written refutation should be tested in this way.
A trap is to apply the bindings one after the other, as if $y$ were first replaced and then $x$.
A substitution acts on all variables at once.
