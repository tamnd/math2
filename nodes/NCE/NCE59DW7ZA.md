---
tag: NCE59DW7ZA
kind: example
name: A FG p is not equivalent to AF AG p
msc: ["03B44", "68Q60"]
topics: [CQM9SRN8PM]
audience: grad
not_instance_of:
  - target: F6JA5C5BJX
    note: the path property FG p on all paths is not a CTL formula, and the CTL formula AF AG p that looks like it is strictly stronger
uses: [1DA0Y6KDF8, 8S64VZ6A1S, RFQ8DJZNQT]
sources:
  - url: https://en.wikipedia.org/wiki/Computation_tree_logic
    locator: section Relations with other logics
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapter 6
---

## Example

Let $M$ have states $s_0$, $s_1$, $s_2$ with edges $s_0 \to s_0$, $s_0 \to s_1$, $s_1 \to s_2$ and $s_2 \to s_2$.
Let $L(s_0) = L(s_2) = \{p\}$ and $L(s_1) = \emptyset$.
We compare the [[LTL|8S64VZ6A1S]] formula $FGp$, read on all paths, with the [[CTL|1DA0Y6KDF8]] formula $AF\,AG\,p$.

1. The paths from $s_0$ are $s_0^\omega$ and $s_0^n s_1 s_2^\omega$ for $n \ge 1$.
2. On $s_0^\omega$, $p$ holds everywhere, so $FGp$ holds.
3. On $s_0^n s_1 s_2^\omega$, $p$ holds from position $n + 1$ on, so $FGp$ holds.
   So every path from $s_0$ satisfies $FGp$, and $s_0$ satisfies $FGp$ in the LTL sense.
4. Now $[\![ AG\,p ]\!] = \{s_2\}$, because from $s_0$ the state $s_1$ is reachable, and $s_1$ fails $p$.
5. $AF\,AG\,p$ at $s_0$ needs every path to reach $s_2$, and the path $s_0^\omega$ never does.
   So $s_0 \not\models AF\,AG\,p$, although $s_0$ satisfies $FGp$ on all paths.

## Remarks

The implication goes one way only.
Every state that satisfies $AF\,AG\,p$ satisfies $FGp$ on all paths, since on each path the state where $AG\,p$ holds is a point from which $p$ holds forever.
So the CTL formula is strictly stronger.
On the path $s_0^\omega$ each state still has the option to leave through $s_1$, and that is why no point of the path satisfies $AG\,p$.

Emerson and Halpern showed that no CTL formula is equivalent to $FGp$ on all paths.
With [[the LTL non-example|RDRSPX5MM7]], this shows that LTL and CTL are incomparable, and [[CTL*|Y4XZ94GRXV]] contains both.
If we delete the edge $s_0 \to s_0$, the only path is $s_0 s_1 s_2^\omega$, and both formulas hold at $s_0$.

## Explanations

### L1 human

A light is on, and at any moment it may flicker off once and then stay on forever.
On every run, the light is in the end on for good.
But at no moment while it waits can we say "from now on it is on for good", because the flicker is still possible.

### L2 human

The method is to list the paths and check $FGp$ on each, then compute $[\![ AG\,p ]\!]$ as a set of states, and finally ask whether every path reaches that set.
Here the paths all satisfy $FGp$, the set is $\{s_2\}$, and the path $s_0^\omega$ misses it.
Watch out: CTL quantifies over paths again at each state, so "eventually always" in CTL is about the whole future tree at a point, not about the rest of one path.
