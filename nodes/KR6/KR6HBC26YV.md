---
tag: KR6HBC26YV
kind: example
name: The greedy algorithm for Egyptian fractions
msc: ["00A35", "11D68"]
topics: [MEKKHHQTKB]
audience: ug1
instance_of: [X5HG1RNWQX]
uses: [X5HG1RNWQX, VB4CMQ82C0, 5KY9WBX45G, PSM6NKYJB8, 01BX15HSRR]
sources:
  - url: https://en.wikipedia.org/wiki/Greedy_algorithm_for_Egyptian_fractions
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Egyptian_fraction
    locator: lead section
---

## Example

We prove that each rational number $\frac{p}{q}$ with $0 < \frac{p}{q} < 1$ is a sum of distinct [[unit fractions|5KY9WBX45G]] $\frac{1}{n}$, that is, it has an [[Egyptian fraction|VB4CMQ82C0]] expansion.
The proof is an [[algorithm|X5HG1RNWQX]], and the algorithm is [[greedy|PSM6NKYJB8]]: at each step it takes the largest unit fraction that fits.

1. Procedure: while the remainder $\frac{p}{q}$ is not $0$, let $n = \lceil q/p \rceil$, record $\frac{1}{n}$, and replace $\frac{p}{q}$ by $\frac{p}{q} - \frac{1}{n} = \frac{pn - q}{qn}$.
2. Choice of $n$: $n$ is the least integer with $n \ge q/p$, so $(n - 1) p < q \le np$.
   So $\frac1n \le \frac pq$, and the new remainder is not negative.
3. Also $n \ge 2$, because $q/p > 1$.
4. Termination: the new numerator $pn - q$ is less than $p$, because $(n - 1)p < q$.
   The numerators strictly decrease in the natural numbers, so by the [[well-ordering principle|01BX15HSRR]] the procedure stops after at most $p$ steps, with remainder $0$.
5. Invariant: (original fraction) $=$ (sum of the recorded unit fractions) $+$ (current remainder).
   It holds at the start, each step moves $\frac1n$ from the remainder to the sum, and at the stop the remainder is $0$.
6. Distinct denominators: $(n - 1)p < q$ gives $\frac pq < \frac{1}{n - 1}$, so the new remainder is less than $\frac{1}{n-1} - \frac1n = \frac{1}{n(n-1)}$.
7. So the next denominator $n'$ satisfies $n' \ge \frac{1}{\text{remainder}} > n(n - 1) \ge n$, since $n \ge 2$, and the unit fractions are distinct.

A run with $\frac{4}{13}$ goes as follows.
First $\lceil 13/4 \rceil = 4$, and $\frac{4}{13} - \frac14 = \frac{16 - 13}{52} = \frac{3}{52}$.
Next $\lceil 52/3 \rceil = 18$, and $\frac{3}{52} - \frac{1}{18} = \frac{54 - 52}{936} = \frac{1}{468}$.
The last step records $\frac{1}{468}$ and leaves $0$, so $\frac{4}{13} = \frac14 + \frac{1}{18} + \frac{1}{468}$.
Check: over the denominator $468$ the sum is $\frac{117 + 26 + 1}{468} = \frac{144}{468} = \frac{4}{13}$, and $18 > 4 \cdot 3$ and $468 > 18 \cdot 17$, as step 7 predicts.

## Remarks

The termination proof uses the numerator, not the denominator, as the decreasing quantity, because the denominators grow.
The bound "at most $p$ steps" is often far from sharp: for $\frac{4}{13}$ the run has $3$ steps.
The denominators can grow very fast, since $n' > n(n - 1)$, so the greedy expansion is correct but usually not the shortest.

The expansion is not unique.
The identity $\frac1n = \frac{1}{n + 1} + \frac{1}{n(n+1)}$ splits the last term into two smaller distinct terms, so each fraction has infinitely many expansions, and the algorithm picks one.

## Explanations

### L1 human

The ancient Egyptians wrote fractions as sums of fractions with numerator $1$, all different.
To write $\frac{4}{13}$ in this way, take the biggest such fraction that fits, here $\frac14$, and look at what is left, $\frac{3}{52}$.
Repeat with what is left: take $\frac{1}{18}$, and $\frac{1}{468}$ is left, which already has numerator $1$.
The top number of what is left goes down each time, $4$, then $3$, then $1$, so the process must end.

### L2 human

We run the algorithm on $\frac{5}{6}$ and $\frac{7}{15}$.

1. For $\frac56$: $\lceil 6/5 \rceil = 2$, and $\frac56 - \frac12 = \frac{4}{12} = \frac13$, so $\frac56 = \frac12 + \frac13$.
2. For $\frac{7}{15}$: $\lceil 15/7 \rceil = 3$, and $\frac{7}{15} - \frac13 = \frac{6}{45} = \frac{2}{15}$.
3. Then $\lceil 15/2 \rceil = 8$, and $\frac{2}{15} - \frac18 = \frac{16 - 15}{120} = \frac{1}{120}$.
4. So $\frac{7}{15} = \frac13 + \frac18 + \frac{1}{120}$.
   Check: $\frac{40 + 15 + 1}{120} = \frac{56}{120} = \frac{7}{15}$.

The example is a first termination proof where the natural quantity, the denominator, grows and another, the numerator, shrinks.
Watch out: with $n = \lfloor q/p \rfloor$ instead of $\lceil q/p \rceil$, $\frac1n$ can exceed $\frac pq$, as $\frac13 > \frac{4}{13}$ shows, and the remainder turns negative.
