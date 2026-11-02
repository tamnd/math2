---
tag: WK7MKDWRFF
kind: statement
role: theorem
name: Envelope theorem
msc: [90C31, 49K40, 91B02]
uses: [0135XZZQ8M, 0ABK9V9Y64, 09WRNGPTMV]
sources:
  - url: https://en.wikipedia.org/wiki/Envelope_theorem
    locator: For arbitrary choice sets
same_as:
  wikidata: Q2478371
  wikipedia: Envelope theorem
---

## Statement

Let $X$ be a set, let $T \subseteq \R^k$ be open, and let $f \colon X \times T \to \R$ be a function.
Let $V(t) = \sup_{x \in X} f(x, t)$ be the value function, and assume that $V$ is finite on $T$.
Let $t_0 \in T$ and let $x_0 \in X$ be a maximizer at $t_0$, that is, $f(x_0, t_0) = V(t_0)$.
If $V$ and $t \mapsto f(x_0, t)$ are both [[differentiable|0135XZZQ8M]] at $t_0$, then
$$\nabla V(t_0) = \nabla_t f(x_0, t_0).$$

## Remarks

For every $t$ one has $V(t) \ge f(x_0, t)$, with equality at $t = t_0$.
So $t \mapsto V(t) - f(x_0, t)$ has a [[local minimum|09WRNGPTMV]] at the interior point $t_0$, and its [[gradient|0ABK9V9Y64]] vanishes there.
In words: to first order, the change of the optimal value equals the direct effect of the parameter, with the maximizer held fixed.

Example: $f(x, t) = tx - x^2$ on $\R \times \R$.
The maximizer is $x = t/2$ and $V(t) = t^2/4$, so $V'(t) = t/2$.
The theorem predicts $V'(t) = \partial_t f(x, t) = x = t/2$, which agrees.

The classical version assumes that $X$ is an open subset of $\R^n$, that $f$ is continuously differentiable, and that a maximizer $x^*(t)$ depends differentiably on $t$.
Then the chain rule gives $\nabla V = \nabla_t f + (\nabla_x f) \, Dx^*$, and the second term vanishes because $\nabla_x f(x^*(t), t) = 0$.
For a constrained problem, the same idea shows that the derivative of the optimal value with respect to a constraint level is the corresponding Lagrange multiplier.
Differentiability of $V$ is a real hypothesis: for $X = \set{-1, 1}$ and $f(x, t) = xt$, the value $V(t) = \abs{t}$ is not differentiable at $0$.

## Explanations

### L1 human

Suppose you choose the best option for every value of a parameter, and you watch how the best value changes when the parameter moves.
The envelope theorem says that for a small change you may ignore that the best option also changes.
Only the direct effect of the parameter on the payoff counts.
The name comes from a picture.
The value function is the upper envelope of the graphs of $t \mapsto f(x, t)$ for all $x$, and it touches the graph of the optimal $x$ there.

### L2 human

The theorem is used throughout economics, for example to derive Hotelling's lemma and Roy's identity, and in optimization to compute sensitivities of optimal values.
In optimal control and the calculus of variations, the same reasoning shows that the costate is the gradient of the value function, when the latter is differentiable.
The version stated here, which needs no differentiability of the maximizer, is due to Paul Milgrom and Ilya Segal.
When $V$ is not differentiable, one-sided derivatives of $V$ are given by Danskin's theorem under compactness assumptions.
