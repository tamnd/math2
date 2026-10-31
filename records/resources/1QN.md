---
records:
    - id: 1QN2CFM0K3
      kind: problem-set
      title: BMO Round 2 2012
      date: "2012-01-26"
      expressions:
        - key: e1
          kind: edition
          date: "2012-01-26"
          structure: 1QN2CFM0K3/e1.json
      relations:
        - kind: part_of
          to: 8XFPR5H74Q
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: bmo
          snapshot: blake3:68eb2251465334659a3c67c12bc8e13877594a5a11510cf9a756eaf0f62db81c
          native_id: bmo2-2012
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
