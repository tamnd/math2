---
tag: CJ7PTCRQED
kind: concept
name: Second derivative as a limit of difference quotients
msc: [26A24]
uses: [0V1EJCT8G6, 0QKJ6NT0R9, 0PKRYB8ATM, AZBDB5F4M4]
sources:
  - url: https://github.com/active-calculus/active-calculus-single-mbx/blob/e597daa657ba5ec0953157aa8c44834dceb63eb2/source/sec-1-6-second-d.xml#L208
    locator: source/sec-1-6-second-d.xml:208
---

## Summary

Take any function $f$ and any point $x$ of its domain. The second derivative of $f$ at $x$ is the [[derivative|0V1EJCT8G6]] of the [[derivative function|0QKJ6NT0R9]] $f'$, computed straight from the definition.

In symbols, form the [[difference quotient|AZBDB5F4M4]] of $f'$ with step $h$. Then

$$f''(x) = \lim_{h \to 0} \frac{f'(x+h) - f'(x)}{h}.$$

The value is defined exactly when this [[limit|0PKRYB8ATM]] exists. Where it exists for every $x$ in a set, $f''$ is a new function on that set. No interval or global differentiability of $f$ is assumed beyond what the limit needs.
