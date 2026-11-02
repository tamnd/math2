---
tag: KA4MW1FRZ4
kind: example
name: Random walk as a difference equation
msc: [39A50, 60G50]
instance_of: [WPYG78BSD5]
uses: [04VZE3FZXF, 00MRN0FARV]
sources:
  - url: https://en.wikipedia.org/wiki/Random_walk
---

## Example

Let $\xi_1, \xi_2, \dots$ be [[independent and identically distributed|00MRN0FARV]] random variables with $P(\xi_n = 1) = P(\xi_n = -1) = \tfrac{1}{2}$.
The simple symmetric [[random walk|04VZE3FZXF]] on $\Z$ is the solution of the stochastic difference equation
$$S_{n+1} = S_n + \xi_{n+1}, \qquad S_0 = 0.$$
It has the form $X_{n+1} = f(X_n, \xi_{n+1})$ with $f(x, e) = x + e$, so it is a [[stochastic difference equation|WPYG78BSD5]].
Solving the recursion gives $S_n = \xi_1 + \cdots + \xi_n$.
Taking expectations in the equation gives the deterministic difference equation $E[S_{n+1}] = E[S_n]$, so $E[S_n] = 0$.
Squaring gives $S_{n+1}^2 = S_n^2 + 2 S_n \xi_{n+1} + 1$, and since $\xi_{n+1}$ is independent of $S_n$ with mean $0$, $E[S_{n+1}^2] = E[S_n^2] + 1$, so $E[S_n^2] = n$.

Probabilities of the walk also solve difference equations.
Fix an integer $N \ge 1$ and let $p_j$ be the probability that the walk started at $j \in \set{0, \dots, N}$ reaches $N$ before $0$.
Conditioning on the first step gives $p_j = \tfrac{1}{2} p_{j+1} + \tfrac{1}{2} p_{j-1}$ for $0 < j < N$, with $p_0 = 0$ and $p_N = 1$.
This linear recurrence has characteristic polynomial $(z - 1)^2$, so $p_j = a + bj$, and the boundary values give $p_j = j/N$.

## Explanations

### L1 human

Flip a fair coin at each step and move one unit up for heads and one unit down for tails.
Your position follows the rule: new position equals old position plus a random step.
That rule is a difference equation with a random term.
It tells you right away that you stay at $0$ on average while your typical distance grows like $\sqrt{n}$.
It also gives the gambler's ruin rule: starting with $j$ euros and playing fair one-euro bets, you reach $N$ euros before going broke with probability $j/N$.
