---
tag: EMMGBY1KYH
kind: example
name: The no-counterexample interpretation of the minimum principle
msc: ["03F10", "03F30"]
topics: [8XY7JYZKFW]
audience: research
instance_of: [4BCD1EM542]
uses: [4BCD1EM542, J2P9FWBP3Q, KZSB5E471K, KE1C94RNF3]
sources:
  - url: https://en.wikipedia.org/wiki/Herbrandization
    locator: Definition and examples
---

## Example

Let $g : \mathbb{N} \to \mathbb{N}$ be a function.
The minimum principle $A = \exists n\, \forall m\, (g(n) \le g(m))$ says that $g$ takes a smallest value.
It follows from the [[well-ordering principle|J2P9FWBP3Q]], and PA proves it for each function given by a formula.
Its [[no-counterexample interpretation|4BCD1EM542]] asks for a functional $X(g, f)$ with $g(X) \le g(f(X))$ for every $f : \mathbb{N} \to \mathbb{N}$.

We build $X$ by following $f$ from $0$.
Define $n_0 = 0$ and $n_{k + 1} = f(n_k)$, and let $X(g, f) = n_k$ for the least $k$ with $g(n_k) \le g(f(n_k))$.
We check that this $k$ exists and that $X$ is correct.

1. Suppose that $g(n_j) > g(f(n_j)) = g(n_{j + 1})$ for all $j < k$.
2. Each step lowers the value by at least $1$, so induction on $k$ gives $g(n_k) \le g(0) - k$.
3. Values are natural numbers, so $k \le g(0)$.
4. Hence some $k \le g(0)$ has $g(n_k) \le g(f(n_k))$, and the least such $k$ exists.
5. By the choice of $k$, $X = n_k$ satisfies $g(X) \le g(f(X))$.

So $X$ satisfies the n.c.i., and it uses at most $g(0) + 1$ evaluations of $f$ and at most $g(0) + 2$ of $g$, the values $g(n_0), \ldots, g(n_{k+1})$.

## Remarks

The witness of $A$ itself, the place of the minimum of $g$, is not a [[computable function|KZSB5E471K]] of $g$.
After seeing the values $g(0), \ldots, g(N)$, an algorithm still cannot rule out a smaller value at $N + 1$.
The functional $X$ avoids this, because it lets $f$ decide which values of $g$ to inspect.

The bound $g(0) + 1$ does not depend on $f$, and that is the information the classical proof hides.
It is the same bound as in the [[infinite descent example|KE1C94RNF3]] for the A-translation.
The search is bounded by $g(0)$, so $X$ is primitive recursive in $g$ and $f$.

If we start the sequence at another point $c$ in place of $0$, the same argument works with the bound $g(c) + 1$.
If $g$ is allowed to take values in the integers, the argument breaks: for $g(m) = -m$ and $f(n) = n + 1$ the descent never stops, and indeed $g$ has no minimum.

## Explanations

### L1 human

The claim "the function $g$ has a smallest value" is true, but a computer cannot find the smallest value, because it can never look at all values.
The no-counterexample interpretation changes the task.
An opponent claims that every number $n$ is beaten by a number $f(n)$ with a smaller value.
The program follows the claim: $0$, then $f(0)$, then $f(f(0))$, and so on.
The values go down at every step, so after at most $g(0)$ steps a claim fails, and the program has caught the opponent.

### L2 human

We run $X$ on $g(m) = |m - 5| + 2$ and $f(n) = n + 1$.
We start at $n_0 = 0$ with $g(0) = 7$, and $g(f(0)) = g(1) = 6 < 7$, so we continue.
The points $n_1, \ldots, n_4$ are $1, 2, 3, 4$, with the values $6, 5, 4, 3$, and each test fails in the same way.
At $n_5 = 5$ we have $g(5) = 2$ and $g(f(5)) = g(6) = 3 \ge 2$, so $X = 5$.
Check: we used $6$ evaluations of $f$, within the bound $g(0) + 1 = 8$.

Here $X$ is the true minimum, but only because $f$ moved toward it.
For $f(n) = 0$ the functional stops at once with $X = 0$, since $g(0) \le g(f(0))$, and $0$ is not the minimum.
The typical use is to show what finite information a classical existence proof contains.
Watch out: $X$ only refutes the given $f$, and it need not find the true minimum.
