---
records:
    - id: T8BET1RFXE
      kind: problem-set
      title: Kvant 1983, no. 6
      date: "1983"
      expressions:
        - key: e1
          kind: edition
          date: "1983"
          structure: T8BET1RFXE/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 1983-6
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: T8BQ6HHZYT
      kind: preprint
      title: Time-changed Markov processes and space-time coupled non-local equations
      creators:
        - name: Giacomo Ascione
          role: author
        - name: Enrico Scalas
          role: author
        - name: Bruno Toaldo
          role: author
        - name: Lorenzo Torricelli
          role: author
      date: "2024-12-19"
      subjects:
        - system: arxiv
          code: math.PR
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2024-12-19"
          ids:
            arxiv: "2412.14956"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2412.14956"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
