---
records:
    - id: 4VZSDPAJ63
      kind: problem-set
      title: Kvant 1979, no. 9
      creators:
        - name: Kvant editorial board
          role: editor
      date: "1979"
      msc:
        - code: 00A07
          from: kvant
        - code: 97U40
          from: kvant
      expressions:
        - key: e1
          kind: edition
          language: ru
          date: "1979"
          structure: 4VZSDPAJ63/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 1979-9
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
    - id: 4VZV5V0YD6
      kind: preprint
      title: The Information Bottleneck is NP-hard
      creators:
        - name: Roberto Bruno
          role: author
        - name: Ugo Vaccaro
          role: author
      date: "2026-10-15"
      subjects:
        - system: arxiv
          code: cs.IT
        - system: arxiv
          code: math.IT
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-10-15"
          ids:
            arxiv: "2610.22272"
      scope:
        value: in
        rule: S2
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.22272"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2610.22272"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
---
