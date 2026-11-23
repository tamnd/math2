---
tag: KFWXHKBHYT
kind: example
name: The theory of infinite sets
msc: ["03C07", "03B10"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [92SWXST1ZM]
uses: [92SWXST1ZM, FZRMYTQFRR, DKFGQTRYZE, 1NR3HAWG9D]
sources:
  - url: https://en.wikipedia.org/wiki/Theory_(mathematical_logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Compactness_theorem
    locator: lead section
---

## Example

Let $\sigma$ be the empty signature, so the only atomic formulas are equations $x = y$ between variables.
For $n \ge 2$ let
$$\lambda_n = \exists x_1 \cdots \exists x_n \bigwedge_{1 \le i < j \le n} \neg (x_i = x_j),$$
where the big conjunction is a finite conjunction of $\binom{n}{2}$ formulas.
Let $T_\infty = \{ \lambda_n : n \ge 2 \}$.
We check that $T_\infty$ is a [[first-order theory|92SWXST1ZM]] whose models are exactly the infinite sets.

1. Each variable $x_i$ in $\lambda_n$ is bound by $\exists x_i$, so $\lambda_n$ is a [[sentence|DKFGQTRYZE]].
   So $T_\infty$ is a theory, by the [[definition|FZRMYTQFRR]].
2. A structure for $\sigma$ is a nonempty set $M$.
   It satisfies $\lambda_n$ exactly when it has $n$ pairwise distinct elements, that is, when $|M| \ge n$.
3. If $M$ is infinite, then $|M| \ge n$ for every $n$, so $M$ is a model of $T_\infty$.
4. If $M$ is finite with $k$ elements, then $M$ does not satisfy $\lambda_{k+1}$, so $M$ is not a model.

So $\mathrm{Mod}(T_\infty)$ is the class of infinite sets.

## Remarks

No finite theory has exactly the infinite sets as models.
Suppose a finite theory did, and let $\tau$ be the conjunction of its sentences.
Then $T_\infty \cup \{ \neg \tau \}$ has no model, since a model would be infinite and so satisfy $\tau$.
But each finite subset of it holds in a finite set with enough elements, because finite sets satisfy $\neg \tau$.
By the [[compactness theorem|1NR3HAWG9D]], $T_\infty \cup \{ \neg \tau \}$ has a model, which is a contradiction.
So $T_\infty$ is not finitely axiomatizable.

The finite sets are not the models of any theory $T$.
If they were, every finite subset of $T \cup T_\infty$ would hold in a large finite set.
Compactness would then give a model of $T \cup T_\infty$, which is an infinite model of $T$.

## Explanations

### L1 human

The sentence $\lambda_3$ says "there are at least three different things".
A set satisfies all the sentences $\lambda_2, \lambda_3, \lambda_4, \dots$ exactly when it has no finite size.
So this list of sentences describes the infinite sets.
For example, $\mathbb{N}$ satisfies all of them, and $\{ 1, 2, 3 \}$ fails $\lambda_4$.

### L2 human

We write $\lambda_3$ in full.

1. The pairs $i < j$ with $i, j \le 3$ are $(1, 2)$, $(1, 3)$ and $(2, 3)$.
2. So $\lambda_3 = \exists x_1 \, \exists x_2 \, \exists x_3 \, (\neg (x_1 = x_2) \land \neg (x_1 = x_3) \land \neg (x_2 = x_3))$, with the brackets of the conjunction grouped to the left.
3. In $\{ a, b \}$, any three values repeat one element, so one of the inequations fails, and $\lambda_3$ is false.
4. In $\{ a, b, c \}$, the values $a, b, c$ make all three inequations true, so $\lambda_3$ is true.

The typical use of the sentences $\lambda_n$ is to control the size of models in compactness arguments.
Watch out: "there are exactly $n$ elements" needs $\lambda_n \land \neg \lambda_{n+1}$, not $\lambda_n$ alone.
