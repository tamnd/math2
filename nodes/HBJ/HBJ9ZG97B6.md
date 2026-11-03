---
tag: HBJ9ZG97B6
kind: problem
name: Principal–agent problem
msc: [91B43, 91B41, 91B44]
uses: [GZZS4MTDG9, T1GTBBMHCW, 0WQNRCNY3M]
about: [DTXJQKEHDP]
sources:
  - url: https://en.wikipedia.org/wiki/Principal%E2%80%93agent_problem
same_as:
  wikidata: Q1053211
  wikipedia: Principal–agent problem
history:
  posed_by: "Stephen Ross"
  first_stated: "1973"
---

## Problem

A principal hires an agent to take an action $a$ from a set $\mathcal{A}$, such as a level of effort.
The principal does not observe $a$; it observes only an outcome $x$, a random variable whose distribution $F(\cdot \mid a)$ depends on $a$.
The agent has a [[utility function|GZZS4MTDG9]] $u(w) - c(a)$, where $w$ is the payment received and $c(a)$ is the cost of the action.
The agent accepts the contract only if the [[expected|0WQNRCNY3M]] utility is at least a reservation level $\bar u$.
The principal keeps $x - w$ and is risk neutral.

Find a payment rule $w(x)$ and an action $a^*$ that maximize the principal's expected profit $E[x - w(x) \mid a^*]$ subject to:

1. participation: $E[u(w(x)) \mid a^*] - c(a^*) \ge \bar u$;
2. [[incentive compatibility|T1GTBBMHCW]]: $a^*$ maximizes $E[u(w(x)) \mid a] - c(a)$ over $a \in \mathcal{A}$.

## Remarks

If the principal could observe the action, the incentive constraint would disappear; the principal would then pay a fixed wage that fully insures a risk-averse agent, the first-best solution.
If the agent is risk neutral and the agent's liability is not limited, the first best is still reached.
The principal then sells the outcome to the agent for a fixed fee.
With a risk-averse agent and hidden action, the optimal contract must trade off incentives against insurance.
In general it cannot reach the first best, and this loss is called the agency cost.
A standard solution method, the first-order approach, replaces the incentive constraint by the first-order condition of the agent's choice; it is valid only under extra conditions on $F$.

The problem was set out in the economics of agency in the early 1970s.
Stephen Ross's 1973 paper "The economic theory of agency: the principal's problem" is a standard reference for it.
The same name is used more broadly for any situation in which one party acts on behalf of another with different interests and better information.

## Explanations

### L1 human

An owner hires a manager to run a shop, but cannot watch how hard the manager works.
Profits depend on effort but also on luck, so a bad month may be bad luck or laziness.
Paying a fixed salary gives the manager little reason to work hard, while paying only a share of profits loads all the risk on the manager.
The principal–agent problem asks for the best pay scheme between these extremes.
