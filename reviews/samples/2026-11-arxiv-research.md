# The audit of the research stratum, 2026-11

The research stratum (corpus arxiv AX9, K9.7) is the nodes of the layer `research`: the nodes whose source is a paper of arXiv. On 2026-11-03 it has 10 nodes. K9.7 audits a stratum with fewer than 100 merges in three months in full, so this audit is a census of the 10 nodes, not a sample, and its rate has no sampling interval.

The audit was blind, with the checklist of K9.7: each node and the text of the paper item that it cites (each paper has an open licence), and no word of who or what wrote the node. The auditor was the codex gpt-6-sol review pass (LLM pass chosen by the owner; not a person). No person has audited the stratum yet.

| Round | Date | Nodes | Nodes with an error | Errors |
|---|---|---|---|---|
| 1 | 2026-11-03 | 10 | 1 | `convention_not_stated` in 2VQDK71A27: the theorem needs a compact Hausdorff space |
| 2 | 2026-11-03 | 10 | 0 | none |

After round 1, #242 stated that the space of 2VQDK71A27 is Hausdorff, as "Above the threshold" of K9.7 asks: the output is fixed, then audited again. Round 2 audited the 10 nodes again, with the fixed node.

| Property | Errors in round 2 | Rate | Threshold of K9.7 |
|---|---|---|---|
| truth (false statement, wrong definition, dropped hypothesis, step that does not follow) | 0 | 0/10 | 1% |
| faithfulness (unfaithful, stronger than the source, wrong attribution, wrong source) | 0 | 0/10 | 2% |
| readability (convention not stated, style, card) | 0 | 0/10 | 5% |

The rate of round 1 was 1/10 for readability, above its threshold. The rate of round 2 is 0 for each property, below each threshold. The packets of the sample of K9.7 for this month are in `2026-11-arxiv.jsonl`, with 12 of the strata `research nodes` and `research nodes of a new area`; the census covers each of their nodes.
