---
tag: FYV2YKJ0A2
kind: definition
name: Actuarial present value
msc: [91G05]
defines: 9R2M84SW0V
uses: [0WQNRCNY3M, 0PNRKMRC55, PWBQ7GKQGD]
sources:
  - url: https://en.wikipedia.org/wiki/Actuarial_present_value
---

## Definition

Fix an effective annual interest rate $i > -1$ and the discount factor $v = 1/(1 + i)$.
Consider a contract that pays the random amounts $C_1, \dots, C_m$ at the fixed times $t_1, \dots, t_m \ge 0$ (in years).
Each $C_k$ is an integrable [[random variable|0PNRKMRC55]], which may take the value $0$.
Its *actuarial present value* is the [[expected value|0WQNRCNY3M]] of the discounted payments:
$$\mathrm{APV} = E\left[\sum_{k=1}^{m} v^{t_k} C_k\right] = \sum_{k=1}^{m} v^{t_k} E[C_k].$$
More generally, the APV of a random present value $Z$ of a contract is $E[Z]$.

## Remarks

Example: a pure endowment pays $1$ at time $n$ if a person aged $x$ is alive then.
Here $C = 1$ with probability ${}_n p_x$ and $0$ otherwise, so $\mathrm{APV} = v^n \, {}_n p_x$, written ${}_n E_x$; the survival probability is read from a [[life table|PWBQ7GKQGD]] as $l_{x+n}/l_x$.
Example: whole life insurance paying $1$ at the end of the year of death has present value $Z = v^{K+1}$, where $K$ is the curtate future lifetime, so $A_x = E[v^{K+1}] = \sum_{k \ge 0} v^{k+1} \, {}_k p_x \, q_{x+k}$.
Non-example: the plain discounted value $\sum_k v^{t_k} c_k$ of the largest possible payments $c_k$ is not the APV unless each payment is certain; it ignores the probabilities.
The equivalence principle sets the APV of premiums equal to the APV of benefits.
