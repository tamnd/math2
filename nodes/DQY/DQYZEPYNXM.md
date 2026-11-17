---
tag: DQYZEPYNXM
kind: example
name: The 1896 proofs of the prime number theorem use complex analysis
msc: ["00A35", "11N05"]
topics: [Z2WNQ1DNTX]
audience: ug2
not_instance_of:
  - target: 84SZZBACP3
    note: the proofs study the zeta function as a function of a complex variable
uses: [0EHBY5Y84N, 1XWBY4N0VT, 0M3YQJ81NB, 28T3Z4VEHH, 84SZZBACP3]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_proof
    locator: Prime number theorem
  - url: https://en.wikipedia.org/wiki/Prime_number_theorem
    locator: lead section
---

## Example

The [[prime number theorem|0EHBY5Y84N]] states that $\pi(x) \log x / x \to 1$ as $x \to \infty$.
Hadamard and de la Vallée Poussin proved it independently in 1896.
We list the main steps of this kind of proof and check that it is not [[elementary|84SZZBACP3]].

1. For real $s > 1$, the [[Riemann zeta function|1XWBY4N0VT]] is $\zeta(s) = \sum_{n \ge 1} n^{-s}$. This step is elementary.
2. The proof takes $s$ complex, with $\operatorname{Re} s > 1$, and extends $\zeta$ by [[analytic continuation|0M3YQJ81NB]] to $\operatorname{Re} s \ge 1$, $s \ne 1$. This step uses [[complex analysis|28T3Z4VEHH]].
3. The proof shows that $\zeta(1 + i t) \ne 0$ for every real $t \ne 0$. A standard modern argument uses the identity $3 + 4 \cos \theta + \cos 2\theta = 2(1 + \cos \theta)^2 \ge 0$, applied to $\log |\zeta|$ at complex points.
4. The proof passes from the zeros of $\zeta$ to the primes with a contour integral or a theorem on analytic functions.

Steps 2, 3 and 4 need functions of a complex variable, so the proof is not elementary in the sense of number theory.

## Remarks

The identity in step 3 is elementary, but the step is not: it applies the identity to values of $\zeta$ at complex points.
A proof is elementary only if every step is elementary.
In 1948, new methods of Selberg led him and Erdős to elementary proofs of the same theorem.

## Explanations

### L1 human

The first proofs that the primes thin out at a known rate used complex numbers.
They studied a function of a complex variable, not only the primes.
So these proofs are not elementary.
Mathematicians found elementary proofs about 50 years later.

### L2 human

To see that a proof is not elementary, find one step whose tools are outside the allowed list.

1. The allowed tools are integers, real numbers and real inequalities.
2. Step 2 uses analytic continuation of a function of a complex variable.
3. Analytic continuation is not in the list, so the proof is not elementary.

A trap: a non-elementary proof is not a worse proof.
Here the analytic proof is shorter than the elementary proofs.
